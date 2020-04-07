from __future__ import unicode_literals, division

from math import sqrt

from lunr.exceptions import BaseLunrException


class Vector:
    """A vector is used to construct the vector space of documents and queries.
    These vectors support operations to determine the similarity between two
    documents or a document and a query.

    Normally no parameters are required for initializing a vector, but in the
    case of loading a previously dumped vector the raw elements can be provided
    to the constructor.

    For performance reasons vectors are implemented with a flat array, where an
    elements index is immediately followed by its value.
    E.g. [index, value, index, value].

    TODO: consider implemetation as 2-tuples.

    This allows the underlying array to be as sparse as possible and still
    offer decent performance when being used for vector calculations.
    """

    def __init__(self, elements=None):
        self._magnitude = 0
        self.elements = elements or []

    def __repr__(self):
        return "<Vector magnitude={}>".format(self.magnitude)

    def __iter__(self):
        return iter(self.elements)

    def position_for_index(self, index):
        """Calculates the position within the vector to insert a given index.

        This is used internally by insert and upsert. If there are duplicate
        indexes then the position is returned as if the value for that index
        were to be updated, but it is the callers responsibility to check
        whether there is a duplicate at that index
        """
        if not self.elements:
            return 0

        start = 0
        end = int(len(self.elements) / 2)
        slice_length = end - start
        pivot_point = int(slice_length / 2)
        pivot_index = self.elements[pivot_point * 2]

        while slice_length > 1:
            if pivot_index < index:
                start = pivot_point
            elif pivot_index > index:
                end = pivot_point
            else:
                break

            slice_length = end - start
            pivot_point = start + int(slice_length / 2)
            pivot_index = self.elements[pivot_point * 2]

        if pivot_index == index:
            return pivot_point * 2
        elif pivot_index > index:
            return pivot_point * 2
        else:
            return (pivot_point + 1) * 2

    def insert(self, insert_index, val):
        """Inserts an element at an index within the vector.

        Does not allow duplicates, will throw an error if there is already an
        entry for this index.
        """

        def prevent_duplicates(index, val):
            raise BaseLunrException("Duplicate index")

        self.upsert(insert_index, val, prevent_duplicates)

    def upsert(self, insert_index, val, fn=None):
        """Inserts or updates an existing index within the vector.

        Args:
            - insert_index (int): The index at which the element should be
                inserted.
            - val (int|float): The value to be inserted into the vector.
            - fn (callable, optional): An optional callable taking two
                arguments, the current value and the passed value to generate
                the final inserted value at the position in case of collision.
        """
        fn = fn or (lambda current, passed: passed)
        self._magnitude = 0
        position = self.position_for_index(insert_index)
        if position < len(self.elements) and self.elements[position] == insert_index:
            self.elements[position + 1] = fn(self.elements[position + 1], val)
        else:
            self.elements.insert(position, val)
            self.elements.insert(position, insert_index)

    def to_list(self):
        """Converts the vector to an array of the elements within the vector"""
        output = []
        for i in range(1, len(self.elements), 2):
            output.append(self.elements[i])
        return output

    def serialize(self):
        # TODO: the JS version forces rounding on the elements upon insertion
        # to ensure symmetry upon serialization
        return [round(element, 3) for element in self.elements]

    @property
    def magnitude(self):
        if not self._magnitude:
            sum_of_squares = 0
            for i in range(1, len(self.elements), 2):
                value = self.elements[i]
                sum_of_squares += value * value

            self._magnitude = sqrt(sum_of_squares)

        return self._magnitude

    def dot(self, other):
        """Calculates the dot product of this vector and another vector."""
        dot_product = 0
        a = self.elements
        b = other.elements
        a_len = len(a)
        b_len = len(b)
        i = j = 0

        while i < a_len and j < b_len:
            a_val = a[i]
            b_val = b[j]
            if a_val < b_val:
                i += 2
            elif a_val > b_val:
                j += 2
            else:
                dot_product += a[i + 1] * b[j + 1]
                i += 2
                j += 2

        return dot_product

    def similarity(self, other):
        """Calculates the cosine similarity between this vector and another
        vector."""
        if self.magnitude == 0 or other.magnitude == 0:
            return 0

        return self.dot(other) / self.magnitude
