# Getting started

Install the locked development and documentation environments:

```bash
uv sync --frozen --group docs
uv run pre-commit install --install-hooks
```

Run the example command:

```bash
uv run fgcz-reference "Example Project"
```

Expected output:

```text
example-project
```

Run the fast checks:

```bash
uv run pre-commit run --hook-stage pre-commit --all-files
```
