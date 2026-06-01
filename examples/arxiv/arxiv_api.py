"""ArXiv API examples for the Nestling ArXiv track.

Demonstrates searching ArXiv by keyword and fetching a paper by its identifier
using the `arxiv` Python package, which wraps the official ArXiv API.

Install: pip install arxiv
"""

import arxiv

# ---------------------------------------------------------------------------
# 1. Keyword search
# ---------------------------------------------------------------------------


def search_arxiv(query: str, max_results: int = 5) -> list[arxiv.Result]:
    """Search ArXiv and return a list of results.

    Parameters
    ----------
    query : str
        Search query string. Supports boolean operators (AND, OR, NOT)
        and field prefixes such as ``ti:`` (title), ``au:`` (author),
        ``abs:`` (abstract), ``cat:`` (category).
        Example: ``"ti:dark matter AND cat:hep-ph"``
    max_results : int, optional
        Maximum number of results to return. Default is 5.

    Returns
    -------
    list[arxiv.Result]
        List of result objects. Each has ``.title``, ``.authors``,
        ``.published``, ``.entry_id``, ``.summary``, and ``.pdf_url``.
    """
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )
    return list(client.results(search))


# ---------------------------------------------------------------------------
# 2. Fetch a single paper by ArXiv identifier
# ---------------------------------------------------------------------------


def fetch_by_id(arxiv_id: str) -> arxiv.Result | None:
    """Fetch a single paper by its ArXiv identifier.

    Parameters
    ----------
    arxiv_id : str
        ArXiv identifier, e.g. ``"2312.01234"`` or ``"hep-ph/0503172"``.

    Returns
    -------
    arxiv.Result or None
        The paper record, or ``None`` if no match is found.
    """
    client = arxiv.Client()
    search = arxiv.Search(id_list=[arxiv_id])
    results = list(client.results(search))
    return results[0] if results else None


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== ArXiv keyword search: 'neutrino mass' in hep-ph ===\n")
    results = search_arxiv("ti:neutrino mass AND cat:hep-ph", max_results=3)
    for r in results:
        authors = ", ".join(str(a) for a in r.authors[:3])
        if len(r.authors) > 3:
            authors += " et al."
        print(f"Title  : {r.title}")
        print(f"Authors: {authors}")
        print(f"Date   : {r.published.date()}")
        print(f"ArXiv  : {r.entry_id.split('/')[-1]}")
        print()

    print("=== Fetch by ArXiv ID: 1207.7214 (Higgs discovery) ===\n")
    paper = fetch_by_id("1207.7214")
    if paper:
        print(f"Title  : {paper.title}")
        print(f"Authors: {', '.join(str(a) for a in paper.authors[:3])} et al.")
        print(f"Date   : {paper.published.date()}")
        print(f"URL    : {paper.entry_id}")
