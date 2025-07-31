"""Duration pattern matching engine."""
from __future__ import annotations

from typing import Iterable, Optional, Dict, Any

import re

from pattern_store.pattern_loader import get_patterns


def match_duration_patterns(sentences: Iterable[str]) -> Optional[Dict[str, Any]]:
    """Match duration patterns within the provided sentences.

    This first checks for literal string patterns and then attempts regex based
    patterns before falling back to fuzzy matching (not yet implemented).
    """
    patterns = get_patterns()
    literals = patterns.get("literal_patterns", [])
    regexes = patterns.get("regex_patterns", [])

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

    # Try regex-based patterns
    for sentence in sentences:
        for entry in regexes:
            regex = entry.get("pattern", "")
            if not regex:
                continue
            match = re.search(regex, sentence, flags=re.IGNORECASE)
            if match:
                group_idx = entry.get("extract_group", 1)
                normalized_value = None
                try:
                    value_str = match.group(group_idx)
                    normalized_value = int(value_str)
                except (IndexError, ValueError, TypeError):
                    continue

                unit = entry.get("unit")
                unit_group = entry.get("unit_group")
                if unit_group is not None:
                    try:
                        unit = match.group(unit_group)
                    except IndexError:
                        pass
                elif unit is None and match.lastindex and match.lastindex >= 2:
                    unit = match.group(2)

                return {
                    "matched_sentence": sentence,
                    "pattern": regex,
                    "normalized_value": normalized_value,
                    "unit": unit,
                    "confidence": entry.get("confidence"),
                }

    return None
