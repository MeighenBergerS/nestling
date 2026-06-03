# Lesson 05: GitHub Actions

Every time code is pushed to a repository, the same questions arise:
do the tests still pass, does the linter raise any warnings, does the documentation build?
GitHub Actions answers those questions automatically, without anyone having to remember to check.
This lesson explains what Actions is, how workflow files work, and how Nestling uses it.

---

## What GitHub Actions is

GitHub Actions is a continuous integration (CI) system built into GitHub.
You define workflows in YAML files stored in `.github/workflows/`.
GitHub runs those workflows on its own servers whenever specified events occur,
typically a push to a branch or the opening of a pull request.

The result of each workflow run is shown on the pull request page as a green checkmark or red cross.
A failing check blocks the PR from being merged (if branch protection rules are enabled),
so problems are caught before they reach `main`.

---

## Anatomy of a workflow file

A workflow file has three main parts: a name, triggers, and jobs.

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: pip install -e ".[dev]"
      - name: Run tests
        run: pytest tests/
```

| Part | What it does |
| --- | --- |
| `name` | Label shown on the GitHub Actions tab |
| `on` | Events that trigger the workflow |
| `jobs` | Independent units of work, each running on a fresh machine |
| `runs-on` | The operating system for the runner (`ubuntu-latest` is the most common) |
| `steps` | Ordered list of actions or shell commands within a job |
| `uses` | Runs a reusable action from the GitHub Actions marketplace |
| `run` | Runs a shell command directly |

---

## How Nestling uses Actions

Nestling has two workflow files:

**`.github/workflows/ci.yml`**: runs on every push to `main` and on every pull request targeting `main`.
It runs three jobs in parallel:

| Job | What it checks |
| --- | --- |
| `quality` | Linting with ruff and markdownlint via pre-commit |
| `test` | Unit tests with pytest and notebook tests with nbmake |
| `docs` | Documentation build with `mkdocs build --strict` |

**`.github/workflows/deploy-mkdocs.yml`**: runs only on pushes to `main`.
It deploys the documentation site to GitHub Pages using `mkdocs gh-deploy`.

The CI job must pass before any pull request can be merged.
The deploy job runs after merge to keep the live documentation site up to date.

---

## Status checks and branch protection

On GitHub, go to **Settings → Branches** and create a branch protection rule for `main`.

Useful settings for a research project:

- **Require a pull request before merging**: prevents direct pushes to `main`.
- **Require status checks to pass before merging**: blocks merge if any CI job fails.
- **Require branches to be up to date before merging**: ensures the PR is tested against the current `main`.

With these rules in place, nothing reaches `main` unless the tests pass and at least one person has reviewed it.

---

## Reading workflow output

When a workflow run fails, navigate to the **Actions** tab on GitHub and click the failing run.
Each job is listed. Click into the failing job to see the step-by-step output.

Common failures and what they mean:

| Error | Likely cause |
| --- | --- |
| `pytest: N failed` | A test assertion is wrong or a function changed its behaviour |
| `ruff: E501` | A line exceeds the maximum character length |
| `markdownlint` | A markdown file violates a formatting rule |
| `mkdocs build --strict` | A broken link or missing file in the documentation |

Fix the issue locally, commit, and push. The workflow re-runs automatically.

---

## Writing your own workflow

To add CI to a new repository, create the workflow directory and file:

```sh
mkdir -p .github/workflows
```

Create a minimal workflow at `.github/workflows/ci.yml` that installs your dependencies and runs your tests.
Start simple. A single job that runs pytest is enough to begin with.
Add linting and documentation checks once the basic test job is working.

!!! tip "Test locally before pushing"
    Run your tests locally before pushing to avoid cycles of push-fix-push.
    The [act](https://github.com/nektos/act) tool can run GitHub Actions workflows locally,
    which is useful for debugging complex workflows before they reach GitHub.

!!! note "Actions minutes"
    GitHub provides a generous free tier of Actions minutes for public repositories (unlimited)
    and private repositories (a monthly allowance).
    For typical research code with fast test suites, the free tier is more than sufficient.

---

## Further reading

The [GitHub Actions documentation](https://docs.github.com/en/actions) covers everything beyond
what this lesson introduces: workflow syntax in full, the available runner environments, secrets
management, reusable workflows, and the Actions marketplace. When your CI needs grow beyond a
basic test-and-lint setup, the official docs are the right place to start.

## What to read next

This is the last lesson in the Git & GitHub track.
If you have worked through all five lessons, you now have a complete Git workflow,
from making your first commit to automated CI running on every push.
That is a genuinely substantial set of skills, and the habits you have built here
(clear commits, code review, automated checks) will serve you throughout your research.

For the next step in building good research software practices, see the
[Coding Practices](../05-coding/index.md) track.
