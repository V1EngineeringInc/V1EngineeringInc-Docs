from __future__ import unicode_literals, division

from collections import defaultdict

from builtins import str, dict  # noqa

from lunr.pipeline import Pipeline
from lunr.tokenizer import Tokenizer
from lunr.token_set import TokenSet
from lunr.field_ref import FieldRef
from lunr.index import Index
from lunr.vector import Vector
from lunr.idf import idf as Idf


class Field:
    """Represents a field with boost and extractor functions."""

    def __init__(self, field_name, boost=1, extractor=None):
        self.name = field_name
        self.boost = boost
        self.extractor = extractor

    def __repr__(self):
        return '<Field "{0.name}" boost="{0.boost}">'.format(self)

    def __hash__(self):
        return hash(self.name)


class Builder:
    """Performs indexing on a set of documents and returns instances of
    lunr.Index ready for querying.

    All configuration of the index is done via the builder, the fields to
    index, the document reference, the text processing pipeline and document
    scoring parameters are all set on the builder before indexing.
    """

    def __init__(self):
        self._ref = "id"
        self._fields = {}
        self.inverted_index = {}
        self.field_term_frequencies = {}
        self.field_lengths = {}
        self.pipeline = Pipeline()
        self.search_pipeline = Pipeline()
        self._documents = {}
        self.document_count = 0
        self._b = 0.75
        self._k1 = 1.2
        self.term_index = 0
        self.metadata_whitelist = []

    def ref(self, ref):
        """Sets the document field used as the document reference.

        Every document must have this field. The type of this field in the
        document should be a string, if it is not a string it will be coerced
        into a string by calling `str`.

        The default ref is 'id'. The ref should _not_ be changed during
        indexing, it should be set before any documents are added to the index.
        Changing it during indexing can lead to inconsistent results.

        """
        self._ref = ref

    def field(self, field_name, boost=1, extractor=None):
        """Adds a field to the list of document fields that will be indexed.

        Every document being indexed should have this field. None values for
        this field in indexed documents will not cause errors but will limit
        the chance of that document being retrieved by searches.

        All fields should be added before adding documents to the index. Adding
        fields after a document has been indexed will have no effect on already
        indexed documents.

        Fields can be boosted at build time. This allows terms within that
        field to have more importance on search results. Use a field boost to
        specify that matches within one field are more important that other
        fields.

        Args:
            field_name (str): Name of the field to be added, must not include
                a forward slash '/'.
            boost (int): Optional boost factor to apply to field.
            extractor (callable): Optional function to extract a field from
                the document.

        Raises:
            ValueError: If the field name contains a `/`.
        """
        if "/" in field_name:
            raise ValueError("Field {} contains illegal character `/`")

        self._fields[field_name] = Field(field_name, boost, extractor)

    def b(self, number):
        """A parameter to tune the amount of field length normalisation that is
        applied when calculating relevance scores.

        A value of 0 will completely disable any normalisation and a value of 1
        will fully normalise field lengths. The default is 0.75. Values of b
        will be clamped to the range 0 - 1.
        """
        if number < 0:
            self._b = 0
        elif number > 1:
            self._b = 1
        else:
            self._b = number

    def k1(self, number):
        """ A parameter that controls the speed at which a rise in term
        frequency results in term frequency saturation.

        The default value is 1.2. Setting this to a higher value will give
        slower saturation levels, a lower value will result in quicker
        saturation.
        """
        self._k1 = number

    def add(self, doc, attributes=None):
        """Adds a document to the index.

        Before adding documents to the index it should have been fully
        setup, with the document ref and all fields to index already having
        been specified.

        The document must have a field name as specified by the ref (by default
        this is 'id') and it should have all fields defined for indexing,
        though None values will not cause errors.

        Args:
            - doc (dict): The document to be added to the index.
            - attributes (dict, optional): A set of attributes corresponding
            to the document, currently a single `boost` -> int will be
            taken into account.
        """
        doc_ref = str(doc[self._ref])
        self._documents[doc_ref] = attributes or {}
        self.document_count += 1

        for field_name, field in self._fields.items():
            extractor = field.extractor
            field_value = doc[field_name] if extractor is None else extractor(doc)
            tokens = Tokenizer(field_value)
            terms = self.pipeline.run(tokens)
            field_ref = FieldRef(doc_ref, field_name)
            field_terms = defaultdict(int)

            # TODO: field_refs are casted to strings in JS, should we allow
            # FieldRef as keys?
            self.field_term_frequencies[str(field_ref)] = field_terms
            self.field_lengths[str(field_ref)] = len(terms)

            for term in terms:
                # TODO: term is a Token, should we allow Tokens as keys?
                term_key = str(term)

                field_terms[term_key] += 1
                if term_key not in self.inverted_index:
                    posting = {_field_name: {} for _field_name in self._fields}
                    posting["_index"] = self.term_index
                    self.term_index += 1
                    self.inverted_index[term_key] = posting

                if doc_ref not in self.inverted_index[term_key][field_name]:
                    self.inverted_index[term_key][field_name][doc_ref] = defaultdict(
                        list
                    )

                for metadata_key in self.metadata_whitelist:
                    metadata = term.metadata[metadata_key]
                    self.inverted_index[term_key][field_name][doc_ref][
                        metadata_key
                    ].append(metadata)

    def build(self):
        """Builds the index, creating an instance of `lunr.Index`.

        This completes the indexing process and should only be called once all
        documents have been added to the index.
        """
        self._calculate_average_field_lengths()
        self._create_field_vectors()
        self._create_token_set()

        return Index(
            inverted_index=self.inverted_index,
            field_vectors=self.field_vectors,
            token_set=self.token_set,
            fields=list(self._fields.keys()),
            pipeline=self.search_pipeline,
        )

    def _create_token_set(self):
        """Creates a token set of all tokens in the index using `lunr.TokenSet`
        """
        self.token_set = TokenSet.from_list(sorted(list(self.inverted_index.keys())))

    def _calculate_average_field_lengths(self):
        """Calculates the average document length for this index"""
        accumulator = defaultdict(int)
        documents_with_field = defaultdict(int)

        for field_ref, length in self.field_lengths.items():
            _field_ref = FieldRef.from_string(field_ref)
            field = _field_ref.field_name

            documents_with_field[field] += 1
            accumulator[field] += length

        for field_name in self._fields:
            accumulator[field_name] /= documents_with_field[field_name]

        self.average_field_length = accumulator

    def _create_field_vectors(self):
        """Builds a vector space model of every document using lunr.Vector."""
        field_vectors = {}
        term_idf_cache = {}

        for field_ref, term_frequencies in self.field_term_frequencies.items():
            _field_ref = FieldRef.from_string(field_ref)
            field_name = _field_ref.field_name
            field_length = self.field_lengths[field_ref]
            field_vector = Vector()
            field_boost = self._fields[field_name].boost
            doc_boost = self._documents[_field_ref.doc_ref].get("boost", 1)

            for term, tf in term_frequencies.items():
                term_index = self.inverted_index[term]["_index"]

                if term not in term_idf_cache:
                    idf = Idf(self.inverted_index[term], self.document_count)
                    term_idf_cache[term] = idf
                else:
                    idf = term_idf_cache[term]

                score = (
                    idf
                    * ((self._k1 + 1) * tf)
                    / (
                        self._k1
                        * (
                            1
                            - self._b
                            + self._b
                            * (field_length / self.average_field_length[field_name])
                        )
                        + tf
                    )
                )
                score *= field_boost
                score *= doc_boost
                score_with_precision = round(score, 3)

                field_vector.insert(term_index, score_with_precision)

            field_vectors[field_ref] = field_vector

        self.field_vectors = field_vectors

    def use(self, fn, *args, **kwargs):
        """Applies a plugin to the index builder.

        A plugin is a function that is called with the index builder as its
        context. Plugins can be used to customise or extend the behaviour of
        the index in some way.

        A plugin is just a function, that encapsulated the custom behaviour
        that should be applied when building the index. The plugin function
        will be called with the index builder as its argument, additional
        arguments can also be passed when calling use.
        """
        fn(self, *args, **kwargs)
