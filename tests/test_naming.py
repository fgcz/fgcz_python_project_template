"""Tests for project naming helpers."""

import pytest

from fgcz_reference_project import naming


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Example Project", "example-project"),
        ("  FGCZ / Proteomics 2026  ", "fgcz-proteomics-2026"),
        ("already-stable", "already-stable"),
    ],
)
def test_project_slug(name: str, expected: str) -> None:
    assert naming.project_slug(name) == expected


def test_project_slug_rejects_empty_value() -> None:
    with pytest.raises(ValueError, match="at least one letter or digit"):
        naming.project_slug(" -- ")
