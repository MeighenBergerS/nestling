# Lesson 05: Code Style & Quality

Code is read far more often than it is written.
A consistent style makes it easier for collaborators, and your future self, to understand
and modify code. This lesson introduces PEP 8, type hints, and the tools that enforce style
automatically so you do not have to think about it.

---

## PEP 8

[PEP 8](https://peps.python.org/pep-0008/) is Python's official style guide.
You do not need to memorise it. A linter will tell you when you violate it, but
understanding the core rules prevents the most common problems.

### Naming conventions

| Thing | Convention | Example |
|-------|-----------|---------|
| Variables, functions | `snake_case` | `particle_energy`, `compute_flux()` |
| Classes | `PascalCase` | `NeutrinoFlux`, `DetectorConfig` |
| Constants | `UPPER_SNAKE_CASE` | `SPEED_OF_LIGHT`, `MAX_EVENTS` |
| Private attributes | `_leading_underscore` | `_cache`, `_validate()` |

[Prometheus](https://github.com/Harvard-Neutrino/prometheus) follows this correctly
throughout. `PrometheusConfig`, `DetectorConfig`, `RunConfig` are all `PascalCase`;
helper functions are `snake_case`.

### Line length

Keep lines under **88 characters**, the `ruff`/`black` default.
Long lines are hard to read side-by-side with a diff and awkward in terminal output.
Prometheus sets a limit of 100 in `pyproject.toml`, slightly generous, but documented
and consistently enforced.

### Imports

Imports go at the **top of the file**, grouped and ordered:

1. Standard library (`os`, `math`, `copy`)
2. Third-party (`numpy`, `scipy`)
3. Local (`from .config import Config`)

Separate groups with a blank line:

```python
import os
from pathlib import Path

import numpy as np
from scipy import integrate

from prometheus.config import PrometheusConfig
```

### Blank lines

Two blank lines between top-level functions and classes; one blank line between methods
inside a class.

---

## ruff

[ruff](https://docs.astral.sh/ruff/) is a fast Python linter and formatter.
It replaces `flake8`, `isort`, and `black` in a single tool.

```sh
pip install ruff
```

Run the linter:

```sh
ruff check .
```

Auto-fix what can be fixed:

```sh
ruff check --fix .
```

Format all files:

```sh
ruff format .
```

### Configuration in pyproject.toml

Ruff is configured in `pyproject.toml`. This is what Prometheus uses:

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "W", "I"]
exclude = ["resources", "paper_plots", "site", "olympus", "examples/legacy"]
```

Rule codes:

| Code | What it checks |
|------|---------------|
| `E` | PEP 8 style errors |
| `F` | Pyflakes (undefined names, unused imports) |
| `W` | Warnings |
| `I` | Import sorting (replaces `isort`) |
| `N` | Naming conventions (add this) |
| `UP` | pyupgrade: flags outdated Python patterns (add this) |

For a new project add `"N"` and `"UP"` to the select list.

---

## Type hints

Type hints annotate what types a function expects and returns.
They do not change runtime behaviour, but Pylance and ruff use them to catch errors
before you run the code.

```python
def compute_flux(energy: float, gamma: float, norm: float = 1.0) -> float:
    return norm * energy ** (-gamma)
```

For collections, use the **built-in generic forms** (Python 3.9+):

```python
def mean_energy(events: list[float]) -> float:
    return sum(events) / len(events)

def load_config(path: str) -> dict[str, float]:
    ...
```

!!! warning "Avoid typing.List and typing.Dict"
    Older code uses `from typing import List, Dict` and then `List[float]`.
    This was required before Python 3.9. In modern Python, use the built-in types
    directly: `list[float]`, `dict[str, int]`, `tuple[float, ...]`.
    Prometheus contains several instances of the old style (`List[Particle]`), harmless
    but unnecessary. ruff's `UP` rule flags these automatically.

### Optional and Union

```python
def find_mass(name: str) -> float | None:
    """Return the mass in MeV if known, else None."""
    masses = {"muon": 105.7, "electron": 0.511}
    return masses.get(name)
```

`float | None` is the Python 3.10+ shorthand for `Optional[float]`. Prefer it in new code.

---

## VSCode integration

With the **Ruff** and **Pylance** extensions installed, problems appear as underlines as
you type and are listed in the Problems panel (⇧⌘M / Ctrl+Shift+M).

Enable format-on-save by adding this to your project's `.vscode/settings.json`:

```json
{
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll.ruff": "explicit"
        }
    }
}
```

With this in place, every time you save a file it is automatically reformatted and
fixable lint errors are resolved. Style stops being something you need to consciously manage.

---

## What to read next

[Lesson 06](lesson-06.md) covers performance: when Python is too slow for the calculation
you are trying to run, and which tool to reach for first.
