from __future__ import unicode_literals

import logging

from builtins import str
import six

from lunr.exceptions import BaseLunrException
from lunr.token import Token

log = logging.getLogger(__name__)


class Pipeline:
    """lunr.Pipelines maintain a list of functions to be applied to all tokens
    in documents entering the search index and queries ran agains the index.

    """

    registered_functions = {}

    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def __repr__(self):
        return '<Pipeline stack="{}">'.format(",".join(fn.label for fn in self._stack))

    # TODO: add iterator methods?

    @classmethod
    def register_function(cls, fn, label):
        """Register a function with the pipeline."""
        if label in cls.registered_functions:
            log.warning("Overwriting existing registered function %s", label)

        fn.label = label
        cls.registered_functions[fn.label] = fn

    @classmethod
    def load(cls, serialised):
        """Loads a previously serialised pipeline."""
        pipeline = cls()
        for fn_name in serialised:
            try:
                fn = cls.registered_functions[fn_name]
            except KeyError:
                raise BaseLunrException(
                    "Cannot load unregistered function ".format(fn_name)
                )
            else:
                pipeline.add(fn)

        return pipeline

    def add(self, *args):
        """Adds new functions to the end of the pipeline.

        Functions must accept three arguments:
        - Token: A lunr.Token object which will be updated
        - i: The index of the token in the set
        - tokens: A list of tokens representing the set
        """
        for fn in args:
            self.warn_if_function_not_registered(fn)
            self._stack.append(fn)

    def warn_if_function_not_registered(self, fn):
        try:
            return fn.label in self.registered_functions
        except AttributeError:
            log.warning(
                'Function "{}" is not registered with pipeline. '
                "This may cause problems when serialising the index.".format(
                    getattr(fn, "label", fn)
                )
            )

    def after(self, existing_fn, new_fn):
        """Adds a single function after a function that already exists in the
        pipeline."""
        self.warn_if_function_not_registered(new_fn)
        try:
            index = self._stack.index(existing_fn)
            self._stack.insert(index + 1, new_fn)
        except ValueError as e:
            six.raise_from(BaseLunrException("Cannot find existing_fn"), e)

    def before(self, existing_fn, new_fn):
        """Adds a single function before a function that already exists in the
        pipeline.

        """
        self.warn_if_function_not_registered(new_fn)
        try:
            index = self._stack.index(existing_fn)
            self._stack.insert(index, new_fn)
        except ValueError as e:
            six.raise_from(BaseLunrException("Cannot find existing_fn"), e)

    def remove(self, fn):
        """Removes a function from the pipeline."""
        try:
            self._stack.remove(fn)
        except ValueError:
            pass

    def run(self, tokens):
        """Runs the current list of functions that make up the pipeline against
        the passed tokens."""
        for fn in self._stack:
            results = []
            for i, token in enumerate(tokens):
                # JS ignores additional arguments to the functions but we
                # force pipeline functions to declare (token, i, tokens)
                # or *args
                result = fn(token, i, tokens)
                if not result:
                    continue
                if isinstance(result, (list, tuple)):  # simulate Array.concat
                    results.extend(result)
                else:
                    results.append(result)
            tokens = results

        return tokens

    def run_string(self, string, metadata=None):
        """Convenience method for passing a string through a pipeline and
        getting strings out. This method takes care of wrapping the passed
        string in a token and mapping the resulting tokens back to strings."""
        token = Token(string, metadata)
        return [str(tkn) for tkn in self.run([token])]

    def reset(self):
        self._stack = []

    def serialize(self):
        return [fn.label for fn in self._stack]
