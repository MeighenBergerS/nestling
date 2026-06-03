# Paper Outline Template

Use this template before you write a word of prose.
Filling it in forces you to make the argument explicit. You will find the weak points in the logic
before you have invested days in writing around them.

Work through the sections in order.
The most important field is the one-sentence main result: if you cannot fill that in, you are not ready to write.

---

## Before you start: the one result

**What is the single claim this paper makes, in one sentence with one number?**

> _Example: "We demonstrate that UHECR survival in NGC 1068 excludes σ_χp ≳ 10⁻³³ (m_χ/GeV) cm²,
> three orders of magnitude below current direct-detection limits."_

Your version:

> [fill in]

Every section of this paper exists either to derive this number or to test how robust it is.
If a planned section does neither, remove it.

---

## Abstract (4–5 sentences: fill in each slot)

| Sentence | Role | Draft |
| --- | --- | --- |
| 1 | Setting + motivation: the physical system and why it is interesting | |
| 2 | What we do: method, systems studied, scope. Begin with "We..." | |
| 3 | **Main quantitative result**: a specific number, not "significant improvement" | |
| 4 | Broader implication: what this adds to the field or opens up | |
| 5 (optional) | Second implication or complementarity statement | |

Check: no citations. No section summary. Result sentence contains a number.

---

## Introduction outline

### Paragraph 1: Broad physical setting (3–5 sentences)

Why is this system or environment interesting from first principles?
Which landmark experiments or observations motivate it?
(One citation per result, not clusters of five.)

> [bullet points → prose later]

### Paragraph 2: Specific opportunity and prior work (3–5 sentences)

What is the precise gap this paper fills?
Who has worked on this before, and what did they miss or leave open?

> [bullet points → prose later]

### Paragraph 3: What this paper does (2–4 sentences)

Begin with "In this work, we..." or "In this paper, we show...".
Name the two or three key things computed or proposed.

> [bullet points → prose later]

### Paragraph 4: Paper structure (1–2 sentences, optional)

Only include if the structure is non-obvious.
"In Section II, we... In Section III, we... We conclude in Section IV."

> [fill in or leave blank]

### Figure 1 (introduction sketch)

Figure 1 is a sketch or overview diagram that appears in the introduction.
It is not a data figure. It introduces the setup visually.
Describe what it shows.

> [description: e.g., "Schematic of the physical setup: UHECR path from AGN through DM halo to Earth, with the relevant length scales labelled."]

---

## Order-of-magnitude estimate (for introduction or Section I)

Write the estimate before computing the full result.
If you cannot do this, it is a signal that you do not yet understand which physics controls the answer.

| Step | Content |
| --- | --- |
| Controlling quantity | What one or two quantities dominate the answer? |
| Scaling | Write the result as a product/ratio using ~ |
| Numerical plug-in | One significant figure, with units |
| Expected result | What number do you expect? |

After the full calculation: does the full result agree with this estimate to within an order of magnitude?
If not, identify the physical effect that bridges the gap.

---

## Methods sections

For each Methods section, fill in:

### Section [number]: [title, short noun phrase]

**Purpose** (one sentence): What question does this section answer?

**Key equations or assumptions:**

- [list]

**Scope constraints** (go at the end of the opening paragraph):

- "For simplicity, we assume..."
- "We conservatively require..."

**Figure [N]** (if any):

- What does it show?
- What question does it answer?

---

## Results sections

For each Results subsection, fill in:

### Section [number].[letter]: [title]

**OOM estimate** (opening of the subsection, before the full result):
> [one or two sentences of scaling argument]

**Main result:**
> [the number or bound, with units]

**Figure [N]:**

- What does it show?
- What is the takeaway sentence (goes in `\textit{...}` at the end of the caption)?

**Does this section derive the one main result, or test its robustness?** (tick one)

- [ ] Derives it
- [ ] Tests robustness / sensitivity
- [ ] Other: [explain why it belongs]

---

## Final figure (main constraint or exclusion plot)

This is the most important figure in the paper, the one the reader takes away.

**What does it show?**
> [description]

**What is the one-sentence takeaway for the caption?**
> [fill in]

**Are all axis labels finalised, with units and `\mathrm{}` subscripts?**

- [ ] Yes
- [ ] Not yet

---

## Conclusion outline

### Paragraph 1: Main result (1–2 sentences)

"We have shown/computed/demonstrated [main result]."
Restate the key quantitative finding. No new results.

> [fill in]

### Paragraph 2: Broader implications (≤ 4 sentences)

What does this mean for the field?
Which complementary experiments does it connect to?

> [bullet points → prose later]

### Paragraph 3: Future outlook (3–4 concrete directions)

What are the natural follow-up calculations or measurements?
End on a forward-looking note.

> [bullet points → prose later]

---

## Acknowledgements

"We are grateful for helpful discussions with [names]."

Funding: [grant numbers and agencies]

Closing line (always include verbatim):
> "This work is based on the ideas and calculations of the authors, plus publicly available information."

---

## Reference list (planning stage)

List the key references you already know you will cite.
Use INSPIRE texkeys (`Author:YYYYabc`).
When multiple references are cited together, note the chronological order (oldest first).

| texkey | Paper | Role in argument |
| --- | --- | --- |
| | | |

---

## Checklist before you start writing

- [ ] The one-sentence main result is filled in and contains a specific number.
- [ ] Every planned section either derives that number or tests its robustness.
- [ ] Figure 1 is a sketch, not a data figure.
- [ ] The last named figure is the main constraint plot.
- [ ] The introduction–conclusion contract holds: everything promised in the abstract is discharged in the body.
- [ ] The simplest scenario is presented first in each Results section.
- [ ] No result appears before the method that produces it.
