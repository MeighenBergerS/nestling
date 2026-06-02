"""Power-law spectrum with a shaded uncertainty band.

Shows how to combine ``ax.plot`` and ``ax.fill_between`` for a central
value and confidence interval, a common pattern in astroparticle physics.
Corresponds to Lesson 02 of the Nestling plotting track.
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

STYLE = Path(__file__).parent.parent / "styles" / "nestling.mplstyle"

# IceCube best-fit astrophysical flux parameters (approximate, for illustration)
_PHI0 = 1.44e-18  # GeV^{-1} cm^{-2} s^{-1} sr^{-1} at E0 = 100 TeV
_E0 = 1e5  # 100 TeV in GeV


def _power_law(E: np.ndarray, gamma: float) -> np.ndarray:
    return _PHI0 * (E / _E0) ** (-gamma)


def spectrum_with_band(output_path: str = "uncertainty_band.pdf") -> None:
    """Astrophysical neutrino flux with spectral-index uncertainty band.

    Plots E^2-weighted flux (conventional representation) with a shaded
    1-sigma uncertainty band from the spectral index uncertainty.

    Parameters
    ----------
    output_path : str, optional
        Path to save the output figure. Default is ``'uncertainty_band.pdf'``.
    """
    plt.style.use(str(STYLE))

    gamma_best = 2.37
    gamma_lo = gamma_best + 0.13  # softer → lower flux at high E
    gamma_hi = gamma_best - 0.13  # harder → higher flux at high E

    E = np.logspace(3, 7, 400)  # 1 TeV – 10 PeV in GeV

    central = E**2 * _power_law(E, gamma_best)
    lower = E**2 * _power_law(E, gamma_lo)
    upper = E**2 * _power_law(E, gamma_hi)

    fig, ax = plt.subplots()
    ax.fill_between(E, lower, upper, alpha=0.25, label=r"$1\sigma$ uncertainty")
    ax.loglog(E, central, label=r"best fit $\gamma = 2.37$")
    ax.set_xlabel(r"$E$ / GeV")
    ax.set_ylabel(r"$E^2\,\phi_\nu$ / GeV cm$^{-2}$ s$^{-1}$ sr$^{-1}$")
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    spectrum_with_band()
