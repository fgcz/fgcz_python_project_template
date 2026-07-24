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

## Type checking

Strict [Pyright](https://github.com/microsoft/pyright) runs as a blocking
pre-commit hook. To use [basedpyright](https://docs.basedpyright.com/) instead
— a stricter, pure-Python fork that installs through uv without a separate
Node runtime — make three changes:

- replace `pyright` with `basedpyright` in the `dev` group of `pyproject.toml`;
- change the `pyright` hook `entry` in `.pre-commit-config.yaml` to
  `uv run --frozen basedpyright`;
- configure it under `[tool.basedpyright]` (it reads the existing
  `[tool.pyright]` keys).

Pyright is the default because Microsoft maintains it; basedpyright adds
strictness and richer reporting at the cost of a single-maintainer fork.

## Python and dependency ranges

The frozen pre-commit and pre-push stages run on a single pinned interpreter for
a fast local loop. CI additionally runs the test suite across the supported
range: the minimum Python with the oldest direct dependencies
(`--resolution lowest-direct`) and the maximum Python with the newest
(`--resolution highest`). This catches both under-specified lower bounds and
breakage on new interpreters.
