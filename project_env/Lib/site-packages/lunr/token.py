from __future__ import unicode_literals

from builtins import str

import six


@six.python_2_unicode_compatible
class Token:
    def __init__(self, string="", metadata=None):
        self.string = string
        self.metadata = metadata or {}

    def __str__(self):
        return self.string

    def __repr__(self):
        return '<Token "{}">'.format(str(self))

    def update(self, fn):
        """A token update function is used when updating or optionally
        when cloning a token."""
        # TODO: we require functions to have two parameters, JS doesn't care
        self.string = fn(self.string, self.metadata)
        return self

    def clone(self, fn=None):
        """Applies the given function to the wrapped string token."""
        fn = fn or (lambda s, m: s)
        return Token(fn(self.string, self.metadata), self.metadata)
