"""Helper to load pattern definitions."""
from __future__ import annotations

from pathlib import Path
import yaml


def get_patterns() -> dict:
    """Load patterns from ``patterns_library.yaml`` and return as a dict."""
    yaml_path = Path(__file__).with_name("patterns_library.yaml")
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return {
        "literal_patterns": data.get("literal_patterns", []),
        "regex_patterns": data.get("regex_patterns", []),
        "fuzzy_terms": data.get("fuzzy_terms", []),
    }
