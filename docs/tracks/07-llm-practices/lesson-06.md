# Lesson 06: Verification Habits

The previous lessons covered what LLMs can and cannot do, and how to use them
in specific contexts.
This lesson distils those lessons into a set of habits you can apply consistently
to any LLM-assisted work.

Good verification habits are not about distrust. They are about knowing what
to check and doing it efficiently.

---

## The verification mindset

The core habit is simple: **treat every LLM output as a first draft that requires review,
not as a finished product.**

This is not a counsel of paranoia. LLMs produce genuinely useful output most of the time.
But the failure modes, confident wrong answers, hallucinated citations, subtle code bugs,
are hard to spot and consequential in research.
A consistent habit of checking costs little time and prevents most problems.

The analogy from the previous lessons bears repeating: the LLM is a fast, capable junior
colleague who is occasionally confidently wrong. You would not publish a junior colleague's
draft without reading it. Apply the same standard here.

---

## Verification by type of output

### Factual claims

**Check:** Does the claim appear in a primary source you can access?

- For numerical values (cross-sections, distances, physical constants): verify against a
  textbook, a reviewed paper, or an authoritative database (PDG, NIST).
- For statements about papers ("Smith et al. showed that..."): find the paper and read
  the relevant passage.
- For current events, policies, or recent results: the model has a training cutoff.
  Use a current source.

**Red flag:** The claim is plausible but you cannot find a source for it.
Plausible and correct are not the same thing.

### Citations

**Check:** Does this paper exist? Does it say what is claimed?

1. Search for the paper by title, authors, and year in arXiv, ADS, InspireHEP, or Google Scholar.
2. Confirm the DOI or arXiv identifier.
3. Read the abstract. If the paper is central to your argument, read the relevant section.

Never include a citation you have not verified at step 1–2 at minimum.

### Code

**Check:** Does the code do what the specification says, for all inputs?

- Read every line before running.
- Run the code on a case you can verify by hand.
- Test edge cases: empty input, extreme values, NaN/inf.
- Check for security issues if the code handles external input.
- Confirm random seeds and version pins are set.

### Summaries of text you provided

**Check:** Is the summary accurate? Has anything been omitted or changed?

- Read the original alongside the summary.
- The model can drop qualifications ("not always true" becomes "true"),
  change quantifiers ("most" becomes "all"), or lose important caveats.

### Explanations and concept descriptions

**Check:** Is the explanation correct at the level of detail that matters for your use?

- Explanations of well-known concepts are usually reliable.
- Explanations of niche or recent topics are higher risk.
- Verify the key technical claims against a textbook or a reviewed source
  before teaching or repeating them.

---

## The verification checklist

Use this before incorporating any LLM output into your work.

### Factual content

- [ ] Every numerical value has been checked against a primary source.
- [ ] Every attribution ("X showed that Y") has been verified against the cited source.
- [ ] No claim relies solely on LLM output as its basis.

### Citations

- [ ] Every cited paper was found in a real database.
- [ ] Authors, title, journal, year, and DOI/arXiv number are correct.
- [ ] The paper says what I am claiming it says.

### Code

- [ ] I have read every line of LLM-generated code.
- [ ] The code has been tested on expected inputs and edge cases.
- [ ] I can explain what every function does.
- [ ] Random seeds and version pins are set.
- [ ] Security issues have been checked if the code handles external input.

### Writing

- [ ] Every idea and argument originated with me.
- [ ] I have disclosed LLM assistance where required.
- [ ] I have read every sentence for accuracy, not just fluency.
- [ ] Qualifications and caveats are preserved.

---

## Building habits over time

A checklist is most useful when it becomes automatic, when you run through it
without thinking, as part of your normal workflow.
The habits that matter most, in order of impact:

1. **Never include a citation you have not verified.** This is the highest-consequence
   failure mode and the easiest to prevent.

2. **Read every line of code before using it.** You are responsible for what runs in
   your analysis.

3. **Verify numerical values against a primary source.** A wrong constant propagates
   silently through a whole analysis.

4. **Disclose assistance where required.** Know your institution's and journal's policy
   and apply it consistently.

5. **Treat confident output with the same scepticism as uncertain output.**
   Fluency and accuracy are independent properties of LLM output.

---

## Industrial context: systematic verification practices

**Red-teaming and adversarial testing.** Before deploying an LLM-based system,
organisations test it by trying to make it fail: produce wrong answers, unsafe content,
or policy violations.
For your own use, "red-teaming" your workflow means occasionally asking the LLM
a question you already know the answer to, to calibrate how often and how badly it
is wrong on your kinds of tasks.

**Audit trails.** In regulated industries, every LLM-generated output that influences
a decision is logged: the prompt, the output, the reviewer, and the action taken.
For research, keeping a record of which parts of a paper or analysis involved
LLM assistance is good practice and increasingly expected by journals.

**Staged review.** Industrial pipelines for high-stakes LLM use have multiple review
stages, automated checks, then human review, then subject-matter expert review,
before output is acted on.
For a research paper, the analogous stages are: you verify the LLM output,
your supervisor or collaborators review the work, and the peer review process provides
a further check.

**Calibration.** Organisations that depend on LLM output track how often the model
is correct on their specific task domain.
If you use an LLM heavily for a specific type of task (code in a particular language,
summaries of astrophysics papers, etc.), periodically spot-check a sample of its
output to maintain calibration on its error rate for that task.

---

## A note on models and their limitations changing over time

LLM capabilities improve rapidly. A task that a model handled unreliably in 2023 may
be handled well in 2025, and vice versa. New models sometimes regress on specific tasks.

This means:

- Habits that rely on specific known failure modes may need updating.
- Model cards and evaluation reports for the specific model you are using are more
  reliable than general reputation.
- When you switch to a new model version, spot-check your common tasks rather than
  assuming the same reliability profile.

The verification habits in this lesson are robust to model changes: they do not assume
any particular failure mode, only that LLMs can be wrong in ways that are hard to detect
without checking.

---

## Summary

| Output type | Key check | Most important habit |
|-------------|-----------|---------------------|
| Factual claims | Find the primary source | Never cite what you have not read |
| Citations | Verify paper exists and says what you claim | Verify before including, not after |
| Code | Read every line, test edge cases | Understand before committing |
| Summaries | Compare to original | Check qualifications are preserved |
| Explanations | Verify key claims in a textbook | Higher scrutiny for niche topics |

---

## What to revisit

This lesson is designed to be a reference you return to. After completing the track,
the most useful practice is to re-read the verification checklist at the start of
each new LLM-assisted task until the checks are automatic.

[Back to track overview](index.md)
