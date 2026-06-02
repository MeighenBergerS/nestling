"""
neutrino_flux — spectral models and flux integration for neutrino sources.

This package is a worked example for the nestling coding track.
It demonstrates: dataclass-based models, custom exceptions, NumPy-style
docstrings, and a clean public API.

Examples
--------
Compute the IceCube best-fit diffuse flux and find the energy above which
the integrated flux drops below a given threshold:

>>> from neutrino_flux import PowerLaw, flux_above, threshold_energy
>>> model = PowerLaw(gamma=2.37, norm=1.66e-18, E_ref=1e5)
>>> flux_above(model, E_min=1e4, E_max=1e7)  # doctest: +ELLIPSIS
...
>>> threshold_energy(model, threshold=1e-22)  # doctest: +ELLIPSIS
...
"""

from .integrate import flux_above, threshold_energy
from .models import BrokenPowerLaw, PowerLaw

__all__ = ["PowerLaw", "BrokenPowerLaw", "flux_above", "threshold_energy"]
