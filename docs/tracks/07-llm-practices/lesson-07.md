# Lesson 07: Skill Files

Previous lessons covered how to write effective prompts for individual tasks.
But much of the context you need, your project's structure, the conventions you follow,
the rules you want applied every time, is repetitive.
Typing it again in every conversation is tedious and error-prone.

A **skill file** solves this problem.
It is a document that encodes persistent context for an LLM: the things the model should
always know when working in a particular domain or on a particular project.
You load it once at the start of a session and the model behaves consistently from that point.

This lesson explains what skill files are, when to use them, how to read an existing one,
and how to write your own. It also presents two ready-to-use examples:
a general coding and documentation template, and a writing skill file built from the
conventions in the [Writing Papers track](../03-writing/index.md).

---

## What a skill file is

A skill file is a text document, usually Markdown, that you pass to an LLM as
persistent context.
It is not a prompt for a single task.
It is a briefing that applies to an entire session or workflow.

The contents vary by purpose, but a useful skill file typically covers:

| Section | What it contains |
|---------|-----------------|
| Environment | How to run the code; which interpreter, which commands |
| Project structure | Where things live; what each directory contains |
| Conventions | Style rules, naming conventions, forbidden patterns |
| Workflow | The sequence of steps for common tasks |
| Checklists | What to verify before a result is trusted |

In Claude Code and similar tools, skill files are stored in `.claude/commands/`
as Markdown files and are loaded by name when you invoke them with a slash command
(e.g. `/prometheus`).
But skill files are not tool-specific: you can paste one into any LLM conversation
as a system prompt or opening message.

---

## A real example: Prometheus

The [Prometheus neutrino simulation package](https://github.com/Harvard-Neutrino/prometheus)
uses a skill file at `.claude/commands/prometheus.md`.
Here is the opening section:

```markdown
## Environment

**Python interpreter** (use paths relative to repo root — never rely on `python` or
`python3` being on PATH):

    .prometheus_env/bin/python

**Pytest binary:**

    .prometheus_env/bin/pytest

**Activate for interactive terminal sessions:**

    source scripts/activate.sh .prometheus_env
```

This one section prevents a common class of error: running the wrong Python.
Without it, the LLM might call `python` and get a system Python with the wrong
packages, producing confusing import errors.
The skill file makes the correct behaviour automatic.

Further down, the skill file documents the simulation pipeline:

```text
Prometheus.sim()
└─ inject()            ← LeptonInjector generates neutrino events
└─ propagate()
   └─ OlympusPhotonPropagator.propagate(particle, rng_key)
      ├─ [tracks]  generate_realistic_track()
      └─ [cascades] generate_cascade()
```

And it records domain knowledge that is not in the source code:

```markdown
| Thing | Value / location |
|---|---|
| Distance cutoff | 300 m (normalizing flow not trained beyond this) |
| Cascade resolution | 0.2 m longitudinal step |
| Noise window | 5000 ns |
```

These are the numbers a contributor needs to avoid subtle bugs, and they are exactly
the kind of thing that is forgotten between sessions and expensive to re-derive.
The skill file makes the model aware of them permanently.

Finally, it records coding conventions:

```markdown
## Docstring style

NumPy format. Summary line must not start with "make". Use "create" or "build" for
factory functions.
```

This single rule prevents a whole class of inconsistency without requiring anyone to
remember it.

### What the Prometheus skill file achieves

- A developer opening this project in a new session does not need to re-explain the
  environment, the architecture, or the naming conventions.
- The LLM consistently uses `.prometheus_env/bin/python`, writes NumPy docstrings,
  and respects the 300 m cutoff.
- The skill file is version-controlled alongside the code, so it stays accurate as
  the project evolves.

---

## A general coding and documentation template

A reusable coding skill file template is provided at
`examples/skill-files/coding-docs-template.md`.
It covers the most important elements for any Python research project:
environment setup, project layout, testing workflow, coding conventions, and
documentation style.

Adapt it for your project by filling in the bracketed placeholders.
The key principle is: **include anything that you find yourself explaining repeatedly,
or anything that the model gets wrong if you do not say it explicitly.**

### What to include in a coding skill file

#### Environment

```markdown
## Environment
Python: `.venv/bin/python` (never use bare `python3`)
Install: `.venv/bin/pip install -e .`
Tests: `.venv/bin/pytest tests/ -x`
Lint: `.venv/bin/ruff check src/`
```

#### Project layout (list only the directories that matter to working tasks)

```markdown
## Structure
src/mypackage/        main package
  core.py             [what it contains]
  analysis.py         [what it contains]
tests/                pytest test suite
examples/             runnable scripts demonstrating key workflows
```

#### Key invariants (the things the model should never violate)

```markdown
## Invariants
- All results in physical units (GeV, cm², etc.) — no dimensionless intermediates
- Numpy random state always passed explicitly — no global seeds
- Output arrays are always shape (N,) not (N,1)
```

#### Docstring and style conventions

```markdown
## Conventions
- Docstrings: NumPy format
- All public functions have type hints
- No magic numbers in function bodies — define named constants at module level
```

---

## A writing skill file for physics papers

For the context of writing and revising physics papers, skill files are
equally powerful.
The conventions of HEP writing, described in the [Writing Papers track](../03-writing/index.md),
are detailed enough that an LLM can apply them reliably if told exactly what they are.
But they are also too numerous to type into every session.

A writing skill file encodes these conventions once, so that every LLM interaction
in a writing session automatically respects them.

The file `examples/skill-files/writing-hep.md` is a full writing skill file
based on:

- The conventions taught in the Writing Papers track (lessons 01–05)
- An exhaustive list of rules one learns to follow when writing with John Beacom

### What the writing skill file encodes

The skill file is a condensed, LLM-optimised version of the style guide.
It covers:

| Area | Key rules encoded |
|------|------------------|
| Voice | First-person plural "we"; active verbs; never passive for key results |
| Abstract | 4–5 sentence structure; quantitative result required; no citations |
| Introduction | Four-paragraph structure; "In this work, we..." in paragraph 3; Figure 1 in paragraph 3 |
| Paragraph structure | Opening sentence states the main point; 3–6 sentences; no orphan sentences |
| Results | Figure-first ("Figure X shows..."); at least one OOM estimate per results section |
| Conclusion | Opens "We have shown/computed/demonstrated..."; no new results |
| LaTeX | `Figure~\ref{}` not `Fig.`; `Eq.~(\ref{})` not `\eqref{}`; `\mathrm{}` for subscripts |
| Figures | 3-sentence caption structure; key takeaway in `\textit{...}` |
| Citations | Chronological order; max 3–4 per claim; no citations in abstract |
| Forbidden phrases | "As can be seen in Figure X..." → "Figure X shows..."; passive constructions |

### How this connects to the Writing Papers track

Track 03 teaches the rules through explanation and examples.
The writing skill file operationalises those same rules as a persistent LLM context.
The relationship is:

> Track 03 = understanding the rules
> Writing skill file = enforcing the rules in every session

A student who has worked through track 03 can load the skill file and have the LLM
check their draft against the exact conventions they have learned.
A student who has not yet done track 03 will still get useful corrections from the skill
file, and the corrections are a concrete entry point into the underlying rules.

### Using the writing skill file: two modes

#### Mode 1: Drafting

Load the skill file and give the model your notes or bullet points for a section.
Ask it to draft the section following the style guide.

```text
[Skill file loaded]

Draft the following as a Introduction paragraph 3 (the "In this work, we..." paragraph).
My notes:
- We study the sensitivity of Hyper-K to atmospheric neutrino flux
- We compute event rates for CC and NC interactions
- Main result: we reduce flux uncertainty from ~20% to ~7%
- Figure 1 shows the ratio of measured to predicted flux as a function of energy
```

The model will produce a paragraph that follows the style conventions without you
having to specify them in the prompt.

#### Mode 2: Review

Load the skill file and paste a section of your draft.
Ask the model to check it against the style rules and list violations.

```text
[Skill file loaded]

Review the following Introduction section for style violations.
For each violation, quote the offending text, name the rule, and suggest the fix.

[paste your text]
```

This is the same workflow as the automated pipeline in the SMB_style_guidelines
project, but interactive, so you can ask follow-up questions about each flagged item.

### Example interaction

**Input:**

```text
It is shown that the sensitivity of IceCube to the diffuse supernova neutrino background
is significant. As can be seen in Figure 2, the expected event rate peaks at 20 MeV.
The analysis is performed using the maximum likelihood method.
```

**Expected output from a model with the skill file loaded:**

```text
Three violations:

1. VOICE: "It is shown that..." → "We show that..." (passive for key result)
2. FIGURE: "As can be seen in Figure 2..." → "Figure 2 shows..." (forbidden phrase)
3. VOICE: "The analysis is performed using..." → "We perform the analysis using..."
   (passive construction in body text)
```

Without the skill file, the model might paraphrase these sentences without catching
the violations. With the skill file, the specific rules are in its context and it
applies them reliably.

---

## Writing your own skill file

### Start from what goes wrong

The most valuable items in a skill file are the things the LLM gets wrong if you
do not tell it.
Start by listing:

- Commands or paths the model uses incorrectly.
- Style decisions the model makes wrong (units, variable names, docstring format).
- Domain invariants it violates (numerical cutoffs, sign conventions, required disclaimers).
- Workflow steps it skips.

These are your highest-priority items.

### Keep it honest

A skill file that is out of date is worse than no skill file:
the model follows stale instructions and produces inconsistent output.
Treat the skill file as part of the codebase or document:
update it when the conventions change, and review it when a model starts behaving unexpectedly.

### Keep it concise

A skill file that is too long will overwhelm the model's context and will not be
read carefully.
Aim for the minimum that prevents the most important errors.
If a rule is already enforced by a linter or formatter, you do not need to repeat it
in the skill file.

### Organise by role, not by tool

Write the skill file for what the model needs to know, not for how the tool works.
"Run tests with `.venv/bin/pytest tests/ -x`" is useful.
"Claude Code supports skill files in `.claude/commands/`" is not. That belongs in
the documentation for the tool, not in the project skill file.

---

## Industrial context

**System prompts.** In API-based deployments, the persistent context provided to
an LLM is called a **system prompt**.
It plays exactly the role of a skill file: it is loaded once and shapes every
response in the session.
Professional deployments version-control system prompts as carefully as application code,
because a change to the system prompt can alter the behaviour of every downstream interaction.

**Prompt libraries.** Large organisations maintain libraries of validated system prompts
for different task types: customer support, code generation, document review.
A skill file is the individual contributor's equivalent: a validated context document
for a specific project or domain.

**RAG over style guides.** Some organisations embed their style and convention documents
in a retrieval system, so the model can look up the relevant rule at query time rather
than having the entire document in context.
For most research uses, a single well-maintained skill file is simpler and equally
effective. Retrieval adds complexity without benefit at this scale.

**Evaluation and regression testing.** When a skill file is updated, its effect on
model behaviour can be measured by running a fixed set of test inputs and checking
that the outputs respect the new conventions.
For example one can run a set of test sections through the style checker and
check that violations are correctly identified.
For a hand-maintained skill file, periodic spot-checks serve the same purpose.

---

## Summary

| Concept | Description |
|---------|-------------|
| Skill file | A persistent context document loaded into an LLM session |
| Why useful | Avoids repeating context; enforces conventions; encodes domain knowledge |
| Prometheus example | Covers environment, architecture, pipeline, and coding conventions |
| Coding template | `examples/skill-files/coding-docs-template.md` |
| Writing skill file | `examples/skill-files/writing-hep.md`: encodes track 03 + SMB style guide |
| Two modes | Drafting mode (generate text that follows the style) and review mode (check violations) |
| System prompt | The industrial equivalent: persistent context in API deployments |

---

## What to read next

This is the final lesson in the track.
Return to the [track overview](index.md) for the verification checklist from
[Lesson 06](lesson-06.md), which applies to everything, including LLM-assisted
revision of a draft checked against a skill file.
