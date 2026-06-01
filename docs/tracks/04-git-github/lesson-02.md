# Lesson 02 — Branching

A branch is an independent line of development within a repository.
Branches let you work on a new feature, try an experiment, or fix a bug in isolation —
without touching the main line of the project until you are ready.
This lesson covers how to create, switch between, merge, and delete branches,
and how to resolve conflicts when two branches have edited the same file.

---

## What a branch is

Every repository starts with one branch, conventionally named `main`.
Every commit you make on `main` extends its history forward in a straight line.

When you create a new branch, Git creates a new pointer starting at the current commit.
From that point on, commits on the new branch do not affect `main`, and commits on `main`
do not affect the new branch.

This separation is safe and cheap: creating a branch takes milliseconds and costs almost no disk space.

---

## Creating and switching branches

Create a new branch and switch to it immediately:

```sh
git switch -c my-feature
```

List all branches (the current one is marked with `*`):

```sh
git branch
```

Switch to an existing branch:

```sh
git switch main
```

!!! note "git switch vs. git checkout"
    Older tutorials use `git checkout -b branch-name` to create branches and `git checkout branch-name` to switch.
    Both work, but `git switch` (introduced in Git 2.23) is clearer about intent.
    Use `git switch` in new work.

---

## Making commits on a branch

Once you are on the new branch, any commits you make are recorded there and do not appear on `main`.

```sh
git switch -c add-energy-loss
```

Edit files, stage, and commit as normal:

```sh
git add physics/energy_loss.py
```

```sh
git commit -m "Add energy loss calculation for iron nuclei"
```

Switch back to `main` and your working directory reverts to its state on `main`:

```sh
git switch main
```

---

## Merging

When you are ready to bring your branch's work into `main`, merge it.

First, switch to the branch you want to merge *into*:

```sh
git switch main
```

Then merge your feature branch:

```sh
git merge add-energy-loss
```

If `main` has not changed since the branch was created, Git performs a **fast-forward merge**:
it simply moves the `main` pointer forward to the tip of the feature branch.
No merge commit is created.

If `main` has new commits that are not on the feature branch, Git creates a **merge commit**
that combines both histories.

---

## Resolving conflicts

A conflict occurs when both branches have edited the same lines of the same file.
Git cannot decide which version to keep, so it asks you to resolve it manually.

During a merge with conflicts, `git status` shows which files are conflicted:

```sh
git status
```

Open each conflicted file. Git marks the conflict with:

```text
<<<<<<< HEAD
code from your current branch
=======
code from the branch being merged
>>>>>>> add-energy-loss
```

Edit the file to keep the version you want (or a combination of both), removing all the conflict markers.
Then stage the resolved file:

```sh
git add physics/energy_loss.py
```

Complete the merge:

```sh
git commit
```

Git opens your editor with a pre-written merge commit message. Save and close it to finish.

!!! tip "Prevent conflicts by merging frequently"
    Long-lived branches diverge more from `main` and accumulate harder conflicts.
    Merge your feature branch back into `main` as soon as the feature is complete.
    Regularly pulling changes from `main` into your branch (see [Lesson 03](lesson-03.md)) also helps.

---

## Deleting a branch

Once a branch has been merged, it is safe to delete:

```sh
git branch -d add-energy-loss
```

Git warns you if the branch has not been merged, protecting you from accidentally discarding work.

---

## Rebasing

**Rebasing** is an alternative to merging for incorporating changes from one branch into another.
Instead of creating a merge commit, rebase replays your commits one by one on top of the target branch,
producing a linear history with no merge commits.

Rebase your feature branch onto the current tip of `main`:

```sh
git switch my-feature
```

```sh
git rebase main
```

Git replays each commit on `my-feature` as if you had started the branch from the current tip of `main`.
The result is identical code, but with a cleaner, straight-line history.

If there are conflicts during replay, Git pauses and asks you to resolve them — one commit at a time.
After resolving each conflict:

```sh
git add the-conflicted-file.py
```

```sh
git rebase --continue
```

To abort and return to the state before the rebase:

```sh
git rebase --abort
```

!!! warning "Never rebase a branch others have cloned"
    Rebase rewrites commit hashes. If someone else has cloned or checked out your branch,
    rebasing it leaves their copy pointing at commits that no longer exist in the shared history.
    Only rebase branches that only you are working on.

When to use rebase, when to use merge:

| Situation | Recommendation |
| --- | --- |
| Updating a private feature branch before a PR | **Rebase** — keeps the history linear and clean |
| Merging a completed feature branch into `main` | **Merge** — creates a clear record that the feature landed |
| Updating a shared branch that others have cloned | **Merge** — never rebase shared branches |

See [Lesson 03](lesson-03.md) for the full pre-PR rebase workflow with remotes.

---

## Stashing work in progress

If you need to switch branches but have uncommitted changes you are not ready to commit,
use `git stash` to temporarily set them aside:

```sh
git stash
```

Switch to another branch, do your work, then return and restore the stashed changes:

```sh
git switch main
```

```sh
git switch add-energy-loss
```

```sh
git stash pop
```

!!! note "Stash is a stack"
    You can stash multiple times; `git stash pop` restores the most recent stash.
    Use `git stash list` to see all stashed states.

---

## When to branch

A useful rule of thumb for research code: branch whenever you want to try something that might not work.

Common cases:

- Adding a new physical process or cross-section model.
- Refactoring a module while keeping the working version on `main`.
- Running a sensitivity study that changes the simulation parameters.
- Fixing a bug that requires more than one commit.

For tiny, obvious fixes (correcting a typo, fixing a broken import), committing directly to `main` is fine.

---

## What to read next

[Lesson 03](lesson-03.md) covers GitHub: how to push your local repository to a remote,
open pull requests to propose merging a branch, and review other people's code.
