# Lesson 03: Managing Papers

Finding and reading papers is only useful if you can find them again later.
A reference manager keeps your literature organised, stores your notes,
and generates citations automatically when you write.

---

## Why you need a system

Without a system, papers accumulate in a downloads folder, filenames like `2312.01234.pdf`
tell you nothing, and the note you wrote three months ago about why a paper mattered is gone.

A good reference manager lets you:

- Store papers with metadata (title, authors, year, journal, abstract).
- Search your own library by keyword or author.
- Attach notes, highlights, and tags to each paper.
- Generate BibTeX entries for use in LaTeX documents.
- Sync across devices so your library is available wherever you work.

Setting this up early, before your library grows large, is much easier than organising retroactively.

---

## Zotero (recommended)

[Zotero](https://www.zotero.org) is a free, open-source reference manager widely used in academia.
It is the most common choice in physics and related fields.

### Getting started with Zotero

1. Download and install Zotero from [zotero.org](https://www.zotero.org/download/).
2. Install the **Zotero Connector** browser extension, which lets you save papers to your library with one click while browsing ArXiv or journal websites.
3. Create a free Zotero account to sync your library across devices.

### Adding papers from ArXiv

With the Zotero Connector installed:

1. Open the ArXiv page for a paper (e.g. `arxiv.org/abs/2312.01234`).
2. Click the Zotero Connector icon in your browser toolbar.
3. Zotero will save the paper's metadata and, in most cases, download the PDF automatically.

You can also add papers manually using their ArXiv identifier or DOI:
in Zotero, click **File → Add item by identifier** and paste the number.

### Organising your library

- Create **Collections** (folders) by project or topic.
- Use **Tags** for cross-cutting themes (e.g. `to-read`, `important`, `method-paper`).
- Add notes to each paper while you read. The note field in Zotero is a good home for your per-paper summaries from [Lesson 02](lesson-02.md).
- Use **Zotero Groups** to share a library with your research group. Many labs maintain a shared group
  library so that everyone has access to the papers the group has collected and annotated.
  Ask your supervisor whether your group has one. Joining it is often the fastest way to bootstrap
  your library with relevant papers.

### Exporting BibTeX

When writing a paper in LaTeX, you will need a `.bib` file containing your references.

In Zotero:

1. Select the papers (or a whole collection) you want to export.
2. Right-click and choose **Export Collection**.
3. Select **BibTeX** as the format and save the `.bib` file.

Alternatively, use the [Better BibTeX](https://retorque.re/zotero-better-bibtex/) plugin,
which keeps an auto-updated `.bib` file linked to your Zotero library, very convenient for active writing projects.

---

## Other reference managers

Zotero is a solid default, but alternatives exist:

| Tool | Notes |
|---|---|
| [Mendeley](https://www.mendeley.com) | Free, owned by Elsevier. Good PDF annotation. Institutional accounts are common. |
| [JabRef](https://www.jabref.org) | Open-source, BibTeX-native. Good if you prefer to manage `.bib` files directly. |
| [Papers](https://www.papersapp.com) | Polished interface, Mac and iOS focus. Paid. |
| Manual `.bib` file | Works, but scales poorly and has no annotation or search. |

Ask your group what they use. Sharing a group Zotero library (Zotero Groups feature) is common in some labs.

---

## Annotating PDFs

Reading on screen with annotations is more efficient than printing.

Most reference managers include basic annotation (highlighting, sticky notes).
For more powerful annotation:

- **Zotero's built-in PDF reader** (version 6+) supports highlights and notes that sync with your library.
- **[Okular](https://okular.kde.org)** (Linux): free, excellent for annotation.
- **[PDF Expert](https://pdfexpert.com)** (Mac/iOS): paid, very polished.
- **[Adobe Acrobat Reader](https://www.adobe.com/acrobat/pdf-reader.html)**: free version supports basic highlighting.

Whatever tool you use, the key habit is to add a brief note when you highlight: not just a yellow stripe, but a word or two about why the passage mattered.

---

## Building a reading list

Tracking what you intend to read is as important as tracking what you have read.

Simple approaches that work:

- A `to-read` tag in Zotero.
- A plain text or Markdown file listing paper identifiers with a sentence on why each is relevant.
- A shared document with your supervisor, reviewed in meetings.

The right system is one you will actually use.
Start simple and add complexity only when you feel the need.

---

## Keeping your library healthy

A reference library is only useful if it stays accurate.

A few habits that help:

- **Save immediately**: add a paper to Zotero when you first open it, not after you read it. Papers you intend to save later often disappear.
- **Check metadata on import**: ArXiv metadata is usually correct, but author names and titles occasionally need fixing.
- **Note why you saved it**: even one sentence reminds you why a paper was relevant when you come back to it months later.
- **Prune occasionally**: if a paper turned out to be irrelevant, removing it keeps searches clean.

!!! tip "Your reference library is a long-term asset"
    The library you build during your PhD or first research project will still be useful years later.
    The few minutes it takes to file a paper properly are worth it.
