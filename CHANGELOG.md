# Changelog

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- The `check-tests-structure` hook, consolidated from
  `leoschwarz/check-tests-structure` into `.ci/check-tests-structure/` and
  published from this repository through `.pre-commit-hooks.yaml`, so that FGCZ
  projects no longer depend on a personal account. It runs on this repository in
  the `pre-commit` stage, and its own test suite runs in the `pre-push` stage.

- CI matrix that runs the tests across the supported Python range and
  dependency-resolution bounds (`lowest-direct` on the minimum interpreter,
  `highest` on the maximum).
- Dependabot configuration for the `uv` and GitHub Actions ecosystems.
- Documented how to switch the type-check gate from Pyright to basedpyright.

### Changed

- Documented the reference project's intent and complete quality-gate stack.
- Enabled blocking Ruff complexity and function-design checks.
- Switched the build backend from hatchling to `uv_build`.
- Run Ruff as a local `uv run` hook so its version lives only in the lockfile;
  upgraded Ruff to 0.16.0 and expanded the lint rule set (security, docstrings,
  annotations, pytest, pathlib, and more).

## [0.1.0] - 2026-07-23

### Added

- Initial reference package, CLI, tests, documentation, and aligned quality gates.
