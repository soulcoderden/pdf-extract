"""Fuzzy term matcher."""

from __future__ import annotations

from typing import Iterable, Optional, Dict, Any


def match_fuzzy_terms(sentences: Iterable[str], fuzzy_terms: Iterable) -> Optional[Dict[str, Any]]:
    """Return match info if any fuzzy term is present."""
    for sentence in sentences:
        lower_sentence = sentence.lower()
        for entry in fuzzy_terms:
            if isinstance(entry, dict):
                term = entry.get("term", "").lower()
                mapped_value = entry.get("mapped_value")
                unit = entry.get("unit")
                confidence = entry.get("confidence")
            else:
                term = str(entry).lower()
                mapped_value = None
                unit = None
                confidence = None

            if term and term in lower_sentence:
                return {
                    "matched_sentence": sentence,
                    "pattern": entry.get("term", term) if isinstance(entry, dict) else entry,
                    "normalized_value": mapped_value,
                    "unit": unit,
                    "confidence": confidence,
                }
    return None
