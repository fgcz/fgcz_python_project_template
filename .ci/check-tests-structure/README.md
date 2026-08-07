# check-tests-structure

Validates that a project's tests folder structure mirrors its sources folder
structure, so that every module has a test module next to the same relative
path. Configured entirely from the checked project's `pyproject.toml`.

```toml
[tool.check-tests-structure]
sources_path = "src/my_package"   # required
tests_path = "tests/unit"         # required
allow_missing_tests = true        # do not fail on sources without a test
```

| Key | Default | Purpose |
|---|---|---|
| `sources_path` | required | Root of the sources tree, relative to the working directory |
| `tests_path` | required | Root of the tests tree, relative to the working directory |
| `inputs_glob` | `["*.py"]` | Source files to consider |
| `tests_glob` | `["test_*.py"]` | Test files to consider |
| `tests_pattern` | `test_(.*).py` | Maps a test filename back to its source name |
| `allow_missing_sources` | `false` | Tolerate tests without a matching source |
| `allow_missing_tests` | `false` | Tolerate sources without a matching test |
| `excluded_files` | `["__init__.py", "__main__.py"]` | Never reported |

Unmatched files are printed with fuzzy-matched suggestions, and the command
exits non-zero unless the corresponding `allow_missing_*` option is set.

Both paths are resolved against the **working directory**, not against the
directory holding the `pyproject.toml`. In a workspace, run the check from the
member's own directory.

See [the project documentation](../../docs/check-tests-structure.md) for how
other repositories consume this as a pre-commit hook.

## Development

This is a self-contained subproject: it is not part of the reference package,
not a uv workspace member, and it keeps its own `uv.lock`.

```bash
uv run --directory .ci/check-tests-structure --frozen pytest
```

## Provenance

Imported from <https://github.com/leoschwarz/check-tests-structure> at commit
`1228f93`, including the then-unreleased fixes to the `allow_missing_*` options
and the simplified entry point. Consolidated here so that FGCZ projects do not
depend on a personal account. Distributed under the MIT license (see `LICENSE`),
unlike the Apache-2.0 licensed reference project around it.
