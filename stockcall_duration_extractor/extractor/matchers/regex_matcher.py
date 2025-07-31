"""Regex pattern matcher."""

from __future__ import annotations

from typing import Iterable, Optional, Dict, Any
import re


def match_regex(sentences: Iterable[str], regexes: Iterable[dict]) -> Optional[Dict[str, Any]]:
    """Return match info if any regex pattern matches."""
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
