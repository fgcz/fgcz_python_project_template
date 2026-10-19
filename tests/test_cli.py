"""Tests for the example command-line interface."""

from collections.abc import Iterator

import pytest
from loguru import logger

from fgcz_reference_project import cli


@pytest.fixture(autouse=True)
def _reset_logging() -> Iterator[None]:
    yield
    logger.remove()


def test_main_prints_slug(capsys: pytest.CaptureFixture[str]) -> None:
    assert cli.main(["Example Project"]) == 0

    captured = capsys.readouterr()
    assert captured.out == "example-project\n"
    assert "Slug for" not in captured.err


def test_main_verbose_logs_debug(capsys: pytest.CaptureFixture[str]) -> None:
    assert cli.main(["--verbose", "Example Project"]) == 0

    captured = capsys.readouterr()
    assert captured.out == "example-project\n"
    assert "Slug for 'Example Project': 'example-project'" in captured.err


def test_main_reports_invalid_name(capsys: pytest.CaptureFixture[str]) -> None:
    assert cli.main(["///"]) == 1

    captured = capsys.readouterr()
    assert captured.out == ""
    assert "at least one letter or digit" in captured.err
