"""Generate the before/after example figures used in the plotting track docs.

Run from the repo root:

    python examples/plotting/scripts/generate_doc_figures.py

Outputs go to docs/tracks/06-plotting/figures/ so MkDocs can serve them.
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

STYLE = Path(__file__).parent.parent / "styles" / "nestling.mplstyle"
OUT = Path(__file__).parents[3] / "docs" / "tracks" / "06-plotting" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

DARK2 = ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02"]

x = np.linspace(0, 2 * np.pi, 200)


def bad_figure() -> None:
    """matplotlib defaults — demonstrates common mistakes."""
    with plt.rc_context(
        {
            "font.family": "sans-serif",
            "font.size": 12,
            "axes.grid": True,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.top": False,
            "ytick.right": False,
            "legend.frameon": True,
            "axes.prop_cycle": plt.rcParams["axes.prop_cycle"],
        }
    ):
        fig, ax = plt.subplots(figsize=(3.5, 3.5))
        ax.plot(x, np.sin(x), label="sin(x)")
        ax.plot(x, np.cos(x), label="cos(x)")
        ax.set_title("Sine and Cosine")  # title inside panel
        ax.set_xlabel("x")  # no symbols, no units
        ax.set_ylabel("y")
        ax.legend()  # framed legend
        plt.tight_layout()
        plt.savefig(OUT / "before.png", dpi=150, bbox_inches="tight")
        plt.close(fig)


def good_figure() -> None:
    """Nestling style — demonstrates preferred approach."""
    plt.style.use(str(STYLE))

    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), color=DARK2[3])
    ax.plot(x, np.cos(x), color=DARK2[0])

    # Direct annotations — no legend box needed
    ax.text(2.9, np.sin(3), r"$\sin(x)$", va="center", fontsize=7, rotation=-70, color=DARK2[3])
    ax.text(2.7, np.cos(3) + 0.16, r"$\cos(x)$", va="center", fontsize=7, color=DARK2[0])

    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_xlim(0, 2 * np.pi)

    plt.tight_layout()
    plt.savefig(OUT / "after.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    bad_figure()
    good_figure()
    print(f"Figures written to {OUT}")
