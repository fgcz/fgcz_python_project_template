"""Build and inspect the reference package without installing from PyPI."""

from __future__ import annotations

import configparser
import subprocess
import tempfile
import zipfile
from pathlib import Path

_ENTRY_POINT = "fgcz_reference_project.cli:main"


def _verify_wheel(wheel: Path) -> None:
    with zipfile.ZipFile(wheel) as archive:
        names = set(archive.namelist())
        required = {
            "fgcz_reference_project/__init__.py",
            "fgcz_reference_project/cli.py",
            "fgcz_reference_project/naming.py",
            "fgcz_reference_project/py.typed",
        }
        if missing := required - names:
            raise RuntimeError(f"Wheel is missing package files: {sorted(missing)}")

        entry_point_files = [name for name in names if name.endswith(".dist-info/entry_points.txt")]
        if len(entry_point_files) != 1:
            raise RuntimeError(f"Expected one entry_points.txt, found {entry_point_files}")

        parser = configparser.ConfigParser()
        parser.read_string(archive.read(entry_point_files[0]).decode())
        actual = parser["console_scripts"].get("fgcz-reference")
        if actual != _ENTRY_POINT:
            raise RuntimeError(f"Unexpected fgcz-reference entry point: {actual!r}")


def main() -> None:
    """Build an sdist and wheel, then inspect the wheel's public contract."""
    with tempfile.TemporaryDirectory(prefix="fgcz-reference-package-") as temp_dir:
        output_dir = Path(temp_dir)
        subprocess.run(["uv", "build", "--out-dir", str(output_dir)], check=True)
        wheels = list(output_dir.glob("*.whl"))
        if len(wheels) != 1:
            raise RuntimeError(f"Expected one wheel, found {wheels}")
        _verify_wheel(wheels[0])
        print(f"Package smoke passed: {wheels[0].name}")


if __name__ == "__main__":
    main()
