# Contributing

This project uses uv for dependency management and pre-commit for local quality
checks.

```bash
uv sync --frozen --group docs
uv run pre-commit install --install-hooks
```

Before committing:

```bash
uv run pre-commit run --hook-stage pre-commit --all-files
```

Before pushing:

```bash
uv run pre-commit run --hook-stage pre-push --all-files
```

Add user-visible changes under `Unreleased` in `CHANGELOG.md`. Do not weaken a
quality gate to make a change pass; fix the underlying code, test, dependency,
or documentation issue.
