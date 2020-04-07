from __future__ import unicode_literals

from builtins import str

from copy import deepcopy
import re

from lunr.token import Token
from lunr.utils import as_string

SEPARATOR = re.compile(r"[\s\-]+")


def Tokenizer(obj, metadata=None, separator=SEPARATOR):
    """Splits a string into tokens ready to be inserted into the search index.

    This tokenizer will convert its parameter to a string by calling `str` and
    then will split this string on characters matching `separator`.
    Lists will have their elements converted to strings and wrapped in a lunr
    `Token`.

    Optional metadata can be passed to the tokenizer, this metadata will be
    cloned and added as metadata to every token that is created from the object
    to be tokenized.
    """
    if obj is None:
        return []

    metadata = metadata or {}

    if isinstance(obj, (list, tuple)):
        return [
            Token(as_string(element).lower(), deepcopy(metadata)) for element in obj
        ]

    string = str(obj).lower()
    length = len(string)
    tokens = []
    slice_start = 0
    for slice_end in range(length + 1):
        char = string[slice_end] if slice_end != length else ""
        slice_length = slice_end - slice_start
        if separator.match(char) or slice_end == length:
            if slice_length > 0:
                token_metadata = {}
                token_metadata["position"] = [slice_start, slice_length]
                token_metadata["index"] = len(tokens)
                token_metadata.update(metadata)

                sl = slice(slice_start, slice_end)
                tokens.append(Token(string[sl], token_metadata))

            slice_start = slice_end + 1

    return tokens
