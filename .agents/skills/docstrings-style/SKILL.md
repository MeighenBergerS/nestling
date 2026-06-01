---
name: docstrings-style
description: Enforces style rules for docstrings. Use when checking or generating docstrings in Nestling.
---

# Docstring Style

## When to Use This Skill

Use this skill whenever the user asks to "generate docstrings", "normalise docstrings",
"convert docstrings to NumPy style", "check docstrings", or otherwise clean up Python docstrings.

Use it when generating docstrings alongside new code as well.

Do **not** apply these rules to pure code identifiers unless explicitly allowed below.

## Instructions

1. Use the NumPy docstring formatting rules defined in the [numpy-docstring-format](../numpy-docstring-format/SKILL.md) skill.

2. Use the project-specific text styling rules defined in the
   [text-style-nestling](../text-style-nestling/SKILL.md) skill.

3. Keep new or edited docstrings **consistent with existing docstrings** in formatting, styling, and type notation.

4. **Preserve content and tone in existing docstrings**: when editing, do not change the high-level
   meaning or intent. Preserve informal phrasing where possible.

5. **Keep types in docstrings consistent with type hints**:

   - Variable types in docstrings must exactly match the type hints, if available.
   - If type hints are unavailable, refer to the
     [Python documentation](https://docs.python.org/3/library/stdtypes.html) for type names.
   - Types from imported libraries must match how those libraries are imported.

   ```python
   import numpy as np

   def scale(x: np.ndarray, factor: float) -> np.ndarray:
       """Scale an array by a constant factor.

       Parameters
       ----------
       x : np.ndarray
           Input array.
       factor : float
           Scaling factor.

       Returns
       -------
       result : np.ndarray
           Scaled array.
       """
   ```

6. **Do not rename parameters or change function signatures**: treat the code as the source of
   truth. If a docstring parameter name differs from the signature, update the docstring to match.

## Good Docstring Examples

Constructor:

```python
def __init__(self, data: list[float], label: str) -> None:
    """Initialize the data container.

    Parameters
    ----------
    data : list of float
        List of numerical values.
    label : str
        Human-readable label for this dataset.
    """
```

Function with parameters, returns, and raises:

```python
def normalise(values: np.ndarray, axis: int = 0) -> np.ndarray:
    """Normalise an array along the given axis.

    Parameters
    ----------
    values : np.ndarray
        Input array to normalise.
    axis : int, optional
        Axis along which to normalise. Default is 0.

    Returns
    -------
    result : np.ndarray
        Normalised array with values in [0, 1].

    Raises
    ------
    ValueError
        Raised if the range along ``axis`` is zero.
    """
```
