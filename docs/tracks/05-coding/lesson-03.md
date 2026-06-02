# Lesson 03 — Package Management

Python's strength is its ecosystem of libraries. `pip` installs them; virtual environments
keep each project's dependencies isolated so they do not conflict.

---

## pip

`pip` is Python's package installer. It downloads packages from
[PyPI](https://pypi.org/) — the Python Package Index.

Install a package:

```sh
pip install numpy
```

Install a specific version:

```sh
pip install numpy==2.0.0
```

Install several packages at once:

```sh
pip install numpy scipy matplotlib
```

Upgrade an existing package:

```sh
pip install --upgrade numpy
```

Remove a package:

```sh
pip uninstall numpy
```

List what is currently installed:

```sh
pip list
```

---

## Virtual environments

A **virtual environment** is an isolated Python installation for a single project.
It has its own copies of pip and all installed packages, separate from every other project
on your machine.

Without virtual environments, every project shares one Python installation, which causes
two problems:

1. Project A needs `numpy==1.24` and Project B needs `numpy==2.0` — you cannot have both at once.
2. Installing packages system-wide can break other tools that rely on the system Python.

### Creating a virtual environment

In your project directory:

```sh
python -m venv .venv
```

This creates a `.venv/` folder containing a self-contained Python installation.
The name `.venv` is a convention; use it consistently so that VSCode finds it automatically.

### Activating

On macOS and Linux:

```sh
source .venv/bin/activate
```

On Windows (PowerShell):

```sh
.venv\Scripts\Activate.ps1
```

Your prompt changes to show `(.venv)` when the environment is active.
From this point, `pip` and `python` refer to the ones inside `.venv`.

Deactivate when you are done:

```sh
deactivate
```

!!! note "Always activate before installing"
    If you run `pip install` without an active virtual environment, the package installs
    globally. The safe habit: activate first, then install.

---

## requirements.txt

A `requirements.txt` file records exactly what your project depends on so collaborators
can reproduce your environment.

Create one from your current environment:

```sh
pip freeze > requirements.txt
```

Install from one:

```sh
pip install -r requirements.txt
```

A typical `requirements.txt` for a physics project:

```text
numpy>=2.0
scipy>=1.13
matplotlib>=3.9
pandas>=2.2
h5py>=3.11
```

---

## pyproject.toml

For projects you intend to share or install properly, `pyproject.toml` replaces
`requirements.txt` and the old `setup.py` in one file.
[Prometheus](https://github.com/Harvard-Neutrino/prometheus) uses this approach:

```toml
[project]
name = "prometheus-astro"
version = "1.0.0"
requires-python = ">=3.9"
dependencies = [
    "numpy>=1.24",
    "scipy>=1.10",
]
```

This is covered in depth in [Lesson 11](lesson-11.md). For now, `requirements.txt` is
sufficient.

---

## conda

[conda](https://docs.conda.io/) is an alternative to pip that manages non-Python
dependencies (C libraries, CUDA, HDF5) and creates environments, all in one tool.
Many physics codes recommend conda because their dependencies include compiled extensions
that pip cannot easily install.

```sh
conda create -n myenv python=3.11
conda activate myenv
conda install numpy scipy
```

For most pure-Python projects, pip + venv is simpler and faster.
Use conda when a package's installation instructions specifically recommend it, or when
you need GPU libraries.

---

## What to read next

[Lesson 04](lesson-04.md) covers the scientific Python stack — NumPy, SciPy, and Pandas —
the libraries you will use in almost every physics calculation.
