# Plotting

This track teaches you to create clear, publication-quality scientific figures.
You will learn the principles of good data visualisation and how to apply them
using matplotlib and the Nestling style file.

!!! note "Acknowledgement"
    Several lessons in this track draw on Ciaran O'Hare's
    [HowToMakeAPlot](https://github.com/cajohare/HowToMakeAPlot), a concise and practical
    guide to scientific plotting in Python.

## Lessons

- [**Lesson 01 — Figure Design Principles**](lesson-01.md): What makes a good scientific figure: clarity, honesty, and accessibility.
- [**Lesson 02 — matplotlib Basics**](lesson-02.md): Creating line plots, scatter plots, histograms, and multi-panel figures.
- [**Lesson 03 — Publication Style**](lesson-03.md): Using the Nestling matplotlib style, LaTeX labels, and exporting to PDF.
- [**Lesson 04 — Colour and Accessibility**](lesson-04.md): Choosing colourblind-friendly palettes and avoiding common pitfalls.

## Examples

See the [`examples/plotting/`](https://github.com/MeighenBergerS/nestling/tree/main/examples/plotting) folder
for runnable scripts demonstrating basic and publication-quality plots.

The Nestling matplotlib style file is at `examples/plotting/styles/nestling.mplstyle`.

## Quick-start

```python
import matplotlib.pyplot as plt
from pathlib import Path

STYLE = Path("examples/plotting/styles/nestling.mplstyle")
plt.style.use(str(STYLE))

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9], label=r"$x^2$")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.legend()
plt.tight_layout()
plt.savefig("figure.pdf", bbox_inches="tight")
plt.close(fig)
```
