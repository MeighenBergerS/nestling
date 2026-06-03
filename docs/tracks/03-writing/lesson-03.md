# Lesson 03: Writing Conventions

Physics writing has a dialect.
It is not literary prose, and it is not the informal style of a lab notebook.
It is precise, first-person, active, and built around a logical skeleton that the reader can skim.
This lesson covers the conventions that govern every sentence and paragraph in a HEP paper.

---

## Voice and person

Always use first-person plural "we" throughout the paper.
Never use passive voice for key results.

| ✅ Write this | ❌ Not this |
| --- | --- |
| "We show that S4714 is sensitive to..." | "It is shown that S4714 is sensitive to..." |
| "We compute the total event rate." | "The total event rate is computed." |
| "We find σχp ≲ 10⁻³³ cm²." | "A bound of σχp ≲ 10⁻³³ cm² is obtained." |

Lead the first sentence of each paragraph with the subject and an active verb:
"We compute...", "We find...", "We demonstrate...", "We propose...", "Figure X shows...", "This approach..."

**State conclusions at the right confidence level.**
Use "we demonstrate" or "we show" for established results.
Use "we find" for numerical outputs.
Use "in principle" and "could" for genuine possibilities that have not been calculated.

**Never start a sentence with:**

- "It is important to note that..."
- "It should be noted that..."
- "One can see that..."
- "It is worth mentioning that..."

These phrases add words without adding information. Cut them and start with the actual claim.

---

## Paragraph structure

Each paragraph has three parts: an opening sentence that states the main point,
middle sentences that support it, and a closing sentence that concludes or bridges forward.

**Length**: 3–6 sentences. Hard limit: 8 lines in two-column format.

**The opening sentence is a claim, not a setup.**
A reader skimming only the first sentence of every paragraph should understand the logical skeleton of the paper.

| ✅ Write this | ❌ Not this |
| --- | --- |
| "Atmospheric neutrinos constitute a critical signal." | "In this section, we discuss the atmospheric neutrino flux." |
| "The interaction length constraint follows immediately from the AGN size." | "We now turn to the interaction length." |
| "The UHECR survival requirement sets a direct bound on the DM–nucleon cross section." | "Having established the physical setup, we now consider the constraint." |
| "Figure~\ref{fig:main} shows that the bound scales linearly with DM mass." | "We now present the main result of this paper." |

**No orphan sentences.** Every sentence must connect causally or logically to the adjacent one.
Test: could you swap any two sentences without breaking meaning? If yes, the paragraph lacks cohesion.

**Transitions are load-bearing.** Use them precisely:

| Purpose | Words to use |
| --- | --- |
| Contrast | "however", "on the other hand", "while", "by contrast" |
| Elaboration | "specifically", "in particular", "for example" |
| Consequence | "therefore", "as a result", "this implies" |
| Addition | "additionally", "furthermore" (use sparingly) |
| Sequential | "first...then", "subsequently", "finally" |

Avoid "Firstly,... Secondly,... Thirdly,...". Use causal or contrast flow instead.

**The opening sentence must not contain a citation.**
Citations belong in supporting sentences, not in claims.

| ✅ Write this | ❌ Not this |
| --- | --- |
| "The UHECR spectrum cuts off sharply above 50 EeV. This behaviour was first measured by [ref]." | "The UHECR spectrum [ref] cuts off sharply above 50 EeV." |
| "Solar neutrino detection at DUNE can proceed via neutral-current interactions on argon. This channel was proposed in Refs. [ref1, ref2]." | "Solar neutrino detection [ref1, ref2] can proceed via neutral-current interactions on argon." |

---

## Standard paragraph forms

Three patterns cover most paragraphs in a HEP paper.

**Claim → Evidence → Consequence** (most common in body sections)

> Opening sentence states the main point directly. Middle sentences provide the supporting
> calculation, observation, or prior result. The closing sentence states the consequence
> or bridges forward to the next paragraph.

Example (from [arXiv:2605.16721](https://inspirehep.net/literature/3157184), adapted):
> "Atmospheric neutrinos constitute a critical signal for measuring the CP-violating phase.
> A precise understanding of the low-energy atmospheric neutrino flux is crucial for multiple physics goals:
> probing neutrino oscillations, mass ordering, and flavor ratios, and it acts as a background in the
> search for the DSNB, proton decay, and indirect dark matter searches.
> We demonstrate in Section III that the subdominant flux uncertainty is the limiting systematic at
> next-generation detectors."

**Problem → Technique → Scope** (used at section and subsection openings)

> Opening sentence poses the question this section answers. Middle sentence names the method
> or criterion used. Closing sentence states the scope constraint or conservative assumption.

Example (from [arXiv:2512.18093](https://inspirehep.net/literature/3094737)):
> "Assuming that UHECRs near the GZK cut-off (E_CR ~ 50 EeV) are all accelerated within AGNs,
> we can set a basic requirement on the interaction length for CR–DM interactions. The interaction
> length λ_CR,χ needs to be larger than the acceleration distance l_acc of the CR.
> Conservatively, we can set l_acc to the size of the AGN."

**Result → Refinement → Forward pointer** (used in multi-subsection derivations)

> First sentence states the result just derived. Middle sentence identifies the leading approximation
> that can be improved. Closing sentence points to the next subsection.

Example (from [arXiv:2512.18093](https://inspirehep.net/literature/3094737)):
> "We can refine the estimate in Equation 6 by observing that if a particle escapes its
> acceleration region, it no longer accumulates energy."

---

## Section titles

Section titles are short noun phrases, not full sentences, not questions, and not gerunds.

| ✅ Write this | ❌ Not this |
| --- | --- |
| "Flux Measurement" | "Measuring the Flux" |
| "DM Densities" | "The Dark Matter Density Profile" |
| "Conclusions and Outlook" | "Summary and Conclusions" |
| "Measurement Potential" | "The Measurement Potential of Hyper-K" |

The final section is always "Conclusion" (singular) or "Conclusions and Outlook".
Never "Summary and Conclusions".

---

## Order-of-magnitude estimates

Every paper should contain at least one clearly signposted order-of-magnitude (OOM) estimate,
an argument a reader can reproduce with pencil and paper in under five minutes.
Its role is to build intuition for *why* the answer comes out the way it does, not to replace the full calculation.

**Where to place it:**

- In the introduction or at the end of Section 1, for the paper's main result.
- At the opening of each Results subsection, as a scaling argument before the full calculation.
- After a surprising result, to explain which physical effect bridges the gap from naive expectation.

Set it off explicitly: "To build intuition, we note that..." or "A simple estimate gives..."

**Structure of a well-formed estimate:**

1. Name the one or two quantities that dominate the answer.
2. Write the scaling: a product or ratio of those quantities, using ~ freely.
3. Plug in numbers and state the result (one significant figure).

Example (from arXiv:2512.18093):
> "Assuming that UHECRs near the GZK cut-off (E_CR ~ 50 EeV) are accelerated inside AGN,
> a basic constraint on the DM–nucleon cross section follows immediately. The CR mean free path
> must exceed the AGN size, l_acc ~ 10¹⁶ cm, giving λ_CR,χ = (nχ σχp)⁻¹ ≳ l_acc.
> With the local DM density ρχ ~ 10⁻²⁴ g cm⁻³ and mχ ~ 1 GeV, this requires
> σχp ≲ 10⁻³⁰ cm², already three orders of magnitude below existing direct-detection limits."

Always close the estimate paragraph with a sentence comparing it to the full result:

| ✅ Write this | ❌ Not this |
| --- | --- |
| "The full calculation (Section III) gives σ ≃ 2.3 × 10⁻³³ cm², consistent with this estimate." | (Present only the full result with no estimate to orient the reader.) |
| "The full result is a factor of ~3 larger because of the spike profile, discussed in Section IV." | |

**Notation for estimates:** Use ~ for order-of-magnitude equalities, ≃ for approximate numerical equality
(within 10–20%). Do not use ≈ for rough estimates. Reserve it for numerical approximations in equations.

### Before and after: a poorly-written versus a well-formed estimate

**❌ Poor version**: no controlling quantities named, no algebra shown, no comparison to the full result:

> "The DM–nucleon cross section is constrained to be small. The mean free path of a UHECR must be
> large enough for it to escape the AGN. This gives a rough bound on the cross section."

This paragraph says nothing a reader could reproduce. It has no numbers, no scaling, and no link to
the full result. A reader cannot check it and gains no physical intuition from it.

**✅ Well-formed version** (from [arXiv:2512.18093](https://inspirehep.net/literature/3094737)):

> "To build intuition, we note that the UHECR mean free path must exceed the AGN acceleration
> region, $l_\mathrm{acc} \sim 10^{16}$~cm. The interaction length is
> $\lambda_{\mathrm{CR},\chi} = (n_\chi \sigma_{\chi p})^{-1}$, where
> $n_\chi = \rho_\chi / m_\chi \sim 10^{-3}$~cm$^{-3}$ for a local DM density
> $\rho_\chi \sim 10^{-24}$~g~cm$^{-3}$ and $m_\chi \sim 1$~GeV.
> The requirement $\lambda_{\mathrm{CR},\chi} \gtrsim l_\mathrm{acc}$ then gives
> $\sigma_{\chi p} \lesssim 10^{-30}$~cm², already three orders of magnitude below
> current direct-detection limits. The full numerical result in Section~\ref{sec:results}
> tightens this to $\sigma_{\chi p} \lesssim 10^{-33}$~cm² once the spike profile is included."

Three steps visible: (1) controlling quantity named ($l_\mathrm{acc}$), (2) scaling written out with
numbers, (3) estimate compared to the full result. A reader can reproduce this in two minutes.

---

## Figures in text

Always introduce a figure before or at the start of the paragraph that interprets it.

| ✅ Write this | ❌ Not this |
| --- | --- |
| "Figure 3 shows the predicted event rate as a function of energy." | "As can be seen in Figure 3, the event rate..." |
| "The results are presented in Figure 3." | "The event rate (Figure 3) is..." (when Figure 3 hasn't been referenced yet) |

Always spell out "Figure", never "Fig.". See [Lesson 04](lesson-04.md) for the LaTeX conventions.

---

## Lists

In the main text, use in-line enumeration rather than bullet points:
"We compute (i) the total energy exchange, (ii) the orbital modulation, and (iii) the sensitivity to the spike profile."

Bulleted lists (`itemize`) belong in appendices or for genuinely unordered parallel items such as a list of assumptions.
Numbered lists (`enumerate`) are appropriate only when sequence or hierarchy matters, and should contain 3–5 items at most.
If you find yourself using bullet points in a Results section, convert them to prose.

---

## Common phrases: use and avoid

The left column is the standard phrasing in this group's papers.
The right column is the version that will be flagged in review, sometimes by a co-author,
sometimes by a referee, and sometimes by an automated checker.

| ✅ Use | ❌ Avoid | Why |
| --- | --- | --- |
| "We show that..." | "It is shown that..." | Passive hides agency; "we" is shorter and clearer |
| "Figure~\ref{fig:X} shows..." | "As can be seen in Figure~\ref{fig:X}..." | The figure does the showing; the reader does not need to be told they can see it |
| "We have computed..." (conclusion) | "We have tried to compute..." | "Tried" implies failure; state what was done |
| "In this work, we..." | "In this paper, the authors..." | You are one of the authors; use "we" |
| "as we discuss below" | "as will be discussed later" | Forward reference should be specific and active |
| "We are grateful for helpful discussions with..." | "The authors would like to thank..." | Direct and in first person; "would like to" is hedged |
| "we find" (numerical output) | "it turns out that" | "It turns out" is conversational and implies surprise; "we find" is the standard result verb |
| "we adopt" (model or parameter choice) | "we assume without loss of generality" | WLOG is almost never literally true in a phenomenology paper |
| "in principle" | "theoretically speaking" | "In principle" has a precise meaning (allowed by the laws of physics but not yet achieved); use it accurately |
| "We compute the sensitivity to..." | "We attempt to constrain..." | State what was done, not what was attempted |
| "This bound is three orders of magnitude below..." | "This is a significant improvement over..." | Quantify the improvement; "significant" is vague |

---

## Further reading

George Gopen and Judith Swan's
["The Science of Scientific Writing"](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing)
(American Scientist, 1990) is a two-page paper that explains, from a linguistic perspective, why
readers struggle with scientific prose and what structural choices cause those difficulties.
It is not a style guide for physics specifically, but the underlying theory of why paragraph
structure matters is worth reading alongside this lesson.

## What to read next

[Lesson 04](lesson-04.md) covers the LaTeX conventions that implement these writing rules in practice:
figure environments, equation formatting, cross-references, and citations.
