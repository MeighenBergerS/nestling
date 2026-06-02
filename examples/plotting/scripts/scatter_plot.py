"""Scatter plot with a continuous colour encoding.

Demonstrates ax.scatter with a colorbar, suitable for three-variable data.
Corresponds to Lesson 02 of the Nestling plotting track.
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

STYLE = Path(__file__).parent.parent / "styles" / "nestling.mplstyle"


def scatter_with_colorbar(output_path: str = "scatter_plot.pdf") -> None:
    """Scatter plot of simulated neutrino events coloured by reconstructed energy.

    Parameters
    ----------
    output_path : str, optional
        Path to save the output figure. Default is ``'scatter_plot.pdf'``.
    """
    plt.style.use(str(STYLE))

    rng = np.random.default_rng(0)
    n = 300
    # Simulated arrival directions (zenith, azimuth in degrees)
    zenith = rng.uniform(0, 180, n)
    azimuth = rng.uniform(0, 360, n)
    log_energy = rng.uniform(2, 6, n)  # log10(E / GeV)

    fig, ax = plt.subplots()
    sc = ax.scatter(
        azimuth,
        np.cos(np.radians(zenith)),
        c=log_energy,
        cmap="viridis",
        s=8,
        linewidths=0,
    )
    cb = plt.colorbar(sc, ax=ax)
    cb.set_label(r"$\log_{10}(E\,/\,\mathrm{GeV})$")
    ax.set_xlabel(r"azimuth / ${}^{\circ}$")
    ax.set_ylabel(r"$\cos\,\theta_\mathrm{zen}$")
    ax.set_xlim(0, 360)
    ax.set_ylim(-1, 1)
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    scatter_with_colorbar()
