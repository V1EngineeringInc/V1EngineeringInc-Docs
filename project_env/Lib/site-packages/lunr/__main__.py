from __future__ import unicode_literals


from past.builtins import basestring

from lunr import languages as lang
from lunr.builder import Builder
from lunr.stemmer import stemmer
from lunr.trimmer import trimmer
from lunr.stop_word_filter import stop_word_filter


def lunr(ref, fields, documents, languages=None):
    """A convenience function to configure and construct a lunr.Index.

    Args:
        ref (str): The key in the documents to be used a the reference.
        fields (list): A list of strings defining fields in the documents to
            index. Optionally a list of dictionaries with three keys:
            `field_name` defining the document's field, `boost` an integer
            defining a boost to be applied to the field, and `extractor`
            a callable taking the document as a single argument and returning
            a string located in the document in a particular way.
        documents (list): The list of dictonaries representing the documents
            to index. Optionally a 2-tuple of dicts, the first one being
            the document and the second the associated attributes to it.
        languages (str or list, optional): The languages to use if using
            NLTK language support, ignored if NLTK is not available.

    Returns:
        Index: The populated Index ready to search against.
    """
    if languages is not None and lang.LANGUAGE_SUPPORT:
        if isinstance(languages, basestring):
            languages = [languages]

        unsupported_languages = set(languages) - set(lang.SUPPORTED_LANGUAGES)
        if unsupported_languages:
            raise RuntimeError(
                "The specified languages {} are not supported, "
                "please choose one of {}".format(
                    ", ".join(unsupported_languages),
                    ", ".join(lang.SUPPORTED_LANGUAGES.keys()),
                )
            )
        builder = lang.get_nltk_builder(languages)
    else:
        builder = Builder()
        builder.pipeline.add(trimmer, stop_word_filter, stemmer)
        builder.search_pipeline.add(stemmer)

    builder.ref(ref)
    for field in fields:
        if isinstance(field, dict):
            builder.field(**field)
        else:
            builder.field(field)

    for document in documents:
        if isinstance(document, (tuple, list)):
            builder.add(document[0], attributes=document[1])
        else:
            builder.add(document)

    return builder.build()
