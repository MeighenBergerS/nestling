"""Basic matplotlib plot example for the Nestling plotting track."""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")


def basic_line_plot(output_path: str = "basic_plot.png") -> None:
    """Create a basic line plot and save it to a file.

    Parameters
    ----------
    output_path : str, optional
        Path to save the output figure. Default is ``'basic_plot.png'``.
    """
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label="sin(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Basic Line Plot")
    ax.legend()

    plt.tight_layout()
    plt.savefig(output_path, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    basic_line_plot()
