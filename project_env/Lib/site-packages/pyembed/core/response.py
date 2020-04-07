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


class OEmbedResponse(object):
    """Base representation of an OEmbed response.  Each response type is
       represented by a different subclass.
    """

    def __init__(self, value_function):
        """Constructor.

        :param value_function: function that takes a single string parameter,
        and returns the value of the field with that name from an OEmbed
        response (or None, if the field is not present).
        """
        for field in self.fields():
            self.__set_attr_from_dict(value_function, field)

    def __set_attr_from_dict(self, value_function, field):
        self.__dict__[field] = value_function(field)

    def fields(self):
        """Returns the list of field names applicable for this response.

        On this base class, this is the list of fields common to all response
        types.  Subclasses can override this to add in type-specific fields.

        :returns: list of field names applicable for this response.
        """
        return ['type',
                'version',
                'title',
                'author_name',
                'author_url',
                'provider_name',
                'provider_url',
                'cache_age',
                'thumbnail_url',
                'thumbnail_width',
                'thumbnail_height']

    def __setattr__(self, *args):
        raise TypeError('Responses are immutable')


class OEmbedPhotoResponse(OEmbedResponse):
    """Represents an OEmbed photo response."""

    def fields(self):
        return super(OEmbedPhotoResponse, self).fields() + \
            ['url', 'width', 'height']


class OEmbedVideoResponse(OEmbedResponse):
    """Represents an OEmbed video response."""

    def fields(self):
        return super(OEmbedVideoResponse, self).fields() + \
            ['html', 'width', 'height']


class OEmbedLinkResponse(OEmbedResponse):
    """Represents an OEmbed link response."""
    pass


class OEmbedRichResponse(OEmbedResponse):
    """Represents an OEmbed rich response."""

    def fields(self):
        return super(OEmbedRichResponse, self).fields() + \
            ['html', 'width', 'height']
