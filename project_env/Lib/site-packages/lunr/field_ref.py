from __future__ import unicode_literals

import six

from lunr.exceptions import BaseLunrException


@six.python_2_unicode_compatible
class FieldRef:

    JOINER = "/"

    def __init__(self, doc_ref, field_name, string_value=None):
        self.doc_ref = doc_ref
        self.field_name = field_name
        self._string_value = string_value

    def __repr__(self):
        return '<FieldRef field="{}" ref="{}">'.format(self.field_name, self.doc_ref)

    @classmethod
    def from_string(cls, string):
        if cls.JOINER not in string:
            raise BaseLunrException("Malformed field ref string")
        field_ref, doc_ref = string.split(cls.JOINER, 1)
        return cls(doc_ref, field_ref, string)

    def __str__(self):
        if self._string_value is None:
            self._string_value = self.field_name + self.JOINER + str(self.doc_ref)

        return self._string_value
