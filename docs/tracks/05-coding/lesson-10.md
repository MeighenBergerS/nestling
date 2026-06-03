# Lesson 10: Testing

Research code that is not tested is likely wrong in ways you have not found yet.
This is not hypothetical. Every physicist who has written numerical code has eventually
found a bug they thought was physics.
Tests do not eliminate bugs, but they catch the common ones early and give you confidence
when refactoring.

---

## pytest basics

[pytest](https://docs.pytest.org/) is the standard Python testing framework.

```sh
pip install pytest
```

A test file is any file matching `test_*.py` or `*_test.py`.
A test function starts with `test_`.

```python
# tests/test_flux.py
from mypackage.physics import compute_flux

def test_flux_at_unit_energy():
    # flux(1 GeV, gamma=2) = 1^(-2) = 1
    assert compute_flux(energy=1.0, gamma=2.0) == 1.0

def test_flux_scales_with_spectral_index():
    # Flux at 10x the energy should drop by 10^gamma
    flux_low = compute_flux(energy=1e3, gamma=2.0)
    flux_high = compute_flux(energy=1e4, gamma=2.0)
    assert abs(flux_low / flux_high - 100.0) < 1e-10
```

Run all tests:

```sh
pytest
```

Run with verbose output:

```sh
pytest -v
```

---

## Floating-point comparisons

Never use `==` to compare floats.
Use `pytest.approx`, which allows a small relative tolerance:

```python
from pytest import approx

def test_flux_value():
    result = compute_flux(1e5, 2.37)
    assert result == approx(1e5 ** -2.37, rel=1e-6)
```

[Prometheus](https://github.com/Harvard-Neutrino/prometheus) uses this correctly
throughout `tests/test_detector_unit.py`.
Using bare `==` on floats produces intermittent failures that are hard to debug.

---

## Testing error cases

Test that your code raises the right exception for invalid input:

```python
import pytest
from mypackage.physics import compute_flux

def test_negative_gamma_raises():
    """Negative spectral index is unphysical."""
    with pytest.raises(ValueError, match="gamma must be positive"):
        compute_flux(1e5, gamma=-1.0)
```

The `match` argument verifies the error message, making tests self-documenting and
preventing silent mis-matches where the right exception type is raised for the wrong reason.

---

## Fixtures

A **fixture** is setup code shared between multiple tests.
Define one with `@pytest.fixture`:

```python
import pytest
import numpy as np
from mypackage.detector import Detector

@pytest.fixture
def simple_detector():
    return Detector(n_modules=10, spacing=50.0, seed=42)

def test_detector_has_correct_module_count(simple_detector):
    assert len(simple_detector.modules) == 10

def test_detector_volume_is_positive(simple_detector):
    assert simple_detector.volume > 0
```

Put shared fixtures in `tests/conftest.py`. Pytest finds them automatically.
Prometheus uses `conftest.py` to define detectors and particle configurations reused
across its 16+ test modules.

---

## What to test

| Test type | Example |
|-----------|---------|
| Known analytical result | `compute_flux(1.0, 2.0) == 1.0` |
| Boundary conditions | Zero energy, empty list, single event |
| Error paths | Wrong input raises the right exception with a clear message |
| Physics invariants | Total flux integrates to the expected value; direction vector norm is 1 |
| Regression test | Fix a bug, add a test that would have caught it |

**What not to test**: implementation details that change during refactoring, third-party
library behaviour, trivial one-line getters.

---

## Slow tests

Mark end-to-end tests that take minutes as slow so they can be excluded from fast
development runs:

```python
import pytest

@pytest.mark.slow
def test_full_neutrino_simulation():
    ...
```

Configure the marker in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
markers = ["slow: full end-to-end simulation tests, excluded from CI"]
```

Run excluding slow tests:

```sh
pytest -m "not slow"
```

Prometheus uses exactly this pattern. The e2e tests in `tests/test_e2e.py` are marked slow
and excluded from the CI workflow. They are run locally before opening a pull request.

---

## Docstring examples as tests

Short usage examples in docstrings can be tested automatically:

```python
def compute_flux(energy: float, gamma: float) -> float:
    """
    Examples
    --------
    >>> compute_flux(1.0, 2.0)
    1.0
    """
    return energy ** (-gamma)
```

Run with:

```sh
pytest --doctest-modules mypackage/
```

This is a lightweight way to keep examples in docstrings accurate without maintaining
a separate test file.

---

## What to read next

[Lesson 11](lesson-11.md) covers packaging: making your project installable with
`pip install` so collaborators can use it without copying files.
