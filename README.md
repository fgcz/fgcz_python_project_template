# FGCZ Python Project Reference

This repository is a small, runnable reference for starting Python packages at
the Functional Genomics Center Zurich. Its purpose is to demonstrate a complete
package layout and an aligned local/remote quality workflow, not to provide
domain functionality that other projects should depend on.

The example slug library and CLI are intentionally minimal. They make the
package build, public interface, success path, error path, tests, coverage,
documentation, and console entry point concrete enough to validate. When
starting a real project, replace that example while retaining the relevant
structure and quality gates.

## What this reference includes

| Area | Included |
|---|---|
| Packaging | `src/` layout, `pyproject.toml`, hatchling, uv lockfile, typed-package marker, console entry point |
| Example | One typed library function and a small `argparse` CLI |
| Tests | Unit and CLI error-path tests with 100% line and branch coverage |
| Documentation | MkDocs Material site built with `--strict` and deployable to GitHub Pages |
| Agent guidance | Verified root and scoped `AGENTS.md` files with Claude/Gemini symlinks |
| Automation | Pre-commit, pre-push, pull-request CI, Pages deployment, and a weekly security audit |

## Quality gates

The GitHub Actions CI job invokes the same hook stages used locally, so bypassing
a local hook does not bypass the merge gate.

| Stage | Checks |
|---|---|
| `pre-commit` | Ruff lint and format, including complexity/design rules; strict Pyright; deptry |
| `pre-push` | pytest with 100% branch coverage; 100% changed-line coverage; sdist/wheel inspection; strict MkDocs |
| Manual and weekly CI | pip-audit against the frozen installed environment |

The hook definitions live in `.pre-commit-config.yaml`; CI calls the complete
stages rather than maintaining a second copy of their commands. Project-specific
checks should follow the same pattern.

## Quick start

```bash
uv sync --frozen --group docs
uv run pre-commit install --install-hooks
uv run fgcz-reference "Example Project"
uv run pre-commit run --hook-stage pre-commit --all-files
```

The full pre-push gate runs tests and branch coverage, changed-line coverage,
package inspection, and strict documentation:

```bash
uv run pre-commit run --hook-stage pre-push --all-files
```

See the [getting-started guide](docs/getting-started.md) and
[development guide](docs/development.md).

## Reusing this reference

Rename the distribution and import package, replace the example code and tests,
and adjust project metadata, documentation, license attribution, and supported
Python version. Keep local hooks and CI commands paired. Add domain-specific
gates only when the project needs them; examples include browser tests, notebook
validation, multiple installation profiles, or service integration tests.

## License

Apache-2.0.
