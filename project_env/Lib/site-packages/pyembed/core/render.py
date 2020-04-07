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


class PyEmbedRenderer(object):
    """Base class for rendering OEmbed responses."""

    def render(self, content_url, response):
        """Generates an HTML representation of an OEmbed response.

        :param content_url: the content URL.
        :param response: the response to render.
        :returns: an HTML representation of the resource.
        """
        raise NotImplementedError(
            'No render method for renderer of type %s' % type(self).__name__)


class DefaultRenderer(PyEmbedRenderer):
    """Default renderer, using a simple representation of each response
    type.
    """

    TEMPLATES = {
        'link': '<a href="%(content_url)s">%(title)s</a>',
        'photo': '<img src="%(url)s" width="%(width)s" height="%(height)s" />',
        'rich': '%(html)s',
        'video': '%(html)s'
    }

    def render(self, content_url, response):
        params = dict(response.__dict__)
        params['content_url'] = content_url

        return self.TEMPLATES[response.type] % params
