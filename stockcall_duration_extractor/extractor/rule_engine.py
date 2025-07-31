"""Duration pattern matching engine."""
from __future__ import annotations

from typing import Iterable, Optional, Dict, Any

from pattern_store.pattern_loader import get_patterns
from .matchers import match_literal, match_regex, match_fuzzy_terms


def match_duration_patterns(sentences: Iterable[str]) -> Optional[Dict[str, Any]]:
    """Match duration patterns within ``sentences`` using different matchers."""
    patterns = get_patterns()

    result = match_literal(sentences, patterns.get("literal_patterns", []))
    if result:
        return result

    result = match_regex(sentences, patterns.get("regex_patterns", []))
    if result:
        return result

    return match_fuzzy_terms(sentences, patterns.get("fuzzy_terms", []))
