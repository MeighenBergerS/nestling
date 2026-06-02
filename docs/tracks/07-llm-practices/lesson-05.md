# Lesson 05 — Prompt Engineering for Research

Prompt engineering is the practice of writing inputs to an LLM that reliably produce
useful outputs.
It is not a mystical art — it is the application of clear communication to a system
that responds well to clear communication.

This lesson covers the techniques that matter most for research tasks:
summarisation, explanation, brainstorming, and structured output.

---

## The mental model: briefing a smart assistant

Write your prompt as if you were briefing a knowledgeable colleague who has just joined
the project.
They are capable but know nothing about your specific context unless you tell them.
They will do exactly what you ask — not more, not less — so be specific about what
you want.

---

## Core techniques

### 1. Give context before the task

Bad:

> "Summarise this."

Better:

> "I am a PhD student in astroparticle physics writing a thesis introduction.
> Summarise the following abstract in two sentences suitable for a specialist audience."

The context shapes the register, the level of detail, and what counts as important.

### 2. Specify the format of the output

If you want a bullet list, say so. If you want a single paragraph, say so.
If you want structured output (JSON, a table, a numbered list), describe the exact format.

> "Return your answer as a markdown table with columns: Term | Definition | Example."
> "List the five most important points as a numbered list. One sentence per point."

### 3. Set the audience and level

> "Explain this to a physicist who has not worked in machine learning."
> "Write this for a general audience with no physics background."
> "Assume I am familiar with the standard model but new to cosmology."

The model will adjust vocabulary, assumed knowledge, and depth accordingly.

### 4. Ask for reasoning (chain-of-thought)

For complex problems, asking the model to reason step by step before giving an answer
often produces more accurate results.

> "Think through this step by step before giving your answer."
> "First identify what information is needed, then answer the question."

This is especially useful for checking whether the model's reasoning is sound,
even if the answer is ultimately wrong.

### 5. Give examples (few-shot prompting)

If you want output in a specific style or format, the most reliable way to get it
is to show an example.

> "Rewrite the following sentences in the style of the example below.
>
> Example input: The measurements were performed at low temperature.
> Example output: Measurements were performed at low temperature.
>
> Input: The analysis was conducted using the software developed by the team."

### 6. Constrain what to avoid

> "Do not include citations."
> "Do not use bullet points."
> "Do not suggest anything that requires internet access."

Constraints prevent the model from producing output you will have to discard.

---

## Prompts for common research tasks

### Summarisation

> "Summarise the following [abstract / paper / section] in [N sentences / one paragraph /
> a bullet list].
> Audience: [graduate students / specialists / general public].
> Focus on: [the main result / the methodology / the limitations]."

### Concept explanation

> "Explain [concept] at the level of a [first-year PhD student / undergraduate / expert].
> Cover: what it is, why it matters, and the main caveats.
> Do not use analogies I would need to fact-check."

### Brainstorming

> "I am investigating [problem].
> Generate [N] hypotheses or approaches I might not have considered.
> For each, give one sentence on why it might be worth pursuing and one sentence on its
> main weakness."

### Code generation

(See [Lesson 02](lesson-02.md) for code-specific prompts.)

### Structured extraction

> "From the following text, extract all named physical quantities, their values,
> and their units. Return a markdown table with columns: Quantity | Value | Unit | Source sentence."

### Argument strengthening

> "I am making the following argument in a paper: [argument].
> Identify the two weakest points in this argument and suggest how to address each."

---

## System prompts and persistent context

If you are using an LLM via an API or a tool that supports system prompts, you can
provide persistent context that applies to all messages in a session.
This is useful for:

- Setting your role and background once rather than repeating it every prompt.
- Enforcing output format constraints.
- Specifying style conventions.

Example system prompt for research writing:

```text
You are assisting a PhD student in astroparticle physics.
The student is fluent in physics but not in machine learning.
Respond concisely. Use LaTeX for all mathematical expressions.
Do not generate citations — the student will find references independently.
Flag any claim you are uncertain about.
```

---

## Temperature and parameters

Most LLM interfaces expose at least one generation parameter:

**Temperature** controls randomness. A higher temperature (e.g. 0.9) makes the model
sample more diverse tokens; a lower temperature (e.g. 0.2) makes it more deterministic
and focused.

| Task | Temperature guidance |
|------|---------------------|
| Factual extraction or summarisation | Low (0.0–0.3) — you want the most likely correct answer |
| Brainstorming or creative drafting | Higher (0.7–1.0) — you want variety |
| Code generation | Low to medium (0.0–0.5) — you want correct, predictable output |

For most research tasks, the default temperature (typically 0.7–1.0) is fine.
If you are using the API and need reproducible output, set temperature to 0 and fix the
random seed if the API supports it.

---

## Iterating on prompts

Your first prompt is rarely optimal.
Prompt engineering is an iterative process:

1. Write a first prompt and look at the output.
2. Identify what is wrong: too long, wrong level, missing something, wrong format.
3. Revise the prompt to address that specific issue.
4. Repeat until the output is useful.

Keep a record of prompts that work well.
A prompt that reliably produces good summaries of astrophysics abstracts is worth saving.

---

## Industrial context: prompt engineering as a discipline

**Prompt versioning.** Organisations that deploy LLMs in production treat prompts
as code: they are version-controlled, reviewed, and tested.
For research workflows you use repeatedly, document the prompts that work.

**Prompt injection.** When user-supplied text is incorporated into a prompt, adversarial
inputs can manipulate the model's behaviour.
If you are building an automated pipeline that feeds external data to an LLM, sanitise
inputs and constrain the model's output format.

**Structured outputs.** Modern APIs support JSON mode or structured output schemas,
where the model is constrained to produce valid JSON matching a specified structure.
This is much more reliable than asking the model to "return a JSON object" in free text.
Use structured outputs for any pipeline that processes LLM output programmatically.

**Evaluation.** Industrial teams evaluate prompts systematically: a prompt change
is tested on a benchmark set of inputs before deployment.
For research, this means testing a new prompt on several representative examples
before relying on it for important work.

---

## Checklist

- [ ] My prompts include relevant context (my role, the purpose of the task, the audience).
- [ ] My prompts specify the desired output format.
- [ ] I iterate on prompts rather than accepting the first output.
- [ ] I have saved prompts that reliably produce useful results.
- [ ] I use low temperature for tasks where accuracy matters.
- [ ] For automated pipelines, I use structured output formats.

---

## What to read next

[Lesson 06](lesson-06.md) brings everything together in a verification checklist:
the habits that separate researchers who use LLMs safely from those who do not.
