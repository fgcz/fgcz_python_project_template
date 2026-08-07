<!-- Managed by agent: keep commands and file references verified -->
<!-- Last updated: 2026-07-23 | Last verified: 2026-07-23 -->

# AGENTS.md - documentation

## Overview

Applies to MkDocs sources in `docs/`.

## Setup

Install the locked documentation group from the repository root:
`uv sync --frozen --group docs`.

## Commands

| Task | Command |
|---|---|
| Strict build | `uv run --frozen --group docs mkdocs build --strict` |

## Files

| File | Purpose |
|---|---|
| `index.md` | Project overview and library example |
| `check-tests-structure.md` | Shared hook: configuration and consumer snippets |
| `getting-started.md` | Installation and first command |
| `development.md` | Local and CI quality workflow |

## Code style

- Use one H1 page title and relative links for internal pages.
- Keep commands synchronized with `.pre-commit-config.yaml`.
- Keep examples runnable against the checked-in package.

## Security

- Never include credentials, internal hosts, or sensitive datasets.

## Checklist

- Run the strict documentation build.
- Check that every documented path and command exists.

## Patterns to Follow

Use `development.md` for command documentation and `index.md` for concise code
examples.

## When stuck

Read `mkdocs.yml`, then compare the command with the `mkdocs-strict` hook.
