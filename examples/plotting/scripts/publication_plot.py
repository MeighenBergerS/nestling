"""Publication-quality matplotlib plot using the Nestling style."""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

STYLE = Path(__file__).parent.parent / "styles" / "nestling.mplstyle"


def publication_line_plot(output_path: str = "publication_plot.pdf") -> None:
    """Create a publication-quality line plot and save it to a file.

    Parameters
    ----------
    output_path : str, optional
        Path to save the output figure. Default is ``'publication_plot.pdf'``.
    """
    plt.style.use(str(STYLE))

    x = np.linspace(0, 2 * np.pi, 200)

    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), label=r"$\sin(x)$")
    ax.plot(x, np.cos(x), label=r"$\cos(x)$")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.legend()

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close(fig)


if __name__ == "__main__":
    publication_line_plot()
