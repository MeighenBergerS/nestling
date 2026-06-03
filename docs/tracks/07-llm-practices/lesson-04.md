# Lesson 04: LLMs for Literature Search

Literature search is one of the most dangerous areas in which to use an LLM carelessly.
The failure mode is specific and severe: models generate plausible-sounding citations
that do not exist, and the errors are hard to spot without checking each source.

This lesson explains why this happens, what safe workflows look like, and where LLMs
can legitimately help with literature search.

---

## Why LLMs hallucinate citations

Citation hallucination is not a bug that will be fixed in the next model version.
It is a structural consequence of how LLMs work.

The model was trained on text that contains many papers, many citations, and many
references to research.
When asked to provide a citation, the model generates a plausible token sequence in the
format of a citation.
It is not retrieving from a database. It is sampling from the distribution of text that
looks like citations.

The result can look exactly like a real paper:

> Smith, J. & Jones, A. (2019). High-energy neutrino flux constraints from IceCube data.
> *Physical Review Letters*, 122(4), 041101.

This paper may not exist.
The authors, journal, volume, issue, and page number are all individually plausible,
and the combination is plausible, but the combination may never have been published.

Even if a real paper by those authors exists, the model may have the year wrong,
the title wrong, or the journal wrong.

---

## The rule: never use a citation you have not verified

**Every citation you include in your work must be verified against the actual source.**

Verification means:

1. You found the paper in a real database (arXiv, ADS, InspireHEP, Google Scholar, etc.).
2. You confirmed the authors, title, journal, year, and DOI or arXiv number.
3. You confirmed that the paper says what you are claiming it says.

Step 3 is not optional. An LLM may hallucinate not just the citation but also the claim
attributed to it. A paper may exist but say something different from what the model claimed.

---

## What to do instead of asking an LLM for references

Use real search tools:

| Tool | Best for |
|------|---------|
| [arXiv](https://arxiv.org) | Preprints in physics, maths, CS, quantitative biology |
| [ADS (NASA Astrophysics Data System)](https://ui.adsabs.harvard.edu) | Astronomy and astrophysics |
| [InspireHEP](https://inspirehep.net) | High-energy physics |
| [Google Scholar](https://scholar.google.com) | Broad search across all disciplines |
| [Semantic Scholar](https://www.semanticscholar.org) | AI-assisted search with citation graph |
| [Connected Papers](https://www.connectedpapers.com) | Exploring citation networks around a seed paper |

These tools search indexed databases and return real papers.
Use them for finding references.

---

## Where LLMs legitimately help with literature

LLMs are genuinely useful for several literature-adjacent tasks that do not require
citing a specific paper.

### Explaining a concept before you search

> "Explain the neutrino floor in direct dark matter detection at a graduate student level.
> I will verify and find references myself."

The model can give you a conceptual orientation before you read the primary literature.
Treat this as background, not as citable content.

### Summarising a paper you have pasted

When you paste the full text (or abstract) of a paper and ask for a summary, the model
is working from the ground truth in its context rather than sampling from memory.
Hallucination risk is much lower.
Still verify that the summary is accurate before acting on it.

### Identifying search terms and related concepts

> "I am searching for papers about anomalous magnetic moment measurements of the muon.
> What other terms, concepts, and authors should I search for?"

The model can surface vocabulary and names you might not think to search for.
The suggestions are starting points for your own search, not a reading list.

### Finding connections between papers you already have

Give the model a list of real papers you have already read and ask it to identify
themes, contradictions, or gaps.
It is working from your supplied content, not hallucinating.

---

## Retrieval-augmented generation (RAG)

Some tools combine an LLM with a real document retrieval system.
The model searches a database, retrieves relevant passages, and generates a response
grounded in the retrieved text, with citations pointing to the actual documents.

Examples include Semantic Scholar's AI features, Perplexity AI (with source linking),
and custom RAG pipelines.

These tools are substantially more reliable for citations than a plain LLM, because
the citations are drawn from the retrieval step rather than generated from the language
model.

**However:** you should still verify that the retrieved passage actually says what the model
claims, and that the passage is from the paper it claims.
RAG systems can still mis-attribute or misquote.

---

## A safe workflow for LLM-assisted literature work

1. **Identify the concept or question you are researching.**
2. **Ask the LLM for background and search terms.** Do not ask for specific papers.
3. **Use a real database to find actual papers.** Use the search terms the LLM suggested.
4. **Read the abstracts and papers you find.**
5. **If you want a summary or comparison of the papers you found,**
   paste the text into the LLM and ask it to work from what you have provided.
6. **Never include a citation** unless you have completed step 4 for that citation.

---

## Industrial context

**Scientific publishing and preprint servers.** Physics preprints on arXiv have been
indexed since 1991, and the arXiv API supports programmatic access.
For systematic literature reviews, scripted searches against indexed databases are
more reliable than LLM-generated reading lists.

**Citation graph tools.** Semantic Scholar, Connected Papers, and ResearchRabbit build
on citation graphs to surface related work.
These tools are more reliable for discovery than asking an LLM, because they operate
on a structured database rather than a language model.

**AI search assistants with grounding.** Tools that display the source document alongside
the claim (such as Perplexity AI or AI-assisted search in Microsoft Bing) provide a way
to check the claim against the source immediately.
This is better practice than accepting ungrounded LLM output.

**Retractions and errors.** Even real papers can be wrong or retracted.
The [Retraction Watch](https://retractionwatch.com/) database tracks retracted papers.
For any paper that forms a cornerstone of your argument, check its citation history
and retraction status.

---

## Checklist

- [ ] I use real databases (arXiv, ADS, InspireHEP, Google Scholar) to find references.
- [ ] I have verified every citation: authors, title, journal, year, DOI.
- [ ] I have read the abstract (at minimum) of every cited paper.
- [ ] I have confirmed that every cited paper says what I claim it says.
- [ ] I have not included any citation the LLM generated without completing the above steps.

---

## What to read next

[Lesson 05](lesson-05.md) covers prompt engineering: how to write prompts that get
the most useful responses for research tasks like summarisation, explanation, and
brainstorming.
