from __future__ import unicode_literals
from itertools import chain
from functools import partial

import lunr
from lunr.builder import Builder
from lunr.languages.trimmer import generate_trimmer
from lunr.languages.stemmer import nltk_stemmer, get_language_stemmer
from lunr.pipeline import Pipeline
from lunr.stop_word_filter import stop_word_filter, generate_stop_word_filter

# map from ISO-639-1 codes to SnowballStemmer.languages
# Languages not supported by nltk but by lunr.js: thai, japanese and turkish
# Languages upported by nltk but not lunr.js: arabic

SUPPORTED_LANGUAGES = {
    "ar": "arabic",
    "da": "danish",
    "nl": "dutch",
    "en": "english",
    "fi": "finnish",
    "fr": "french",
    "de": "german",
    "hu": "hungarian",
    "it": "italian",
    "no": "norwegian",
    "pt": "portuguese",
    "ro": "romanian",
    "ru": "russian",
    "es": "spanish",
    "sv": "swedish",
}

try:  # pragma: no cover
    import nltk

    LANGUAGE_SUPPORT = True
except ImportError:  # pragma: no cover
    LANGUAGE_SUPPORT = False


def _get_stopwords_and_word_characters(language):
    nltk.download("stopwords")
    verbose_language = SUPPORTED_LANGUAGES[language]
    stopwords = nltk.corpus.stopwords.words(verbose_language)
    # TODO: search for a more exhaustive list of word characters
    word_characters = {c for word in stopwords for c in word}
    return stopwords, word_characters


def get_nltk_builder(languages):
    """Returns a builder with stemmers for all languages added to it.

    Args:
        languages (list): A list of supported languages.
    """
    all_stemmers = []
    all_stopwords_filters = []
    all_word_characters = set()

    for language in languages:
        if language == "en":
            # use Lunr's defaults
            all_stemmers.append(lunr.stemmer.stemmer)
            all_stopwords_filters.append(stop_word_filter)
            all_word_characters.update({r"\w"})
        else:
            stopwords, word_characters = _get_stopwords_and_word_characters(language)
            all_stemmers.append(
                Pipeline.registered_functions["stemmer-{}".format(language)]
            )
            all_stopwords_filters.append(
                generate_stop_word_filter(stopwords, language=language)
            )
            all_word_characters.update(word_characters)

    builder = Builder()
    multi_trimmer = generate_trimmer("".join(sorted(all_word_characters)))
    Pipeline.register_function(
        multi_trimmer, "lunr-multi-trimmer-{}".format("-".join(languages))
    )
    builder.pipeline.reset()

    for fn in chain([multi_trimmer], all_stopwords_filters, all_stemmers):
        builder.pipeline.add(fn)
    for fn in all_stemmers:
        builder.search_pipeline.add(fn)

    return builder


def register_languages():
    """Register all supported languages to ensure compatibility."""
    for language in set(SUPPORTED_LANGUAGES) - {"en"}:
        language_stemmer = partial(nltk_stemmer, get_language_stemmer(language))
        Pipeline.register_function(language_stemmer, "stemmer-{}".format(language))


if LANGUAGE_SUPPORT:  # pragma: no cover
    # TODO: registering all possible stemmers feels unnecessary but it solves
    # deserializing with arbitrary language functions. Ideally the schema would
    # provide the language(s) for the index and we could register the stemmers
    # as needed
    register_languages()
