"""Worked example of a small modular Python project.

This package demonstrates project layout, NumPy-style docstrings,
and how to split logic across modules.
"""

from .core import compute
from .utils import format_result

__all__ = ["compute", "format_result"]
