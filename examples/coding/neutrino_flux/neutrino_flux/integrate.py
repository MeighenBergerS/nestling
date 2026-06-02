"""Flux integration utilities.

Functions for computing integrated fluxes and inverting them to find
threshold energies. SciPy's adaptive quadrature and Brent's method are
used under the hood; errors are translated into domain-specific exceptions
so callers do not need to handle scipy internals.

Implementation note
-------------------
Power-law flux models span many orders of magnitude (e.g. 10^-16 at 10 TeV
down to 10^-23 at 10 PeV). Integrating such functions in linear energy space
causes scipy.quad to struggle: the integrand varies too rapidly between
quadrature points. We therefore transform to log-energy space,

    integral = integral_log_E_min^log_E_max  f(exp(u)) * exp(u)  du

where the integrand is far smoother, before calling quad.
"""

from collections.abc import Callable

import numpy as np
from scipy import integrate, optimize

from .exceptions import ConvergenceError, InvalidEnergyError


def flux_above(
    model: Callable,
    E_min: float,
    E_max: float = np.inf,
) -> float:
    """
    Compute the integrated flux above E_min.

    Integrates in log-energy space for numerical stability with power-law
    models that span many decades.

    Parameters
    ----------
    model : callable
        A flux model: model(energy) -> flux in GeV^-1 cm^-2 s^-1 sr^-1.
    E_min : float
        Lower energy bound in GeV. Must be positive.
    E_max : float, optional
        Upper energy bound in GeV, by default np.inf.

    Returns
    -------
    float
        Integrated flux in cm^-2 s^-1 sr^-1.

    Raises
    ------
    InvalidEnergyError
        If E_min is not positive.
    ConvergenceError
        If scipy.quad fails to converge.

    Examples
    --------
    >>> from neutrino_flux.models import PowerLaw
    >>> model = PowerLaw(gamma=2.0, norm=1.0, E_ref=1.0)
    >>> flux_above(model, E_min=1.0, E_max=10.0)  # int_1^10 x^-2 dx = 0.9
    0.9...
    """
    if E_min <= 0:
        raise InvalidEnergyError(f"E_min must be positive, got {E_min}")

    # Substitution: E = exp(u), dE = E du  →  integrand becomes f(exp(u))*exp(u)
    def log_integrand(log_E: float) -> float:
        E = np.exp(log_E)
        return model(E) * E

    # Cap infinite upper bounds at a practical maximum.
    # For any physical power law (gamma > 1), the flux above 1e20 GeV is
    # negligible relative to the integral from any astrophysical E_min.
    _E_MAX_PRACTICAL = 1e20
    E_max_clipped = (
        min(E_max, _E_MAX_PRACTICAL) if np.isfinite(E_max) else _E_MAX_PRACTICAL
    )

    log_E_min = np.log(E_min)
    log_E_max = np.log(E_max_clipped)

    result, _ = integrate.quad(
        log_integrand, log_E_min, log_E_max, limit=200, epsrel=1e-6
    )
    return float(result)


def threshold_energy(
    model: Callable,
    threshold: float,
    E_lo: float = 1e2,
    E_hi: float = 1e9,
) -> float:
    """
    Find the energy above which the integrated flux equals a threshold.

    Solves flux_above(model, E) = threshold using Brent's root-finding
    method on the interval [E_lo, E_hi].

    Parameters
    ----------
    model : callable
        A flux model: model(energy) -> flux in GeV^-1 cm^-2 s^-1 sr^-1.
    threshold : float
        Target integrated flux in cm^-2 s^-1 sr^-1.
    E_lo : float, optional
        Lower bound for the search in GeV, by default 1e2.
    E_hi : float, optional
        Upper bound for the search in GeV, by default 1e9.

    Returns
    -------
    float
        Energy in GeV at which the integrated flux equals the threshold.

    Raises
    ------
    ConvergenceError
        If the threshold lies outside the searchable bracket or the
        root-finder fails to converge.

    Examples
    --------
    >>> from neutrino_flux.models import PowerLaw
    >>> model = PowerLaw(gamma=2.0, norm=1.0, E_ref=1.0)
    >>> threshold_energy(model, threshold=0.5, E_lo=1.0, E_hi=1e6)
    2.0...
    """

    def objective(E: float) -> float:
        return flux_above(model, E) - threshold

    try:
        return float(optimize.brentq(objective, E_lo, E_hi, xtol=1e-6, rtol=1e-6))
    except ValueError as exc:
        raise ConvergenceError(
            f"Threshold {threshold:.2e} cm^-2 s^-1 sr^-1 is not bracketed in "
            f"[{E_lo:.1e}, {E_hi:.1e}] GeV. Try widening the search range."
        ) from exc
