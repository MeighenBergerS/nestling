# Lesson 03 — GitHub Collaboration

GitHub hosts your Git repository on the internet so that others can read it, contribute to it,
and review your work.
This lesson covers how to push your local history to GitHub, how to collaborate using forks and
pull requests, and how to keep your copy of a repository up to date with changes from others.

---

## Remotes

A **remote** is a repository stored somewhere other than your local machine.
GitHub is the most common host, but the Git commands are the same regardless of where the remote lives.

After creating a repository on GitHub, connect it to your local repository:

```sh
git remote add origin https://github.com/username/repo-name.git
```

The name `origin` is a convention for the primary remote. You can verify it was added:

```sh
git remote -v
```

---

## Pushing

Push your local commits to the remote:

```sh
git push -u origin main
```

The `-u` flag sets `origin main` as the default upstream for the current branch.
After the first push, subsequent pushes only need:

```sh
git push
```

Push a feature branch:

```sh
git push -u origin my-feature
```

---

## Pulling

Pull brings remote commits into your local branch.
It is equivalent to `git fetch` followed by `git merge`.

```sh
git pull
```

Use `git fetch` if you want to see what is on the remote without merging it immediately:

```sh
git fetch origin
```

Then inspect the difference before merging:

```sh
git diff main origin/main
```

### Pruning stale remote-tracking branches

On an active repository, branches are created and deleted frequently.
Git does not automatically remove your local references to remote branches that have been deleted on the remote —
these stale references (`origin/some-old-feature`) accumulate over time and clutter `git branch -r` output.

Pass `--prune` to clean them up during a fetch:

```sh
git fetch --prune
```

Or prune without fetching:

```sh
git remote prune origin
```

!!! tip "Make pruning automatic"
    You can tell Git to always prune when fetching:
    ```sh
    git config --global fetch.prune true
    ```
    After this, every `git fetch` and `git pull` prunes stale references automatically.

---

## Cloning

To start working on an existing repository, clone it:

```sh
git clone https://github.com/username/repo-name.git
```

This downloads the full history and automatically sets the remote to `origin`.

---

## Forks

A **fork** is a copy of someone else's repository under your own GitHub account.
Forks are used when you do not have write access to the original repository —
which is the standard situation for contributing to any project you do not own.

To fork a repository, click **Fork** on its GitHub page.
Then clone your fork:

```sh
git clone https://github.com/your-username/repo-name.git
```

Add the original repository as a second remote, conventionally named `upstream`:

```sh
git remote add upstream https://github.com/original-owner/repo-name.git
```

This lets you pull new changes from the original project into your fork:

```sh
git fetch upstream
```

```sh
git merge upstream/main
```

---

## Pull requests

A **pull request** (PR) is a proposal to merge a branch or fork into another branch.
It is the primary mechanism for code review on GitHub.

The typical workflow:

1. Create a branch for your changes: `git switch -c fix-cross-section`
2. Commit your changes on that branch.
3. Before opening the PR, update `main` and rebase your branch onto it (see below).
4. Push the branch to GitHub: `git push -u origin fix-cross-section`
5. On GitHub, open a pull request from `fix-cross-section` into `main`.
6. Collaborators review the code, leave comments, and request changes if needed.
7. Address any feedback by adding more commits to the same branch.
8. Once approved, merge the pull request on GitHub.

!!! tip "Your first pull request does not need to be perfect"
    The review process exists precisely to catch things.
    If you miss something, a collaborator will flag it and you will know for next time.
    Opening a PR that gets comments is not a failure — it is how the workflow is supposed to function.

!!! tip "Keep pull requests small"
    A PR that touches one thing is much easier to review than one that touches ten.
    If your branch has grown large, consider splitting it into several smaller PRs.
    Reviewers are more thorough and faster when there is less to read.

---

## Pull request best practices

### Write a useful title and description

The PR title follows the same rules as a commit subject line: imperative, specific, under 72 characters.

The description should answer three questions:

1. **What changed?** A short summary — one paragraph or a brief bullet list.
2. **Why?** The motivation. Link to the relevant issue if one exists (`Fixes #12`).
3. **How to verify it?** What a reviewer should check to confirm the change works correctly.

A PR with a blank description forces reviewers to read every line of code before they even
understand what they are looking at.
A clear description means they can review faster and catch real problems instead of asking
orientation questions.

### Self-review before requesting a review

Before tagging anyone as a reviewer, open your own PR on GitHub and read the diff yourself.

Look for:

- Leftover debug prints or commented-out code.
- Files you did not mean to include.
- Typos in variable names or commit messages.
- Any change that looks confusing without an explanation.

**Why this matters**: finding these yourself takes two minutes.
Making a reviewer find them wastes their time and adds an unnecessary round of back-and-forth.

**Common pitfall**: pushing the branch and immediately requesting a review without looking at the
GitHub diff. The web view renders the diff differently from your editor and regularly catches
things you missed locally.

### Use draft pull requests for work in progress

If you want early feedback on an incomplete change, open the PR as a **Draft** on GitHub
(use the dropdown next to "Create pull request" and select "Create draft pull request").
Draft PRs are visible to the team but clearly marked as not ready for review.

When the work is complete, convert it to a regular PR with the "Ready for review" button.

**Why this matters**: a draft PR starts the discussion early, makes your work visible to the team,
and runs CI checks — so you catch failures before the final review.
It also signals to collaborators what you are working on, which avoids duplicated effort.

### Respond to every review comment

When a reviewer leaves a comment, respond to it — even if only to say you have addressed it.
If you disagree with a suggestion, explain why rather than silently ignoring it.
Once all threads are resolved, re-request a review.

**Common pitfall**: fixing the code but not replying to the comment thread.
The reviewer does not know whether their feedback was read and the PR stalls.

### Do not push significant changes after approval

Once a PR has been approved, only push small, unambiguous fixes (a typo, a missing docstring).
Adding significant code after approval means the reviewer has not seen what is about to be merged.

If you realise a substantial change is needed after approval, notify the reviewer and ask them
to re-review before you merge.

---

## Reviewing a pull request

When someone asks you to review their code, your job is not to approve everything —
it is to check whether the changes are correct, readable, and consistent with the project.

On GitHub, you can:

- Leave a **comment** on any line to ask a question or flag something unclear.
- Mark a comment as a **suggestion** to propose a specific replacement (the author can apply it with one click).
- **Approve** the PR when you are satisfied.
- **Request changes** when something must be addressed before merging.

Use the comment field on the PR page to leave a summary review.
Keep comments specific: "Line 42: this loop will fail if `particles` is empty" is more useful than "looks off".

---

## Keeping your branch up to date

!!! note "This section is for when you are comfortable with the basics"
    If this is your first or second pull request, you can skip this section for now.
    Once you are working on a project where `main` is moving frequently, come back to it.

On a project with multiple developers, `main` moves forward continuously.
Before opening a pull request, it is good practice to update your local `main` and rebase your feature branch onto it.
This ensures your PR is tested against the latest code and produces a clean, linear history for reviewers.

**Step 1** — update your local `main` to match the remote:

```sh
git switch main
```

```sh
git pull --rebase
```

**Step 2** — rebase your feature branch onto the updated `main`:

```sh
git switch my-feature
```

```sh
git rebase main
```

**Step 3** — force-push the rebased branch (its commit hashes have changed):

```sh
git push --force-with-lease
```

Use `--force-with-lease` rather than `--force`.
It fails if someone else has pushed to the branch since your last fetch,
protecting you from overwriting work you did not know about.

If conflicts arise during the rebase, Git pauses at each conflicted commit.
Resolve the file, stage it, and continue:

```sh
git add the-conflicted-file.py
```

```sh
git rebase --continue
```

See [Lesson 02](lesson-02.md) for a full explanation of what rebase does and how to abort if needed.

!!! warning "Only rebase your own branch"
    Rebase rewrites commit hashes, so anyone else who has checked out your branch will have a diverged copy.
    Rebase is safe on a feature branch that only you are working on.
    Never rebase `main` itself or any branch shared with others.

---

## What to read next

[Lesson 04](lesson-04.md) covers GitHub Issues — how to track work, report bugs, and link issues
to specific commits and pull requests.
