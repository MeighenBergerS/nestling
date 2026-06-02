"""Overlapping histograms with step style.

Demonstrates stacking multiple distributions on the same axes using
``histtype='step'`` and ``density=True`` for direct shape comparison.
Corresponds to Lesson 02 of the Nestling plotting track.
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

STYLE = Path(__file__).parent.parent / "styles" / "nestling.mplstyle"


def overlapping_histograms(output_path: str = "histogram.pdf") -> None:
    """Histogram of simulated muon and electron energies.

    Parameters
    ----------
    output_path : str, optional
        Path to save the output figure. Default is ``'histogram.pdf'``.
    """
    plt.style.use(str(STYLE))

    rng = np.random.default_rng(1)
    bins = np.linspace(0, 10, 40)

    # Two populations with different energy distributions
    muons = rng.exponential(scale=3.5, size=4000)
    electrons = rng.exponential(scale=1.5, size=4000)

    fig, ax = plt.subplots()
    ax.hist(
        muons,
        bins=bins,
        histtype="step",
        density=True,
        linewidth=1.0,
        label=r"muons",
    )
    ax.hist(
        electrons,
        bins=bins,
        histtype="step",
        density=True,
        linewidth=1.0,
        linestyle="--",
        label=r"electrons",
    )
    ax.set_xlabel(r"$E$ / GeV")
    ax.set_ylabel("probability density / GeV$^{-1}$")
    ax.set_xlim(0, 10)
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    overlapping_histograms()
