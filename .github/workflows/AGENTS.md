<!-- Managed by agent: keep commands and file references verified -->
<!-- Last updated: 2026-07-23 | Last verified: 2026-07-23 -->

# AGENTS.md - GitHub workflows

## Overview

Applies to GitHub Actions workflows in this directory.

## Files

| File | Purpose |
|---|---|
| `ci.yml` | Pull-request and main-branch quality gate |
| `pages.yml` | Strict documentation build and Pages deployment |
| `security.yml` | Weekly and manual dependency audit |

## Design

- `.pre-commit-config.yaml` owns quality commands.
- `ci.yml` invokes the complete pre-commit and pre-push stages so local and
  remote checks cannot drift.
- `DIFF_COVER_BASE` is `main` locally and the pull request base branch in CI.
- All dependency installation uses the frozen uv lockfile.

## Setup

GitHub runners install Python through uv and sync only from `uv.lock`.

## Commands

Run the pre-commit and pre-push stages from the repository root before changing
workflow commands.

## Code style

- Keep permissions minimal and declare them explicitly.
- Pin actions to explicit released versions.
- Preserve full Git history where changed-line coverage needs the base branch.

## Security

- Do not add secrets or `secrets: inherit`.
- Add a local hook before adding a new blocking CI-only command.

## Checklist

- Parse workflow YAML.
- Run both hook stages locally.
- Confirm the scheduled audit invokes the manual local hook.

## Patterns to Follow

Use `ci.yml` for mirrored local gates and `security.yml` for scheduled manual
hooks.

## When stuck

Compare workflow commands with `.pre-commit-config.yaml`; the hook definition is
the command source of truth.
