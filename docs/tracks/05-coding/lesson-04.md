# Lesson 04: Scientific Python Stack

These libraries underpin almost all computational physics in Python.
You do not need to memorise the API. You need to understand what each one is for
and how to look things up efficiently.

Install everything at once:

```sh
pip install numpy scipy pandas matplotlib h5py
```

---

## NumPy

NumPy provides the `ndarray`: a fast, multi-dimensional array that supports vectorised
operations. Almost every other scientific library builds on it.

### Creating arrays

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])         # from a list
b = np.zeros(100)                       # 100 zeros
c = np.linspace(0, 1, 50)              # 50 evenly spaced values in [0, 1]
d = np.logspace(2, 6, 100)             # 100 points, 10^2 to 10^6
e = np.arange(0, 10, 0.5)             # 0.0, 0.5, 1.0, ...
M = np.zeros((3, 3))                   # 2-D array, shape (3, 3)
```

### Operations are element-wise

```python
E = np.logspace(2, 6, 1000)   # energies in GeV
phi = 1e-4 * E ** -2.0        # power-law spectrum — no loop needed
```

This is **vectorisation**: operations apply to every element simultaneously.
It is typically 100–1000× faster than an equivalent Python `for` loop, because the loop
runs in compiled C code inside NumPy rather than in the Python interpreter.
Vectorisation is your single most important performance tool.
See [Lesson 06](lesson-06.md) for a deeper discussion.

### Indexing and slicing

```python
a = np.arange(10)       # [0, 1, 2, ..., 9]

a[0]                    # 0      — first element
a[-1]                   # 9      — last element
a[2:5]                  # [2, 3, 4]
a[a > 5]                # [6, 7, 8, 9]   — boolean mask
```

Boolean masks are particularly useful in physics: `events[events["energy"] > 1e5]` selects
only high-energy events without a loop.

### Useful functions

```python
np.sum(a)                        # sum all elements
np.mean(a), np.std(a)            # statistics
np.max(a), np.min(a)             # extremes
np.sort(a)                       # sorted copy (does not modify a)
np.where(a > 3, a, 0)            # conditional: keep if > 3, else 0
np.dot(v1, v2)                   # dot product
np.cross(v1, v2)                 # cross product
np.linalg.norm(v)                # vector norm
np.histogram(data, bins=50)      # histogram
```

### Saving and loading

```python
np.save("spectrum.npy", phi)
phi_loaded = np.load("spectrum.npy")

# Plain text (slower, human-readable)
np.savetxt("spectrum.txt", np.column_stack([E, phi]))
data = np.loadtxt("spectrum.txt")
```

---

## SciPy

SciPy extends NumPy with algorithms for integration, optimisation, interpolation,
linear algebra, and statistics. Each lives in a submodule.

### Integration

```python
from scipy import integrate

def integrand(E, gamma):
    return E ** (-gamma)

result, error = integrate.quad(integrand, 1e2, 1e6, args=(2.0,))
print(f"Integral = {result:.4e} ± {error:.2e}")
```

For 2-D integrals, use `integrate.dblquad`.
For integrals over sampled data, use `integrate.trapezoid`.

### Interpolation

```python
from scipy.interpolate import interp1d

f = interp1d(E_data, phi_data, kind="cubic", bounds_error=False, fill_value=0.0)
phi_fine = f(E_fine)
```

### Optimisation and fitting

```python
from scipy.optimize import curve_fit, brentq

def power_law(E, norm, gamma):
    return norm * E ** (-gamma)

popt, pcov = curve_fit(power_law, E_data, phi_data, p0=[1e-4, 2.0])
norm_fit, gamma_fit = popt
perr = np.sqrt(np.diag(pcov))   # 1-sigma uncertainties

# Root finding
E_cross = brentq(lambda E: power_law(E, *popt) - threshold, 1e3, 1e8)
```

### Statistics

```python
from scipy import stats

ks_stat, p_value = stats.kstest(samples, "norm")  # Kolmogorov-Smirnov
chi2, p = stats.chisquare(observed, expected)
```

---

## Pandas

Pandas provides the `DataFrame`: a labelled 2-D table, analogous to a spreadsheet or SQL
table. It is most useful when you have tabular data: event catalogues, parameter scans,
observational tables with mixed column types.

```python
import pandas as pd

df = pd.read_csv("events.csv")      # load
df.head()                           # inspect first five rows
df.describe()                       # summary statistics

# Selecting columns
energies = df["energy_GeV"]

# Filtering rows
high_energy = df[df["energy_GeV"] > 1e5]

# Grouping
by_type = df.groupby("particle_type")["energy_GeV"].mean()

# Saving
df.to_csv("output.csv", index=False)
df.to_hdf("output.h5", key="events")
```

Pandas is less useful for pure numerical computation. Prefer NumPy arrays there.
It shines for loading mixed-type data, quick aggregation, and preparing tables for a paper.

---

## HDF5 and h5py

Physics simulations produce large binary files.
HDF5 is the standard format: structured, compressed, and fast.

```python
import h5py

# Writing
with h5py.File("simulation.h5", "w") as f:
    f.create_dataset("energies", data=E_array, compression="gzip")
    f.create_dataset("weights", data=w_array)
    f.attrs["description"] = "Neutrino MC run 001"
    f.attrs["n_events"] = len(E_array)

# Reading
with h5py.File("simulation.h5", "r") as f:
    E = f["energies"][:]     # [:] loads into memory
    w = f["weights"][:]
    print(f.attrs["description"])
```

[Prometheus](https://github.com/Harvard-Neutrino/prometheus) writes its output in HDF5.
The Pandas `read_hdf` / `to_hdf` methods use the same format.

---

## Matplotlib

Matplotlib produces publication-quality plots.
Full coverage is in the [Plotting track](../06-plotting/index.md); a minimal example:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4))
ax.loglog(E, phi, color="steelblue", label=r"$\gamma = 2.37$")
ax.set_xlabel("Energy [GeV]")
ax.set_ylabel(r"$\Phi$ [GeV$^{-1}$ cm$^{-2}$ s$^{-1}$ sr$^{-1}$]")
ax.legend()
fig.tight_layout()
fig.savefig("spectrum.pdf")
```

Always save to PDF for vector graphics; use PNG only for quick inspection.

---

## Domain-specific libraries worth knowing

| Library | Purpose |
| ------- | ------- |
| [astropy](https://www.astropy.org/) | Coordinate systems, FITS files, cosmology, units |
| [healpy](https://healpy.readthedocs.io/) | HEALPix sky maps (CMB, neutrino sky maps) |
| [iminuit](https://scikit-hep.org/iminuit/) | Maximum-likelihood fitting (MINUIT wrapper) |
| [uproot](https://uproot.readthedocs.io/) | Read/write ROOT files without a ROOT installation |

---

## A worked physics example

Compute the muon neutrino flux from a power-law source, then find the energy at which
the integrated flux above that energy drops below a given threshold.

```python
import numpy as np
from scipy import integrate, optimize

GAMMA = 2.37                  # spectral index (IceCube best-fit)
NORM = 1.66e-18               # normalisation [GeV^-1 cm^-2 s^-1 sr^-1] at 100 TeV
E_REF = 1e5                   # reference energy [GeV]

def flux(E: float) -> float:
    return NORM * (E / E_REF) ** (-GAMMA)

def flux_above(E_min: float) -> float:
    """Integrated flux above E_min [cm^-2 s^-1 sr^-1]."""
    result, _ = integrate.quad(flux, E_min, np.inf)
    return result

threshold = 1e-22             # cm^-2 s^-1 sr^-1

E_cutoff = optimize.brentq(
    lambda E: flux_above(E) - threshold,
    1e3, 1e8
)
print(f"Integrated flux drops below threshold at {E_cutoff:.2e} GeV")
```

This pattern, define a flux function, integrate it, invert the integral, appears constantly
in neutrino physics, cosmic-ray analysis, and gravitational-wave parameter estimation.

---

## What to read next

[Lesson 05](lesson-05.md) covers code style: why consistent formatting matters,
and how to enforce it automatically with `ruff`.
