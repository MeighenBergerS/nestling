"""Utility functions for the modular project example."""


def format_result(value: float, precision: int = 3) -> str:
    """Format a numerical result as a string.

    Parameters
    ----------
    value : float
        The value to format.
    precision : int, optional
        Number of decimal places. Default is 3.

    Returns
    -------
    result : str
        Formatted string representation of ``value``.

    Examples
    --------
    >>> format_result(3.14159)
    '3.142'
    >>> format_result(3.14159, precision=2)
    '3.14'
    """
    return f"{value:.{precision}f}"
