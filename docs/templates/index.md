# Templates

Ready-to-use templates for common research tasks.
Copy the relevant template and adapt it to your needs.

## Available Templates

| Template | Description |
| --- | --- |
| [Journal Club](journal-club.md) | Slide structure and discussion prompts for presenting a paper |
| [Paper Outline](paper-outline.md) | Section-by-section planning scaffold for a physics paper |

## LaTeX Paper Template

The `resources/paper-template/` folder in the repository contains a full LaTeX template
for a two-column RevTeX physics paper, configured to match the group style guide.
It includes:

- `main.tex` — document class, packages, author block, all section scaffolding,
  figure and equation environments with comments, acknowledgements, appendix block, and bibliography call.
- `references.bib` — example BibTeX entries in INSPIRE format, including the three group reference papers.
- `figures/` — placeholder directory; place all figure PDFs here.

To use it, copy the entire `resources/paper-template/` folder, rename it for your paper,
and start filling in `main.tex`.
Retrieve BibTeX entries for your references from [INSPIRE-HEP](https://inspirehep.net) and add them to `references.bib`.
