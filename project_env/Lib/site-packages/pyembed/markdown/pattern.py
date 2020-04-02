# The MIT License(MIT)

# Copyright (c) 2013-2014 Matt Thomson

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from markdown.inlinepatterns import Pattern

try:  # pragma: no cover
    from urlparse import parse_qs
except ImportError:  # pragma: no cover
    from urllib.parse import parse_qs

REMBED_PATTERN = '\[!embed(\?(.*))?\]\((.*)\)'


class PyEmbedPattern(Pattern):

    def __init__(self, pyembed, md):
        super(PyEmbedPattern, self).__init__(REMBED_PATTERN)

        self.pyembed = pyembed
        self.md = md

    def handleMatch(self, m):
        url = m.group(4)
        (max_width, max_height) = self.__parse_params(m.group(3))
        html = self.pyembed.embed(url, max_width, max_height)
        return self.md.htmlStash.store(html)

    def __parse_params(self, query_string):
        if not query_string:
            return None, None

        query_params = parse_qs(query_string)
        return (self.__get_query_param(query_params, 'max_width'),
                self.__get_query_param(query_params, 'max_height'))

    @staticmethod
    def __get_query_param(query_params, name):
        if name in query_params:
            return int(query_params[name][0])
        else:
            return None
