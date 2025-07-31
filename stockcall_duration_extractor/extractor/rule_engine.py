"""Duration pattern matching engine."""
from __future__ import annotations

from typing import Iterable, Optional, Dict, Any

from pattern_store.pattern_loader import get_patterns


def match_duration_patterns(sentences: Iterable[str]) -> Optional[Dict[str, Any]]:
    """Match duration patterns within the provided sentences.

    Currently only literal pattern matching is implemented.
    """
    patterns = get_patterns()
    literals = patterns.get("literal_patterns", [])

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
