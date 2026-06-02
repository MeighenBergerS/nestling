# Lesson 01 — IDE Setup

A good editor makes you significantly more productive: it catches errors before you run code,
navigates large codebases instantly, and integrates with Git, terminals, and debuggers.
Choosing one and learning it well is worth the upfront investment.

---

## Choosing an editor

For physics research the practical choice is **Visual Studio Code (VSCode)**.
It is free, cross-platform, and has excellent Python tooling — autocompletion, a built-in
debugger, Git integration, and Jupyter notebook support all work out of the box.
It is also what most people in the group use, which means help is easy to find.
The examples in this track assume VSCode, but the concepts apply to any editor.

If you prefer a terminal-based workflow — common in HPC environments where you SSH into a
cluster — **Neovim** is the modern choice, with a large plugin ecosystem that replicates most
of what VSCode offers. The learning curve is steep; only pursue it if you spend most of your
time on remote machines and genuinely value that workflow.

The important thing is to pick one editor and learn it properly rather than switching constantly.

---

## Installing VSCode

Download from [code.visualstudio.com](https://code.visualstudio.com/). The installer handles
everything.

Open a project by passing a directory:

```sh
code /path/to/your-project
```

or via **File → Open Folder**.

---

## Essential extensions

Install these via the Extensions panel (⇧⌘X on macOS, Ctrl+Shift+X elsewhere):

| Extension | Publisher | Why |
| --- | --- | --- |
| **Python** | Microsoft | Language support, interpreter selection, debugger |
| **Pylance** | Microsoft | Fast type checking and autocompletion |
| **Jupyter** | Microsoft | Run `.ipynb` notebooks inside the editor |
| **GitLens** | GitKraken | Inline `git blame`, history browsing |
| **Ruff** | Astral | Linting and auto-fix on save (covered in Lesson 05) |

After installing the Python extension, select your interpreter:
Command Palette (⇧⌘P) → **"Python: Select Interpreter"** → choose your `.venv`
(see [Lesson 03](lesson-03.md) for virtual environments).

---

## The integrated terminal

VSCode has a built-in terminal (⌃\` on macOS, Ctrl+\` elsewhere) that opens in your project
root. Use it for all shell commands rather than switching windows.
When you activate a virtual environment in this terminal it applies to all commands you run
there, including `pip install` and `python`.

---

## Running and debugging Python

For quick runs, click the play button (▷) in the top-right of any `.py` file.
For real debugging:

1. Click to the left of a line number to set a **breakpoint** — a red dot appears.
2. Press **F5** to start the debugger.
3. Execution pauses at the breakpoint. Inspect variables in the left panel;
   step through with **F10** (next line) / **F11** (step into function).

The debugger is far more useful than scattering `print()` statements everywhere.
Learning to use it early saves hours later.

---

## Keyboard shortcuts worth learning now

| Action | macOS | Linux/Windows |
| --- | --- | --- |
| Command palette | ⇧⌘P | Ctrl+Shift+P |
| Go to file | ⌘P | Ctrl+P |
| Go to symbol | ⌘⇧O | Ctrl+Shift+O |
| Find in files | ⇧⌘F | Ctrl+Shift+F |
| Open terminal | ⌃\` | Ctrl+\` |
| Format document | ⇧⌥F | Ctrl+Shift+I |

**Go to file** and **Find in files** are the two you will use most in a large codebase like
[Prometheus](https://github.com/Harvard-Neutrino/prometheus), which spans a dozen subpackages.

---

## Remote development

Physics often means working on HPC clusters. VSCode handles this cleanly with the
**Remote - SSH** extension: install it, connect to the cluster once, and the full editor
experience (file browser, terminal, debugger) runs locally while files and processes live
on the remote machine.

---

## What to read next

[Lesson 02](lesson-02.md) covers Python basics and Jupyter notebooks — the interactive
environment where most day-to-day physics work happens.
