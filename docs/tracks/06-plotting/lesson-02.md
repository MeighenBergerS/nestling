# Lesson 02: matplotlib Basics

matplotlib is the standard plotting library in scientific Python.
It is verbose by design. Every element of a figure can be controlled explicitly, and that
verbosity pays off when you need publication-quality output.

This lesson covers the API patterns you will use in almost every figure, illustrated with
physics-relevant examples.

---

## The Figure / Axes model

matplotlib separates the canvas from the plot area:

- **`Figure`**: the whole image, including all panels and any surrounding whitespace.
- **`Axes`**: a single plot panel, with its own axis limits, labels, ticks, and data.

One Figure can contain many Axes.
Always create them together:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()          # one panel
fig, axes = plt.subplots(1, 3)    # one row, three panels
fig, axes = plt.subplots(2, 2)    # 2x2 grid
```

The `ax` / `axes` objects are where you draw data.
The `fig` object is what you save.

!!! tip "Prefer the object-oriented API"
    matplotlib has two interfaces: the `plt.plot(...)` shortcut (procedural) and `ax.plot(...)`
    (object-oriented). Always use the object-oriented form. It makes multi-panel figures and
    function-based code unambiguous.

---

## Line plots

The workhorse of physics plots.

```python
import numpy as np
import matplotlib.pyplot as plt

E = np.logspace(0, 6, 300)       # 1 GeV to 1 PeV
phi = 1e-18 * (E / 1e5) ** -2.7  # E^{-2.7} spectrum

fig, ax = plt.subplots()
ax.loglog(E, phi, label=r"$E^{-2.7}$ spectrum")
ax.set_xlabel(r"$E$ / GeV")
ax.set_ylabel(r"$\phi$ / GeV$^{-1}$ cm$^{-2}$ s$^{-1}$ sr$^{-1}$")
ax.legend()
plt.tight_layout()
plt.savefig("spectrum.pdf")
plt.close(fig)
```

Key points:

- `ax.loglog` sets both axes to log scale; `ax.semilogx` / `ax.semilogy` for one axis.
- Raw strings (`r"..."`) let you write LaTeX without doubling backslashes.
- Always call `plt.close(fig)` when saving in scripts to release memory.

### Labelling curves: annotations over legends

Legends are fine for exploratory work, but for publication figures a **direct annotation**
placed close to each curve is almost always clearer.
The reader's eye does not have to travel to a separate box and back, and the figure needs
less whitespace reserved for the legend.
The Nestling style already removes the legend frame (`legend.frameon: False`), which is a
step in the right direction, but consider going further:

```python
fig, ax = plt.subplots()
ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x))

# Place the label at the right end of each curve
ax.text(x[-1] + 0.05, np.sin(x[-1]), r"$\sin(x)$", va="center", fontsize=7)
ax.text(x[-1] + 0.05, np.cos(x[-1]), r"$\cos(x)$", va="center", fontsize=7)

ax.set_xlim(0, x[-1] + 0.8)   # leave room for the labels
```

`ax.annotate` gives more control when you need a pointer arrow:

```python
ax.annotate(
    r"$\sin(x)$",
    xy=(np.pi / 2, 1.0),          # tip of the arrow (on the curve)
    xytext=(np.pi / 2 + 0.4, 0.8),  # label position
    arrowprops=dict(arrowstyle="-", linewidth=0.6),
    fontsize=7,
)
```

!!! tip "When a legend is still appropriate"
    Use a legend when there are many curves, when the curves overlap so much that
    direct annotation would collide, or when a referee specifically requests one.
    In those cases keep it: no frame, outside the data area if possible.

---

## Scatter plots

```python
fig, ax = plt.subplots()
ax.scatter(x, y, s=20, c=z, cmap="viridis", zorder=3)
cb = plt.colorbar(ax.collections[0], ax=ax)
cb.set_label(r"$z$")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
plt.tight_layout()
plt.savefig("scatter.pdf")
plt.close(fig)
```

- `s` sets marker size in points².
- `c` and `cmap` colour-code each point by a third variable.
- `zorder` controls drawing order (higher = drawn on top).

---

## Histograms

```python
rng = np.random.default_rng(42)
data = rng.exponential(scale=1.0, size=5000)

fig, ax = plt.subplots()
ax.hist(data, bins=50, histtype="step", density=True, label="data")
ax.set_xlabel(r"$x$")
ax.set_ylabel("probability density")
ax.legend()
plt.tight_layout()
plt.savefig("histogram.pdf")
plt.close(fig)
```

- `histtype="step"` draws an outline without fill, cleaner for overlaying multiple distributions.
- `density=True` normalises to a probability density (area = 1).
- `bins` can be an integer (number of bins) or an array of bin edges.

---

## Shaded uncertainty bands

Shading the region between lower and upper bounds is clearer than two dashed lines:

```python
E = np.logspace(0, 6, 300)
central = 1e-18 * (E / 1e5) ** -2.7
lower   = 0.8 * central
upper   = 1.2 * central

fig, ax = plt.subplots()
ax.loglog(E, central, label="best fit")
ax.fill_between(E, lower, upper, alpha=0.3, label=r"$\pm 20\,\%$")
ax.set_xlabel(r"$E$ / GeV")
ax.set_ylabel(r"$\phi$")
ax.legend()
plt.tight_layout()
plt.savefig("band.pdf")
plt.close(fig)
```

---

## Multi-panel figures

```python
fig, axes = plt.subplots(1, 2, figsize=(6.4, 3.0), sharey=False)

axes[0].plot(x1, y1)
axes[0].set_xlabel(r"$x_1$")
axes[0].set_ylabel(r"$y$")

axes[1].plot(x2, y2, color="C1")
axes[1].set_xlabel(r"$x_2$")

fig.suptitle("Two panels", y=1.02)  # above both panels
plt.tight_layout()
plt.savefig("two_panels.pdf")
plt.close(fig)
```

- `sharey=True` / `sharex=True` links axis limits across panels, useful when comparing the
  same quantity side by side.
- `fig.suptitle` places a shared title above all panels.
- Adjust `figsize` so the final printed width matches the journal column width.

---

## Inset axes

For a zoomed inset or a secondary plot within a panel:

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fig, ax = plt.subplots()
ax.plot(x, y)

axins = inset_axes(ax, width="40%", height="40%", loc="upper right")
axins.plot(x_zoom, y_zoom)
axins.set_xlim(x_lo, x_hi)
```

---

## Saving figures

```python
plt.savefig("figure.pdf")                         # vector, best for journals
plt.savefig("figure.svg")                         # vector, editable in Inkscape
plt.savefig("figure.png", dpi=300)                # raster, 300 DPI minimum for print
plt.savefig("figure.pdf", bbox_inches="tight")    # trims whitespace
```

Always save at the **final print size**, not scaled down later.
PDF and SVG scale without quality loss; PNG does not.

---

## What to read next

[Lesson 03](lesson-03.md) shows how to apply the Nestling style file so every figure you
produce is immediately publication-ready, and covers LaTeX axis labels and figure sizing for
single- and two-column layouts.
