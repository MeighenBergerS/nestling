# Lesson 05: Revision Checklist

Writing a paper is an extended, often arduous process.
Expect many drafts, far more than feels reasonable before you have done it.
You will write a version, share it with a co-author, receive substantial feedback, rewrite it,
discover the argument is wrong in one section, rewrite that section, share it again,
incorporate feedback from two people who disagree with each other, and rewrite it again.
This is normal. It is not a sign that the paper is bad or that you are doing it wrong.

Co-authors, especially experienced ones, will catch structural problems you cannot see
because you are too close to the material.
Let them.
Responding to feedback is itself a skill: understanding what the co-author is actually pointing at
(often deeper than the specific sentence they flagged), and deciding what to change and what to defend.

This lesson is not a description of the full writing process.
It is a checklist for the final systematic pass, the one you run on a draft that is already close to done,
before it goes to co-authors for the last round or before submission.
Work through it in order. Check each item before moving to the next.

---

## Before you start revising

Print or open the paper and read it straight through once, as a reader who has not seen it.
Note where you lose the thread, where a claim appears before the method that justifies it,
and where a figure is discussed without first being referenced.
This read-through gives you the structural issues to fix before you apply the item-level checklist.

---

## Structure and argument

- [ ] The paper has exactly one primary claim, statable in one sentence with one number.
- [ ] The introduction promises exactly what the results sections deliver, no more, no less.
- [ ] The conclusion restates the main result with the same numbers as the introduction and results sections.
      No new results appear in the conclusion.
- [ ] Every section mentioned in the introduction ("In Section III, we...") maps to an actual section
      with a matching title and content.
- [ ] Methods sections precede the results they produce. No result appears before its method is introduced.
- [ ] When multiple scenarios are presented, the simplest appears first.
- [ ] Every appendix contains either a long derivation, a robustness check, or a reader objection, not a main result.

---

## Abstract

- [ ] The abstract is four or five sentences. No more.
- [ ] Sentence 3 contains a specific number, not "significant improvement" or "competitive sensitivity".
- [ ] There are no in-text citations in the abstract.
- [ ] The abstract does not summarise sections ("In Section II, we derive...").

---

## Writing

- [ ] Every paragraph opens with a sentence that states the paragraph's main point as a claim.
      A reader skimming only first sentences understands the logical skeleton of the paper.
- [ ] No paragraph begins with "It is important to note that...", "It should be noted that...",
      "One can see that...", or "It is worth mentioning that...".
- [ ] Key results use active, first-person voice: "We show that...", "We find...", "We demonstrate...".
      No passive voice for main results.
- [ ] The conclusion opens with "We have shown/computed/demonstrated [main result]."
- [ ] Section titles are short noun phrases. No gerunds at the start, no full sentences.
      The final section is "Conclusion" or "Conclusions and Outlook", not "Summary and Conclusions".
- [ ] Every Results subsection opens with a scaling argument or OOM estimate before presenting the full calculation.
- [ ] Every OOM estimate closes with a sentence comparing it to the full numerical result.
- [ ] In-line enumeration is used in the main text instead of bulleted lists.

---

## Figures

- [ ] Every figure is referenced in the text before or at the start of the paragraph that interprets it.
- [ ] No figure is introduced with "As can be seen in Figure X...". Only "Figure X shows..."
      or "The results are presented in Figure X."
- [ ] "Figure" is spelled out everywhere, never "Fig.".
- [ ] Every caption is self-contained (three-sentence structure: what it shows, data/model used, key takeaway).
- [ ] The key takeaway sentence in each caption is wrapped in `\textit{...}`.
- [ ] Multi-panel captions use `\textbf{Left panel:}`, `\textbf{Right panel:}` labels.
- [ ] All figures are saved as PDF from the plotting script. No PNG in the main text.
- [ ] Figure filenames are `lowercase_with_underscores.pdf`. Files live in `figures/`.
- [ ] Color assignments are consistent across all figures. The same quantity uses the same color throughout.
- [ ] All axis labels use `\mathrm{}` for non-italic subscripts and include explicit units.
- [ ] Figure 1 is a sketch or overview figure in the introduction, not a data figure.
- [ ] Figures are cited in the order they appear in the source file. Figure 3 is not cited before Figure 2.
- [ ] Every figure is cited at least once in the text.

---

## Equations and notation

- [ ] Every symbol is defined immediately after the equation in which it first appears.
- [ ] Equation references use `Eq.~(\ref{eq:label})`, not `\eqref{}`, not `(1)` alone.
- [ ] Non-italic subscripts use `\mathrm{}`: `m_{\mathrm{p}}`, `\rho_{\mathrm{sp}}`.
- [ ] Upright differentials: `\mathrm{d}` in `\frac{\mathrm{d}\Phi}{\mathrm{d}E}`.
- [ ] `\sim` for order-of-magnitude, `\simeq` for approximate numerical equality in equations.
      `\approx` is not used in displayed equations.
- [ ] Each equation block has a bare `%` comment line immediately above and below it.
- [ ] Equations end with punctuation matching the surrounding sentence.

---

## Citations

- [ ] No citations in the abstract.
- [ ] Opening sentences of paragraphs do not contain citations.
- [ ] No more than 3–4 references per claim. Larger clusters use a review reference.
- [ ] Multiple simultaneous citations are ordered chronologically (oldest first).
- [ ] Experiment names are spelled out on first use, then abbreviated: "the Xenon One Ton experiment (XENON1T) [ref]".
- [ ] BibTeX keys follow the INSPIRE convention (`Author:YYYYabc`). ArXiv IDs are included for preprints.

---

## LaTeX hygiene

- [ ] All `\Scomm{}` and `\AGcomm{}` inline author notes are removed.
- [ ] `\label{}` immediately follows `\caption{}` on the next line for every figure.
- [ ] Cross-references use non-breaking tildes: `Figure~\ref{}`, `Eq.~(\ref{})`, `Section~\ref{}`.
- [ ] `\autoref{}` and `\Cref{}` are not used anywhere.
- [ ] `\clearpage` appears before `\bibliography{}`.
- [ ] `\counterwithin{figure}{section}` appears immediately after `\appendix`.
- [ ] The build runs clean: `latexmk -pdf main.tex` with zero undefined-reference warnings.

---

## LaTeX self-check: strings to grep

Run a find-in-file (Ctrl+F in Overleaf, or `grep` in the terminal) for each of these strings
before every round of co-author sharing.
Each one represents a class of mistake that is easy to introduce and easy to miss by eye.

| Search for | What is wrong | Fix |
| --- | --- | --- |
| `Fig.` | Abbreviated "Figure" | `Figure~\ref{fig:label}` |
| `\eqref{` | Non-standard equation reference | `Eq.~(\ref{eq:label})` |
| `\autoref{`, `\Cref{`, `\cref{` | Forbidden reference macros | Explicit `Figure~\ref{}` / `Eq.~(\ref{})` etc. |
| `\cite` inside `\begin{abstract}` | Citation in abstract | Remove; name the result in words |
| `\begin{figure}[h` or `[H` | Wrong placement specifier | `[t]` for most figures; `[b]` for Figure 1 |
| `\approx` inside `\begin{equation}` | Wrong approximate-equality symbol | `\simeq` |
| `\begin{itemize}` before `\appendix` | Bullet list in main body | Convert to inline `(i)\ldots (ii)\ldots` |
| `It is shown`, `It is demonstrated`, `It is found` | Passive voice for results | "We show", "We demonstrate", "We find" |
| `It is important to note`, `It should be noted` | Filler opener | Delete; start with the claim |
| `As can be seen in Fig` | Forbidden figure introduction | `Figure~\ref{fig:X} shows\ldots` |
| `\ref{` not preceded by `~` | Missing non-breaking space | Add `~` before every `\ref{}` |
| digit`-`digit in text (e.g. `3-10`) | Single-hyphen range | `3--10` |
| `\section{...ing` | Gerund section title | Noun phrase: "Flux Measurement" not "Measuring the Flux" |
| `\bibliography{` without `\clearpage` above | Floats not flushed | Add `\clearpage` immediately before |
| Multi-letter `_{word}` in math (e.g. `_{tot}`) | Unformatted subscript | `_{\mathrm{tot}}` |

### Examples of the less obvious fixes

Missing non-breaking space before `\ref{}`:

```latex
% ❌
as shown in Figure \ref{fig:main}, the rate peaks near 1~GeV.

% ✅
as shown in Figure~\ref{fig:main}, the rate peaks near 1~GeV.
```

Single-hyphen range in text:

```latex
% ❌
We consider energies in the range 1-100~GeV.

% ✅
We consider energies in the range 1--100~GeV.
```

Multi-letter subscript without `\mathrm{}`:

```latex
% ❌
$\phi_{tot}$    $\sigma_{det}$    $E_{kin}$

% ✅
$\phi_{\mathrm{tot}}$    $\sigma_{\mathrm{det}}$    $E_{\mathrm{kin}}$
```

`\approx` inside a displayed equation:

```latex
% ❌
\begin{equation}
    \sigma \approx \frac{G_F^2}{\pi} E_\nu^2.
\end{equation}

% ✅
\begin{equation}
    \sigma \simeq \frac{G_F^2}{\pi} E_\nu^2.
\end{equation}
```

`\eqref{}` instead of explicit reference:

```latex
% ❌
The cross section is given by \eqref{eq:sigma}.

% ✅
The cross section is given by Eq.~(\ref{eq:sigma}).
```

---

## Equation self-check

Beyond the format rules above, run this four-step physical verification on every displayed equation
before the paper goes out. Format mistakes are easy to catch; physics mistakes are expensive to correct
after submission.

### Step 1: Dimensional consistency

Every additive term in an equation must carry the same units.
Check this mentally for every `+` and `−` sign in your displayed equations.

Example from [arXiv:2410.00330](https://inspirehep.net/literature/2836055) (NC argon cross section):

```latex
\sigma_j(E_\nu) = \frac{G_F^2}{\pi}(E_\nu - \omega_j)^2 B_j(GT)
```

Dimension check: `[G_F^2/π]` = GeV⁻⁴, `[(E_ν − ω)²]` = GeV² (same units on both sides of the
subtraction), `B(GT)` dimensionless → result is GeV⁻² (cross section in natural units). ✓

A red flag: energy added to a number density, or a rate added to a cross section, is always wrong.

### Step 2: Prefactors, signs, and exponents

Compare your formula against the textbook or paper form you are following. Check specifically:

- Factors of 2, π, 4π (missing a 4π in a flux integral is a common error)
- Signs of interaction terms (an attractive potential has the opposite sign from a repulsive one)
- Power-law indices: is it $E^2$ or $E^3$? is it $m^{-1}$ or $m^{-2}$?
- Velocity arguments: $v$ vs. $v^2$ vs. relative velocity

If you are using a standard named formula (Gould 1987 stellar capture rate, NFW density profile,
Maxwell-Boltzmann distribution, Rutherford cross section), locate the original paper and compare
your equation against it equation-by-equation.
Note: factors of 2 and sign errors have passed through peer review before and been corrected only in erratum.

### Step 3: Literature match

For any established formula, write next to it the reference and equation number you are following:

```latex
% Gould (1987) Eq. (2.1), corrected for spin-independent coupling
\begin{equation}
    \Omega_c(\sigma) = \frac{\rho_\chi}{m_\chi} \sigma v_\mathrm{esc}^2 \int \ldots
\end{equation}
```

This comment does not go into the submitted paper, but it is invaluable during review.
If a referee asks "where does this formula come from?", you will have the answer in the source.

### Step 4: Notation consistency

Run through every symbol that appears in a displayed equation and ask:

- Is it defined? ("where $R_\star$ is the stellar radius" must appear after its first equation.)
- Does it mean the same thing in Section II as in Section IV?
- Do the axis labels in the figures use the same symbol?

A notation inconsistency between equations and figure axis labels is one of the most common
last-minute errors caught during internal review.

!!! tip "OOM estimate as a sanity check"
    After completing the full calculation, re-derive the OOM estimate from Section I.
    If the two disagree by more than one order of magnitude, either the estimate is missing
    a key physics factor (name it explicitly) or there is a numerical bug.
    This check has caught real errors in calculations that looked correct line by line.

---

## Narrative flow

Beyond individual sentences and paragraphs, the paper must read as a coherent whole.
These three checks are easy to miss when revising section by section.

### Forward pointers between sections

Every section should end with a sentence that tells the reader what comes next.
This is not filler. It is a contract with the reader.

```text
✅  "We now apply this framework to compute the detection prospects at DUNE,
    which we discuss in Section~\ref{sec:results}."

✅  "In the following, we show that this scaling implies a sensitivity
    three orders of magnitude below current direct-detection limits."

❌  "We have derived the interaction cross section."
    [Ends abruptly. Reader does not know what to expect next.]
```

### Back-reference anti-patterns

Never open a section by summarising the previous one:

```text
❌  "In the previous section, we showed that the cross section scales as E^{-2}.
    We now turn to the implications for direct detection."

✅  "The E^{-2} energy scaling has a direct implication for detector thresholds:
    lower-threshold detectors gain disproportionately."
```

The reader has just finished the previous section.
Recapping it wastes a sentence and makes the opening sentence weak. It cannot carry the paragraph.

### Figure citation order

Figures must be cited in the same order they appear in the source file.
Search the text for all `Figure~\ref{fig:...}` references and confirm that Figure 2 is first cited
before Figure 3, and so on.

Also check: is every figure referenced at least once in the text?
A figure never mentioned in the text either belongs in an appendix or does not belong in the paper.

---

## Acknowledgements

- [ ] Acknowledgements open with: "We are grateful for helpful discussions with [names]."
- [ ] Funding statement follows the discussion acknowledgement.
- [ ] The section closes with: "This work is based on the ideas and calculations of the authors,
      plus publicly available information."

---

## The automated pipeline

The [SMB_style_guidelines](https://github.com/MeighenBergerS/SMB_style_guidelines) repository
contains an automated pipeline that runs all of the above checks, and more, directly on a `.tex` file.

| Stage | What it checks | LLM? |
| --- | --- | --- |
| Mechanical (Stage 1a) | All 15 grep rules above, via regex | No |
| Style (Stage 1b) | Voice, abstract form, OOM presence per section | Fast |
| Estimate (Stage 3) | Re-derives your OOM estimates independently; flags >1 OOM disagreement | Fast |
| Equations (Stage 3b) | Dimensional consistency, prefactors, signs, literature match | Smart |
| Flow (Stage 3c) | Figure citation order + full narrative structure analysis | Smart |
| Review (Stage 4) | Full PRD-style structured referee report | Smart |

The mechanical stage runs with no API key and produces results immediately. It is worth running
even on an early draft to catch the trivial violations before focusing on the harder ones.
Once a draft is close to submission-ready, the full pipeline gives a structured list of remaining issues.

---

## Final check

Once the checklist is clear, compile the paper one more time from scratch and read the abstract,
the first sentence of every paragraph, and the conclusion in sequence.
That reading should tell a coherent story without any of the intervening text.
If it does not, the structure needs another pass.

---

## Worked example: spotting violations

Below are six passages, each containing one or more violations.
Identify the violation(s) before reading the analysis.

---

### Passage A

> "It is worth noting that the atmospheric neutrino flux plays a key role in our analysis [12, 4, 37].
> This flux has been measured by Super-Kamiokande [ref]. As can be seen in Fig. 3, the predicted
> event rate peaks near 1~GeV. The calculation is described in the following section."

Three violations:

1. **Forbidden opener**: "It is worth noting that..." adds no information. Rewrite the opening sentence
   as a claim: "The atmospheric neutrino flux is the primary signal in our analysis."
2. **Citation in the opening sentence**: `[12, 4, 37]` belongs in a supporting sentence, not the claim.
   Three simultaneous citations are fine only if all three are needed for this specific point;
   for a general literature cluster, use a review.
3. **"As can be seen in Fig. 3"**: two violations in one phrase: forbidden figure introduction and
   abbreviated "Fig.". Rewrite as: "Figure~\ref{fig:rates} shows the predicted event rate..."

---

### Passage B

> "Measuring the Cosmic-Ray Spectrum with Atmospheric Neutrinos"

This is a section title.

One violation:

1. **Gerund section title**: "Measuring" is a gerund. Use a noun phrase:
   "Cosmic-Ray Spectrum Measurement" or "CR Spectrum Sensitivity".

---

### Passage C: from a LaTeX source

```latex
The result is given by \eqref{eq:sigma}, where $G_F$ is the Fermi coupling constant.
```

One violation:

1. **`\eqref{}` instead of `Eq.~(\ref{})`**: replace with:

   ```latex
   The result is given by Eq.~(\ref{eq:sigma}), where $G_F$ is the Fermi coupling constant.
   ```

---

### Passage D: from a LaTeX source

```latex
\begin{equation}
    \sigma \approx \frac{G_F^2}{\pi} (E_\nu - \omega_j)^2.
\end{equation}
```

One violation:

1. **`\approx` in a displayed equation**: use `\simeq` for approximate numerical equalities.
   `\approx` is reserved for numerical approximations outside the equation environment.

   ```latex
   \begin{equation}
       \sigma \simeq \frac{G_F^2}{\pi} (E_\nu - \omega_j)^2.
   \end{equation}
   ```

---

### Passage E

> "In this section, we turn to the results. In the previous section, we derived the cross section
> scaling. We find that the sensitivity reaches $\sigma_{\chi p} \lesssim 10^{-33}$~cm² at
> $m_\chi \sim 1$~GeV, as can be seen from Figure 4. We also note that this is several
> orders of magnitude below current limits."

Four violations:

1. **Setup opening sentence**: "In this section, we turn to the results" is filler.
   Replace with the main claim: "The DM–nucleon cross section is constrained to
   $\sigma_{\chi p} \lesssim 10^{-33}$~cm² at $m_\chi \sim 1$~GeV."
2. **Back-reference recap**: "In the previous section, we derived the cross section scaling"
   recaps what the reader just read. Delete it.
3. **"as can be seen from Figure 4"**: use "Figure~\ref{fig:constraint} shows..."
   and introduce the figure before interpreting it.
4. **"We also note that..."**: "note" is a weak hedge. State the result directly:
   "This bound lies three orders of magnitude below current direct-detection limits at this mass."

Corrected version:

> "The DM–nucleon cross section is constrained to $\sigma_{\chi p} \lesssim 10^{-33}$~cm²
> at $m_\chi \sim 1$~GeV. Figure~\ref{fig:constraint} shows the full exclusion curve as a function
> of DM mass. This bound lies three orders of magnitude below current direct-detection limits,
> as we discuss in Section~\ref{sec:conclusion}."

---

### Passage F: equation with a notation problem

> "The capture rate is
>
> $\Omega_c = A \cdot \rho \cdot \sigma \cdot v$
>
> where $A$ is a numerical factor and $\sigma$ is the cross section.
> The total event rate in Figure 5 is then $\mathcal{R} = N_T \cdot \sigma \cdot t$,
> where $\sigma$ is the detection cross section."

One violation:

1. **Symbol reuse**: `\sigma` is used for two different quantities in the same passage:
   the DM–nucleon cross section in the capture rate equation, and the detection cross section
   in the event rate expression. Introduce a new symbol for one of them,
   e.g. `\sigma_{\mathrm{det}}` for the detection cross section, and redefine it explicitly
   at first use: "where $\sigma_{\mathrm{det}}$ is the neutrino detection cross section."
