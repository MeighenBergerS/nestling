# Lesson 11 — Packaging

A **package** is a Python project that can be installed with `pip install`.
Making your project installable means collaborators can use it without copying files into
their own directories, and you can pin exact versions for reproducibility.

---

## pyproject.toml

`pyproject.toml` is the modern, single-file replacement for `setup.py`, `setup.cfg`,
and `requirements.txt`. It records metadata, dependencies, and tool configuration in one place.

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "my-physics-project"
version = "0.1.0"
description = "Neutrino flux calculator"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}

dependencies = [
    "numpy>=2.0",
    "scipy>=1.13",
    "matplotlib>=3.9",
    "h5py>=3.11",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "ruff>=0.4",
    "mkdocs>=1.6",
    "mkdocstrings[python]>=0.25",
]
```

Install the project and its dependencies in **editable mode**
(changes to source take effect immediately without reinstalling):

```sh
pip install -e .
```

Install with development extras:

```sh
pip install -e ".[dev]"
```

Editable installs also mean that `import mypackage` works from anywhere on your machine
while pointing at your actual source files — no more `sys.path` hacks.

---

## Tool configuration in pyproject.toml

All tool configuration lives in the same file.
This is the pattern Prometheus follows for ruff and pytest:

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "W", "I", "N", "UP"]

[tool.pytest.ini_options]
testpaths = ["tests"]
markers = ["slow: full end-to-end simulation tests"]
```

Having everything in `pyproject.toml` means a new contributor can clone the repository,
run `pip install -e ".[dev]"`, and have a fully working development environment without
reading multiple config files.

---

## Versioning

Follow [semantic versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

| Bump | When |
|------|------|
| `PATCH` (0.1.1) | Bug fix, no API change |
| `MINOR` (0.2.0) | New feature, backward compatible |
| `MAJOR` (1.0.0) | Breaking change |

Before a stable release, use `0.x.y` to signal that the API may still change.
Prometheus is at `1.0.0`, meaning its public API is stable and the team commits to
not breaking it without a major version bump.

---

## Installing from GitHub

For research code that is not yet on PyPI, collaborators can install directly from
the repository:

```sh
pip install git+https://github.com/username/my-project.git
```

Install a specific tag or branch:

```sh
pip install git+https://github.com/username/my-project.git@v0.3.0
pip install git+https://github.com/username/my-project.git@feature-branch
```

This is how most physics collaborators share code before a formal PyPI release.

---

## Publishing to PyPI

When your project is stable and you want anyone to install it with `pip install my-project`:

```sh
pip install build twine
python -m build
twine upload dist/*
```

`build` creates a `.whl` (wheel) and a `.tar.gz` (source distribution) in `dist/`.
`twine upload` pushes them to PyPI — you will need a PyPI account and an API token.

---

## Alternative build tools

Prometheus uses [Poetry](https://python-poetry.org/) rather than plain setuptools.
Poetry manages dependencies and creates a `poetry.lock` that pins every transitive
dependency, making environments fully reproducible.
Both approaches produce standard packages; setuptools is simpler to start with.

---

## What to read next

[Lesson 12](lesson-12.md) covers the final step: automating lint checks, tests, and
documentation deployment in CI so that quality is enforced on every pull request.
