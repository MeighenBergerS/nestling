# [Project Name] — coding and documentation skill

Use this skill whenever working in the [Project Name] repository.
Copy this file to `.claude/commands/coding.md` in your project and fill in the bracketed
placeholders. Load it with `/coding` at the start of a session.

---

## Environment

**Python interpreter** — always use the project virtual environment; never rely on a
bare `python` or `python3` in PATH:

```text
.venv/bin/python
```

**Install the package in editable mode** (once, after cloning):

```sh
.venv/bin/pip install -e .
```

**Run the test suite:**

```sh
.venv/bin/pytest tests/ -x          # stop at first failure
.venv/bin/pytest tests/ -x -k name  # run tests matching 'name'
.venv/bin/pytest tests/ -s -v       # verbose with stdout
```

**Lint and format:**

```sh
.venv/bin/ruff check src/           # linting
.venv/bin/ruff format src/          # formatting
```

Always run from the **repository root**. Resource paths and conftest.py both assume this.

---

## Project structure

```text
src/[package]/          main Python package
  __init__.py           public API re-exports
  [core module].py      [brief description]
  [analysis module].py  [brief description]
  [io module].py        [brief description]

tests/                  pytest test suite (mirrors src/ layout)
examples/               runnable scripts demonstrating key workflows
docs/                   documentation source (MkDocs)
resources/              data files, model weights, reference tables
```

Key entry point: `[describe the main class or function a user calls]`.

---

## Running the code

**Minimal example:**

```python
from [package] import [MainClass]

obj = [MainClass]([config])
result = obj.[main_method]()
```

**Configuration:** [describe how configuration works — TOML file, dataclass, dict, etc.]

---

## Key invariants

These are constraints the code assumes. Violating them produces silent wrong results,
not exceptions — do not introduce code that breaks them.

- [Physical units]: all quantities in SI / [field convention] units throughout.
  Never store dimensionless intermediates in module-level state.
- [Array shapes]: output arrays are always shape `(N,)`, never `(N, 1)`.
- [Random state]: numpy/JAX random state is always passed explicitly to functions that use it.
  No global seeds in library code.
- [Domain cutoff]: [describe any numerical domain limit, e.g. "distance cutoff at 300 m — model
  not trained beyond this"].

---

## Coding conventions

### Naming

- Classes: `PascalCase`
- Functions, variables, module-level constants: `snake_case`
- Private helpers: prefix with `_` (`_compute_weight`)
- Constants that are physically meaningful: `ALL_CAPS` (`C_LIGHT_CM_PER_NS = 29.979`)

### Type hints

All public functions must have complete type hints.
Use `numpy.typing.NDArray` for array arguments.

```python
def bin_counts(events: NDArray[np.float64], edges: NDArray[np.float64]) -> NDArray[np.int64]:
    ...
```

### Docstrings

NumPy format for all public functions:

```python
def function_name(arg1: type, arg2: type) -> type:
    """One-line summary (imperative, ≤ 79 chars).

    Extended description if needed — only when the WHY is non-obvious.

    Parameters
    ----------
    arg1 : type
        Description.
    arg2 : type
        Description.

    Returns
    -------
    type
        Description.

    Raises
    ------
    ValueError
        If [condition].
    """
```

Rules:

- Summary line must start with an **imperative verb** ("Compute...", "Return...",
  "Build...", "Create..."). Never "Makes...", never a noun phrase.
- Do not repeat the function name in the summary.
- Do not document parameters that are obvious from the type hint.

### Error handling

- Raise `ValueError` for invalid inputs at public API boundaries.
- Do not catch and re-raise exceptions without adding information.
- Do not use bare `except:` — always specify the exception type.

### Testing

- One test file per source module: `tests/test_[module].py`.
- Test names must describe the scenario: `test_bin_counts_empty_input`,
  not `test_1` or `test_bin_counts`.
- Every public function must have at least one test covering the expected input
  and one covering a boundary condition (empty input, single element, extreme value).
- Tests must not depend on network access, external files outside `tests/resources/`,
  or wall-clock time.

---

## Documentation

### Docstrings vs. comments

- **Docstrings** explain the public contract: what the function does, what it takes,
  what it returns.
- **Inline comments** explain non-obvious WHY: a hidden constraint, a workaround
  for a known bug, a physical approximation. One line maximum.
- Do not comment what the code obviously does. `# increment i` is noise.

### Building the docs

```sh
source .venv/bin/activate
mkdocs serve      # local preview at http://localhost:8000
mkdocs build      # build static site in site/
```

---

## Common mistakes to avoid

| Do not do this | Do this instead |
| -------------- | --------------- |
| `import [package]` from outside the repo root | Always run from repo root |
| `python script.py` with system Python | `.venv/bin/python script.py` |
| `git add -A` without reviewing `git status` | Stage specific files by name |
| Merge code you cannot explain | Ask for an explanation before accepting |
| Add a result to the conclusion that is not derived in the body | Keep conclusion to restating body results |

---

## Before committing

- [ ] All new public functions have docstrings and type hints.
- [ ] New code has corresponding tests; tests pass (`pytest tests/ -x`).
- [ ] Lint passes (`ruff check src/`).
- [ ] No hard-coded paths, credentials, or API keys.
- [ ] Random seeds set for any function that produces numeric results.
- [ ] `git diff` reviewed — no unintended changes included.
