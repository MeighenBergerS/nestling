"""Tests for the ArXiv track example scripts.

These tests make real network requests to the ArXiv and Inspire-HEP APIs.
They are marked ``network`` and can be skipped in offline environments:

    pytest tests/ -m "not network"
"""

import subprocess
import sys
from pathlib import Path

import pytest

ARXIV_EXAMPLES = Path(__file__).parent.parent / "examples" / "arxiv"


def _run(script: Path, cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
        cwd=str(cwd),
    )


@pytest.mark.network
def test_arxiv_api_script(tmp_path):
    """Test that the ArXiv API script runs without error."""
    result = _run(ARXIV_EXAMPLES / "arxiv_api.py", tmp_path)
    assert result.returncode == 0, result.stderr


@pytest.mark.network
def test_inspire_api_script(tmp_path):
    """Test that the Inspire-HEP API script runs without error."""
    result = _run(ARXIV_EXAMPLES / "inspire_api.py", tmp_path)
    assert result.returncode == 0, result.stderr
