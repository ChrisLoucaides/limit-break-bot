import re
from synonyms import SYNONYMS


def normalize(text: str) -> str:
    """
    Normalize input text by:
    - lowercasing
    - removing punctuation
    - replacing synonyms with canonical terms
    """
    cleaned_text = _clean_text(text)
    words = _tokenize(cleaned_text)
    synonym_lookup = _build_synonym_lookup(SYNONYMS)
    normalized_words = _replace_with_canonical_terms(words, synonym_lookup)

    return _join_words(normalized_words)


def _clean_text(raw_text: str) -> str:
    """Lowercase and remove punctuation."""
    lowercase_text = raw_text.lower()
    return re.sub(r"[^\w\s]", "", lowercase_text)


def _tokenize(text: str) -> list[str]:
    """Split text into individual words."""
    return text.split()


def _build_synonym_lookup(synonym_dict: dict[str, list[str]]) -> dict[str, str]:
    """
    Convert synonyms structure into a reverse lookup:
    synonym -> canonical term
    """
    lookup = {}

    for canonical_term, synonym_list in synonym_dict.items():
        for synonym in synonym_list:
            lookup[synonym] = canonical_term

    return lookup


def _replace_with_canonical_terms(
    words: list[str],
    synonym_lookup: dict[str, str]
) -> list[str]:
    """Replace words with their canonical synonym if available."""
    return [
        synonym_lookup.get(word, word)
        for word in words
    ]


def _join_words(words: list[str]) -> str:
    """Join words back into a single string."""
    return " ".join(words)