"""Utilities for cleaning and segmenting text."""

from __future__ import annotations

import spacy

# Load spaCy model at module import time.
# This avoids re-loading for each function call.
_nlp = spacy.load("en_core_web_sm")


def segment_sentences(text: str) -> list[str]:
    """Split raw text into sentences using spaCy.

    Parameters
    ----------
    text : str
        The raw text to segment.

    Returns
    -------
    list[str]
        List of individual sentences with surrounding whitespace removed.
    """
    doc = _nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]
    return [s for s in sentences if s]
