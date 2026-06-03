# Lesson 01: What LLMs Are and Are Not

Large language models are among the most useful tools available to researchers today.
They are also among the most misunderstood.
This lesson explains what LLMs actually do, why they produce confident-sounding errors,
and what mental model you should carry whenever you use one.

---

## What an LLM does

An LLM is a statistical model trained to predict the next token in a sequence.
A **token** is roughly a word fragment: "uncer" and "tainty" might each be one token.
Given a prompt, the model assigns probabilities over its vocabulary and samples the next token,
then repeats until a stopping condition is met.

That is it. There is no reasoning engine, no knowledge database being looked up,
no internal simulation of the world. The model has learned extraordinarily rich statistical
patterns from text, and it uses those patterns to produce text that is likely to follow
the input.

This has important consequences:

- The model produces whatever token sequence is *statistically likely given the training data*,
  not whatever sequence is *true*.
- It has no access to information newer than its training cutoff.
- It has no persistent memory between conversations unless given explicit context.
- It cannot run code unless a tool is wired up to do so.

---

## Hallucination

**Hallucination** is the term used when a model generates factually incorrect content
with apparent confidence.
It is not a bug or a rare failure mode. It is an intrinsic property of how these models work.

A model that produces a plausible-sounding citation is not lying. It is doing exactly what
it was trained to do: generating a token sequence that looks like a citation. Whether the
paper exists is simply not part of the prediction objective.

### Why hallucinations are dangerous in research

- They are hard to spot. The output reads fluently and the claim may be plausible.
- They can propagate. A hallucinated reference copied into a draft may survive peer review
  if nobody checks the source.
- They are inconsistent. The model may give correct information on the same question
  in one conversation and wrong information in another.

### When hallucinations are most likely

| Situation | Risk |
|-----------|------|
| Asking for specific citations | High: model generates plausible-looking but nonexistent papers |
| Asking about recent events | High: model has a training cutoff |
| Asking about niche or specialised topics | High: sparse training data means poor calibration |
| Asking for well-established general knowledge | Lower, but still possible |
| Asking the model to summarise text you have provided | Lower: model has the ground truth in context |

The practical rule: **the further the question is from the centre of the training
distribution, the less you should trust the answer without external verification.**

---

## Confidence does not imply correctness

LLMs are trained on text produced by humans who are often confident.
As a result, the model has learned to produce confident-sounding text regardless of whether
the content is correct.

This is fundamentally different from how scientific uncertainty works.
A calibrated scientist hedges when uncertain. A language model hedges when the *training
distribution* contains hedged text about that topic, which is not the same thing.

You cannot use fluency, certainty of tone, or apparent authority as a proxy for accuracy.
The only proxy for accuracy is **checking the claim against a reliable source**.

!!! warning "The confident wrong answer"
    If you ask a model "what is the best evidence for X?" and it gives you a fluent,
    confident, well-structured answer, resist the temptation to accept it.
    The answer is a prediction about what a helpful response would look like,
    not a retrieval from a database of vetted facts.

---

## The transformer architecture (brief)

You do not need to understand the architecture in depth to use LLMs well, but a high-level
picture helps clarify the limits.

Modern LLMs are **transformer** models.
The key mechanism is **self-attention**: the model can, at each position in the output,
attend to all previous tokens and weight their influence.
This allows the model to capture long-range dependencies. It can use a term defined early
in a document when generating text thousands of tokens later.

Critically, the model has a **context window**, a maximum number of tokens it can attend to
at once. Anything outside this window is simply not available.
Current frontier models have context windows in the range of 100 000 to 1 000 000 tokens,
but performance typically degrades on tasks that require precise retrieval from the far end
of a very long context.

---

## What LLMs are actually good at

Given the above, it might seem like LLMs are unreliable. In some domains they are.
But used correctly they are extraordinarily powerful.

**LLMs are good at:**

- Drafting, paraphrasing, and restructuring text.
- Explaining concepts at a requested level of abstraction.
- Translating between programming languages or styles.
- Suggesting approaches to problems (which you then evaluate).
- Brainstorming a list of options (which you then filter).
- Summarising text you have provided (where hallucination risk is low).
- Writing boilerplate code in well-represented languages and frameworks.
- Identifying possible errors in text or code you have written.

**LLMs are not good at:**

- Providing reliable citations.
- Performing precise arithmetic or symbolic manipulation (though tool-augmented models are better).
- Keeping track of state across long or multi-session interactions without explicit context.
- Tasks that require real-time or post-training information.
- Tasks where a single subtle error is catastrophic and undetectable.

---

## Industrial context: how the field thinks about this

In industry, organisations deploying LLMs at scale have converged on several practices:

**Model cards and system cards.** Leading labs publish documentation summarising
a model's capabilities, limitations, failure modes, and intended use cases before release.
Reading the model card for a model you use heavily is a good habit.

**Red-teaming.** Before deployment, models are tested by teams whose job is to find
failure modes: incorrect outputs, unsafe responses, and edge cases.
The existence of red-teaming reflects the fact that all current models have failure modes
that are not fully characterised.

**Calibration and uncertainty.** Research groups such as Anthropic, DeepMind, and others
publish work on model calibration, measuring how well the model's expressed confidence
tracks actual accuracy. Current models are imperfectly calibrated. Do not infer correctness
from confidence.

**Human-in-the-loop.** High-stakes industrial deployments, in medicine, law,
and financial services, require human review of LLM output before it is acted on.
The same principle applies to research: you are the expert, and you bear responsibility
for what you publish.

---

## Checklist

- [ ] I understand that LLMs predict tokens, not retrieve facts.
- [ ] I understand what hallucination is and why it happens.
- [ ] I treat confident LLM output with the same scepticism as any uncited claim.
- [ ] I know which tasks LLMs handle reliably and which they do not.
- [ ] I verify specific factual claims (citations, numbers, dates) against primary sources.

---

## What to read next

[Lesson 02](lesson-02.md) applies this mental model to code: how to pair-program with
an LLM while keeping you, not the model, in control of correctness.
