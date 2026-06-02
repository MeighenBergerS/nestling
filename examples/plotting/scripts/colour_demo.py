"""Colour and accessibility demonstration.

Three sub-figures:
  1. Qualitative palette comparison — Dark2 (Nestling default) vs jet colours.
  2. Sequential colourmap comparison — viridis vs jet on a 2D histogram.
  3. Redundant encoding — colour + line style for greyscale robustness.

Corresponds to Lesson 04 of the Nestling plotting track.
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

STYLE = Path(__file__).parent.parent / "styles" / "nestling.mplstyle"

# Dark2 palette (Nestling default, from ColorBrewer)
DARK2 = ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02"]

# Six colours sampled from jet for comparison
_JET = plt.get_cmap("jet")
JET6 = [_JET(v) for v in np.linspace(0.05, 0.95, 6)]

_PHI0 = 1.44e-18
_E0 = 1e5


def _power_law(E: np.ndarray, gamma: float) -> np.ndarray:
    return _PHI0 * (E / _E0) ** (-gamma)


def qualitative_palette_comparison(output_path: str = "palette_comparison.pdf") -> None:
    """Side-by-side: Dark2 palette vs jet-sampled colours on six spectra.

    Parameters
    ----------
    output_path : str, optional
        Path to save the output figure. Default is ``'palette_comparison.pdf'``.
    """
    plt.style.use(str(STYLE))

    E = np.logspace(3, 7, 300)
    gammas = np.linspace(2.0, 2.7, 6)

    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(6.4, 3.0), sharey=True)

    for i, gamma in enumerate(gammas):
        label = rf"$\gamma={gamma:.1f}$"
        ax_l.loglog(E, E**2 * _power_law(E, gamma), color=DARK2[i], label=label)
        ax_r.loglog(E, E**2 * _power_law(E, gamma), color=JET6[i], label=label)

    for ax, title in zip([ax_l, ax_r], ["Dark2 (CVD-safe)", "jet-sampled"]):
        ax.set_xlabel(r"$E$ / GeV")
        ax.set_title(title, fontsize=8)
        ax.legend(fontsize=6, handlelength=1.5)

    ax_l.set_ylabel(r"$E^2\,\phi_\nu$ / GeV cm$^{-2}$ s$^{-1}$ sr$^{-1}$")
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def colormap_comparison(output_path: str = "colormap_comparison.pdf") -> None:
    """Side-by-side 2D histogram: viridis (perceptually uniform) vs jet.

    Parameters
    ----------
    output_path : str, optional
        Path to save the output figure. Default is ``'colormap_comparison.pdf'``.
    """
    plt.style.use(str(STYLE))

    rng = np.random.default_rng(7)
    x = rng.standard_normal(50_000)
    y = rng.standard_normal(50_000) + 0.5 * x  # correlated

    bins = 60
    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(6.4, 2.8))

    for ax, cmap, title in zip(
        [ax_l, ax_r],
        ["viridis", "jet"],
        ["viridis (perceptually uniform)", "jet (avoid)"],
    ):
        h, xedges, yedges, img = ax.hist2d(x, y, bins=bins, cmap=cmap)
        plt.colorbar(img, ax=ax, label="counts")
        ax.set_xlabel(r"$x$")
        ax.set_ylabel(r"$y$")
        ax.set_title(title, fontsize=8)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def redundant_encoding(output_path: str = "redundant_encoding.pdf") -> None:
    """Six spectra distinguished by both colour and line style.

    Readable in greyscale and under colour vision deficiency.

    Parameters
    ----------
    output_path : str, optional
        Path to save the output figure. Default is ``'redundant_encoding.pdf'``.
    """
    plt.style.use(str(STYLE))

    E = np.logspace(3, 7, 300)
    gammas = np.linspace(2.0, 2.7, 6)
    linestyles = ["-", "--", ":", "-.", (0, (3, 1, 1, 1)), (0, (5, 2))]

    fig, ax = plt.subplots()
    for i, (gamma, ls) in enumerate(zip(gammas, linestyles)):
        ax.loglog(
            E,
            E**2 * _power_law(E, gamma),
            color=DARK2[i],
            linestyle=ls,
            label=rf"$\gamma={gamma:.1f}$",
        )

    ax.set_xlabel(r"$E$ / GeV")
    ax.set_ylabel(r"$E^2\,\phi_\nu$ / GeV cm$^{-2}$ s$^{-1}$ sr$^{-1}$")
    ax.legend(fontsize=6, handlelength=2.5)
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    qualitative_palette_comparison()
    colormap_comparison()
    redundant_encoding()
