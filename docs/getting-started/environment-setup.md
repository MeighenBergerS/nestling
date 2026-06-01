# Environment Setup

This guide walks you through setting up a local environment to use Nestling's examples and run the documentation site.

!!! note "Under construction"
    Detailed step-by-step instructions are being developed. The outline below describes what this guide will cover.

## What You Will Need

- Python 3.11 or later
- Git
- A terminal (Linux, macOS, or WSL on Windows)

## Planned Steps

- **Step 01 — Install Python**: using the official installer or a package manager.
- **Step 02 — Clone the repository**: using `git clone`.
- **Step 03 — Create a virtual environment**: using `venv` or `conda`.
- **Step 04 — Install dependencies**: using `pip install -e ".[dev]"`.
- **Step 05 — Install pre-commit hooks**: two commands are required.

    ```sh
    pre-commit install
    ```

    ```sh
    pre-commit install --hook-type commit-msg
    ```

    The first installs file-level hooks (ruff, markdownlint, nbstripout).
    The second installs the commit-message hook that notices LLM co-authors.

- **Step 06 — Verify the setup**: running `pytest` and `mkdocs build`.
