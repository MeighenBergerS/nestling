# Nestling

A beginner-friendly, physics-first learning repository for early-career researchers and graduates.

This project aims to make practical research skills accessible through short guides, templates, examples, and exercises.

## Goals

- Help physics graduates get productive quickly.
- Provide a supportive path from novice to independent contributor.
- Offer clear documentation, examples, and tests where relevant.
- Encourage good habits in writing, coding, and collaboration.

## Proposed Learning Tracks

1. ArXiv and reading papers
2. Journal club
3. Writing papers
4. Git and GitHub
5. Coding practices
6. Plotting and scientific visualization

## Suggested Repository Structure

```text
nestling/
  README.md
  LICENSE
  .gitignore

  docs/
    index.md
    getting-started/
      environment-setup.md
      how-to-use-this-repo.md
    tracks/
      arxiv-and-reading-papers.md
      journal-club.md
      writing-papers.md
      git-and-github.md
      coding-practices.md
      plotting.md
    glossary.md
    faq.md

  lessons/
    arxiv/
      01-finding-papers.md
      02-reading-strategy.md
    journal-club/
      01-how-to-present.md
      02-discussion-prompts.md
    writing/
      01-paper-structure.md
      02-revision-checklist.md
    git-github/
      01-git-basics.md
      02-github-collaboration.md
    coding/
      01-project-layout.md
      02-testing-basics.md
    plotting/
      01-figure-design.md
      02-matplotlib-basics.md

  templates/
    journal-club-template.md
    paper-outline-template.md
    code-review-checklist.md
    issue-template.md
    pull-request-template.md

  examples/
    plotting/
      simple-line-plot.py
      publication-style-plot.py
    git/
      branching-workflow.md

  tests/
    README.md
```

## What We Need First (MVP)

1. A concise onboarding path for new users
2. One complete lesson per learning track
3. Reusable templates for journal club and writing
4. Simple, runnable coding and plotting examples
5. Basic test and quality checks for code examples
6. Contribution guidelines for community growth

## Accessibility and Novice-Friendliness Principles

- Define jargon before using it.
- Keep lessons short and stepwise.
- Include expected outcomes and common mistakes.
- Add checklists and worked examples.
- Prefer practical tasks over abstract descriptions.

## Testing and Quality Approach

- Add lightweight tests for executable examples.
- Validate links and markdown formatting in docs.
- Keep examples minimal and reproducible.
- Use CI once initial example code exists.

## License

This repository is licensed under the GNU General Public License v3.0 or later (GPL-3.0-or-later).
See the [LICENSE](LICENSE) file.
