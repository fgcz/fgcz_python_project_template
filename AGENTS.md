<!-- FOR AI AGENTS - Human readability is a side effect, not a goal -->
<!-- Managed by agent: keep commands and file references verified -->
<!-- Last updated: 2026-07-23 | Last verified: 2026-07-23 -->

# AGENTS.md

**Precedence:** the closest `AGENTS.md` to changed files wins. Explicit user
instructions override repository files.

## Commands

| Task | Command |
|---|---|
| Install | `uv sync --frozen --group docs` |
| Fast checks | `uv run pre-commit run --hook-stage pre-commit --all-files` |
| Full gate | `uv run pre-commit run --hook-stage pre-push --all-files` |
| Single test | `uv run pytest tests/test_naming.py -q` |
| Security audit | `uv run pre-commit run dependency-audit --hook-stage manual --all-files` |

## File map

| Path | Purpose |
|---|---|
| `src/fgcz_reference_project/` | Minimal typed library and CLI |
| `tests/` | Unit and CLI error-path tests |
| `scripts/` | Changed-line coverage and wheel inspection |
| `docs/` | MkDocs source; see `docs/AGENTS.md` |
| `.github/workflows/` | CI, Pages, and scheduled audit; see its `AGENTS.md` |
| `.ci/check-tests-structure/` | Vendored `check-tests-structure` hook; self-contained subproject |
| `.pre-commit-hooks.yaml` | Hook manifest other repositories consume |

## Golden samples

| For | Reference |
|---|---|
| Public typed function | `src/fgcz_reference_project/naming.py` |
| CLI boundary | `src/fgcz_reference_project/cli.py` |
| Tests | `tests/test_naming.py` and `tests/test_cli.py` |

## Project rules

- uv and `uv.lock` are the only dependency workflow; never add
  `requirements.txt`.
- Keep `src/fgcz_reference_project/__init__.py` empty; import from concrete
  modules.
- Pyright strict mode and 100% line/branch coverage are blocking.
- CLIs use `cyclopts`; logging uses `loguru`. Library modules only emit log
  records; the CLI entry point configures sinks and levels.
- Add domain-specific checks as hooks, then invoke the same hooks from CI.
- Record user-visible changes under `Unreleased` in `CHANGELOG.md`.
- `.ci/check-tests-structure/` is vendored, MIT-licensed, and keeps its own
  `pyproject.toml` and `uv.lock`; it is not a uv workspace member and not part of
  the reference distribution. Root Ruff lints it, but Pyright, coverage, and
  deptry deliberately exclude it. Run its suite with
  `uv run --directory .ci/check-tests-structure --frozen pytest`.
- Changing `.pre-commit-hooks.yaml` changes a public interface for other
  repositories; the `additional_dependencies` relative path there is what makes
  the subdirectory installable through pre-commit.

## Boundaries

### Always

- Fix the root cause of failing quality checks.
- Keep local hooks and GitHub Actions aligned.
- Run the smallest relevant check after edits and the full gate before handoff.

### Ask first

- Adding runtime dependencies or changing public interfaces.
- Lowering type, coverage, security, or documentation gates.

### Never

- Commit credentials, generated `public/`, build artifacts, or `.venv/`.
- Push, create a remote, or publish packages without explicit authorization.

## Scoped AGENTS.md

- [Documentation](./docs/AGENTS.md)
- [GitHub workflows](./.github/workflows/AGENTS.md)
