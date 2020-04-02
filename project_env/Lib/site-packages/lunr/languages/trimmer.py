from __future__ import unicode_literals

import re


def generate_trimmer(word_characters):
    """Returns a trimmer function from a string of word characters.

    TODO: lunr-languages ships with lists of word characters for each language
    I haven't found an equivalent in Python, we may need to copy it.
    """
    start_re = r"^[^{}]+".format(word_characters)
    end_re = r"[^{}]+$".format(word_characters)

    def trimmer(token, i=None, tokens=None):
        def trim(s, metadata=None):
            s = re.sub(start_re, "", s)
            s = re.sub(end_re, "", s)
            return s

        return token.update(trim)

    return trimmer
