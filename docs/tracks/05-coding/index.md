# Coding Practices

This track takes you from a blank machine to writing efficient, well-structured research
code. The first seven lessons are practical: you will set up your tools, learn enough
Python to run physics calculations, and get familiar with the packages used throughout
the research group. The final five lessons cover the habits that make code maintainable
and reproducible over time.

[Prometheus](https://github.com/Harvard-Neutrino/prometheus), a neutrino telescope
simulation used in IceCube and KM3NeT analyses, is used as a running example throughout.
It is a real production codebase, so it has both things done well and things that could
be better. Both are worth learning from.

## Lessons

### Foundations

- **[Lesson 01: IDE Setup](lesson-01.md)**: Choosing and configuring a code editor;
  VSCode walkthrough and essential extensions.
- **[Lesson 02: Python & Jupyter Notebooks](lesson-02.md)**: Core Python and working
  interactively with notebooks.
- **[Lesson 03: Package Management](lesson-03.md)**: Installing packages with pip and
  isolating projects with virtual environments.
- **[Lesson 04: Scientific Python Stack](lesson-04.md)**: NumPy, SciPy, Pandas, and the
  libraries you will use every day.
- **[Lesson 05: Code Style & Quality](lesson-05.md)**: PEP 8, ruff, and type hints,
  introduced as a habit early rather than an afterthought.
- **[Lesson 06: Performance & Parallelism](lesson-06.md)**: Vectorisation, multiprocessing,
  Numba, and JAX.
- **[Lesson 07: ML Basics with PyTorch](lesson-07.md)**: Tensors, neural networks, the
  training loop, and where ML fits in physics research.

### Best Practices

- **[Lesson 08: Project Layout](lesson-08.md)**: How to organise files and modules in a
  Python project.
- **[Lesson 09: Documentation](lesson-09.md)**: Writing NumPy-style docstrings and building
  a docs site with MkDocs.
- **[Lesson 10: Testing](lesson-10.md)**: Writing unit tests with pytest and understanding
  what to test.
- **[Lesson 11: Packaging](lesson-11.md)**: Using `pyproject.toml` and pip to make a
  project installable.
- **[Lesson 12: Linting & Automation](lesson-12.md)**: pre-commit hooks, GitHub Actions CI,
  and automated documentation deployment.

## Examples

See the [`examples/coding/`](https://github.com/MeighenBergerS/nestling/tree/main/examples/coding)
folder for a worked example of a modular Python project with docstrings, tests, and packaging.

The `examples/coding/requirements.txt` lists every package needed to run the notebooks and
scripts. Install everything with:

```sh
pip install -r examples/coding/requirements.txt
pip install -e examples/coding/neutrino_flux/
```

For the PyTorch notebook (Lesson 07), install the CPU-only wheel if you do not have a GPU:

```sh
pip install torch --index-url https://download.pytorch.org/whl/cpu
```
