# Lesson 12 — Linting & Automation

Manual discipline breaks down under deadline pressure.
The solution is to automate quality checks so they run without conscious effort:
on every save (VSCode), on every commit (pre-commit hooks), and on every pull request
(GitHub Actions CI).

---

## pre-commit hooks

[pre-commit](https://pre-commit.com/) runs a configured set of checks before
`git commit` completes. If any check fails, the commit is blocked and you fix the
problem before it enters the repository history.

```sh
pip install pre-commit
```

Create `.pre-commit-config.yaml` in your project root:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.10
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-merge-conflict
      - id: check-added-large-files
        args: [--maxkb=500]
```

Install the hooks into your local repository:

```sh
pre-commit install
```

From now on, `git commit` automatically runs ruff and the file checks.
If ruff auto-fixes something, the commit is blocked once — you stage the changes and
commit again.

Run all hooks manually on every file at any time:

```sh
pre-commit run --all-files
```

!!! note "Prometheus is missing pre-commit"
    Prometheus has a well-configured ruff setup in `pyproject.toml` and enforces linting
    in CI, but has no `.pre-commit-config.yaml`.
    This means style issues are caught late — during a pull request review — rather than
    before the commit is created. Adding pre-commit hooks is one of the easiest
    improvements you can make to any existing project.

---

## GitHub Actions

GitHub Actions runs workflows automatically on push and pull request events.
For a Python project, the minimum useful workflow runs linting and tests separately.

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install ruff
      - run: ruff check .
      - run: ruff format --check .

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: pytest -m "not slow" -v
```

Prometheus's `.github/workflows/ci.yml` follows exactly this pattern: a separate `lint`
job and a separate `test` job, triggered on all PRs and pushes to `main`.
Separating them means a lint failure appears in the lint job and a test failure in the
test job — you know immediately where to look.

---

## Documentation deployment

Automatically rebuild and deploy docs on every merge to `main`:

```yaml
name: Deploy docs

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install mkdocs mkdocstrings[python]
      - run: mkdocs gh-deploy --force
```

Prometheus uses this in `.github/workflows/deploy-mkdocs.yml` — every merge to `main`
automatically updates the public documentation at `harvard-neutrino.github.io/prometheus`.

---

## The full quality pipeline

With everything in place, quality checks run at every stage automatically:

```text
Developer saves a file
  └─ VSCode formats with ruff on save

Developer commits
  └─ pre-commit: ruff check, ruff format, file hygiene checks

Developer opens a pull request
  └─ CI lint job: ruff check, ruff format --check
  └─ CI test job: pytest (slow tests excluded)

Pull request merged to main
  └─ Deploy job: mkdocs gh-deploy (public docs updated)
```

At each stage, problems are caught before they reach the next stage.
The result: a codebase that stays clean without requiring constant conscious effort.

---

## Track summary checklist

By the end of this track you should have:

- [ ] VSCode with Python, Pylance, Jupyter, and Ruff extensions; format-on-save enabled
- [ ] A `.venv` virtual environment activated for all work
- [ ] `pyproject.toml` listing dependencies and tool configuration
- [ ] NumPy and SciPy for numerical work; Pandas for tabular data
- [ ] `ruff` running clean on your codebase
- [ ] Performance profiled before any optimisation; vectorisation tried first
- [ ] A `tests/` directory with at least smoke tests and one physics regression test
- [ ] NumPy-style docstrings on all public functions and classes
- [ ] A `README.md` answering the five standard questions
- [ ] `.pre-commit-config.yaml` with ruff hooks installed
- [ ] A GitHub Actions workflow running lint and tests on every PR
- [ ] Docs deploying automatically on merge to `main`
