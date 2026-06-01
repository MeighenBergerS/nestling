"""Inspire-HEP API examples for the Nestling ArXiv track.

Demonstrates searching Inspire-HEP, fetching a paper by its ArXiv identifier,
and verifying whether a paper actually exists — useful for catching hallucinated
citations produced by LLMs.

Note: Inspire-HEP indexes high-energy physics literature and is the standard
citation database in that community. These examples reflect that bias.

API documentation: https://inspirehep.net/api/
No authentication is required for read-only access.

Install: pip install requests
"""

import requests

INSPIRE_API = "https://inspirehep.net/api"


# ---------------------------------------------------------------------------
# 1. Keyword search
# ---------------------------------------------------------------------------


def search_inspire(query: str, max_results: int = 5) -> list[dict]:
    """Search Inspire-HEP and return a list of paper records.

    Parameters
    ----------
    query : str
        Inspire search query. Supports field qualifiers such as
        ``t`` (title), ``a`` (author), ``k`` (keyword), ``eprint`` (ArXiv ID).
        Example: ``"t neutrino mass AND k dark matter"``
        Full query syntax: https://inspirehep.net/search?ui-citation-summary=true
    max_results : int, optional
        Maximum number of results to return. Default is 5.

    Returns
    -------
    list[dict]
        List of Inspire metadata records. Each record contains keys such as
        ``"arxiv_eprints"``, ``"titles"``, ``"authors"``, ``"texkeys"``,
        ``"citation_count"``, and ``"dois"``.
    """
    response = requests.get(
        f"{INSPIRE_API}/literature",
        params={"q": query, "size": max_results, "sort": "mostrecent"},
        timeout=10,
    )
    response.raise_for_status()
    return response.json().get("hits", {}).get("hits", [])


# ---------------------------------------------------------------------------
# 2. Fetch a paper by its ArXiv identifier
# ---------------------------------------------------------------------------


def fetch_by_arxiv_id(arxiv_id: str) -> dict | None:
    """Fetch a single Inspire record by ArXiv identifier.

    Parameters
    ----------
    arxiv_id : str
        ArXiv identifier, e.g. ``"1207.7214"`` or ``"hep-ph/0503172"``.

    Returns
    -------
    dict or None
        The Inspire metadata record, or ``None`` if no match is found.
    """
    hits = search_inspire(f"eprint {arxiv_id}", max_results=1)
    return hits[0]["metadata"] if hits else None


# ---------------------------------------------------------------------------
# 3. Verify a paper exists (hallucination check)
#
# LLMs sometimes invent plausible-sounding citations. Querying Inspire with
# the arXiv ID or the Inspire texkey (e.g. "Collaboration:2012gk") is a fast
# way to confirm a paper is real. A miss does not guarantee the paper is fake
# (it may be outside HEP or too recent to be indexed), but a clean hit with
# matching title is strong evidence it exists.
# ---------------------------------------------------------------------------


def verify_paper(arxiv_id: str) -> bool:
    """Check whether a paper with the given ArXiv ID exists in Inspire-HEP.

    Parameters
    ----------
    arxiv_id : str
        ArXiv identifier to look up, e.g. ``"1207.7214"``.

    Returns
    -------
    bool
        ``True`` if Inspire returns at least one matching record.
    """
    return fetch_by_arxiv_id(arxiv_id) is not None


# ---------------------------------------------------------------------------
# 4. Retrieve the Inspire BibTeX citation
#
# Inspire-HEP is the standard source for BibTeX entries in HEP.
# The texkey (e.g. "ATLAS:2012yve") is what you use in \cite{} commands.
# ---------------------------------------------------------------------------


def get_bibtex(inspire_id: int) -> str:
    """Retrieve the BibTeX entry for a paper from Inspire-HEP.

    Parameters
    ----------
    inspire_id : int
        The numeric Inspire literature ID (visible in the paper's Inspire URL).

    Returns
    -------
    str
        BibTeX string ready to paste into a ``.bib`` file.
    """
    response = requests.get(
        f"{INSPIRE_API}/literature/{inspire_id}",
        headers={"Accept": "application/x-bibtex"},
        timeout=10,
    )
    response.raise_for_status()
    return response.text


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Inspire-HEP keyword search: 'neutrino oscillations' ===\n")
    records = search_inspire("t neutrino oscillations", max_results=3)
    for hit in records:
        meta = hit["metadata"]
        title = meta.get("titles", [{}])[0].get("title", "N/A")
        texkey = meta.get("texkeys", ["N/A"])[0]
        citations = meta.get("citation_count", 0)
        arxiv = meta.get("arxiv_eprints", [{}])[0].get("value", "N/A")
        print(f"Title    : {title}")
        print(f"Texkey   : {texkey}")
        print(f"ArXiv    : {arxiv}")
        print(f"Citations: {citations}")
        print()

    print("=== Fetch by ArXiv ID: 1207.7214 (Higgs discovery, ATLAS) ===\n")
    record = fetch_by_arxiv_id("1207.7214")
    if record:
        title = record.get("titles", [{}])[0].get("title", "N/A")
        texkey = record.get("texkeys", ["N/A"])[0]
        print(f"Title : {title}")
        print(f"Texkey: {texkey}")
        print()

    print("=== Hallucination check ===\n")
    real_id = "1207.7214"
    fake_id = "9999.99999"
    print(f"ArXiv {real_id} exists in Inspire: {verify_paper(real_id)}")
    print(f"ArXiv {fake_id} exists in Inspire: {verify_paper(fake_id)}")
    print()

    print("=== BibTeX from Inspire (ATLAS Higgs paper, Inspire ID 1124337) ===\n")
    bibtex = get_bibtex(1124337)
    print(bibtex)
