# FGCZ Python Project Reference

A minimal, runnable reference repository for Python package structure and
automated quality gates at the Functional Genomics Center Zurich.

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
and adjust project metadata. Keep local hooks and CI commands paired. Add
domain-specific gates only when the project needs them.

## License

Apache-2.0.
