# How to Contribute to Nestling

Welcome and thank you for investing your time in contributing to Nestling!

The types of contributions we would love to accept are:

- bug reports, enhancement suggestions, and new lesson proposals
- new lessons, examples, notebooks, and templates
- documentation fixes and improvements

## Bug Reports, Enhancements, and New Lesson Proposals

If you found a bug, have an idea for a new lesson, or want to suggest an improvement,
open an issue:

1. Navigate to the [issue template chooser](https://github.com/MeighenBergerS/nestling/issues/new/choose).
2. Select the relevant issue form and fill it in.

Not sure which form to choose? Open a
[discussion](https://github.com/MeighenBergerS/nestling/discussions) instead.

> [!TIP]
> When reporting bugs, include as much detail as you can: your OS, Python version,
> the exact command you ran, and the full error output.

## Content and Code Changes

To contribute a lesson, example, notebook, template, or code fix:

1. Fork the repository.
2. Create a branch and make your changes.
3. Open a pull request.

If you are new to this workflow, see
[GitHub's guide to creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

> [!TIP]
> We recommend enabling [maintainer edits](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/allowing-changes-to-a-pull-request-branch-created-from-a-fork)
> on your pull request so we can fix small issues without extra round-trips.

### Best Practices

#### Include context

In your PR description, reference any related issues and add as much detail as you can.
Screenshots or short recordings of new examples are very helpful.

#### Use good commit messages

Write short, descriptive commit messages in the imperative mood.

Good examples:

- `add lesson on virtual environments to coding track`
- `fix broken link in glossary`

Bad examples:

- `fixed stuff`
- `update`

#### Use the PR checklist

The [pull request template](./github/PULL_REQUEST_TEMPLATE.md) includes a checklist.
Use it to make sure your change is tested, documented, and linted before review.

## Documentation Changes

### How the Docs Work

All documentation is built with [MkDocs](https://www.mkdocs.org/) and published at
<https://meighenbergers.github.io/nestling/>.

Lesson content lives in `docs/tracks/`. Runnable examples live in `examples/`.

### Style Guides, Checks and Best Practices

- Follow the [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/).
- Python docstrings use NumPy style — see the skill file at
  [`.agents/skills/numpy-docstring-format/SKILL.md`](.agents/skills/numpy-docstring-format/SKILL.md).
- For text and docstring style, see
  [`.agents/skills/text-style-nestling/SKILL.md`](.agents/skills/text-style-nestling/SKILL.md).
- Python code is linted with `ruff` (line length 100, rules E/F/W/I).
- Markdown is linted with `markdownlint-cli2`.
- Jupyter notebooks must be stripped of output before committing
  (`nbstripout` runs automatically via the pre-commit hook).

### Setting Up the Development Environment

Install dependencies:

```sh
pip install -e ".[dev]"
```

Install pre-commit hooks (both stages are required):

```sh
pre-commit install
```

```sh
pre-commit install --hook-type commit-msg
```

### Testing Documentation Changes

To preview the site locally:

```sh
mkdocs serve
```

The output will contain the local address. For more details, see the
[MkDocs documentation](https://www.mkdocs.org/getting-started/).

## Questions

Ask anything in [discussions](https://github.com/MeighenBergerS/nestling/discussions).

## A Note for First-Time Contributors

- Look for issues labeled `good first issue` in the
  [issues view](https://github.com/MeighenBergerS/nestling/issues?q=state%3Aopen+label%3A%22good+first+issue%22).
- The best way to get started is to read a lesson, try an example, and see what is unclear.
- Feel free to ask questions by
  [opening a discussion](https://github.com/MeighenBergerS/nestling/discussions).

---

Happy contributing!
