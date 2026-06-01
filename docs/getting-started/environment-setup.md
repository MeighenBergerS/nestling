# Environment Setup

!!! note "Do you need this page?"
    If you are here to read the lessons and follow the tracks, **you do not need to install anything** — this site is all you need.
    Only follow this guide if you want to run the code examples locally.

## What is an environment, and why do I need one?

When you install Python packages (libraries of code that other people have written), they get stored somewhere on your computer.
The problem is that different projects often need different versions of the same package — and they can conflict with each other.

A **virtual environment** solves this by giving each project its own private, isolated space for its packages.
Think of it like a separate toolbox for each project: tools in one box don't interfere with tools in another.

This guide walks you through creating that toolbox for Nestling.
If the terminology feels unfamiliar, check the [Glossary](../glossary.md) or ask your supervisor — this is a normal first hurdle.

---

## What you will need

- Python 3.11 or later
- Git
- A terminal (Linux, macOS, or Windows with WSL)

If any of these are unfamiliar, check the [Glossary](../glossary.md) or ask your supervisor before continuing.

---

## Step 1 — Install Python

Download and install Python 3.11 or later from [python.org](https://www.python.org/downloads/).

On Windows, check **"Add Python to PATH"** during installation.

Verify it worked by opening a terminal and running:

```sh
python --version
```

You should see something like `Python 3.11.x`. If you see an error, ask your supervisor.

---

## Step 2 — Clone the repository

```sh
git clone https://github.com/MeighenBergerS/nestling.git
cd nestling
```

If you have not used Git before, work through the [Git & GitHub](../tracks/04-git-github/index.md) track first,
or ask your supervisor to walk you through this step.

---

## Step 3 — Create a virtual environment

A virtual environment keeps Nestling's dependencies separate from the rest of your system.

```sh
python -m venv .venv
```

Then activate it:

- **Linux or macOS:** `source .venv/bin/activate`
- **Windows (WSL):** `source .venv/bin/activate`
- **Windows (Command Prompt):** `.venv\Scripts\activate`

Your terminal prompt should change to show `(.venv)` at the start.

---

## Step 4 — Install dependencies

```sh
pip install -e ".[dev]"
```

This installs Nestling along with all tools needed to run the examples and notebooks.

---

## Step 5 — Verify the setup

```sh
pytest tests/
```

If all tests pass, you are ready to run examples. Open any notebook in the `examples/` folder with Jupyter:

```sh
jupyter notebook
```

!!! tip "Something not working?"
    Environment setup is genuinely one of the trickier parts of getting started — you are not alone if something goes wrong.
    Ask your supervisor; they have almost certainly hit the same issue before and can help you get unstuck quickly.
