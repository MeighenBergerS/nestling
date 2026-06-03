# Lesson 03: Publication Style

A consistent style across all figures in a paper signals professionalism and makes revision
much easier. Changing the font size across fifteen figures is one edit instead of fifteen.
matplotlib style sheets let you encode all style choices once and apply them everywhere.

This lesson covers the Nestling style file, LaTeX labels, and how to size figures correctly
for journal submission.

!!! note "Acknowledgement"
    The Nestling style is the author's own. Ciaran O'Hare's
    [HowToMakeAPlot](https://github.com/cajohare/HowToMakeAPlot) is an excellent reference
    for the broader question of what distinguishes publication-quality figures and is well
    worth reading alongside this lesson.

---

## The Nestling matplotlib style file

The style file lives at `examples/plotting/styles/nestling.mplstyle`.
Its full contents and the rationale for each setting:

```ini
# Nestling matplotlib style
# Adapted from the Beacom-group conformal style.
# Optimised for publication-quality single or two-column figures.

text.usetex        : False
font.family        : serif
font.size          : 8.0

# Colour cycle — Dark2 palette (colourblind-friendly)
axes.prop_cycle    : cycler('color', ["#e7298a", "#1b9e77", "#d95f02", "#7570b3", "#66a61e", "#e6ab02"])

axes.grid          : False
legend.frameon     : False

axes.titlesize     : 8.0
axes.labelsize     : 8.0

xtick.direction    : in
ytick.direction    : in
xtick.top          : True
ytick.right        : True
xtick.labelsize    : 8
ytick.labelsize    : 8

figure.dpi         : 100
figure.figsize     : 3.0, 3.0

lines.linewidth    : 1.0
```

### What each group does

| Setting | Value | Why |
|---------|-------|-----|
| `text.usetex` | `False` | No local LaTeX required; set to `True` to enable full LaTeX rendering (see below) |
| `font.family` | `serif` | Matches the body text in most physics journals |
| `font.size` | `8.0` | Legible at single-column print size without dominating the data |
| `axes.prop_cycle` | Dark2 colours | Colourblind-friendly; see [Lesson 04](lesson-04.md) |
| `axes.grid` | `False` | Gridlines add clutter; omit unless values need to be read off precisely |
| `legend.frameon` | `False` | The legend box wastes ink; remove it |
| `xtick.direction` / `ytick.direction` | `in` | Ticks point inward, conventional in HEP and astro |
| `xtick.top` / `ytick.right` | `True` | Mirror ticks for readability without a grid |
| `figure.figsize` | `3.0, 3.0` | Matches a single-column panel in most journals |
| `lines.linewidth` | `1.0` | Clean at print size; increase to 1.5 for slides |

---

## Applying the style

Load the style once at the top of your script:

```python
import matplotlib.pyplot as plt
from pathlib import Path

STYLE = Path(__file__).parent / "styles" / "nestling.mplstyle"
plt.style.use(str(STYLE))
```

Every `fig, ax = plt.subplots()` call after this point uses the Nestling style.

You can also combine styles:

```python
plt.style.use([str(STYLE), "path/to/your_overrides.mplstyle"])
```

Or override individual settings inline without a file:

```python
import matplotlib as mpl
mpl.rcParams["lines.linewidth"] = 1.5   # heavier lines for slides
```

---

## LaTeX labels

### Without a local LaTeX installation

With `text.usetex: False` (the default), matplotlib uses its own math renderer.
This covers the vast majority of physics notation:

```python
ax.set_xlabel(r"$E$ / GeV")
ax.set_ylabel(r"$\phi_\nu$ / GeV$^{-1}$ cm$^{-2}$ s$^{-1}$ sr$^{-1}$")
ax.set_title(r"$\bar{\nu}_e$ flux")
```

Use raw strings (`r"..."`) throughout to avoid having to escape backslashes.

### With a local LaTeX installation

For full LaTeX rendering (real Computer Modern font, `\text{}`, custom `\newcommand`s):

```python
import matplotlib as mpl
mpl.rcParams["text.usetex"] = True
mpl.rcParams["text.latex.preamble"] = r"\usepackage{amsmath}"
```

Or add a one-line override style:

```ini
# tex_override.mplstyle
text.usetex: True
```

```python
plt.style.use([str(STYLE), "tex_override.mplstyle"])
```

!!! warning "LaTeX rendering is slow"
    With `text.usetex = True`, each figure takes several seconds to render because matplotlib
    calls a real LaTeX compiler. Keep it off during development; enable it for the final save.

---

## Figure sizing for journals

Most physics journals use one of two column widths:

| Layout | Typical width |
|--------|--------------|
| Single column | 88 mm ≈ 3.46 in |
| Two-column (full page) | 180 mm ≈ 7.09 in |

The Nestling default (3.0 × 3.0 in) is close to single-column.
Adjust for your target journal:

```python
# Single column, 4:3 aspect
fig, ax = plt.subplots(figsize=(3.46, 2.6))

# Full width, two-panel
fig, axes = plt.subplots(1, 2, figsize=(7.09, 3.0))
```

!!! tip "Check at the final size"
    Always open the saved PDF at 100 % zoom, or print a draft copy, before submitting.
    A figure that looks fine on screen at 200 % can have illegible tick labels at print size.

---

## Exporting

```python
plt.savefig("figure.pdf", bbox_inches="tight")
```

- **PDF**: vector format, preferred by journals. Fonts are embedded.
- **SVG**: vector, editable in Inkscape. Useful for final touch-ups.
- **EPS**: accepted by many older journal workflows; avoid if PDF is accepted.
- **PNG**: raster only; use `dpi=300` minimum. Set `dpi=600` for figures with fine lines.

`bbox_inches="tight"` trims excess whitespace around the figure, which avoids
awkward spacing when the figure is included in a LaTeX document.

---

## A minimal complete example

```python
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

STYLE = Path("examples/plotting/styles/nestling.mplstyle")
plt.style.use(str(STYLE))

E = np.logspace(0, 6, 300)

fig, ax = plt.subplots()
ax.loglog(E, 1e-18 * (E / 1e5) ** -2.7, label=r"$E^{-2.7}$")
ax.loglog(E, 1e-18 * (E / 1e5) ** -2.0, label=r"$E^{-2.0}$")
ax.set_xlabel(r"$E$ / GeV")
ax.set_ylabel(r"$\phi$ / GeV$^{-1}$ cm$^{-2}$ s$^{-1}$ sr$^{-1}$")
ax.legend()
plt.tight_layout()
plt.savefig("spectrum.pdf", bbox_inches="tight")
plt.close(fig)
```

The full example is in
[`examples/plotting/scripts/publication_plot.py`](https://github.com/MeighenBergerS/nestling/blob/main/examples/plotting/scripts/publication_plot.py).

---

## What to read next

[Lesson 04](lesson-04.md) covers colour in depth: why colourblind-friendly palettes matter,
how to choose between sequential, diverging, and qualitative colour maps, and tools for
checking your figures before submission.
