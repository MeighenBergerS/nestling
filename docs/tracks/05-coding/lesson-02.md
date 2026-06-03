# Lesson 02: Python & Jupyter Notebooks

Python is the primary language of modern physics research.
It is not the fastest language, but it is expressive, has an enormous scientific ecosystem,
and is easy to read.
This lesson covers enough Python to get you running, and introduces Jupyter notebooks,
the interactive environment used for exploration and analysis.

---

## Why Python

The scientific Python stack (NumPy, SciPy, Matplotlib, and hundreds of domain libraries)
means that most physics tasks, numerical integration, fitting, plotting, reading HDF5 files,
have well-tested implementations you can call rather than write.
Simulation codes like [Prometheus](https://github.com/Harvard-Neutrino/prometheus) are
written in Python precisely because this ecosystem exists.

Python is also readable. Code you wrote six months ago, or code a collaborator wrote last year,
is more likely to make sense than equivalent C++.

---

## Python basics

### Variables and types

```python
energy = 1e12         # float (in eV)
name = "IceCube"      # str
n_events = 10000      # int
is_running = True     # bool
```

Python is dynamically typed: you do not declare types up front.
See [Lesson 05](lesson-05.md) for how to add optional type hints.

### Arithmetic

```python
x = 3.0
y = 2.0

x + y    # 5.0
x ** 2   # 9.0   — exponentiation
x / y    # 1.5
x // y   # 1.0   — floor division
x % y    # 1.0   — remainder
```

### Lists

```python
energies = [1e10, 1e11, 1e12, 1e13]  # ordered, mutable

energies[0]     # 1e10   — first element
energies[-1]    # 1e13   — last element
energies[1:3]   # [1e11, 1e12]   — slice
energies.append(1e14)
```

### Dictionaries

```python
particle = {"name": "muon", "mass_GeV": 0.1057, "charge": -1}

particle["name"]                    # "muon"
particle["lifetime_s"] = 2.2e-6    # add a new key
```

### Loops

```python
for e in energies:
    print(f"Energy: {e:.2e} eV")

for i, e in enumerate(energies):
    print(f"  [{i}] {e:.2e} eV")
```

### Functions

```python
def lorentz_gamma(energy_eV: float, mass_eV: float) -> float:
    """Return the Lorentz factor for a relativistic particle."""
    return energy_eV / mass_eV

gamma = lorentz_gamma(1e12, 1.057e8)   # muon at 1 TeV: γ ≈ 9450
```

### Imports

```python
import math
import numpy as np            # the conventional alias
from scipy import integrate
```

!!! warning "Never import inside a function"
    This works, but it repeats the import machinery on every call and obscures what your
    module depends on. Always put imports at the top of the file.
    [Prometheus `particle.py`](https://github.com/Harvard-Neutrino/prometheus/blob/main/prometheus/particle/particle.py)
    contains exactly this pattern, a useful real-world reminder that even well-maintained
    codebases have small bad habits.

A common mistake is placing imports inside a function body:

```python
def clone(self):
    import copy        # bad: runs on every call
    return copy.deepcopy(self)
```

---

## Jupyter notebooks

A Jupyter notebook is an interactive document that mixes code, output, and text in a single
`.ipynb` file. It is the standard environment for exploratory physics work: you can run one
cell at a time, inspect results immediately, and iterate without rerunning an entire script.

### Starting a notebook

In VSCode: Command Palette (⇧⌘P) → **"Create: New Jupyter Notebook"**.

Or in the terminal (with `jupyter` installed):

```sh
pip install jupyter
jupyter notebook
```

### Cell types

| Type | Purpose |
|------|---------|
| **Code** | Python: press `Shift+Enter` to run |
| **Markdown** | Text, equations ($E = mc^2$), headers |
| **Raw** | Passed through as-is (rarely needed) |

### A minimal physics notebook

```python
# Cell 1 — imports
import numpy as np
import matplotlib.pyplot as plt
```

```python
# Cell 2 — compute a power-law neutrino spectrum
E = np.logspace(2, 6, 500)     # 100 GeV to 1 PeV
gamma = 2.37                   # IceCube best-fit spectral index
phi = E ** (-gamma)            # differential flux (arbitrary units)
```

```python
# Cell 3 — plot
fig, ax = plt.subplots()
ax.loglog(E, phi)
ax.set_xlabel("Energy [GeV]")
ax.set_ylabel(r"$\Phi$ [a.u.]")
ax.set_title("Power-law neutrino spectrum")
plt.show()
```

### Notebooks vs scripts

| Use a **notebook** when | Use a **script** when |
|------------------------|----------------------|
| Exploring data interactively | Running batch jobs on a cluster |
| Producing plots for a paper | Writing reusable library code |
| Teaching or demonstrating | Running automated tests |
| Prototyping a new calculation | Long-running simulations |

A common workflow: prototype in a notebook, then move the cleaned-up logic into a `.py`
module once it works.

!!! warning "Restart and run all before sharing"
    Notebooks maintain state between cells; it is easy to run them out of order and produce
    results that cannot be reproduced.
    Before sharing or committing a notebook, always use
    **Kernel → Restart and Run All** to verify it runs cleanly from top to bottom.

---

## What to read next

[Lesson 03](lesson-03.md) covers `pip` and virtual environments, the machinery that installs
Python packages and keeps project dependencies isolated.
