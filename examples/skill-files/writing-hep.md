# HEP paper writing skill — Meighen-Berger style

Use this skill when drafting or reviewing sections of a high-energy or astroparticle physics
paper. It encodes the conventions taught in the Nestling Writing Papers track (lessons 01–05)
and the SMB style guide (derived from detailed analysis of four representative papers:
arXiv:2512.18093, 2505.09111, 2410.00330, 2311.01667).

Load this skill at the start of a writing or revision session.
You do not need to repeat these rules in individual prompts — they apply to everything
in the session.

---

## How to use this skill

**Drafting mode:**
Give me your bullet-point notes for a section and tell me which section it is
(abstract, introduction paragraph N, results, conclusion).
I will write a draft following these conventions.

**Review mode:**
Paste your draft text and ask me to check for violations.
I will quote each offending passage, name the rule it breaks, and suggest the fix.
I will not paraphrase or silently correct — I will flag every violation explicitly.

---

## 1. Voice and person

- **Always "we"** throughout. Never passive voice for key results.
  - ✅ "We show that..." / "We find σ ≲ 10⁻³³ cm²." / "We compute..."
  - ❌ "It is shown that..." / "A bound of ... is obtained." / "The rate is computed."
- **Lead each paragraph** with the subject and an active verb:
  "We compute...", "We find...", "We demonstrate...", "We propose...", "Figure X shows...", "This approach..."
- **Confidence level:**
  - "we demonstrate" / "we show" — established, fully calculated results
  - "we find" — numerical outputs
  - "in principle" / "could" — speculative possibilities not yet calculated
- **Never start a sentence with:**
  "It is important to note that...", "It should be noted that...",
  "One can see that...", "It is worth mentioning..."
  These add no information. Delete them and start with the actual claim.
- **Never write:** "as will be discussed later" → use "as we discuss below" or
  "Section~\ref{sec:X}".

---

## 2. Abstract

Structure: exactly 4–5 sentences, in this order:

1. **Physical setting + motivation** (1 sentence): establish the system and the opportunity.
   No "In this paper" yet.
2. **What we do** (1–2 sentences): "We..." — name the method, systems studied, scope.
3. **Main quantitative result** (1 sentence): a specific number with units.
   Not "we show significant improvement" — "we find σ ≲ 10⁻³³ cm² at mχ ∼ 1 GeV".
4. **Broader implication** (1 sentence): why it matters; complementarity with other probes.

Rules:

- No citations in the abstract.
- No section-by-section summary.
- Maximum 5 sentences total — if you have 6, merge or cut.

---

## 3. Introduction structure

Exactly four paragraphs:

1. **Broad physical setting** (3–5 sentences): why the system is interesting from first principles.
   Cite landmark experiments concisely. No "In this paper" yet.
2. **Specific gap + prior work** (3–5 sentences): zoom in on the precise gap this paper fills.
   Cite prior work without lengthy review.
3. **What this paper does** (2–4 sentences): begin with "In this work, we..." or
   "In this paper, we show...". Name the two or three key quantities computed.
   Reference Figure 1 here: "Figure 1 illustrates..." or "Figure 1 sketches our approach."
4. **Paper structure** (1–2 sentences, optional): "In Section II, we... We conclude in Section IV."
   Only include if the structure is non-obvious.

---

## 4. Paragraph structure

- **Length:** 3–6 sentences. Hard limit: ≈80 words (8 lines in two-column format).
  Split if longer.
- **Opening sentence:** states the paragraph's main point directly.
  A reader skimming only first sentences should understand the paper's logical skeleton.
- **No orphan sentences:** every sentence connects causally or logically to adjacent sentences.
  Swap test: if any two sentences can be swapped without breaking meaning, the paragraph
  lacks cohesion.
- **No opening citations:** the opening sentence must not contain a `\cite{}`.
  Citations belong in supporting sentences.
- **One idea per paragraph:** if a transition word in the middle introduces an unrelated point, split.
- **Closing sentence:** either concludes the paragraph's claim or creates forward-pointing expectation.

### Standard paragraph forms

**Claim → Evidence → Consequence** (most common in body sections):
Opening states the main point. Middle provides the calculation or prior result.
Closing states the consequence or bridges to the next paragraph.

**Problem → Technique → Scope** (section and subsection openings):
Opening poses the question. Middle names the method. Closing states scope or conservative assumption.

**Result → Refinement → Forward pointer** (multi-subsection derivations):
First sentence states the result just derived. Middle identifies the leading approximation.
Closing points to the next subsection.

---

## 5. Results sections

- **Figure-first:** introduce the figure at the start of the paragraph that interprets it.
  - ✅ "Figure X shows..." / "The results are presented in Figure X."
  - ❌ "As can be seen in Figure X..." (forbidden phrase)
  - ❌ Discussing a figure in a paragraph that does not reference it first.
- **OOM estimate required:** every main results section must contain at least one
  order-of-magnitude estimate paragraph. Begin it with "To build intuition, we note that..."
  or "A simple estimate gives...". Close it with a sentence comparing the estimate to
  the full numerical result.
- **Discuss implications:** do not only describe what the figure looks like.
  State what it means.

---

## 6. Conclusion

Three paragraphs, in this order:

1. "We have computed/shown/demonstrated [main quantitative result]." — one sentence.
   Restate the key number from the results section. Introduce no new results.
2. Broader implications — what this means for the field; complementarity with other experiments.
   ≤ 4 sentences.
3. Future outlook — 3–4 concrete improvements or extensions. End on a forward-looking note.

The conclusion must not introduce any quantitative result not derived in the body.
The numbers must match exactly what appears in the introduction and results sections.

---

## 7. Section titles

- **Short noun phrases**, not sentences: "DM Densities", "Measurement Potential",
  "Conclusions and Outlook".
- **Avoid gerunds at the start:** not "Measuring the Flux" but "Flux Measurement".
- **Final section:** "Conclusion" (singular) or "Conclusions and Outlook".
  Never "Summary and Conclusions".

---

## 8. Figures and captions

### In-text references

- Always "Figure~\ref{fig:name}" — never "Fig.", never `\Cref{}`, never `\autoref{}`.
- Reference pattern: "Figure X shows [what it shows]" — never "Figure X (right panel)"
  unless panels are discussed separately.
- Introduce before interpreting: reference the figure at the start of the paragraph
  that interprets it.

### Captions — three-sentence structure

1. **What it shows** (result-first): "Energy deposited in DUNE as a fraction of
   solar luminosity, as a function of neutrino energy."
2. **What data/model was used**: "Solid (dotted) lines show the full calculation
   (naive estimate). Constraints from [refs] are shown."
3. **Key takeaway** (optional, only if not obvious from sentence 1):
   wrap in `\textit{...}`.

Rules:

- Captions must be **self-contained**: understandable without reading the main text.
- Do not repeat verbatim what the surrounding paragraph says.

---

## 9. Equations

- **Display only essential equations.** Algebraic steps go in appendices.
- **Define every symbol immediately after first appearance:**
  "where $R_\star$ is the stellar radius, $n_i$ is the number density..."
- **In-text reference:** `Eq.~(\ref{eq:label})` — never `\eqref{}` alone,
  never just `(\ref{eq:label})`.
- **Subscripts:** always `\mathrm{}` for non-italic multi-letter subscripts:
  `m_{\mathrm{p}}`, `E_{\mathrm{det}}`, `\frac{\mathrm{d}\Phi}{\mathrm{d}E}`.
- **Never use `\approx` in a displayed equation for rough estimates** — use `\sim` in
  surrounding text.
- Equations end with punctuation (`.` or `,`) matching the surrounding sentence.

---

## 10. Citations

- **Style:** `\cite{key}` rendered as `[N]`. Integrate naturally:
  - ✅ "...as shown in Ref.~[42]" / "...from Refs.~[42, 43]"
  - ❌ "...as has been shown [42]" (too passive)
- **Ordering:** multiple simultaneous citations in chronological order (oldest first).
  Same year → alphabetical by first author.
- **Maximum 3–4 references per claim.** For larger clusters, cite a review.
- **Experiment names:** spell out at first use: "the Xenon One Ton experiment (XENON1T) [ref]".
- **No citations in the abstract.**
- **Bibliography key format:** INSPIRE-style `Author:YYYYabc`. Include arXiv IDs for preprints.

---

## 11. LaTeX conventions

| Object | Correct format | Never |
|--------|---------------|-------|
| Figure ref | `Figure~\ref{fig:name}` | `Fig.`, `\Cref{}`, `\autoref{}` |
| Equation ref | `Eq.~(\ref{eq:name})` | `\eqref{}`, bare `(\ref{})` |
| Section ref | `Section~\ref{sec:name}` | `Sec.`, `\Cref{}` |
| Appendix ref | `Appendix~\ref{app:name}` | `App.` |
| Percent | `10\%` | `10 %` or `10%` (no space or missing backslash) |
| Ranges | `3--10` | `3-10` or `3–10` (typed) |
| Units in text | `100~kton-year`, `$\sim$3~MeV` | missing `~` before units |

**Label prefixes:** `sec:` for sections, `fig:` for figures, `eq:` for equations,
`app:` for appendices, `tab:` for tables.

**Acknowledgements:**

- `\section*{Acknowledgements}` — asterisk, British spelling.
- Standard format: "We are grateful for helpful discussions with [names]."
- Funding statement.
- Mandatory closing sentence: "This work is based on the ideas and calculations
  of the authors, plus publicly available information."

**Remove before submission:** all `\Scomm{}`, `\AGcomm{}`, or other author-note macros.

---

## 12. Order-of-magnitude estimates

Every paper must contain at least one clearly labelled OOM estimate that a reader can
reproduce in under five minutes.

Structure of a well-formed estimate:

1. Identify the controlling physics (name the one or two quantities that dominate).
2. Write the scaling: express the result as a product or ratio using `\sim` freely.
3. Plug in numbers (one significant figure). State the result with matching units.
4. Close with a sentence comparing the estimate to the full numerical result.

Use `\sim` for order-of-magnitude equalities, `\simeq` for ≈10–20% approximations.
Never `\approx` for rough estimates.

---

## 13. Forbidden phrases

| ❌ Never write | ✅ Write instead |
|---|---|
| "As can be seen in Figure X..." | "Figure X shows..." |
| "It is shown that..." | "We show that..." |
| "It is important to note that..." | [state the claim directly] |
| "It should be noted that..." | [state the claim directly] |
| "as will be discussed later" | "as we discuss below" / "Section~\ref{}" |
| "We have tried to..." | "We have..." |
| "In this paper, the authors..." | "In this paper, we..." |
| "it turns out" | "we find" |
| "The authors would like to thank..." | "We are grateful for helpful discussions with..." |
| "Summary and Conclusions" (section title) | "Conclusions and Outlook" |

---

## 14. Paper architecture (whole-paper review)

When reviewing an entire paper, check these structural properties:

- **One main result rule:** the paper has exactly one primary claim statable in one sentence
  with one number. Identify it before reviewing.
- **Introduction–Conclusion contract:** every claim in the introduction is discharged in
  the body. The conclusion restates the main result with the same numbers — no new values.
- **Methods before results:** no result appears before its method is introduced.
- **Simplest case first:** when multiple scenarios exist, present the most general case first.
- **Appendices:** carry derivations, robustness checks, and answers to natural objections —
  never the paper's main results.
- **Figure architecture:**
  - Figure 1 (intro): overview sketch or OOM summary, not a data figure.
  - Each subsequent figure answers exactly one question.
  - Last named figure: the main exclusion/constraint plot.
- **Numerical consistency:** all numbers in the text match the figures. Symbols match
  axis labels.

---

## 15. Submission checklist (run before sending to co-authors)

- [ ] All `\Scomm{}` / `\AGcomm{}` author notes removed.
- [ ] Every symbol defined at first use.
- [ ] Every figure referenced before or at the paragraph that interprets it.
- [ ] All figure captions self-contained (3-sentence structure).
- [ ] "Figure" spelled out (never "Fig.") everywhere.
- [ ] Conclusion opens with "We have shown/computed/demonstrated..."
- [ ] Acknowledgements close with the standard sentence.
- [ ] No citations in the abstract.
- [ ] Introduction contains at least one OOM estimate for the paper's main result.
- [ ] Every OOM estimate closes with a comparison to the full numerical result.
- [ ] All figures saved as PDF from the style file; no PNG in main text.
- [ ] All axis labels use `\mathrm{}` for non-italic subscripts and include units.
- [ ] Build clean: zero undefined-reference warnings.

---

*Skill file version 1.0 — based on Nestling Writing Papers track (lessons 01–05) and
SMB style guide v1.1 (arXiv:2512.18093, 2505.09111, 2410.00330, 2311.01667).*
