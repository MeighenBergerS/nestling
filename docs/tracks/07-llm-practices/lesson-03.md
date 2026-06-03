# Lesson 03: LLMs for Writing

LLMs can help with almost every stage of scientific writing.
They can expand a bullet list into a draft paragraph, tighten verbose prose,
suggest transitions, and flag unclear sentences.
Used well, they make you a more efficient writer.
Used carelessly, they can compromise the integrity of your work and erode your
own ability to write.

This lesson draws a clear line between assistance and authorship, and gives you
practical habits for staying on the right side of it.

---

## Drafting versus authoring

**Authoring** means generating the ideas, the arguments, the structure, and the
scientific judgements that constitute the work.

**Drafting** means putting those ideas into well-formed prose.

An LLM can help with drafting. It cannot author your work.
If you give an LLM your data, your conclusions, and your outline, and it returns
a polished paragraph, you drafted with assistance. You are still the author.
If you ask an LLM "what should I conclude from these results?" and adopt its answer,
the LLM has contributed to the intellectual content of the work, which is a different
matter entirely.

The practical test: **can you defend every claim in the text without the LLM?**
If the answer is no, you have moved from drafting assistance into something that
requires disclosure or rethinking.

---

## Academic integrity

Different institutions and publishers have different policies on LLM use.
Know the rules that apply to your work before you use any AI assistance.

As of 2025, common positions include:

| Context | Typical policy |
|---------|---------------|
| PhD thesis | Varies: many institutions prohibit or require disclosure; check your university's policy |
| Journal submission | Most major journals require disclosure; some prohibit LLM use for manuscript text |
| Conference papers | Policies vary by venue; NeurIPS, ICML, and others require disclosure |
| Grant applications | Most funding agencies prohibit LLM-generated text in proposals |
| Internal reports and notes | Generally unrestricted, but be consistent |

**When in doubt, disclose.**
A note that "portions of this manuscript were drafted with LLM assistance and subsequently
revised by the authors" is honest and increasingly standard.
Submitting LLM-generated text without disclosure where it is required is a form of
academic misconduct.

---

## Where LLMs genuinely help

### Overcoming the blank page

The hardest part of writing is often starting.
Give the LLM your outline, key points, and the intended audience, and ask for a first draft.
You will almost certainly rewrite most of it, but having something to react to is faster
than drafting from nothing.

### Tightening prose

Paste a paragraph and ask: "Make this more concise without losing any meaning."
Or: "This sentence is unclear. Suggest three alternatives."
Use the suggestions as options to evaluate, not replacements to accept.

### Consistency and register

Ask the LLM to check that terminology is used consistently throughout a section,
or that the register is appropriate for the intended audience (general public vs specialists).

### Translation

Non-native English writers can use LLMs to improve grammar and fluency.
This is generally considered acceptable, in the same category as using a spell-checker,
provided the scientific content is your own.

### Explaining to a different audience

Ask the LLM to rewrite a technical paragraph for a general audience, or for a specific
journal's style. Use the output as a starting point, not as final copy.

---

## Where LLMs fail for writing

### Factual accuracy

LLMs will silently introduce incorrect claims.
A fluent sentence with a wrong number, a misattributed idea, or a subtly wrong summary
of a paper can survive editing if you are not reading for content.
Always verify factual claims independently.

### Voice and style

LLMs produce a characteristic style: well-structured, hedged, and slightly formal.
Over time, relying on LLM drafts can flatten your own voice.
Your writing is part of your scientific identity. The goal is to improve your writing,
not to outsource it.

### Hallucinated citations and claims

An LLM asked to draft a related-work section may insert plausible-sounding citations
that do not exist.
Never include a citation in your text unless you have personally verified that the source
exists and says what you claim it says.
See [Lesson 04](lesson-04.md) for more on this.

### Long documents

LLM performance degrades on very long documents.
For a paper-length draft, work section by section rather than submitting the whole
document at once.

---

## A practical workflow

1. **You write the outline.** The structure and the argument are yours.
2. **You write bullet-point notes for each section.** These are the ideas the section
   must convey.
3. **Ask the LLM to draft the section from your notes.**
4. **Read the draft critically.** Every sentence should say something you intended.
   Every factual claim should be one you can verify.
5. **Rewrite in your own voice.** Treat the LLM draft as a rough starting point.
6. **Never include a citation the LLM generated** without checking the source yourself.

---

## Industrial context: LLMs in professional writing

**Disclosure norms.** Most professional and academic contexts now require disclosure
of LLM use. Tools like Turnitin and GPTZero are used by journals and institutions to
detect LLM-generated text, with varying accuracy. The safe strategy is transparent
disclosure.

**Brand voice and consistency.** In industry, organisations use LLMs with detailed
style guides and system prompts to maintain a consistent brand voice across documents.
As a researcher, your equivalent is your field's conventions and your own established
voice, which an LLM can learn if you give it examples.

**Fact-checking pipelines.** Serious media and publishing organisations run LLM-assisted
drafts through fact-checking pipelines before publication. For research papers, the
peer review process is not designed to catch LLM-introduced errors. That responsibility
sits with the authors.

**Human-in-the-loop for consequential text.** In regulated industries (medical device
documentation, legal filings, financial disclosures), LLM-generated text is always
reviewed and approved by a human before use. Research papers are consequential text.
Apply the same standard.

---

## Checklist

- [ ] I know my institution's and target journal's policy on LLM use.
- [ ] Every idea and argument in my text originated with me.
- [ ] I have verified every factual claim and citation independently.
- [ ] I have disclosed LLM assistance where required.
- [ ] I have read every sentence for accuracy, not just fluency.
- [ ] I could defend every claim in a discussion without referring to the LLM.

---

## What to read next

[Lesson 04](lesson-04.md) is specifically about citations: why LLM-generated references
must never be used without verification, and how to use LLMs safely for literature search.
