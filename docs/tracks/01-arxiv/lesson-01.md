# Lesson 01: Finding Papers

Before you can read a paper, you need to find it.
This lesson covers the main tools physicists use to locate research literature,
how ArXiv is structured, and how to set up alerts so new relevant work lands in your inbox automatically.

---

## What is ArXiv?

[ArXiv](https://arxiv.org) is a free, open-access preprint server run by Cornell University.
A **preprint** is a version of a paper that the authors have made publicly available before (or alongside) formal peer review.

In physics, mathematics, and related fields, ArXiv is the central hub for research.
Papers usually appear on ArXiv on the same day they are submitted to a journal,
which means you can read new results weeks or months before they appear in a published journal.

!!! note "ArXiv versus published journals"
    ArXiv preprints have not been formally peer-reviewed.
    In practice, most physics papers on ArXiv are solid, but errors occasionally slip through.
    Your supervisor can help you develop a sense for which papers to trust.

---

## How ArXiv is organised

ArXiv divides papers into **subject categories**.
Each category has a short identifier. The ones most common in physics research are:

| Identifier | Area |
|---|---|
| `hep-ph` | High-energy physics: phenomenology |
| `hep-th` | High-energy physics: theory |
| `hep-ex` | High-energy physics: experiment |
| `astro-ph` | Astrophysics (with sub-categories like `astro-ph.HE`, `astro-ph.CO`) |
| `cond-mat` | Condensed matter physics |
| `gr-qc` | General relativity and quantum cosmology |
| `nucl-th` / `nucl-ex` | Nuclear theory / experiment |
| `physics` | Applied, atomic, plasma, and other physics |
| `math-ph` | Mathematical physics |

Ask your supervisor which categories are most relevant to your project.
It is common to watch two or three related categories at once.

---

## Where to start: review articles

Before diving into primary research papers, look for a **review article** on your topic.
Review articles are written specifically to introduce a field, summarise its current state,
and point to the key primary literature, exactly what you need when you are new to an area.

Good places to find review articles:

- Search ArXiv for your topic with the word "review" or "introduction" in the title:
  `ti:review AND ti:neutrino AND cat:hep-ph`
- [Physics Reports](https://www.sciencedirect.com/journal/physics-reports): in-depth reviews across all physics.
- [Annual Review of Nuclear and Particle Science](https://www.annualreviews.org/journal/nucl): HEP and nuclear physics.
- [Living Reviews in Relativity](https://link.springer.com/journal/41114): continuously updated reviews in GR and cosmology.
- Ask your supervisor directly. They will know which review papers people in your subfield actually read.

!!! tip "Read a review before reading primary papers"
    A good review article will teach you the vocabulary, the open questions, and the ten papers
    everyone in the field knows. Without that background, primary papers are much harder to follow.
    An hour spent on a review can save days of confusion later.

---

## Finding papers on ArXiv

### Browsing new submissions

The ArXiv listing page for a category (e.g. `arxiv.org/list/hep-ph/new`) shows every paper submitted in the last working day.
This is useful once you know roughly what you are looking for, but can be overwhelming at first.

### Searching ArXiv

Use [ArXiv search](https://arxiv.org/search/) to find papers by keyword, author, or title.

**Tips for effective searching:**

- Use `AND`, `OR`, `NOT` to combine terms (e.g. `dark matter AND direct detection`).
- Search by author name to find all papers from a specific researcher.
- Restrict to a category using the "Subject area" dropdown.
- Use the "Abstract" field to search within abstracts rather than just titles.

!!! tip "Your supervisor's name is a useful starting point"
    Search for your supervisor's papers on ArXiv.
    Reading their recent work is one of the fastest ways to understand the context of your project.

### Inspire-HEP

!!! note "HEP bias"
    Inspire-HEP is the standard tool in high-energy physics and related fields.
    If your project is outside that community, Google Scholar or a field-specific database may serve you better.

[Inspire-HEP](https://inspirehep.net) is a database specifically for high-energy physics.
It indexes ArXiv papers and journal articles together, tracks citation counts,
and makes it easy to find which papers cite a given paper (useful for tracing how a field has developed).

Inspire-HEP is also the standard source for **BibTeX citation entries** in HEP.
Each paper has a *texkey*, a short identifier like `ATLAS:2012yve`, which is what you use in `\cite{}`
commands in a LaTeX document. You can copy a ready-to-use BibTeX entry directly from any paper's Inspire page.

If your project is in particle physics or related areas, Inspire-HEP is worth bookmarking alongside ArXiv.

**Following citations forward:** once you find a key paper, use the *Cited by* tab on its Inspire page
to see every paper that has cited it. This is one of the most effective ways to trace how a subfield
has developed and to find the current state of the art. Start from a foundational paper and follow
the thread forward to the most recent work.

### NASA ADS

!!! note "Astrophysics focus"
    NASA ADS is the standard literature database in astrophysics and space science.
    If your project is in astroparticle physics or has an astrophysics component, it is worth knowing
    alongside Inspire-HEP.

[NASA ADS](https://ui.adsabs.harvard.edu/) (Astrophysics Data System) indexes astrophysics,
physics, and space science literature. Like Inspire-HEP, it tracks citations and links ArXiv
preprints to their published journal versions. It covers a broader range of astrophysics
subfields than Inspire-HEP, and its citation tools are widely used in that community.

If you are unsure which database your subfield uses, ask your supervisor.

### Google Scholar

[Google Scholar](https://scholar.google.com) indexes papers across all disciplines,
including ArXiv preprints and published journal articles.
It is useful for finding papers outside physics, or when you want citation counts and links to the published version.

---

## Following a specific paper's identifier

Every ArXiv paper has a unique identifier, for example `2312.01234`.
You can reach any paper directly at `arxiv.org/abs/2312.01234`.

When a colleague or supervisor mentions a paper, they will often give you just this number.

!!! note "Preprint vs. published version"
    The ArXiv version and the published journal version of a paper sometimes differ.
    Most of the time the differences are minor (typos, small clarifications), but occasionally
    a correction is substantial. When a published version exists, that is what you should cite,
    and for papers that are central to your work, it is worth checking whether the published version
    contains corrections relative to the preprint.
    The DOI link on the ArXiv abstract page takes you directly to the published version.

---

## Setting up email alerts

Checking ArXiv daily by hand is impractical once your project is running.
Email alerts let new relevant papers come to you.

### ArXiv email alerts

1. Go to your category listing page (e.g. `arxiv.org/list/hep-ph/new`).
2. Click **"Subscribe"** at the top of the page.
3. Enter your email address. You will receive a daily digest of new submissions.

This gives you everything in the category, which is useful for staying broad, but noisy if the category is large.

### Inspire-HEP author alerts

On [Inspire-HEP](https://inspirehep.net), you can follow a specific author.
When they upload a new paper, you receive a notification.
This is a good way to track your supervisor's collaborators or key figures in your field.

### Google Scholar alerts

1. Search for a keyword or author on Google Scholar.
2. Scroll to the bottom of the results and click **"Create alert"**.
3. Google will email you when new matching papers appear.

This works across disciplines and catches papers that may not be on ArXiv.

---

## What to do with a paper once you find it

Finding a paper is just the first step.
Once you have identified something relevant, save it to your reference manager before you forget about it. You will thank yourself later.
The next lesson, [Lesson 02](lesson-02.md), covers how to actually read a paper efficiently.
[Lesson 03](lesson-03.md) covers how to manage and organise what you find.

!!! tip "Ask your supervisor about the field's key papers"
    Every subfield has a small set of foundational papers that almost everyone knows.
    Ask your supervisor for two or three papers to start with. Reading those first will give you the vocabulary to search more effectively.

---

## Code examples

The [`examples/arxiv/`](https://github.com/MeighenBergerS/nestling/tree/main/examples/arxiv) folder
contains runnable Python scripts and Jupyter notebooks that demonstrate everything covered in this lesson.
You do not need to run these to follow the track. They are for when you want to automate or explore programmatically.
Each topic has a plain script for quick reference and a notebook with step-by-step commentary.

### ArXiv API: [`arxiv_api.py`](https://github.com/MeighenBergerS/nestling/tree/main/examples/arxiv/arxiv_api.py) · [`arxiv_api.ipynb`](https://github.com/MeighenBergerS/nestling/tree/main/examples/arxiv/notebooks/arxiv_api.ipynb)

Uses the [`arxiv`](https://pypi.org/project/arxiv/) Python package to:

- Search ArXiv by keyword with boolean filters and category restrictions.
- Fetch a single paper directly by its ArXiv identifier.

```python
import arxiv

client = arxiv.Client()
search = arxiv.Search(
    query="ti:neutrino mass AND cat:hep-ph",
    max_results=5,
    sort_by=arxiv.SortCriterion.SubmittedDate,
)
for result in client.results(search):
    print(result.title, result.entry_id)
```

### Inspire-HEP API: [`inspire_api.py`](https://github.com/MeighenBergerS/nestling/tree/main/examples/arxiv/inspire_api.py) · [`inspire_api.ipynb`](https://github.com/MeighenBergerS/nestling/tree/main/examples/arxiv/notebooks/inspire_api.ipynb)

!!! note "HEP bias"
    This script uses the Inspire-HEP API, which covers high-energy physics literature.
    The patterns transfer to other REST APIs, but the database itself is HEP-specific.

Uses the [Inspire-HEP REST API](https://inspirehep.net/api/) (no authentication needed) to:

- Search by keyword, author, or any Inspire query syntax.
- Fetch a paper's full metadata, including its texkey and citation count, by ArXiv ID.
- Retrieve a ready-to-use BibTeX entry from Inspire, which is the standard citation format in HEP.
- **Verify that a paper actually exists**: useful when working with LLMs, which sometimes hallucinate
  plausible-sounding citations. Querying Inspire with the ArXiv ID or texkey is a fast sanity check:
  a clean hit with a matching title is strong evidence the paper is real; no hit means proceed with caution.

```python
import requests

# Check whether a paper with a given ArXiv ID exists in Inspire-HEP
response = requests.get(
    "https://inspirehep.net/api/literature",
    params={"q": "eprint 1207.7214", "size": 1},
    timeout=10,
)
hits = response.json()["hits"]["hits"]
print("Found" if hits else "Not found")
```
