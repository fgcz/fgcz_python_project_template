"""Command-line interface for the reference project."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

import cyclopts
from loguru import logger

from fgcz_reference_project import naming

if TYPE_CHECKING:
    from collections.abc import Sequence

app = cyclopts.App(
    name="fgcz-reference",
    help="Normalize a project name to a stable slug.",
)


@app.default
def slug(name: str, *, verbose: bool = False) -> int:
    """Print the stable slug for a project name.

    Args:
        name: Human-readable project name.
        verbose: Also log debug messages to stderr.

    Returns:
        Exit code: 0 on success, 1 when the name has no letters or digits.
    """
    # The CLI owns logging configuration; library modules only emit records.
    logger.remove()
    logger.add(sys.stderr, level="DEBUG" if verbose else "INFO")

    try:
        result = naming.project_slug(name)
    except ValueError as error:
        logger.error(str(error))
        return 1

    print(result)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line interface and return its exit code."""
    return app(argv, result_action="return_value")
