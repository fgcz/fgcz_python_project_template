"""Tests for the example command-line interface."""

import sys

import pytest

from fgcz_reference_project import cli


def test_main_prints_slug(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(sys, "argv", ["fgcz-reference", "Example Project"])

    assert cli.main() == 0
    assert capsys.readouterr().out == "example-project\n"


def test_main_reports_invalid_name(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(sys, "argv", ["fgcz-reference", "///"])

    with pytest.raises(SystemExit) as error:
        cli.main()

    assert error.value.code == 2
    assert "at least one letter or digit" in capsys.readouterr().err
