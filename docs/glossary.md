# Glossary

A reference for common terms used across the Nestling tracks.

!!! note "Under construction"
    This glossary is being expanded. Suggest additions via a GitHub issue.

---

**API (Application Programming Interface)**
: A defined way for programs to communicate with each other.
The arXiv and INSPIRE-HEP APIs let you query paper databases programmatically rather than through a web browser.

**ArXiv**
: A free, open-access repository for preprints in physics, mathematics, computer science, and related fields.
Papers appear here before (and sometimes instead of) formal peer review.

**BibTeX**
: A reference management format used with LaTeX.
Each paper is stored as a structured entry with a cite key (e.g., `Author:2023abc`) that you reference in your `.tex` file.
INSPIRE-HEP exports BibTeX entries directly.

**Branch (Git)**
: An independent line of development in a Git repository.
Branches let you work on a feature or fix without affecting the main codebase.

**CI/CD (Continuous Integration / Continuous Deployment)**
: A practice of automatically running tests and checks every time code is pushed to a repository.
GitHub Actions is the CI tool used in Nestling.

**Clone (Git)**
: Creating a local copy of a remote repository, including its full history.
`git clone <url>` is usually the first command you run when joining a project.

**Code of Conduct**
: A written agreement that sets out expected behaviour in a community, explains what is not acceptable, and describes what happens when someone is harmed.

**Colormap**
: A mapping from data values to colours used in plots.
Choosing a perceptually uniform, colourblind-safe colormap (e.g., `viridis`) is important for accessible and honest visualisation.

**Commit (Git)**
: A snapshot of changes saved to the Git history.
Each commit has a unique identifier and a message describing what changed.

**Conda**
: A package manager and environment manager popular in scientific Python.
It can install non-Python packages (compilers, CUDA drivers) and is an alternative to pip + virtual environments.

**DOI (Digital Object Identifier)**
: A persistent identifier for a published document.
A DOI such as `10.1103/PhysRevLett.130.071001` can be resolved at `doi.org` to find the paper regardless of where it is hosted.

**Docstring**
: A string literal at the start of a Python module, class, or function that documents its purpose.
Nestling uses NumPy-style docstrings.

**Fork (Git)**
: A personal copy of someone else's repository on GitHub.
Forks let you propose changes to projects you do not have direct write access to, by submitting a pull request from your fork.

**Hallucination (LLM)**
: A confident but factually incorrect output from a large language model.
LLMs can generate plausible-sounding citations, equations, or code that are simply wrong.

**HEP (High-Energy Physics)**
: The branch of physics that studies the fundamental constituents of matter and their interactions,
typically using particle accelerators or high-energy cosmic messengers.
Most of the style conventions in Nestling's writing and citation tracks reflect HEP practice.

**IDE (Integrated Development Environment)**
: A program that combines a code editor, file explorer, terminal, and debugger in one interface.
VSCode is the IDE recommended in Nestling.

**INSPIRE-HEP**
: The main literature database for high-energy physics.
It indexes papers from arXiv, journals, and conference proceedings, and provides citation counts and BibTeX export.

**Issue (GitHub)**
: A GitHub feature for tracking tasks, bugs, or questions in a repository.
Issues can be linked to commits and pull requests to record why a change was made.

**Journal Club**
: A regular meeting where researchers present and discuss a recent paper.

**Jupyter Notebook**
: An interactive computing environment that combines code, text, equations, and figures in a single document (`.ipynb` file).
Widely used for exploratory analysis in scientific Python.

**LaTeX**
: A document preparation system widely used in physics for typesetting equations and papers.

**Linting**
: Automated checking of code for style violations and common errors.
In Nestling, `ruff` is the primary linter.

**LLM (Large Language Model)**
: A type of AI model trained on large amounts of text to predict and generate language.
Examples include Claude, GPT-4, and Gemini.
LLMs are useful for code assistance and drafting, but can hallucinate — see [Working with LLMs](tracks/07-llm-practices/index.md).

**Markdown**
: A lightweight markup language for writing formatted text using plain characters (e.g., `**bold**`, `# Heading`).
Used for documentation, README files, and all pages on this site.

**matplotlib**
: The standard Python library for producing scientific plots and figures.
Most other Python plotting tools build on or wrap matplotlib.

**Merge conflict (Git)**
: A situation where two branches have made incompatible changes to the same part of a file and Git cannot automatically combine them.
You resolve conflicts by editing the affected file manually and then committing.

**NumPy**
: The foundational Python library for numerical computing.
It provides arrays, vectorised operations, and mathematical functions that are faster and more convenient than plain Python loops.

**PEP (Python Enhancement Proposal)**
: A design document that proposes a new feature or convention for the Python language or ecosystem.
PEP 8 is the widely adopted Python style guide; PEP 484 introduced type hints.

**pip**
: The standard package installer for Python.
Running `pip install <package>` downloads and installs a library from the Python Package Index (PyPI).

**Preprint**
: A version of a paper shared publicly before formal peer review, typically on ArXiv.

**Prompt (LLM)**
: The text input you give to a large language model to elicit a response.
Writing clear, specific prompts — prompt engineering — significantly affects output quality.

**Pull Request (PR)**
: A GitHub mechanism for proposing changes to a repository and requesting review before merging.

**pytest**
: A Python testing framework used to write and run unit tests.

**Remote (Git)**
: A version of a repository hosted on another machine, typically GitHub.
`origin` is the conventional name for the remote you cloned from.

**Repository (Repo)**
: A directory tracked by Git, containing your project files and the full history of every change ever made to them.
Repositories can be hosted on platforms like GitHub for collaboration and backup.

**RevTeX**
: A LaTeX document class developed by the American Physical Society (APS) for typesetting papers in Physical Review and related journals.
It is the standard document class for HEP papers.

**ruff**
: A fast Python linter and formatter used in Nestling to enforce code style.

**SSH (Secure Shell)**
: A protocol for securely connecting to remote machines or services over a network.
GitHub uses SSH keys as an alternative to passwords for authentication.

**Staging area (Git)**
: An intermediate area where you collect changes before committing them.
`git add` moves changes into the staging area; `git commit` saves everything staged into the repository history.

**Terminal**
: A text-based interface for interacting with your computer by typing commands.
Also called the command line, shell, or console.
On macOS and Linux it is built in; on Windows it is accessible via WSL or the Command Prompt.

**Token (LLM)**
: The basic unit of text that a language model processes — roughly a word or word fragment.
Models have a context window measured in tokens that limits how much text they can process at once.

**Vectorisation**
: Replacing explicit Python loops with array operations (e.g., NumPy) that apply a computation to many elements at once.
Vectorised code is typically 10–1000× faster because it delegates to optimised compiled code.

**Virtual Environment**
: An isolated Python installation that keeps a project's dependencies separate from the system Python and from other projects.

**WSL (Windows Subsystem for Linux)**
: A feature of Windows that lets you run a Linux environment directly inside Windows without a separate virtual machine.
Nestling's setup instructions assume WSL for Windows users.
