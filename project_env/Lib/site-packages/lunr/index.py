from __future__ import unicode_literals

from collections import defaultdict
import json
import logging

from builtins import str, dict  # noqa
from past.builtins import basestring

from lunr.exceptions import BaseLunrException
from lunr.field_ref import FieldRef
from lunr.match_data import MatchData
from lunr.token_set import TokenSet
from lunr.token_set_builder import TokenSetBuilder
from lunr.pipeline import Pipeline
from lunr.query import Query, QueryPresence
from lunr.query_parser import QueryParser
from lunr.utils import CompleteSet
from lunr.vector import Vector

logger = logging.getLogger(__name__)


class Index:
    """An index contains the built index of all documents and provides a query
    interface to the index.

    Usually instances of lunr.Index will not be created using this
    constructor, instead lunr.Builder should be used to construct new
    indexes, or lunr.Index.load should be used to load previously built and
    serialized indexes.
    """

    def __init__(self, inverted_index, field_vectors, token_set, fields, pipeline):
        self.inverted_index = inverted_index
        self.field_vectors = field_vectors
        self.token_set = token_set
        self.fields = fields
        self.pipeline = pipeline

    def __eq__(self, other):
        # TODO: extend equality to other attributes
        return (
            self.inverted_index == other.inverted_index and self.fields == other.fields
        )

    def search(self, query_string):
        """Performs a search against the index using lunr query syntax.

        Results will be returned sorted by their score, the most relevant
        results will be returned first.

        For more programmatic querying use `lunr.Index.query`.

        Args:
            query_string (str): A string to parse into a Query.

        Returns:
            dict: Results of executing the query.
        """
        query = self.create_query()
        # TODO: should QueryParser be a method of query? should it return one?
        parser = QueryParser(query_string, query)
        parser.parse()
        return self.query(query)

    def create_query(self, fields=None):
        """Convenience method to create a Query with the Index's fields.

        Args:
            fields (iterable, optional): The fields to include in the Query,
                defaults to the Index's `all_fields`.

        Returns:
            Query: With the specified fields or all the fields in the Index.
        """
        if fields is None:
            return Query(self.fields)

        non_contained_fields = set(fields) - set(self.fields)
        if non_contained_fields:
            raise BaseLunrException(
                "Fields {} are not part of the index", non_contained_fields
            )

        return Query(fields)

    def query(self, query=None, callback=None):
        """Performs a query against the index using the passed lunr.Query
        object.

        If performing programmatic queries against the index, this method is
        preferred over `lunr.Index.search` so as to avoid the additional query
        parsing overhead.

        Args:
            query (lunr.Query): A configured Query to perform the search
                against, use `create_query` to get a preconfigured object
                or use `callback` for convenience.
            callback (callable): An optional function taking a single Query
                object result of `create_query` for further configuration.
        """
        if query is None:
            query = self.create_query()

        if callback is not None:
            callback(query)

        if len(query.clauses) == 0:
            logger.warning(
                "Attempting a query with no clauses. Please add clauses by "
                "either using the `callback` argument or using `create_query` "
                "to create a preconfigured Query, manually adding clauses and "
                "passing it as the `query` argument."
            )
            return []

        # for each query clause
        # * process terms
        # * expand terms from token set
        # * find matching documents and metadata
        # * get document vectors
        # * score documents

        matching_fields = {}
        query_vectors = {field: Vector() for field in self.fields}
        term_field_cache = {}
        required_matches = {}
        prohibited_matches = defaultdict(set)

        for clause in query.clauses:
            # Unless the pipeline has been disabled for this term, which is
            # the case for terms with wildcards, we need to pass the clause
            # term through the search pipeline. A pipeline returns an array
            # of processed terms. Pipeline functions may expand the passed
            # term, which means we may end up performing multiple index lookups
            # for a single query term.
            if clause.use_pipeline:
                terms = self.pipeline.run_string(clause.term, {"fields": clause.fields})
            else:
                terms = [clause.term]

            clause_matches = CompleteSet()

            for term in terms:
                # Each term returned from the pipeline needs to use the same
                # query clause object, e.g. the same boost and or edit distance
                # The simplest way to do this is to re-use the clause object
                # but mutate its term property.
                clause.term = term

                # From the term in the clause we create a token set which will
                # then be used to intersect the indexes token set to get a list
                # of terms to lookup in the inverted index
                term_token_set = TokenSet.from_clause(clause)
                expanded_terms = self.token_set.intersect(term_token_set).to_list()

                # If a term marked as required does not exist in the TokenSet
                # it is impossible for the search to return any matches.
                # We set all the field-scoped required matches set to empty
                # and stop examining further clauses
                if (
                    len(expanded_terms) == 0
                    and clause.presence == QueryPresence.REQUIRED
                ):
                    for field in clause.fields:
                        required_matches[field] = CompleteSet()
                    break

                for expanded_term in expanded_terms:
                    posting = self.inverted_index[expanded_term]
                    term_index = posting["_index"]

                    for field in clause.fields:
                        # For each field that this query term is scoped by
                        # (by default all fields are in scope) we need to get
                        # all the document refs that have this term in that
                        # field.
                        #
                        # The posting is the entry in the invertedIndex for the
                        # matching term from above.
                        field_posting = posting[field]
                        matching_document_refs = field_posting.keys()
                        term_field = expanded_term + "/" + field
                        matching_documents_set = set(matching_document_refs)

                        # If the presence of this term is required, ensure that
                        # the matching documents are added to the set of
                        # required matches for this clause.
                        if clause.presence == QueryPresence.REQUIRED:
                            clause_matches = clause_matches.union(
                                matching_documents_set
                            )

                            if field not in required_matches:
                                required_matches[field] = CompleteSet()

                        # If the presence of this term is prohibited,
                        # ensure that the matching documents are added to the
                        # set of prohibited matches for this field, creating
                        # that set if it does not exist yet.
                        elif clause.presence == QueryPresence.PROHIBITED:
                            prohibited_matches[field] = prohibited_matches[field].union(
                                matching_documents_set
                            )

                            # prohibited matches should not be part of the
                            # query vector used for similarity scoring and no
                            # metadata should be extracted so we continue
                            # to the next field
                            continue

                        # The query field vector is populated using the
                        # term_index found for the term an a unit value with
                        # the appropriate boost
                        # Using upsert because there could already be an entry
                        # in the vector for the term we are working with.
                        # In that case we just add the scores together.
                        query_vectors[field].upsert(
                            term_index, clause.boost, lambda a, b: a + b
                        )

                        # If we've already seen this term, field combo then
                        # we've already collected the matching documents and
                        # metadata, no need to go through all that again
                        if term_field in term_field_cache:
                            continue

                        for matching_document_ref in matching_document_refs:
                            # All metadata for this term/field/document triple
                            # are then extracted and collected into an instance
                            # of lunr.MatchData ready to be returned in the
                            # query results
                            matching_field_ref = FieldRef(matching_document_ref, field)
                            metadata = field_posting[str(matching_document_ref)]

                            if str(matching_field_ref) not in matching_fields:
                                matching_fields[str(matching_field_ref)] = MatchData(
                                    expanded_term, field, metadata
                                )
                            else:
                                matching_fields[str(matching_field_ref)].add(
                                    expanded_term, field, metadata
                                )

                        term_field_cache[term_field] = True

            # if the presence was required we need to update the required
            # matches field sets, we do this after all fields for the term
            # have collected their matches because the clause terms presence
            # is required in _any_ of the fields, not _all_ of the fields
            if clause.presence == QueryPresence.REQUIRED:
                for field in clause.fields:
                    required_matches[field] = required_matches[field].intersection(
                        clause_matches
                    )

        # We need to combine the field scoped required and prohibited
        # matching documents inot a global set of required and prohibited
        # matches
        all_required_matches = CompleteSet()
        all_prohibited_matches = set()
        for field in self.fields:
            if field in required_matches:
                all_required_matches = all_required_matches.intersection(
                    required_matches[field]
                )
            if field in prohibited_matches:
                all_prohibited_matches = all_prohibited_matches.union(
                    prohibited_matches[field]
                )

        matching_field_refs = matching_fields.keys()
        results = []
        matches = {}

        # If the query is negated (only contains prohibited terms)
        # we need to get _all_ field_refs currently existing in the index.
        # This to avoid any costs of getting all field regs unnecessarily
        # Additionally, blank match data must be created to correctly populate
        # the results
        if query.is_negated():
            matching_field_refs = list(self.field_vectors.keys())

            for matching_field_ref in matching_field_refs:
                field_ref = FieldRef.from_string(matching_field_ref)
                matching_fields[matching_field_ref] = MatchData()

        for matching_field_ref in matching_field_refs:
            # Currently we have document fields that match the query, but we
            # need to return documents. The matchData and scores are combined
            # from multiple fields belonging to the same document.
            #
            # Scores are calculated by field, using the query vectors created
            # above, and combined into a final document score using addition.
            field_ref = FieldRef.from_string(matching_field_ref)
            doc_ref = field_ref.doc_ref

            if doc_ref not in all_required_matches or doc_ref in all_prohibited_matches:
                continue

            field_vector = self.field_vectors[matching_field_ref]
            score = query_vectors[field_ref.field_name].similarity(field_vector)

            try:
                doc_match = matches[doc_ref]
                doc_match["score"] += score
                doc_match["match_data"].combine(matching_fields[matching_field_ref])
            except KeyError:
                match = {
                    "ref": doc_ref,
                    "score": score,
                    "match_data": matching_fields[matching_field_ref],
                }
                matches[doc_ref] = match
                results.append(match)

        return sorted(results, key=lambda a: a["score"], reverse=True)

    def serialize(self):
        from lunr import __TARGET_JS_VERSION__

        inverted_index = [
            [term, self.inverted_index[term]] for term in sorted(self.inverted_index)
        ]
        field_vectors = [
            [ref, vector.serialize()] for ref, vector in self.field_vectors.items()
        ]

        # CamelCased keys for compatibility with JS version
        return {
            "version": __TARGET_JS_VERSION__,
            "fields": self.fields,
            "fieldVectors": field_vectors,
            "invertedIndex": inverted_index,
            "pipeline": self.pipeline.serialize(),
        }

    @classmethod
    def load(cls, serialized_index):
        """Load a serialized index"""
        from lunr import __TARGET_JS_VERSION__

        if isinstance(serialized_index, basestring):
            serialized_index = json.loads(serialized_index)

        if serialized_index["version"] != __TARGET_JS_VERSION__:
            logger.warning(
                "Version mismatch when loading serialized index. "
                "Current version of lunr {} does not match that of serialized "
                "index {}".format(__TARGET_JS_VERSION__, serialized_index["version"])
            )

        field_vectors = {
            ref: Vector(elements) for ref, elements in serialized_index["fieldVectors"]
        }

        tokenset_builder = TokenSetBuilder()
        inverted_index = {}
        for term, posting in serialized_index["invertedIndex"]:
            tokenset_builder.insert(term)
            inverted_index[term] = posting

        tokenset_builder.finish()

        return Index(
            fields=serialized_index["fields"],
            field_vectors=field_vectors,
            inverted_index=inverted_index,
            token_set=tokenset_builder.root,
            pipeline=Pipeline.load(serialized_index["pipeline"]),
        )
