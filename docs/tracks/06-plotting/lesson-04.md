# Lesson 04 — Colour and Accessibility

Colour is the element of a figure most likely to cause problems for readers and most likely to
be handled carelessly.
This lesson covers how to choose palettes that are accurate, accessible, and still visually
effective.

!!! note "Acknowledgement"
    The discussion of palette choice in this lesson draws on Ciaran O'Hare's
    [HowToMakeAPlot](https://github.com/cajohare/HowToMakeAPlot), which contains practical
    examples of colourblind simulations and palette comparisons for physics figures.

---

## Why colour choice matters

Roughly **8 % of men** and **0.5 % of women** have some form of colour vision deficiency (CVD),
most commonly red-green.
On top of that, many readers will encounter your figure in a printed PDF, a black-and-white
photocopy, or a low-contrast projection.

A figure that relies on colour as the sole distinguishing feature excludes a significant fraction
of your audience.
The fix is not to abandon colour — it is to use colour correctly.

---

## Types of colour palette

Choose the palette type to match the type of data:

| Type | When to use | Examples |
|------|-------------|---------|
| **Qualitative** | Distinct categories with no ordering | Model A vs B vs C, different experiments |
| **Sequential** | Ordered data from low to high | Flux intensity, temperature, probability |
| **Diverging** | Data diverging from a meaningful midpoint | Residuals, signed differences, correlation |

Using a sequential palette for categorical data is a common mistake — the implied ordering
misleads the reader.

---

## Qualitative palettes

For line plots and markers comparing distinct categories, use a qualitative palette from
[ColorBrewer](https://colorbrewer2.org/#type=qualitative&scheme=Set1&n=7).

The Nestling style uses **Dark2**, a six-colour qualitative palette that is:

- Distinguishable by the most common CVD types (deuteranopia, protanopia, tritanopia).
- Distinguishable in greyscale when combined with different line styles.
- Distinguishable on screen and in print.

Dark2 hex codes:

```python
DARK2 = ["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02"]
```

These are already set as the default colour cycle in `nestling.mplstyle`.

Other well-tested qualitative palettes from ColorBrewer:

- **Set1** — high-contrast, slightly garish; works when CVD is not a concern.
- **Set2** — softer, but less distinguishable in greyscale.
- **Paired** — six pairs of light/dark variants; good for showing related quantities.

Explore all options interactively at
[colorbrewer2.org](https://colorbrewer2.org/#type=qualitative&scheme=Set1&n=7) —
the site lets you filter by CVD-safe and print-safe status.

---

## Sequential and diverging colormaps

For heatmaps, 2D histograms, and scatter plots coloured by a continuous quantity, use a
**perceptually uniform** colormap.

### Why "jet" is wrong

The default matplotlib colormap for many years was `jet` (rainbow).
It has two fatal flaws:

1. **Not perceptually uniform.** Equal steps in data produce unequal steps in perceived
   brightness, creating false features and hiding real ones.
2. **Not greyscale-friendly.** Distant hues in `jet` map to the same grey value, making
   features invisible in greyscale.

### Recommended sequential colormaps

| Colormap | Character | Good for |
|----------|-----------|---------|
| `viridis` | Blue → green → yellow | General purpose, default choice |
| `cividis` | Blue → yellow, CVD-optimised | When CVD accessibility is critical |
| `plasma` | Purple → orange → yellow | High-contrast alternative to viridis |
| `inferno` | Black → red → yellow | Dark backgrounds, signal detection |

All four are perceptually uniform and CVD-safe.

```python
fig, ax = plt.subplots()
sc = ax.scatter(x, y, c=z, cmap="viridis")
plt.colorbar(sc, ax=ax, label=r"$z$")
```

### Recommended diverging colormaps

| Colormap | Character | Good for |
|----------|-----------|---------|
| `RdBu_r` | Red → white → blue | Signed residuals, correlations |
| `coolwarm` | Blue → white → red | Same, with more saturation |
| `seismic` | Same family | Geophysics convention |

For diverging maps, always set `vmin` and `vmax` symmetrically about the midpoint:

```python
import numpy as np
vmax = np.abs(residuals).max()
sc = ax.scatter(x, y, c=residuals, cmap="RdBu_r", vmin=-vmax, vmax=vmax)
```

---

## Combining colour with other channels

Because colour alone is unreliable, always pair it with a redundant encoding:

```python
import matplotlib.pyplot as plt
import numpy as np

E = np.logspace(0, 6, 300)

fig, ax = plt.subplots()
ax.loglog(E, 1e-18 * (E / 1e5) ** -2.7,
          color="C0", linestyle="-",  label="Model A")
ax.loglog(E, 1e-18 * (E / 1e5) ** -2.0,
          color="C1", linestyle="--", label="Model B")
ax.loglog(E, 1e-18 * (E / 1e5) ** -2.4,
          color="C2", linestyle=":",  label="Model C")
ax.legend()
```

Here colour AND line style distinguish the curves — the figure is still readable when
printed in black and white.

For scatter plots, pair colour with marker shape:

```python
ax.scatter(x_a, y_a, c="C0", marker="o", label="Sample A")
ax.scatter(x_b, y_b, c="C1", marker="s", label="Sample B")
ax.scatter(x_c, y_c, c="C2", marker="^", label="Sample C")
```

---

## Testing your figure for accessibility

### Greyscale test

Convert your saved PDF or PNG to greyscale (in Preview on macOS, or any image editor) and
check whether all curves and regions remain distinguishable.
If they do not, add line style or marker differentiation.

### CVD simulation

Several online tools simulate how your figure appears with common colour vision deficiencies:

- [Coblis — Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/) — upload an image, get CVD-simulated previews.
- [Viz Palette](https://projects.susielu.com/viz-palette) — test named palettes interactively.

The ColorBrewer site also labels palettes as "colorblind safe" — filter by this when choosing.

### matplotlib's built-in greyscale preview

A quick in-notebook check:

```python
import matplotlib.pyplot as plt
import matplotlib.cm as cm

fig.savefig("check.png")
# Reload and desaturate
img = plt.imread("check.png")
grey = img @ [0.2126, 0.7152, 0.0722, 0]   # luminance weights
plt.imsave("check_grey.png", grey, cmap="grey")
```

---

## Colour in context: a few more rules

- **Avoid red and green together** for any information-carrying distinction — this is the most
  common CVD combination.
- **Don't use colour to encode the same information as position.**
  If the x-axis already distinguishes the curves, adding colour is redundant and distracting.
- **Use transparency (`alpha`) with care.** Overlapping transparent regions can create new
  colours that were not in your palette and that are hard to predict under CVD.
- **Match your colour choices to the journal.** Some journals have house styles or restrictions
  on colour figures (especially print journals with per-colour-page charges).

---

## Summary

| Do | Don't |
|----|-------|
| Use Dark2 or another CVD-safe palette from ColorBrewer | Use the default matplotlib colour cycle for publications |
| Use `viridis` / `cividis` for continuous data | Use `jet` or `rainbow` |
| Pair colour with line style or marker shape | Rely on colour as the only distinguishing feature |
| Test in greyscale and with a CVD simulator | Assume your monitor is representative |
| Set symmetric `vmin`/`vmax` for diverging maps | Let matplotlib choose limits automatically for residuals |

---

## Resources

- [ColorBrewer 2.0](https://colorbrewer2.org/#type=qualitative&scheme=Set1&n=7) — interactive palette explorer, filtered by CVD-safe and print-safe status.
- [Ciaran O'Hare — HowToMakeAPlot](https://github.com/cajohare/HowToMakeAPlot) — worked examples of palette choice and CVD simulation in matplotlib.
- [matplotlib colormap reference](https://matplotlib.org/stable/gallery/color/colormap_reference.html) — full list of built-in colormaps.
- [Coblis CVD simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/) — upload any figure and preview CVD variants.
- [Viz Palette](https://projects.susielu.com/viz-palette) — design and test named palettes interactively.
- [Scientific colour maps (Crameri)](https://www.fabiocrameri.ch/colourmaps/) — perceptually uniform, CVD-safe maps optimised for scientific data.
