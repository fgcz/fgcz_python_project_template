"""Naming helpers used by the reference command-line application."""

from __future__ import annotations

import re

_NON_ALPHANUMERIC = re.compile(r"[^a-z0-9]+")


def project_slug(name: str) -> str:
    """Convert a human-readable project name to a stable lowercase slug.

    Args:
        name: Human-readable project name.

    Returns:
        A lowercase slug containing letters, digits, and single hyphens.

    Raises:
        ValueError: The name contains no letters or digits.
    """
    slug = _NON_ALPHANUMERIC.sub("-", name.strip().lower()).strip("-")
    if not slug:
        message = "Project name must contain at least one letter or digit."
        raise ValueError(message)
    return slug
