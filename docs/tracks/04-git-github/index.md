# Git & GitHub

## What is Git?

Git is a **version control system**: a tool that records the complete history of every change
made to a set of files.
Every time you save a snapshot of your work — called a **commit** — Git stores what changed,
who changed it, and when.
You can go back to any previous snapshot at any time.

Think of it as an unlimited undo history for your entire project, not just the last few keystrokes.

Git runs entirely on your own machine.
Your history is stored locally in a hidden `.git/` folder inside your project directory.
No internet connection is required to commit, view history, or undo changes.

## What is GitHub?

GitHub is a website that hosts Git repositories on the internet.
It adds a layer of tools on top of Git for collaboration: pull requests for proposing and
reviewing changes, issues for tracking tasks and bugs, and Actions for running automated checks.

The key distinction: **Git** is the version control tool, **GitHub** is a hosting platform built around it.
You can use Git without GitHub; GitHub without Git makes no sense.
Other hosting platforms (GitLab, Bitbucket) exist, but GitHub is the standard in most research groups.

## Why use version control in research?

The most common alternative to version control is a folder that looks like this:

```text
analysis_final.py
analysis_final_v2.py
analysis_final_v2_REAL.py
analysis_final_corrected.py
analysis_jan_backup.py
```

This breaks down quickly.
You cannot tell what changed between versions, who changed it, or why.
Rolling back to a working state means guessing which file that was.
Sharing the work with a collaborator means emailing files and hoping no one edits the same one simultaneously.

Git solves all of these problems:

- **Every version is preserved.** You can always return to any previous state of the project.
- **Every change is explained.** Commit messages record why a change was made, not just what changed.
- **Collaboration is structured.** Branches and pull requests let multiple people work on the same
  project without overwriting each other.
- **History is searchable.** When a result changes unexpectedly, you can find exactly which commit
  introduced the change.
- **Nothing is lost accidentally.** Uncommitted work can be discarded; committed work cannot.

!!! note "Version control is not just for software"
    Git works well for anything text-based: Python scripts, LaTeX source files, Jupyter notebooks,
    configuration files, and plain-text notes.
    It is not suitable for large binary files (data files, images, compiled outputs) — those should
    be listed in `.gitignore` and stored elsewhere.

## Lessons

| Lesson | Topic | What you will learn |
| --- | --- | --- |
| [01 — Git Basics](lesson-01.md) | Repositories and commits | Initialising a repository, staging changes, committing, and reading history |
| [02 — Branching](lesson-02.md) | Parallel lines of work | Creating and merging branches and resolving conflicts |
| [03 — GitHub Collaboration](lesson-03.md) | Forks and pull requests | Pushing to a remote, opening pull requests, and reviewing code |
| [04 — Issues and Project Management](lesson-04.md) | Tracking work | Creating issues, linking them to commits, and using labels and milestones |
| [05 — GitHub Actions](lesson-05.md) | Automated checks | Running tests and linters on every push with a workflow file |

Work through the lessons in order if you are new to Git.
If you already use Git daily and want a specific topic, jump to the lesson that covers it.
