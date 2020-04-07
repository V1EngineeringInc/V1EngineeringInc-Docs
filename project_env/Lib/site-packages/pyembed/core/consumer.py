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

import logging

import requests

from pyembed.core import parse
from pyembed.core.error import PyEmbedError

try:  # pragma: no cover
    from urlparse import parse_qsl, urljoin, urlsplit, urlunsplit
    from urllib import urlencode
except ImportError:  # pragma: no cover
    from urllib.parse import parse_qsl, urljoin, urlsplit, urlunsplit, urlencode


class PyEmbedConsumerError(PyEmbedError):
    """Thrown if there is an error discovering an OEmbed URL."""


def get_first_oembed_response(oembed_urls, max_width=None, max_height=None):
    """Fetches an OEmbed response from a list of OEmbed URLs.  The URLs will be
    tried in turn until one returns successfully.

    :param oembed_urls: an iterable of OEmbed URLs.
    :param max_width: (optional) the maximum width of the embedded resource.
    :param max_height: (optional) the maximum height of the embedded resource.
    :returns: an PyEmbedResponse, representing the resource to embed.
    :raises PyEmbedError: if there is an error fetching the response.
    """
    for oembed_url in oembed_urls:
        try:
            return get_oembed_response(oembed_url, max_width=max_width, max_height=max_height)
        except PyEmbedError:
            logging.warn('Error consuming URL %s' % oembed_url, exc_info=True)

    raise PyEmbedConsumerError('No valid OEmbed responses for URLs %s' % oembed_urls)


def get_oembed_response(oembed_url, max_width=None, max_height=None):
    """Fetches an OEmbed response for a given URL.

    Deprecated: use get_first_oembed_response.

    :param oembed_url: the OEmbed URL.
    :param max_width: (optional) the maximum width of the embedded resource.
    :param max_height: (optional) the maximum height of the embedded resource.
    :returns: an PyEmbedResponse, representing the resource to embed.
    :raises PyEmbedError: if there is an error fetching the response.
    """

    response = requests.get(__format_url(oembed_url, max_width, max_height))

    if not response.ok:
        raise PyEmbedConsumerError('Failed to get %s (status code %s)' % (
            oembed_url, response.status_code))

    content_type = response.headers['content-type'].split(';')[0]
    return parse.parse_oembed(response.text, content_type)


def __format_url(oembed_url, max_width=None, max_height=None):
    scheme, netloc, path, query_string, fragment = urlsplit(oembed_url)
    query_params = parse_qsl(query_string)

    if max_width is not None:
        query_params.append(('maxwidth', max_width))

    if max_height:
        query_params.append(('maxheight', max_height))

    new_query_string = urlencode(query_params, doseq=True)

    return urlunsplit((scheme, netloc, path, new_query_string, fragment))
