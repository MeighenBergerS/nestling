---
name: text-style-nestling
description: Enforces Nestling-specific text style rules for docstrings, markdown, and prose. Use when checking or generating any non-code text.
---

# Nestling Text Style

## When to Use This Skill

Use this skill whenever you:

- Review or generate **Python docstrings**.
- Edit or create **markdown** (`.md`) or other documentation.
- Write or normalise **comments that read as prose**.
- Produce any **user-facing text** (error messages, logs, CLI help, README sections).

Do **not** apply these rules to pure code identifiers unless explicitly allowed below.

## Formatting Preferences

### Generating Markdown Files

When generating markdown files, use the same formatting style as other files in the [docs directory](../../../docs/).

## Wording and Grammar Preferences

### 1. Use Microsoft Writing Style Guide

When writing or editing text, adhere to the [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/).

### 2. Use `create` or `build` instead of `make` in code-related statements

When describing code (functions, methods, classes), prefer `create` or `build` over `make`.

- ❌ `Make a list of parameters`
- ✅ `Create a list of parameters`
- ❌ `Make a plot`
- ✅ `Build a plot`

### 3. Use present tense in code documentation and docstrings

When describing what classes, methods, and other pieces of code do, prefer present tense.

- ❌ `value: A float which will be used to scale the output.`
- ✅ `value: A float which **is** used to scale the output.`

### 4. Avoid em dashes

Do not use em dashes (—) in prose or documentation. Replace each one with the form that reads
most naturally:

- A **comma**, for parenthetical elaboration: "X, which does Y" not "X — which does Y"
- A **colon**, for introducing a list or description: "the tools: A, B, C" not "the tools — A, B, C"
- A **new sentence**, when two independent clauses are joined: "X. Y." not "X — Y."

### 5. Use one command per code block for shell commands

When generating text that includes shell commands:

- Use one command per code block to make it easy to copy and paste.
- If multiple commands are necessary in the same block, chain them with `&&`.
- Avoid code comments inside shell command blocks; describe the command with text outside the block.

#### Examples

✅ Good: no comments, one command per block

````md
Install the development dependencies:

```sh
pip install -e ".[dev]"
```

Activate pre-commit hooks:

```sh
pre-commit install
```
````

✅ Good: multiple commands chained with `&&`

````md
Clone the repository and navigate into the project directory:

```sh
git clone https://github.com/MeighenBergerS/nestling.git && cd nestling
```
````

❌ Avoid: multiple commands with inline comments

````md
```sh
# Install deps
pip install -e ".[dev]"
# Install hooks
pre-commit install
```
````

## Core Terminology Rules

### 1. Nestling: project name

- Always spell as **Nestling** (capitalised).
- Do not enclose in backticks unless referring to a code identifier named `nestling`.

### 2. Track names

- Refer to learning tracks by their full names: **ArXiv & Reading Papers**, **Journal Club**,
  **Writing Papers**, **Git & GitHub**, **Coding Practices**, **Plotting**, **Working with LLMs**.
- Do not abbreviate in prose (e.g. avoid "the coding track" when "the Coding Practices track" is unambiguous).

### 3. Tool and library names

- **ArXiv**: always capitalised as shown. Not `arxiv`, `Arxiv`, or `ARXIV`.
- **GitHub**: one word, capital G and H. Not `Github` or `github`.
- **Git**: capitalised when referring to the software. Lowercase only in code identifiers.
- **LaTeX**: as shown. Not `Latex` or `LATEX`.
- **matplotlib**: all lowercase in prose, matching the package import name.
- **NumPy**: capitalised as shown. Not `numpy` in prose (lowercase only in code).
- **pytest**: all lowercase.

## Application Guidelines

1. **Respect code identifiers**: do not rename variables, functions, classes, or modules to
   satisfy prose rules. Only adjust surrounding text.
2. **Be consistent**: use the chosen forms uniformly within a document or docstring.
