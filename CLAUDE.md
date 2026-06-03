# Nestling — Claude Code project instructions

## Project

Nestling is a documentation-first learning resource for early-career researchers in
high-energy and astroparticle physics. The audience is PhD students and junior postdocs
encountering research tooling for the first time. Tone is direct, clear, and encouraging.
Content is organised into short self-contained lessons grouped into tracks.

## Environment

Always activate the virtual environment before running any Python, pre-commit, pytest,
or mkdocs command:

```sh
source .venv/bin/activate
```

Never rely on bare `python`, `python3`, or `pip` from PATH.

## Prose and documentation style

These rules apply to all markdown files, docstrings, and any user-facing text you write
or edit. Full rules are in `.agents/skills/text-style-nestling/SKILL.md`.

### No em dashes

Do not use em dashes (—) anywhere in prose or documentation. Replace each one with the
form that reads most naturally:

- A **comma**, for parenthetical elaboration
- A **colon**, for introducing a list or description
- A **new sentence**, when two independent clauses are joined

This is the single most commonly violated rule — enforce it without exception.

### Terminology

| Term | Correct form |
| --- | --- |
| Project name | **Nestling** (capitalised, never in backticks unless a code identifier) |
| ArXiv | **ArXiv** (not `arxiv`, `Arxiv`, or `ARXIV`) |
| GitHub | **GitHub** (capital G and H) |
| Git | **Git** (capitalised when referring to the software) |
| LaTeX | **LaTeX** (not `Latex` or `LATEX`) |
| matplotlib | **matplotlib** (all lowercase in prose) |
| NumPy | **NumPy** (not `numpy` in prose) |
| pytest | **pytest** (all lowercase) |

### Other prose rules

- Follow the Microsoft Writing Style Guide for general wording and grammar decisions.
- Use `create` or `build` instead of `make` when describing code actions.
- Use present tense in code documentation and docstrings.
- Do not use emojis unless explicitly requested.
- Do not write comments that explain what the code does; only write them when the WHY
  is non-obvious.

## Markdown formatting

- Maximum line length: 150 characters.
- Use fenced code blocks (`sh`, `python`, etc. language tags), not indented blocks.
- One shell command per code block. Chain with `&&` only if the commands must run together.
- Do not put comments inside shell code blocks; describe the command with surrounding prose.
- Admonitions (`!!! note`, `!!! tip`, `!!! warning`) are available via the MkDocs
  admonition extension and are used throughout the docs. Match the existing style.

## Python conventions

Full rules are in `.agents/skills/docstrings-style/SKILL.md` and
`.agents/skills/numpy-docstring-format/SKILL.md`.

- **Docstrings**: NumPy format for all public functions and classes.
- **Summary line**: imperative verb, sentence-cased, ends with a period, ≤ 75 characters.
  Start with `"""Summary.` on the same line as the opening triple quotes.
- **Type hints**: all public functions must have complete type hints.
- **Types in docstrings** must match the type hints exactly.
- Raise `ValueError` for invalid inputs at public API boundaries.
- Do not use bare `except:`. Always specify the exception type.

## Git

- Stage specific files by name. Do not use `git add -A` or `git add .`.
- Only commit when explicitly asked to.
