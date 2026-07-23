# FGCZ Python Project Reference

This repository is a small, runnable example of an FGCZ Python package using:

- a `src/` package layout and uv lockfile;
- strict static typing, linting, and dependency checks;
- unit and error-path tests with branch coverage;
- aligned pre-commit, pre-push, and GitHub Actions checks;
- strict MkDocs documentation and a scheduled dependency audit.

The example library turns a human-readable project name into a stable slug:

```python
from fgcz_reference_project.naming import project_slug

assert project_slug("Example Project") == "example-project"
```

Continue with [Getting started](getting-started.md).
