"""Spectral flux models for neutrino sources.

Each model is a callable dataclass: construct it with physical parameters,
then call it like a function to evaluate the differential flux.

    >>> model = PowerLaw(gamma=2.0, norm=1.0, E_ref=1.0)
    >>> model(10.0)   # flux at 10 GeV
    0.01
"""

from dataclasses import dataclass

import numpy as np

from .exceptions import InvalidEnergyError, InvalidSpectralIndexError


@dataclass
class PowerLaw:
    """
    Differential neutrino flux following a single power law.

    The flux is defined as:

        Phi(E) = norm * (E / E_ref) ** (-gamma)

    Parameters
    ----------
    gamma : float
        Spectral index. Must be positive.
    norm : float
        Normalisation at E_ref in GeV^-1 cm^-2 s^-1 sr^-1.
    E_ref : float, optional
        Reference energy in GeV, by default 1e5 (100 TeV).

    Raises
    ------
    InvalidSpectralIndexError
        If gamma <= 0.
    InvalidEnergyError
        If E_ref <= 0.

    Examples
    --------
    >>> model = PowerLaw(gamma=2.0, norm=1.0, E_ref=1.0)
    >>> model(1.0)
    1.0
    >>> model(10.0)
    0.01
    >>> import numpy as np
    >>> model(np.array([1.0, 10.0]))
    array([1.  , 0.01])
    """

    gamma: float
    norm: float
    E_ref: float = 1e5

    def __post_init__(self) -> None:
        if self.gamma <= 0:
            raise InvalidSpectralIndexError(
                f"Spectral index gamma must be positive, got {self.gamma}"
            )
        if self.E_ref <= 0:
            raise InvalidEnergyError(
                f"Reference energy E_ref must be positive, got {self.E_ref}"
            )

    def __call__(self, energy: float | np.ndarray) -> float | np.ndarray:
        """
        Evaluate the flux at the given energy or energies.

        Parameters
        ----------
        energy : float or np.ndarray
            Energy in GeV. Must be positive.

        Returns
        -------
        float or np.ndarray
            Differential flux in GeV^-1 cm^-2 s^-1 sr^-1.
        """
        return self.norm * (energy / self.E_ref) ** (-self.gamma)


@dataclass
class BrokenPowerLaw:
    """
    Differential neutrino flux with a spectral break.

    The flux is:

        Phi(E) = norm * (E / E_break) ** (-gamma1)   if E < E_break
        Phi(E) = norm * (E / E_break) ** (-gamma2)   if E >= E_break

    The model is continuous at E_break by construction
    (both branches equal norm at exactly E_break).

    Parameters
    ----------
    gamma1 : float
        Spectral index below the break. Must be positive.
    gamma2 : float
        Spectral index above the break. Must be positive.
    norm : float
        Normalisation at E_break in GeV^-1 cm^-2 s^-1 sr^-1.
    E_break : float
        Break energy in GeV. Must be positive.

    Raises
    ------
    InvalidSpectralIndexError
        If gamma1 or gamma2 <= 0.
    InvalidEnergyError
        If E_break <= 0.

    Examples
    --------
    >>> model = BrokenPowerLaw(gamma1=2.0, gamma2=3.0, norm=1.0, E_break=1e5)
    >>> model(1e5)   # flux equals norm at the break energy
    1.0
    """

    gamma1: float
    gamma2: float
    norm: float
    E_break: float

    def __post_init__(self) -> None:
        for name, val in [("gamma1", self.gamma1), ("gamma2", self.gamma2)]:
            if val <= 0:
                raise InvalidSpectralIndexError(f"{name} must be positive, got {val}")
        if self.E_break <= 0:
            raise InvalidEnergyError(
                f"Break energy E_break must be positive, got {self.E_break}"
            )

    def __call__(self, energy: float | np.ndarray) -> float | np.ndarray:
        """
        Evaluate the flux at the given energy or energies.

        Parameters
        ----------
        energy : float or np.ndarray
            Energy in GeV. Must be positive.

        Returns
        -------
        float or np.ndarray
            Differential flux in GeV^-1 cm^-2 s^-1 sr^-1.
        """
        E = np.asarray(energy)
        below = (E / self.E_break) ** (-self.gamma1)
        above = (E / self.E_break) ** (-self.gamma2)
        result = self.norm * np.where(E < self.E_break, below, above)
        return float(result) if np.ndim(energy) == 0 else result
