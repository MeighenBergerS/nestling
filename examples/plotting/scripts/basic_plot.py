"""Basic matplotlib plot example for the Nestling plotting track.

Demonstrates the Nestling style and the preferred way to label curves:
direct annotation close to the line rather than a legend box.
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from examples.plotting.scripts.colour_demo import DARK2

matplotlib.use("Agg")

STYLE = Path(__file__).parent.parent / "styles" / "nestling.mplstyle"


def basic_line_plot(output_path: str = "basic_plot.pdf") -> None:
    """Create a basic line plot following the Nestling style guide.

    Labels the curve with a direct text annotation rather than a legend —
    the preferred approach when there are only a few curves.

    Parameters
    ----------
    output_path : str, optional
        Path to save the output figure. Default is ``'basic_plot.pdf'``.
    """
    plt.style.use(str(STYLE))

    x = np.linspace(0, 2 * np.pi, 200)

    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x))
    ax.plot(x, np.cos(x))

    # Direct annotation — preferred over a legend for a small number of curves
    ax.text(2.9, np.sin(3), r"$\sin(x)$", va="center", fontsize=7, rotation=-70, color=DARK2[3])
    ax.text(2.7, np.cos(3) + 0.16, r"$\cos(x)$", va="center", fontsize=7, color=DARK2[0])

    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_xlim(0, x[-1])

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    basic_line_plot()
