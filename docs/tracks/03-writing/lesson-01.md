# Lesson 01 — Paper Structure

A physics paper is not a lab notebook or a chronological account of what you tried.
It is a logical argument: a single central claim, supported by a chain of derivations and figures,
presented in a fixed order that readers expect and rely on.
This lesson explains that structure and why every part of it exists.

---

## The three-act arc

Every HEP paper follows the same narrative arc, regardless of how many sections it has.

**Act I — Motivation (Introduction)**
Establish the physical system as interesting. Identify the specific gap or opportunity this paper addresses.
State the one central question. Show Figure 1 as a visual summary of the answer.
The reader should finish the introduction knowing exactly what the paper does and roughly what the answer is.

**Act II — Derivation (Methods and Results)**
Answer the central question in logically ordered steps.
Each section builds directly on the previous one.
The section sequence you promised in the introduction maps one-to-one to the actual sections.
Never present a result before introducing the method used to derive it.

**Act III — Implications (Conclusion)**
Restate the quantitative result. Explain what it means for the field.
Note what was assumed. Point to future work.
The conclusion makes no claims that are not already established in Act II.

!!! note "The introduction–conclusion contract"
    Every claim in your introduction must be discharged — proved or calculated — before the conclusion.
    The conclusion restates the main result with the same numbers you already gave.
    If the conclusion introduces a new result, that result belongs in a Results section.

---

## The one main result rule

A well-formed HEP paper has exactly one primary claim, statable in a single sentence with a single number.
For example: "We demonstrate that Hyper-K can reduce the cosmic-ray flux uncertainty from ~20% to ~7%,
improving the sin²θ₂₃ measurement by 50--73%."

Secondary results are clearly subordinate: they support the main result, assess its robustness,
or explore a natural extension — but they are never presented as co-equal claims.

Before you write a word, identify your one number. Every section exists either to derive it
or to assess how robust it is. If a section does neither, it probably does not belong in the paper.

The three reference papers for this track each have a single primary claim:

| Paper | Main result in one sentence |
| --- | --- |
| [arXiv:2512.18093](https://inspirehep.net/literature/3094737) | σ_χp ≲ 10⁻³³ (m_χ/GeV) cm² from UHECR survival near NGC 1068 |
| [arXiv:2410.00330](https://inspirehep.net/literature/2836055) | DUNE measures the total active ⁸B solar neutrino flux via NC argon interactions |
| [arXiv:2605.16721](https://inspirehep.net/literature/3157184) | Atmospheric neutrinos at next-generation detectors can constrain the CP-violating phase δ_CP |

---

## What each section must do

### Introduction

The introduction has a fixed four-paragraph structure:

1. **Broad physical setting** (3–5 sentences): Why is this system or environment interesting?
   Reference landmark experiments concisely — one citation per result, not clusters of five.
2. **Specific opportunity and prior work** (3–5 sentences): Zoom in on the precise gap this paper fills.
   Cite prior work without summarising it at length.
3. **What this paper does** (2–4 sentences): Begin explicitly with "In this work, we..." or
   "In this paper, we show...". Name the two or three key things computed or proposed.
4. **Paper structure** (1–2 sentences, optional): "In Section II, we... We conclude in Section IV."
   Only include this if the structure is non-obvious.

Figure 1 — a sketch or overview diagram — belongs in the introduction and must be referenced explicitly
in the text: "Figure 1 illustrates our approach." Never let a figure float past the introduction
without a sentence pointing to it.

### Methods and Results sections

Open each section with one or two sentences stating what this section does and why.
Do not repeat motivation already given in the introduction — a brief back-reference ("As noted above,...")
is sufficient if needed at all.

Present figures before interpreting them. The standard pattern is: "Figure X shows [what]."
Then the paragraph interpreting the figure follows immediately.
Never write "As can be seen in Figure X" — see [Lesson 03](lesson-03.md) for the full list.

When there are multiple scenarios (NFW vs. spike, Milky Way vs. NGC 1068),
present the simplest or most general case first, then the more elaborate one.

### Conclusion

The conclusion has three paragraphs:

1. **Main result**: "We have shown/computed/demonstrated [main result]." Restate the key quantitative
   finding in one sentence. No new results here.
2. **Broader implications**: What this means for the field, and how it complements other experiments.
   Four sentences at most.
3. **Future outlook**: Three or four concrete improvements or extensions.
   End on a forward-looking note without excessive hedging.

### Appendices

An appendix exists for one of three reasons:
(1) a derivation too long for the main text,
(2) a robustness or sensitivity check,
(3) the answer to a natural reader objection.

Appendices never contain the paper's main results.
The main text should state only the conclusion of appendix material, with a pointer:
"...as we show in Appendix A, the star can be treated as optically thin for all cross sections considered."

---

## Figure architecture

How you assign figures to questions is as important as what each figure shows.

- **Figure 1** (Introduction): An overview sketch or order-of-magnitude summary. Not a data figure.
  It introduces the setup visually before any derivation.
- **Figures 2–N** (Methods and Results): Each figure answers exactly one question.
  Never combine two unrelated results in a single multi-panel figure unless the comparison between them is the point.
- **Last named figure** (Results or Conclusion): The main constraint or exclusion plot.
  This is the image the reader takes away. It should be the clearest and most polished figure in the paper.
- **Appendix figures**: Numbered separately (A1, B1, etc.). The main text refers to them,
  but never as primary evidence.

---

## Scope and depth

The reference papers in HEP are topically narrow and technically deep.
They do not survey the field or address every possible scenario.
A useful rule of thumb for page allocation:

| Part | Fraction of pages |
|---|---|
| Core derivation and main result figure | ~60% |
| Introduction and Conclusion | ~20% |
| Appendices | ~20% |

Resist the urge to expand the paper by adding tangential scenarios.
Instead, add depth by stating your assumptions more precisely, quantifying systematic uncertainties,
or connecting your result to one complementary existing bound.

!!! tip "Simplest case first"
    When you have multiple scenarios to show, always start with the simplest one.
    The reader needs to understand the baseline before they can appreciate the comparison.

---

## Sequencing rules

A few hard rules that are easy to violate in a first draft:

- **Methods before Results.** Never quote a result before introducing the method that produces it.
- **Simplest case first.** When scenarios differ in complexity, present the simpler one first.
- **Section titles map to the introduction outline.** If you promised "In Section III, we compute the
  sensitivity", Section III must be titled something like "Sensitivity" and must do exactly that.
- **Forward references must resolve.** If you write "as we will show in Section V", Section V must
  contain that result.

---

## What to read next

[Lesson 02](lesson-02.md) covers the abstract — the most-read part of any paper and the part
most authors write last and least carefully.
[Lesson 03](lesson-03.md) covers sentence- and paragraph-level writing conventions.
