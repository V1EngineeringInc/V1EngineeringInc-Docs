def get_language_stemmer(language):
    """Retrieves the SnowballStemmer for a particular language.

    Args:
        language (str): ISO-639-1 code of the language.
    """
    from lunr.languages import SUPPORTED_LANGUAGES
    from nltk.stem.snowball import SnowballStemmer

    return SnowballStemmer(SUPPORTED_LANGUAGES[language])


def nltk_stemmer(stemmer, token, i=None, tokens=None):
    """Wrapper around a NLTK SnowballStemmer, which includes stop words for
    each language.

    Args:
        stemmer (SnowballStemmer): Stemmer instance that performs the stemming.
        token (lunr.Token): The token to stem.
        i (int): The index of the token in a set.
        tokens (list): A list of tokens representing the set.
    """

    def wrapped_stem(token, metadata=None):
        return stemmer.stem(token)

    return token.update(wrapped_stem)
