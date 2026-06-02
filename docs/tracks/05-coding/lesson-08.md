# Lesson 08 — Project Layout

How you organise your files matters.
A clear structure makes it obvious where code lives, prevents circular imports, and is
required for packaging tools to work correctly.
This lesson covers the layout conventions used in production physics code.

---

## The minimal structure

At minimum, a Python project should look like this:

```text
my-project/
├── mypackage/
│   ├── __init__.py
│   └── core.py
├── tests/
│   └── test_core.py
├── pyproject.toml
├── README.md
└── .gitignore
```

- `mypackage/` is a **package**: a directory with an `__init__.py` that Python recognises
  as importable.
- `tests/` is separate from the package so test code never ships to users.
- `pyproject.toml` records metadata and dependencies (see [Lesson 11](lesson-11.md)).
- `.gitignore` excludes build artifacts, `.venv/`, and data files.

---

## The `__init__.py` file

`__init__.py` marks a directory as a Python package.
It also controls what is exposed when someone writes `from mypackage import ...`.

A well-designed `__init__.py` exports a clean public API and hides internal structure:

```python
# mypackage/__init__.py
from .core import run_simulation, Detector
from .config import Config

__all__ = ["run_simulation", "Detector", "Config"]
```

Users import from the package root, not from internal submodules:

```python
from mypackage import run_simulation      # clean — the intended way
from mypackage.core import run_simulation # works, but exposes internals
```

[Prometheus](https://github.com/Harvard-Neutrino/prometheus) does this correctly.
`prometheus/__init__.py` exports `Prometheus`, `Detector`, and `config` via an explicit
`__all__`. Users are insulated from the internal `lepton_propagation/`,
`photon_propagation/` subpackage structure — if those subpackages are ever restructured,
the public import paths stay the same.

---

## Subpackages

For larger projects, split related code into subpackages:

```text
prometheus/
├── __init__.py
├── prometheus.py          # main class
├── config.py
├── detector/
│   ├── __init__.py
│   └── detector.py
├── lepton_propagation/
│   ├── __init__.py
│   └── proposal.py
└── utils/
    ├── __init__.py
    └── errors.py
```

Import between subpackages using **relative imports**:

```python
# Inside prometheus/lepton_propagation/proposal.py
from ..config import PrometheusConfig
from ..utils.errors import PrometheusLeptonPropagatorError
```

`..` means "one level up in the package hierarchy".
Relative imports make the internal structure refactorable without changing import paths
in user code.

---

## Dataclasses for configuration

Use `@dataclass` instead of plain dictionaries for structured configuration.
Dataclasses give you type-checked attributes, default values, and automatic `__repr__`.

```python
from dataclasses import dataclass, field

@dataclass
class RunConfig:
    n_events: int = 1000
    seed: int = 42
    output_path: str = "output.h5"

@dataclass
class SimConfig:
    run: RunConfig = field(default_factory=RunConfig)
    detector_name: str = "IceCube"
```

Prometheus uses nested dataclass composition (`PrometheusConfig` contains `RunConfig`,
`DetectorConfig`, `InjectionConfig`) — a clean pattern that scales well for complex
configurations.

!!! warning "Always validate at construction time"
    Prometheus's `config_types.py` validates fields in `__post_init__`, catching invalid
    configurations at construction time rather than deep inside a long simulation run.
    Always validate at the boundary where data enters your system.
    In contrast, `PropagatableParticle` has `position: np.ndarray` and
    `direction: np.ndarray` with no validation — if you pass a 2-D array where a 1-D
    one is expected, the error appears far later in propagation and is hard to trace.

---

## Custom exception classes

Define your own exceptions rather than raising generic `ValueError` or `RuntimeError`.
This lets callers catch specific errors and gives users actionable error messages.

Prometheus's `utils/__init__.py` is a good example:

```python
class PrometheusDetectorLoadError(Exception):
    """Raised when a detector configuration file cannot be loaded."""

class PrometheusUnknownPropagator(Exception):
    """Raised when an unrecognised propagator name is requested."""
```

Usage:

```python
if propagator_name not in KNOWN_PROPAGATORS:
    raise PrometheusUnknownPropagator(
        f"Propagator '{propagator_name}' is not recognised. "
        f"Valid options: {list(KNOWN_PROPAGATORS.keys())}"
    )
```

Compare to `raise ValueError("bad propagator")` — the custom exception is immediately
identifiable in a traceback and can be caught specifically by callers.

---

## What to avoid

**Flat scripts**: a single 1000-line `analysis.py` with no functions.
This cannot be tested, imported, or reused — and when something breaks, there is nowhere
to look except the whole file.

**Circular imports**: package A imports from B, and B imports from A.
This usually means you need a third module that both can depend on, or the dependency
direction needs to be inverted.

**`from mypackage import *`**: importing everything into a namespace makes it impossible
to tell where a name came from when reading code months later.

---

## What to read next

[Lesson 09](lesson-09.md) covers documentation: writing docstrings that tools can convert
into a browsable website, as Prometheus does.
