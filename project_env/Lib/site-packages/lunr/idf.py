from __future__ import unicode_literals

import math


def idf(posting, document_count):
    """A function to calculate the inverse document frequency for a posting.
    This is shared between the builder and the index.
    """
    documents_with_term = 0
    for field_name in posting:
        if field_name == "_index":
            continue
        documents_with_term += len(posting[field_name].keys())

    x = (document_count - documents_with_term + 0.5) / (documents_with_term + 0.5)
    return math.log(1 + abs(x))
