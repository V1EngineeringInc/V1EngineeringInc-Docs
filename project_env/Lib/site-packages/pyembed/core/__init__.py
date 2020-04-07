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

import requests

from pyembed.core import consumer
from pyembed.core.discovery import DefaultDiscoverer
from pyembed.core.error import PyEmbedError
from pyembed.core.render import DefaultRenderer


class PyEmbed(object):
    def __init__(self, discoverer=None, renderer=None):
        """OEmbed consumer with automatic discovery.

        :param renderer: (optional) renderer to render the response.
        """
        if not discoverer:
            discoverer = DefaultDiscoverer()

        if not renderer:
            renderer = DefaultRenderer()

        self.discoverer = discoverer
        self.renderer = renderer

    def embed(self, url, max_width=None, max_height=None):
        """Returns an HTML representation of a resource, given a URL.  This
           can be directly embedded in a web page.

        :param url: the content URL.
        :param max_width: (optional) the maximum width of the embedded resource.
        :param max_height: (optional) the maximum height of the embedded resource.
        :returns: an HTML representation of the resource.
        :raises PyEmbedError: if there is an error fetching the response.
        """
        try:
            oembed_urls = self.discoverer.get_oembed_urls(url)
            response = consumer.get_first_oembed_response(
                oembed_urls, max_width=max_width, max_height=max_height)
        except requests.exceptions.RequestException as e:
            raise PyEmbedError(e)

        return self.renderer.render(url, response)
