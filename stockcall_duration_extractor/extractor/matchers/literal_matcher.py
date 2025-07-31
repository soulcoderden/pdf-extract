"""Literal pattern matcher."""

from __future__ import annotations

from typing import Iterable, Optional, Dict, Any


def match_literal(sentences: Iterable[str], literals: Iterable[dict]) -> Optional[Dict[str, Any]]:
    """Return match info if any literal pattern is found."""
    for sentence in sentences:
        lower_sentence = sentence.lower()
        for entry in literals:
            pat = entry.get("pattern", "").lower()
            if pat and pat in lower_sentence:
                return {
                    "matched_sentence": sentence,
                    "pattern": entry.get("pattern"),
                    "normalized_value": entry.get("normalized_value"),
                    "unit": entry.get("unit"),
                    "confidence": entry.get("confidence"),
                }
    return None
