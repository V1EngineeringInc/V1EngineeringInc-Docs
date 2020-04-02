from __future__ import unicode_literals

import re

from lunr.pipeline import Pipeline

start_re = re.compile(r"^\W+")
end_re = re.compile(r"\W+$")


def trimmer(token, i=None, tokens=None):
    def trim(s, metadata=None):
        s = start_re.sub("", s)
        s = end_re.sub("", s)
        return s

    return token.update(trim)


Pipeline.register_function(trimmer, "trimmer")
