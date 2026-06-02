"""Multi-panel figure: spectrum and residuals.

A two-panel layout with a shared x-axis — the standard format for showing
a fit alongside its residuals in particle and astroparticle physics.
Corresponds to Lesson 02 of the Nestling plotting track.
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

STYLE = Path(__file__).parent.parent / "styles" / "nestling.mplstyle"

_PHI0 = 1.44e-18
_E0 = 1e5
_GAMMA = 2.37


def multi_panel_spectrum(output_path: str = "multi_panel.pdf") -> None:
    """Neutrino spectrum with residuals in a two-panel shared-axis layout.

    Parameters
    ----------
    output_path : str, optional
        Path to save the output figure. Default is ``'multi_panel.pdf'``.
    """
    plt.style.use(str(STYLE))

    rng = np.random.default_rng(42)

    E_bins = np.logspace(3, 7, 16)  # bin edges: 1 TeV to 10 PeV
    E_mid = np.sqrt(E_bins[:-1] * E_bins[1:])  # geometric bin centres

    def flux(E: np.ndarray) -> np.ndarray:
        return _PHI0 * (E / _E0) ** (-_GAMMA)

    # Simulated data: normalise so the brightest bin has ~50 counts,
    # then Poisson-fluctuate and rescale back to flux units.
    model_at_mid = flux(E_mid) * E_mid**2
    scale = 50.0 / model_at_mid.max()
    lam = model_at_mid * scale
    data = rng.poisson(lam) / scale
    err = np.sqrt(lam) / scale

    E_fine = np.logspace(3, 7, 400)
    model = flux(E_fine) * E_fine**2

    fig, (ax_top, ax_bot) = plt.subplots(
        2,
        1,
        figsize=(3.46, 4.0),
        sharex=True,
        gridspec_kw={"height_ratios": [3, 1], "hspace": 0.05},
    )

    # Top panel: data + model
    ax_top.loglog(E_fine, model, label="best fit")
    ax_top.errorbar(
        E_mid,
        data,
        yerr=err,
        fmt="o",
        markersize=3,
        linewidth=0.8,
        label="simulated data",
    )
    ax_top.set_ylabel(r"$E^2\,\phi_\nu$ / GeV cm$^{-2}$ s$^{-1}$ sr$^{-1}$")
    ax_top.legend()

    # Bottom panel: (data - model) / model
    residuals = (data - model_at_mid) / model_at_mid
    res_err = err / model_at_mid

    ax_bot.axhline(0, linewidth=0.8, linestyle="--")
    ax_bot.errorbar(
        E_mid,
        residuals,
        yerr=res_err,
        fmt="o",
        markersize=3,
        linewidth=0.8,
    )
    ax_bot.set_xlabel(r"$E$ / GeV")
    ax_bot.set_ylabel("residual")
    ax_bot.set_ylim(-0.8, 0.8)

    plt.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    multi_panel_spectrum()
