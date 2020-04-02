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

import functools
import json
import re

from bs4 import BeautifulSoup
from pkg_resources import resource_filename
import requests

from pyembed.core.error import PyEmbedError


try:  # pragma: no cover
    from urlparse import parse_qsl, urljoin, urlsplit, urlunsplit
    from urllib import urlencode
except ImportError:  # pragma: no cover
    from urllib.parse import parse_qsl, urljoin, urlsplit, urlunsplit, urlencode

from itertools import product

MEDIA_TYPES = [
    {'format': 'json', 'media_type': 'application/json+oembed'},
    {'format': 'xml', 'media_type': 'text/xml+oembed'}
]
FORMATS = [media_type['format'] for media_type in MEDIA_TYPES]

class PyEmbedDiscoveryError(PyEmbedError):
    """Thrown if there is an error discovering an OEmbed URL."""


class PyEmbedDiscoverer(object):
    """Base class for discovering OEmbed URLs."""

    def get_oembed_url(self, url, oembed_format=None):  # pragma: no cover
        """Retrieves the OEmbed URL for a given resource.

        Deprecated - use get_oembed_urls instead.

        :param url: resource URL.
        :param oembed_format: if supplied, restricts the format to use for OEmbed.  If
                       None, then the first URL found will be used.  One of
                       'json', 'xml'.

        :returns: the OEmbed URL for the resource.
        :raises PyEmbedDiscoveryError: if there is an error getting the OEmbed URL.
        """
        urls = self.get_oembed_urls(url, oembed_format)

        if not urls:
            raise PyEmbedDiscoveryError(
                'Could not find OEmbed URL for %s' % url)

        return urls[0]

    def get_oembed_urls(self, url, oembed_format=None):
        """Retrieves the OEmbed URLs for a given resource.

        :param url: resource URL.
        :param oembed_format: if supplied, restricts the format to use for OEmbed.  If
                       None, then the first URL found will be used.  One of
                       'json', 'xml'.

        :returns: a list of OEmbed URLs for the resource.
        :raises PyEmbedDiscoveryError: if there is an error getting the OEmbed URLs.
        """
        raise NotImplementedError(
            'No get_oembed_urls method for discoverer of type %s' % type(self).__name__)


class AutoDiscoverer(PyEmbedDiscoverer):
    """Discoverer that tries to automatically find the OEmbed URL within the
    HTML page.
    """

    def get_oembed_urls(self, url, oembed_format=None):
        media_type = self.__get_type(oembed_format)
        response = requests.get(url)

        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('link', type=media_type, href=True)

            for link in links:
                yield urljoin(url, link['href'])

    @staticmethod
    def __get_type(oembed_format):
        if not oembed_format:
            return [media_type['media_type'] for media_type in MEDIA_TYPES]

        media_types = [media_type['media_type'] for media_type in MEDIA_TYPES if media_type['format'] == oembed_format]

        if not media_types:
            raise PyEmbedDiscoveryError(
                'Invalid format %s specified (must be json or xml)' % oembed_format)

        return media_types


class StaticDiscoverer(PyEmbedDiscoverer):
    """Discoverer that uses a static list of endpoints to discover the OEmbed
       URL.
    """

    def __init__(self, endpoints):
        self.endpoints = endpoints

    def get_oembed_urls(self, url, oembed_format=None):
        if oembed_format and oembed_format not in FORMATS:
            raise PyEmbedDiscoveryError(
                'Invalid format %s specified (must be json or xml)' % oembed_format)

        formats = [oembed_format] if oembed_format else FORMATS

        for (endpoint, oembed_format) in product(self.endpoints, formats):
            if endpoint.matches(url, oembed_format):
                yield endpoint.build_oembed_url(url, oembed_format)

    @staticmethod
    def _build_endpoints_from_providers(providers):
        endpoints = []

        for provider in providers:
            for endpoint in provider["endpoints"]:
                if 'schemes' in endpoint and 'url' in endpoint:
                    endpoints.append(StaticDiscoveryEndpoint(endpoint))

        return endpoints


class StaticDiscoveryEndpoint(object):
    """Applies static discovery rules for a single endpoint.
    """

    def __init__(self, endpoint):
        self.matchers = [self.__create_matcher(s)
                         for s in endpoint.get('schemes')]
        self.endpoint = endpoint.get('url')
        self.oembed_formats = endpoint.get('formats')

    def matches(self, url, oembed_format=None):
        if not self.__format_matches(oembed_format):
            return False

        return any((matcher(url) for matcher in self.matchers))

    def build_oembed_url(self, content_url, oembed_format):
        format_endpoint = self.__add_format_to_endpoint(oembed_format)
        scheme, netloc, path, query_string, fragment = urlsplit(
            format_endpoint)
        query_params = parse_qsl(query_string)
        query_params.append(('url', content_url))

        if oembed_format:
            query_params.append(('format', oembed_format))

        new_query_string = urlencode(query_params, doseq=True)
        return urlunsplit((scheme, netloc, path, new_query_string, fragment))

    def __create_matcher(self, scheme_url):
        scheme, netloc, path, query_string, fragment = urlsplit(scheme_url)
        netloc_regex = re.compile(netloc.replace('*.', '.*\.?'))
        path_regex = re.compile(path.replace('*', '.*'))

        return functools.partial(self.__matcher, netloc_regex, path_regex)

    @staticmethod
    def __matcher(netloc_regex, path_regex, url):
        scheme, netloc, path, query_string, fragment = urlsplit(url)
        return netloc_regex.match(netloc) and path_regex.match(path)

    def __format_matches(self, oembed_format):
        return (not oembed_format) or \
               (not self.oembed_formats) or \
               (oembed_format in self.oembed_formats)

    def __add_format_to_endpoint(self, oembed_format):
        return self.endpoint.replace('{format}', oembed_format)


class FileDiscoverer(StaticDiscoverer):
    """Discoverer that uses a JSON file to discover the OEmbed URL.
    """
    def __init__(self, config_file):
        with open(config_file) as f:
            endpoints = StaticDiscoverer._build_endpoints_from_providers(json.load(f))

        super(FileDiscoverer, self).__init__(endpoints)


class UrlDiscoverer(StaticDiscoverer):
    """Discoverer that uses JSON from a URL to discover the OEmbed URL.
    """
    def __init__(self, url):
        self.url = url
        self.endpoints = None

    def get_oembed_urls(self, url, oembed_format=None):
        if not self.endpoints:
            response = requests.get(self.url)
            try:
                providers = response.json()
            except ValueError:
                providers = None

            if not response.ok or not providers:
                raise PyEmbedDiscoveryError('Failed to get %s (status code %s)' % (
                    self.url, response.status_code))

            self.endpoints = StaticDiscoverer._build_endpoints_from_providers(providers)

        return super(UrlDiscoverer, self).get_oembed_urls(url, oembed_format)


class ChainingDiscoverer(PyEmbedDiscoverer):
    """Discoverer that delegates to a sequence of other discoverers, returning
    the first valid result."""

    def __init__(self, delegates):
        self.delegates = delegates

    def get_oembed_urls(self, url, oembed_format=None):
        seen_oembed_urls = set()

        for delegate in self.delegates:
            try:
                for oembed_url in delegate.get_oembed_urls(url, oembed_format):
                    if oembed_url not in seen_oembed_urls:
                        seen_oembed_urls.add(oembed_url)
                        yield oembed_url
            except PyEmbedDiscoveryError:
                pass


class DefaultDiscoverer(ChainingDiscoverer):
    """Discoverer that uses auto-discovery, followed by the included config
    file."""

    def __init__(self):
        super(DefaultDiscoverer, self).__init__([
            FileDiscoverer(
                resource_filename(__name__, 'config/providers.json')),
            UrlDiscoverer('http://oembed.com/providers.json'),
            AutoDiscoverer()
        ])
