# Lesson 04 — LaTeX Basics

HEP papers are written in LaTeX, specifically using the RevTeX 4-2 document class for APS journals.
This lesson covers the conventions that apply throughout: document setup, figures, equations,
cross-references, and citations.
The goal is not to teach LaTeX from scratch, but to establish the specific patterns used in this subfield
so you do not have to rediscover them from journal guidelines or by copying someone else's preamble.

---

## Where to write: Overleaf

The standard collaborative tool in HEP is [Overleaf](https://www.overleaf.com/project).
Overleaf is a browser-based LaTeX editor that compiles in the cloud, tracks history, and lets multiple
authors edit simultaneously — it removes the need to install a local LaTeX distribution or manage
a shared repository for the source files.

When starting a new paper, create a new project on Overleaf and share it with your collaborators.
This is how most papers in this subfield are written in practice.

!!! tip "Version history"
    Overleaf keeps a full version history. Before a major revision or before sending to collaborators,
    label the current version with a tag ("before referee round 1", "submitted to PRD") so you can
    recover it cleanly if needed.

---

## Document class and essential packages

```latex
\documentclass[aps,prd,twocolumn,superscriptaddress,bibnotes,longbibliography,
               preprintnumbers,floatfix,10pt]{revtex4-2}

\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{amsmath,amsfonts,amsthm,amssymb}
\usepackage[colorlinks]{hyperref}
\usepackage{mathtools}
\usepackage{bm}
\usepackage{multirow}
```

Set all hyperlinks to violet — this is the standard in these papers:

```latex
\hypersetup{
    pdfnewwindow=true,
    colorlinks=true,
    linkcolor=violet,
    citecolor=violet,
    filecolor=violet,
    urlcolor=violet
}
```

Set the figure path once in the preamble:

```latex
\graphicspath{{./figures/}}
```

All `\newcommand` definitions go at the top of the preamble, before `\begin{document}`.
Remove any `\Scomm{}` or `\AGcomm{}` author-note macros from any submitted draft.

---

## Figures

### Single-column figure

```latex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/filename.pdf}
\caption{Caption text here. \textit{Key takeaway in italics.}}
\label{fig:descriptive_name}
\end{figure}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```

### Two-column-wide figure

```latex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/filename.pdf}
\caption{...}
\label{fig:descriptive_name}
\end{figure*}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```

**Rules:**

- `\centering` always appears before `\includegraphics`. Never use `{\centering ...}` or `\begin{center}`.
- `\label{}` always immediately follows `\caption{}` on the next line.
- Width is `\columnwidth` (single-column) or `\textwidth` (two-column). Never `[width=...]` without specifying the fraction.
- The final takeaway sentence of a caption is wrapped in `\textit{...}`.
- Multi-panel captions label panels with `\textbf{Left panel:}`, `\textbf{Right panel:}`, etc.
- Placement: the first figure in the paper uses `[b]`; all others use `[t]`. Never `[h]` or `[H]`.
- Figure filenames are `lowercase_with_underscores.pdf` — no uppercase, no spaces.

### Caption structure

Each caption has a three-sentence structure:

1. **What it shows** (result-first): "Energy deposited in S4714 as a fraction of stellar luminosity, as a function of DM mass."
2. **What data or model was used**: "Solid (dotted) lines show the full Gould formalism (naive estimate). Experimental constraints from [refs] are included."
3. **Key takeaway** (optional): "The spiked profile yields the largest predicted deposition, reaching O(L★) well below current sensitivity." — in `\textit{...}`.

Captions must be self-contained. A reader should understand what the figure shows without reading the main text.
Do not repeat verbatim what the surrounding paragraph says.

---

## Equations

### Single equation

```latex
%
\begin{equation}
    \sigma_j(E_\nu) = \frac{G_F^2}{\pi}(E_\nu - \omega_j)^2 B_j(GT).
    \label{eq:descriptive_name}
\end{equation}
%
```

### Aligned equations

```latex
%
\begin{eqnarray}
    \mathcal{R}^\mathrm{CC} & \propto & \phi_{\nu_e} \label{eq:CC} \\
    \mathcal{R}^\mathrm{ES} & \propto & \phi_{\nu_e} + \tfrac{1}{6}(\phi_{\nu_\mu} + \phi_{\nu_\tau}), \label{eq:ES}
\end{eqnarray}
%
```

**Rules:**

- A bare `%` comment line appears immediately above and below every equation block.
- Four-space indentation inside equation environments.
- Equations end with punctuation (`.` or `,`) matching the surrounding sentence.
- Equation labels: `eq:descriptive_name` — lowercase, underscores only.

---

## Math notation

**Upright text in subscripts** — always `\mathrm{}` for multi-letter labels:

| ✅ Write this | ❌ Not this |
| --- | --- |
| `\mathcal{R}^\mathrm{CC}` | `\mathcal{R}^{CC}` |
| `\phi_\mathrm{tot}` | `\phi_{tot}` |
| `\frac{\mathrm{d}\Phi}{\mathrm{d}E}` | `\frac{d\Phi}{dE}` |

**Approximate equalities:**

| Symbol | When to use |
| --- | --- |
| `$\sim$` | Order-of-magnitude equalities: "σ ~ 10⁻³³ cm²" |
| `$\simeq$` | Approximate numerical equality in equations (within 10–20%) |
| `$\approx$` | Reserved for numerical approximations — do **not** use for rough estimates |

**Calligraphic letters**: `\mathcal{R}` for rates, `\mathcal{N}` for counts.

---

## Cross-references in text

This is one of the most common sources of inconsistency in drafts. Follow these patterns exactly:

| Object | Correct format | LaTeX |
| --- | --- | --- |
| Figure | `Figure~\ref{fig:name}` | Always "Figure", never "Fig." |
| Equation | `Eq.~(\ref{eq:name})` | "Eq." with tilde and explicit parentheses |
| Section | `Section~\ref{sec:name}` | Spelled out |
| Appendix | `Appendix~\ref{app:name}` | Spelled out |

**Do not use** `\eqref{}` — use `Eq.~(\ref{})` explicitly.
**Do not use** `\autoref{}` or `\Cref{}`.

The non-breaking tilde `~` between the word and `\ref{}` is required in every case.

| ✅ Write this | ❌ Not this |
| --- | --- |
| `Figure~\ref{fig:dm_density}` | `Fig.~\ref{fig:dm_density}` |
| `Eq.~(\ref{eq:gould})` | `\eqref{eq:gould}` |
| `Section~\ref{sec:results}` | `Sec.~\ref{sec:results}` |

---

## Label naming conventions

Use these prefixes consistently:

| Type | Prefix | Example |
| --- | --- | --- |
| Section | `sec:` | `\label{sec:results}` |
| Appendix | `app:` | `\label{app:systematics}` |
| Figure | `fig:` | `\label{fig:dm_density}` |
| Equation | `eq:` | `\label{eq:gould}` |
| Table | `tab:` | `\label{tab:stellar_params}` |

---

## Citations

**Citation style:**

| ✅ Write this | ❌ Not this |
| --- | --- |
| "...as shown in Ref. [42]" | "...as has been shown [42]" (too passive) |
| "...from Refs. [42, 43]" | "...previously [42, 43, 44, 45, 46]" (too many at once) |

Maximum 3–4 references per claim. For large literature clusters, use a review reference.

**Citation ordering**: When citing multiple references simultaneously, order them chronologically
by publication or submission year (oldest first). Within the same year, sort alphabetically by first author surname.

```latex
% Correct: oldest → newest
\cite{Author1995abc, Author2003xyz, Author2017def, Author2022ghi}
```

**Do not cite in the abstract.**

Spell out experiment names on first use:
"the Xenon One Ton experiment (XENON1T) [ref]" — then use "XENON1T" throughout.

**BibTeX keys**: Use INSPIRE-style keys (`Author:YYYYabc`). Include arXiv IDs for preprints.

---

## Text formatting details

- **En-dash for ranges**: `3--10` not `3-10`.
- **Non-breaking space before units**: `100~kton-year`, `1.5~km`, `$\sim$3~MeV`.
- **Percent**: `10\%` with no space before `\%`.
- **Acknowledgements**: `\section*{Acknowledgements}` — asterisk (unnumbered), British spelling.

---

## Section separators in source files

Major sections (Introduction, Results, Conclusions, Appendices) are separated by double comment-line blocks:

```latex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Section Title}
```

Figure environments are wrapped in shorter single-line comment blocks:

```latex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{figure}[t]
...
\end{figure}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```

---

## Appendix block

```latex
\appendix
\counterwithin{figure}{section}
\vspace{0.75cm}
\centerline{\Large {\bf Appendices}}
\vspace{0.75cm}

Here, we provide additional details...

\section{Appendix Title}
\label{app:name}
```

`\counterwithin{figure}{section}` must appear immediately after `\appendix` to produce "Figure A1", "Figure B1" labels.
Each appendix is a full `\section{}`, not a `\subsection{}`.

---

## Bibliography

```latex
\clearpage
\bibliography{bibliography}
```

`\clearpage` before `\bibliography` flushes all pending floats.
The `longbibliography` class option is already set — do not override it.

---

## What to read next

[Lesson 05](lesson-05.md) is the revision checklist — a systematic pass through everything covered
in this track, designed to be run on a full draft before submission.
