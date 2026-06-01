# Lesson 04 — Issues and Project Management

GitHub Issues are the primary way to track work, report bugs, and plan new features on a project.
They keep conversations and decisions attached to the repository, where they remain searchable
and linked to the commits that address them.
This lesson covers how to create and manage issues, and how to connect them to your Git workflow.

---

## What an issue is

An issue is a discussion thread attached to a repository.
It can represent a bug, a feature request, a question, or any piece of work that needs tracking.

Issues are public by default on public repositories.
Anyone can open an issue; only repository collaborators can close, label, or assign them.

---

## Creating an issue

On GitHub, navigate to the **Issues** tab and click **New issue**.

A well-written issue has three parts:

1. **Title**: one line that describes the problem or task precisely.
   "Fix normalisation error in flux calculation" is better than "Bug in calculation".

2. **Description**: enough context for someone else (or yourself in three months) to understand
   what the problem is, how to reproduce it (for bugs), and why it matters.

3. **Labels, assignees, and milestone** (set in the sidebar): covered below.

!!! tip "Reproducible bug reports"
    For a bug, include the exact steps to reproduce it, the output you saw, and the output you expected.
    A bug that cannot be reproduced is very hard to fix.

---

## Labels

Labels categorise issues and pull requests, making it easy to filter and prioritise work.

Common label conventions:

| Label | Meaning |
| --- | --- |
| `bug` | Something is not working correctly |
| `enhancement` | A new feature or improvement |
| `documentation` | Changes to documentation only |
| `good first issue` | Suitable for a newcomer to the project |
| `help wanted` | Extra attention or input is needed |
| `question` | A question rather than a task |

Create labels on the **Labels** page under the Issues tab.
Use consistent colours and descriptions so the label list is easy to read at a glance.

---

## Assignees

Assign an issue to the person responsible for resolving it.
On a small research project, this is usually whoever plans to work on it next.

You can assign yourself: on the issue page, click the **Assignees** gear icon and select your username.

---

## Milestones

A milestone groups related issues and pull requests under a shared goal,
typically tied to a deadline or a version.

Examples for a research project:

- `Submission v1` — everything that must be done before the paper is submitted
- `Code release` — cleanup and documentation required before making the code public

Create milestones from **Issues → Milestones → New milestone**.
Each milestone shows a progress bar based on how many of its issues are closed.

---

## Linking issues to commits and pull requests

GitHub recognises certain keywords in commit messages and pull request descriptions
that automatically close issues when the commit or PR is merged into the default branch.

Supported keywords: `close`, `closes`, `closed`, `fix`, `fixes`, `fixed`, `resolve`, `resolves`, `resolved`.

In a commit message:

```sh
git commit -m "Fix normalisation in spectrum calculation (fixes #12)"
```

In a pull request description:

```text
Fixes #12
```

When this PR is merged into `main`, issue #12 is closed automatically.
A cross-reference also appears on the issue timeline, linking it to the PR.

!!! note "Cross-references without closing"
    To reference an issue without closing it, just write `#12` anywhere in a commit message or comment.
    GitHub creates a link in both directions automatically.

---

## Project boards

For larger projects, GitHub **Projects** provides a Kanban-style board where you can organise
issues and pull requests into columns (for example: To Do, In Progress, Done).

Projects are optional for small research groups.
They become useful when multiple people are working in parallel and you need a shared view
of what is being done and what is blocked.

---

## A practical workflow for research code

A simple issue workflow that works for a small group:

1. Before starting any non-trivial piece of work, open an issue describing what needs to be done.
2. Assign it to yourself and add a label (`enhancement`, `bug`, etc.).
3. Create a branch named after the issue: `git switch -c 12-fix-normalisation`.
4. When the work is done, open a pull request with `Fixes #12` in the description.
5. After the PR is merged, the issue closes automatically.

This keeps the repository history connected to the reasoning behind each change.
Six months later, you can look at a commit, follow the link to the PR, follow the link to the issue,
and read exactly why that change was made.

---

## What to read next

[Lesson 05](lesson-05.md) covers GitHub Actions — how to run tests and checks automatically
on every push, so problems are caught before they reach `main`.
