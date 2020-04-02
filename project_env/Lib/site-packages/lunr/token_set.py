from __future__ import unicode_literals

from builtins import str

import six


@six.python_2_unicode_compatible
class TokenSet:
    """
    A token set is used to store the unique list of all tokens
    within an index. Token sets are also used to represent an
    incoming query to the index, this query token set and index
    token set are then intersected to find which tokens to look
    up in the inverted index.

    A token set can hold multiple tokens, as in the case of the
    index token set, or it can hold a single token as in the
    case of a simple query token set.

    Additionally token sets are used to perform wildcard matching.
    Leading, contained and trailing wildcards are supported, and
    from this edit distance matching can also be provided.

    Token sets are implemented as a minimal finite state automata,
    where both common prefixes and suffixes are shared between tokens.
    This helps to reduce the space used for storing the token set.

    TODO: consider https://github.com/glyph/automat
    """

    _next_id = 1

    def __init__(self):
        self.final = False
        self.edges = {}
        self.id = self._next_id
        self.__class__._next_id += 1

    def __str__(self):
        try:
            return self._string
        except AttributeError:
            pass

        string = "1" if self.final else "0"
        for label in sorted(list(self.edges.keys())):
            node = self.edges[label]
            try:
                node_id = str(node.id)
            except AttributeError:
                # TODO: JS seems to rely on undefined for the id attribute?
                node_id = ""

            string = string + label + node_id

        return string

    def __repr__(self):
        return '<TokenSet "{}">'.format(str(self))

    @classmethod
    def from_string(self, string):
        """Creates a TokenSet from a string.

        The string may contain one or more wildcard characters (*) that will
        allow wildcard matching when intersecting with another TokenSet
        """
        node = TokenSet()
        root = node

        # Iterates throough all characters in the passed string appending
        # a node for each character.
        # When a wildcard character is found then a self referencing edge
        # is introduced to continually match any number of characters
        for i, char in enumerate(string):
            final = i == len(string) - 1
            if char == "*":
                node.edges[char] = node
                node.final = final
            else:
                next_ = TokenSet()
                next_.final = final
                node.edges[char] = next_
                node = next_

        return root

    @classmethod
    def from_fuzzy_string(cls, string, edit_distance):
        """Creates a token set representing a single string with a specified
        edit distance.

        Insertions, deletions, substitutions and transpositions are each
        treated as an edit distance of 1.

        Increasing the allowed edit distance will have a dramatic impact
        on the performance of both creating and intersecting these TokenSets.
        It is advised to keep the edit distance less than 3.
        """
        root = TokenSet()

        stack = [{"node": root, "edits_remaining": edit_distance, "string": string}]

        while stack:
            frame = stack.pop()
            # no edit
            if len(frame["string"]) > 0:
                char = frame["string"][0]
                no_edit_node = None
                if char in frame["node"].edges:
                    no_edit_node = frame["node"].edges[char]
                else:
                    no_edit_node = TokenSet()
                    frame["node"].edges[char] = no_edit_node

                if len(frame["string"]) == 1:
                    no_edit_node.final = True

                stack.append(
                    {
                        "node": no_edit_node,
                        "edits_remaining": frame["edits_remaining"],
                        "string": frame["string"][1:],
                    }
                )

            if frame["edits_remaining"] == 0:
                continue

            # insertion, can only do insertion if there are edits remaining
            if "*" in frame["node"].edges:
                insertion_node = frame["node"].edges["*"]
            else:
                insertion_node = TokenSet()
                frame["node"].edges["*"] = insertion_node

            if len(frame["string"]) == 0:
                insertion_node.final = True

            stack.append(
                {
                    "node": insertion_node,
                    "edits_remaining": frame["edits_remaining"] - 1,
                    "string": frame["string"],
                }
            )

            # deletion, can only do a deletion if we have enough edits
            # remaining and if there are characters left to delete in the string
            if len(frame["string"]) > 1:
                stack.append(
                    {
                        "node": frame["node"],
                        "edits_remaining": frame["edits_remaining"] - 1,
                        "string": frame["string"][1:],
                    }
                )

            # deletion, just removing the last character of the string
            if len(frame["string"]) == 1:
                frame["node"].final = True

            # substitution, can only do a substitution if we have enough edits
            # remaining and there are characters left to substitute
            if len(frame["string"]) >= 1:
                if "*" in frame["node"].edges:
                    substitution_node = frame["node"].edges["*"]
                else:
                    substitution_node = TokenSet()
                    frame["node"].edges["*"] = substitution_node

                if len(frame["string"]) == 1:
                    substitution_node.final = True

                stack.append(
                    {
                        "node": substitution_node,
                        "edits_remaining": frame["edits_remaining"] - 1,
                        "string": frame["string"][1:],
                    }
                )

            # transposition, can only do a transposition if there are edits
            # remaining and there are enough characters to transpose
            if frame["edits_remaining"] and len(frame["string"]) > 1:
                char_a = frame["string"][0]
                char_b = frame["string"][1]
                transpose_node = None

                if char_b in frame["node"].edges:
                    transpose_node = frame["node"].edges[char_b]
                else:
                    transpose_node = TokenSet()
                    frame["node"].edges[char_b] = transpose_node

                if len(frame["string"]) == 1:
                    transpose_node.final = True

                stack.append(
                    {
                        "node": transpose_node,
                        "edits_remaining": frame["edits_remaining"] - 1,
                        "string": char_a + frame["string"][2:],
                    }
                )

        return root

    @classmethod
    def from_list(cls, list_of_words):
        from lunr.token_set_builder import TokenSetBuilder

        builder = TokenSetBuilder()
        for word in list_of_words:
            builder.insert(word)

        builder.finish()
        return builder.root

    @classmethod
    def from_clause(cls, clause):
        if clause.edit_distance:
            return cls.from_fuzzy_string(clause.term, clause.edit_distance)
        else:
            return cls.from_string(clause.term)

    def to_list(self):
        words = []
        stack = [{"prefix": "", "node": self}]

        while stack:
            frame = stack.pop()
            if frame["node"].final:
                words.append(frame["prefix"])

            for edge in frame["node"].edges.keys():
                stack.append(
                    {
                        "prefix": frame["prefix"] + str(edge),
                        "node": frame["node"].edges[edge],
                    }
                )

        return words

    def intersect(self, other):
        """Returns a new TokenSet that is the intersection of this TokenSet
        and the passed TokenSet.

        This intersection will take into account any wildcards contained within
        the TokenSet.
        """
        output = TokenSet()
        stack = [{"node": self, "q_node": other, "output": output}]

        while stack:
            frame = stack.pop()
            for q_edge in frame["q_node"].edges.keys():
                for n_edge in frame["node"].edges.keys():
                    if n_edge == q_edge or q_edge == "*":
                        node = frame["node"].edges[n_edge]
                        q_node = frame["q_node"].edges[q_edge]
                        final = node.final and q_node.final
                        next_ = None

                        if n_edge in frame["output"].edges:
                            next_ = frame["output"].edges[n_edge]
                            next_.final = next_.final or final
                        else:
                            next_ = TokenSet()
                            next_.final = final
                            frame["output"].edges[n_edge] = next_

                        stack.append({"node": node, "q_node": q_node, "output": next_})

        return output
