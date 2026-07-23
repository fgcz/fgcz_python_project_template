"""Command-line interface for the reference project."""

from __future__ import annotations

import argparse

from fgcz_reference_project import naming


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fgcz-reference",
        description="Normalize a project name to a stable slug.",
    )
    parser.add_argument("name", help="Human-readable project name.")
    return parser


def main() -> int:
    """Run the example command-line interface."""
    parser = _parser()
    arguments = parser.parse_args()

    try:
        slug = naming.project_slug(arguments.name)
    except ValueError as error:
        parser.error(str(error))

    print(slug)
    return 0
