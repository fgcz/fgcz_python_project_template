# check-tests-structure hook

Besides the reference package, this repository hosts one shared quality hook:
`check-tests-structure` verifies that a project's tests tree mirrors its sources
tree, so that every module has a test module at the same relative path. It lives
in `.ci/check-tests-structure/` as a self-contained subproject and is published
only as a pre-commit hook — there is no package on PyPI to install.

## Configuration

Add the tool's section to the `pyproject.toml` of the project being checked:

```toml
[tool.check-tests-structure]
sources_path = "src/my_package"
tests_path = "tests/unit"
allow_missing_tests = true
```

`sources_path` and `tests_path` are required; the remaining keys are documented
in `.ci/check-tests-structure/README.md`. Unmatched files are printed with
fuzzy-matched suggestions, and the hook fails unless the matching
`allow_missing_sources` / `allow_missing_tests` option is set.

Both paths are resolved against the working directory rather than the directory
containing the `pyproject.toml`, so in a multi-package workspace the check has
to run from the member's own directory.

## Using it from another repository

```yaml
repos:
  - repo: https://github.com/fgcz/fgcz_python_project_template
    rev: v0.2.0
    hooks:
      - id: check-tests-structure
```

Pin `rev` to a released tag of this repository; `pre-commit autoupdate` moves it
to the latest one. The examples below use the same tag.

The hook environment installs this repository's root package, which requires
Python 3.12 or newer. If the hook environment runs an older interpreter, depend
on the subproject directly instead:

```yaml
repos:
  - repo: local
    hooks:
      - id: check-tests-structure
        name: check tests structure
        language: python
        entry: check-tests-structure
        pass_filenames: false
        always_run: true
        additional_dependencies:
          - "fgcz-check-tests-structure @ git+https://github.com/fgcz/fgcz_python_project_template@v0.2.0#subdirectory=.ci/check-tests-structure"
```

The same requirement specifier works outside pre-commit, for example in a nox
session:

```python
@nox.session(default=False)
def tests_structure(session) -> None:
    """Performs a check on the test structure."""
    session.install(
        "git+https://github.com/fgcz/fgcz_python_project_template"
        "@v0.2.0#subdirectory=.ci/check-tests-structure"
    )
    session.run("check-tests-structure")
```

## How it is gated here

This repository runs the hook on itself in the `pre-commit` stage and runs the
subproject's own test suite in the `pre-push` stage:

```bash
uv run --project .ci/check-tests-structure --frozen check-tests-structure
uv run --directory .ci/check-tests-structure --frozen pytest
```

The vendored code keeps its own `pyproject.toml`, `uv.lock`, and MIT license. It
is linted and formatted by the repository-wide Ruff configuration, but excluded
from the strict Pyright, 100% coverage, and deptry gates that apply to the
reference package.
