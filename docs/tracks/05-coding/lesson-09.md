# Lesson 09 — Documentation

Documentation has two audiences: collaborators who will use your code, and your future self
six months from now.
Good docstrings make both audiences' lives easier — and they can be automatically rendered
into a browsable website.

---

## Docstring formats

There are three common styles. The important thing is to **pick one and use it consistently**.

[Prometheus](https://github.com/Harvard-Neutrino/prometheus) uses **Google style** in most
of its source files, but its `mkdocs.yml` tells `mkdocstrings` to render **NumPy style** —
a mismatch that produces imperfect API documentation.
Do not do this: choose one style and configure your tools to match.

This track uses **NumPy style**, which is standard across the scientific Python ecosystem
(NumPy, SciPy, Astropy all use it).

---

## NumPy-style docstrings

```python
def compute_flux(energy: float, gamma: float, norm: float = 1.0) -> float:
    """
    Compute the differential neutrino flux for a power-law spectrum.

    Parameters
    ----------
    energy : float
        Particle energy in GeV.
    gamma : float
        Spectral index. Must be positive.
    norm : float, optional
        Normalisation at 1 GeV, by default 1.0.

    Returns
    -------
    float
        Differential flux in units of GeV^-1 cm^-2 s^-1 sr^-1.

    Raises
    ------
    ValueError
        If `gamma` is not positive.

    Examples
    --------
    >>> compute_flux(1.0, 2.0)
    1.0
    """
    if gamma <= 0:
        raise ValueError(f"gamma must be positive, got {gamma}")
    return norm * energy ** (-gamma)
```

For class attributes, document them in the class docstring under an `Attributes` section:

```python
from dataclasses import dataclass
import numpy as np

@dataclass
class Particle:
    """
    A simulated particle propagating through a detector.

    Attributes
    ----------
    energy : float
        Energy in GeV.
    position : np.ndarray
        Position vector [x, y, z] in metres relative to detector centre.
    direction : np.ndarray
        Unit direction vector [dx, dy, dz]. Must have norm 1.
    """
    energy: float
    position: np.ndarray
    direction: np.ndarray
```

!!! warning "Document array shapes and units"
    When an attribute or parameter is an array, always state its expected shape and the
    physical units. `np.ndarray` alone tells the reader nothing.
    Prometheus's `PropagatableParticle` has `losses: np.ndarray` and `hits: np.ndarray`
    with no docstrings — a real maintenance burden that forces every user to read the
    source code to understand the data structure.

---

## MkDocs

[MkDocs](https://www.mkdocs.org/) builds a documentation website from Markdown files.
[mkdocstrings](https://mkdocstrings.github.io/) extends it to extract and render Python
docstrings automatically — so your API reference stays in sync with the code.

Install:

```sh
pip install mkdocs mkdocstrings[python]
```

Initialise:

```sh
mkdocs new .
```

This creates `mkdocs.yml` and `docs/index.md`. A minimal `mkdocs.yml`:

```yaml
site_name: My Physics Project
theme:
  name: readthedocs

plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: numpy
            show_source: true
```

In any Markdown file, render auto-generated API docs with:

```markdown
::: mypackage.core
```

Build and preview locally:

```sh
mkdocs serve
```

This serves the site at `http://127.0.0.1:8000` and rebuilds on every file change.

---

## Deploying to GitHub Pages

```sh
mkdocs gh-deploy
```

This builds the site and pushes it to the `gh-pages` branch of your repository.
Prometheus hosts its documentation at `harvard-neutrino.github.io/prometheus` exactly
this way — via a GitHub Actions workflow (`.github/workflows/deploy-mkdocs.yml`) that
runs `mkdocs gh-deploy` on every push to `main`.
See [Lesson 12](lesson-12.md) for the CI setup.

---

## README

The `README.md` is the first thing people see. It should answer five questions:

1. What does this code do? (one paragraph)
2. How do I install it?
3. How do I run a basic example?
4. Where is the full documentation?
5. How do I cite this? (if published)

Prometheus's README covers all five. Use it as a reference.

---

## What to read next

[Lesson 10](lesson-10.md) covers testing: the practice that lets you change code
confidently without breaking things silently.
