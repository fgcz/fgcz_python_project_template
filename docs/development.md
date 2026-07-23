# Development

The local hooks are the source for the GitHub Actions quality commands.

## Every commit

```bash
uv run pre-commit run --hook-stage pre-commit --all-files
```

This runs Ruff, strict Pyright, and deptry.

## Every push

```bash
uv run pre-commit run --hook-stage pre-push --all-files
```

This runs tests with branch coverage, changed-line coverage, package inspection,
and a strict documentation build.

## Dependency audit

```bash
uv run pre-commit run dependency-audit --hook-stage manual --all-files
```

GitHub Actions runs the same audit weekly. Add project-specific checks as
separate hooks, then invoke those hooks from CI so local and remote behavior
remain aligned.
