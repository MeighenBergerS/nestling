"""Tests for the Python example scripts and the coding module."""

import subprocess
import sys
from pathlib import Path

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


def _run(script: Path, cwd: Path) -> subprocess.CompletedProcess:
    """Run a Python script in the given working directory."""
    return subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
        cwd=str(cwd),
    )


def test_coding_compute():
    """Test the modular_project compute function."""
    from examples.coding.modular_project.core import compute

    assert compute(1.0, 2.0) == 3.0
    assert compute(-1.0, 1.0) == 0.0


def test_coding_format_result():
    """Test the modular_project format_result function."""
    from examples.coding.modular_project.utils import format_result

    assert format_result(3.14159) == "3.142"
    assert format_result(3.14159, precision=2) == "3.14"
    assert format_result(0.0) == "0.000"


def test_basic_plot(tmp_path):
    """Test that the basic plot script runs without error."""
    result = _run(EXAMPLES_DIR / "plotting" / "scripts" / "basic_plot.py", tmp_path)
    assert result.returncode == 0, result.stderr


def test_publication_plot(tmp_path):
    """Test that the publication plot script runs without error."""
    result = _run(EXAMPLES_DIR / "plotting" / "scripts" / "publication_plot.py", tmp_path)
    assert result.returncode == 0, result.stderr
