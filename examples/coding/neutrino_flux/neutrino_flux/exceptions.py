"""Custom exceptions for neutrino_flux.

Defining specific exception classes (rather than raising generic ValueError or
RuntimeError) lets callers catch exactly the error they care about and gives
users traceback messages that are immediately actionable.
"""


class InvalidSpectralIndexError(ValueError):
    """Raised when a spectral index is non-positive."""


class InvalidEnergyError(ValueError):
    """Raised when an energy value is non-positive or otherwise out of range."""


class ConvergenceError(RuntimeError):
    """Raised when a numerical integration or root-finding step fails to converge."""
