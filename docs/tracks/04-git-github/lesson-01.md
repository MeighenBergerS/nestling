# Lesson 01: Git Basics

Version control is one of the most important habits you can build as a researcher.
It lets you track every change you make to code, scripts, and text files, revert to any previous state,
and collaborate without accidentally overwriting each other's work.
This lesson covers the core workflow you will use every day.

---

## What Git is

Git is a version control system: a tool that records the history of a directory as a series of snapshots called **commits**.
Each commit captures the exact state of every tracked file at a moment in time, along with a message describing what changed and why.

Git is local by default.
Everything in this lesson happens on your own machine.
[Lesson 03](lesson-03.md) covers how to share your history with others via GitHub.

---

## Initial setup

Before using Git for the first time, tell it who you are.
This information is recorded in every commit you create.

Set your name:

```sh
git config --global user.name "Your Name"
```

Set your email:

```sh
git config --global user.email "you@example.com"
```

Set your preferred editor (used when Git opens a text editor for you):

```sh
git config --global core.editor "nano"
```

These settings are stored in `~/.gitconfig` and apply to every repository on your machine.

---

## Creating a repository

To start tracking a directory, navigate into it and run:

```sh
git init
```

This creates a hidden `.git/` folder that stores the entire history of the project.
You never need to touch anything inside `.git/` directly.

To verify that the repository was created:

```sh
git status
```

On a brand-new repository with no files, Git reports that you are on the initial branch and there is nothing to commit yet.

---

## The three areas

Understanding Git's three areas is the key to understanding every command.

| Area | What it contains |
| --- | --- |
| **Working directory** | Your files as they exist on disk right now |
| **Staging area (index)** | Changes you have selected to include in the next commit |
| **Repository (history)** | All committed snapshots, permanently recorded |

`git add` moves changes from the working directory into the staging area.
`git commit` moves everything in the staging area into the repository as a new commit.

The staging area might feel like an unnecessary extra step at first.
Its purpose is control.
At the end of an afternoon of work you may have edited five files for three different reasons.
The staging area lets you group those changes into three separate, focused commits instead of
one large, confusing one.
A clean commit history is much easier to navigate when something breaks later.

---

## Staging and committing

After editing a file, check what has changed:

```sh
git status
```

Stage the file:

```sh
git add filename.py
```

Stage everything in the current directory:

```sh
git add .
```

Commit with a message:

```sh
git commit -m "Add initial simulation script"
```

!!! note "Stage specific files"
    Prefer staging files by name (`git add analysis.py`) rather than staging everything (`git add .`).
    This forces you to review what goes into each commit and keeps your history clean.

---

## Commit best practices

Writing good commit messages is a habit that develops over time. Early commits are often rough and that is completely fine.
The conventions below are worth building from the start, but do not let them slow you down while you are learning the basics.
A well-structured history is easy to search, easy to review, and easy to recover from.

### One logical change per commit

An **atomic commit** contains exactly one logical change, something you can describe in a single sentence.
If your commit message needs "and" to describe what happened, you probably have two commits.

**Why this matters**: when something breaks, Git can search history automatically to find which commit
introduced the problem (using `git bisect`).
An atomic history makes that search fast and precise.
A commit that changes ten unrelated things makes it impossible to isolate what went wrong.
When you need to undo a mistake, you can revert one clean commit without disturbing anything else.

**Common pitfall**: committing everything at the end of the day as "day's work".
The staging area exists precisely so you can commit each logical change as you finish it,
even if you edited several files in the process.

### Keep the subject line short and specific

The subject line is the most important part of a commit message.
It is what appears in `git log --oneline`, on GitHub, and in code review tools.

Write commit messages in the **imperative mood**: "Fix", "Add", "Remove", "Update",
not "Fixed", "Adding", or "I updated".
Think of completing the sentence: "If applied, this commit will..."

Keep the subject under **72 characters**. GitHub truncates longer subjects in the commit list.

!!! note "Credit"
    The imperative mood convention, the 72-character subject limit, and the blank-line-before-body
    rule are drawn from Tim Pope's
    ["A Note About Git Commit Messages"](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
    (2008), which established the conventions now standard across the Git community.

Good subject lines:

- `Fix normalisation factor in flux calculation`
- `Add energy loss model for iron nuclei`
- `Remove unused import in analysis.py`

Bad subject lines:

- `fix stuff`: says nothing
- `WIP`: not a commit message
- `updates`: meaningless
- `Fixed the thing with the numbers that was wrong`: vague and past tense

**Common pitfall**: writing "Update code" or "Fix bug" because you are in a hurry.
Two months later you will not remember what this commit did, and neither will your collaborators.

### Add a body when the why is not obvious

For commits where the reason is not self-evident, open your editor and add a body:

```sh
git commit
```

Write the subject on the first line, leave a blank line, then explain why:

```text
Fix normalisation factor in flux calculation

The previous factor of 2π was correct for isotropic emission but wrong
for the directed beam case used in the sensitivity study. This affects
all results in Section III.
```

The body explains *why* the change was made, not *what* changed. The diff already shows what changed.

### Never commit secrets or large binary files

Do not commit passwords, API keys, or access tokens.
Setting up a `.gitignore` before your first `git add` is the easiest way to prevent this by accident.
See the next section.
If a secret does reach a public repository, treat it as compromised: rotate the key immediately
and notify whoever manages that service.
(Removing a secret from Git history is possible but requires rewriting every commit that followed it,
which is disruptive for everyone who has cloned the repository.)

Do not commit large data files or compiled outputs (see the `.gitignore` section below).

---

## Ignoring files

Not everything in a project directory should be tracked.
Compiled outputs, temporary files, and data files that can be regenerated should be excluded.

**Why this matters**: Git stores the complete history of every file it tracks.
A large data file committed once stays in the repository forever, even after deletion,
because the old version lives in the history.
This bloats the repository for every collaborator who clones it.
Credentials (passwords, API keys) committed to a public repository are immediately exposed
and should be treated as compromised.

Create a `.gitignore` file in the root of the repository:

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
.venv/

# Jupyter
.ipynb_checkpoints/

# Output data
data/output/
*.h5
```

Files matching these patterns will not appear in `git status` and cannot be staged accidentally.

!!! warning "Add to .gitignore before the first commit"
    Adding a `.gitignore` rule after accidentally committing a file does not remove it from history.
    The rule only prevents future commits.
    Set up your `.gitignore` before running `git add` for the first time.

---

## Reading history

View the commit log:

```sh
git log
```

View a compact one-line-per-commit summary:

```sh
git log --oneline
```

Show what changed in a specific commit (replace `abc1234` with the first seven characters of any commit hash):

```sh
git show abc1234
```

---

## Comparing changes

See what you have changed in the working directory since the last commit:

```sh
git diff
```

See what is staged (ready to commit) versus the last commit:

```sh
git diff --staged
```

---

## Undoing changes

Discard changes to a file in the working directory (revert it to the last committed state):

```sh
git restore filename.py
```

Unstage a file you added by accident (without discarding the change):

```sh
git restore --staged filename.py
```

!!! warning "git restore is permanent for uncommitted changes"
    `git restore filename.py` discards changes that have not been committed.
    Once you run it, those changes are gone.
    Committed history is safe; uncommitted work is not.

---

## A typical daily workflow

Most of your Git usage fits into this loop:

1. Edit files.
2. Run `git status` to see what changed.
3. Run `git diff` to review the changes in detail.
4. Stage the files you want to include: `git add filename.py`.
5. Commit with a clear message: `git commit -m "Fix normalisation in spectrum calculation"`.
6. Repeat.

---

## Further reading

[Pro Git](https://git-scm.com/book/en/v2) by Scott Chacon and Ben Straub is the definitive
reference for Git, freely available online. Chapters 1 and 2 cover everything in this lesson
in greater depth; chapters 3 and 5 cover branching and distributed workflows.
If you want to understand what Git is actually doing rather than just how to use it,
this is the book to read.

## What to read next

[Lesson 02](lesson-02.md) covers branches, the mechanism that lets you develop a new feature
or run an experiment without touching the main line of your project.
