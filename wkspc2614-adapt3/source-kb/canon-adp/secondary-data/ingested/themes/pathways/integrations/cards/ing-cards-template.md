---
document:  card integration: golden template
version:   0.1.0, 4 October 2026, 12:29 (D-ing-0061; ing N-0129)
model:     `ing-cards-reflective-practice.md` 0.2.0, the pilot this template is taken from
owner:     adp ing (drafts); the model's author rules the cards
status:    template; not a record
---

# Card integration: golden template

The shape every pathway's card file takes (D-ing-0061). Copy it to `ing-cards-<pathway-id>.md`, keep every heading in this order, fill each section from the sources it names and delete the guidance in italics. A section with nothing to put in it stays, with a line saying why. The file speaks to the pathway's core and is not part of it (D-ing-0055).

**Rules for the whole file**
- Nine cards, three at each tier, ids `<pathway-id>/i1` to `/e3` (D-ing-0060). The letter is the tier note: **i**, introduced, the Introductory course; **d**, developed, the Intermediate course; **e**, extended, the Advanced course.
- Within each tier, card 1 is the most concrete (factual or conceptual), card 2 a procedure, card 3 the most metacognitive; across the tiers the weight moves up, so `e3` is the top of the pathway (D-ing-0060).
- Indicative levels by position, loose and never the anchor: i1 L3, i2 L4, i3 L5; d1 L4, d2 L5, d3 L6; e1 L5, e2 L6, e3 L7 (Abbott, 12:05).
- A card new in this file, or moved or merged from another, carries a Note row saying so and is proposed until the model's author rules it.
- Name no project or product: the tier map is "the pathway model as used" (N-0124).
- Quotations from the guide stay within 25 words, each with its page checked against the guide's Markdown copy; other authors are paraphrased from META's runs, each with its run id and SHA-256 prefix, never quoted.
- Every verb taken from a structured statement is captured with the statement (D-ing-0058).
- Old ids appear only in the change notes' crosswalk.

---
document:  card integration: <Pathway name>
core:      `pathways/ingest-path-<pathway-id>.md` <version> (`ing:doc:pathway-<pathway-id>`), A10 `competencies`, joined by card id
owner:     adp ing (drafts); `path` holds the cards (nts); the model's author rules them (D-0058)
version:   0.1.0, <date>, <time> (ing N-<nnnn>)
status:    working draft; not ingested; not a record
---

# <Pathway name>: the cards in context

*One paragraph: what the file holds and that it speaks to the core (D-ing-0055).*

Sources: *the cards and their theory and frameworks from the core's A10; vocabulary from `ing-card-vocabulary.json`; book topics from the guide's Markdown copy, pages checked; benchmark evidence from adp-0212's card drafts, or ing's own search, labelled as such; other authors from META's INGEST runs in UNI's `library/ingested/theory/`.*

How the benchmark evidence is read: **skill** where the passage describes the learner doing the capability; **theme** where the practice appears only as an item in a list of attributes, methods or assessment types.

## 1. The cards

*One line on the tiers and the order (the rules above). Then one block per card, i1 to e3, in that order.*

### `<pathway-id>/i1` (introduced) <statement>

| | |
|---|---|
| Verbs | *the statement's verbs* |
| Measures | *the qualifiers that say how well or how much* |
| Keywords | *the nouns and phrases a searcher would use* |
| Book topics | *the guide's topics under the card, with pages and short quotes* |
| Benchmark evidence | *passages / texts, of 54; each extract read as skill or theme; "not searched" if none* |
| Pedagogy | *the theory beneath the card: run ids, or the wanted-source row* |
| Frameworks | *professional and other frameworks, with how far each matches (partial, broader)* |
| Other authors | *how other academic skills authors describe it, paraphrased from META's runs* |
| Note | *only where needed: new, moved, merged or placed from another pathway's text* |

*Repeat for i2, i3, d1, d2, d3, e1, e2, e3.*

## 2. Vocabulary

*One line: each card's own words are in its table; this section reads the vocabulary across the cards, in other sources' statements and in the level descriptors.*

### 2a. Across the cards

*Bullets: the guide's vocabulary against the benchmarks'; skill against theme in the evidence; which cards the guide carries, in part or not at all; what META already holds for the pathway.*

### 2b. Verbs in context (D-ing-0058)

*One paragraph on where the statements come from and how they are read. Data: `verbs-in-context.json`.*

| Card | Verbs | Statement | Statement type | Subject | Read as | How it relates the pathway to the subject |
|---|---|---|---|---|---|---|
| | | | | | | |

*One line: what the verbs show.*

### 2c. qualification-frameworks

*The national level descriptors that speak to this practice, recorded beside the cards, never as their anchor, quoted from META's runs of the FHEQ (`std:doc:qaa-fheq-2024-framework`) and the CQFW (`std:doc:welsh-government-cqfw-2009-framework`) with their current SHA-256 prefixes. Say what the frameworks name and what they do not.*

| Level | Framework and statement | Verbs | How it relates to <the practice> | Loosely, the tier |
|---|---|---|---|---|
| | | | | |

## 3a. Tier statements and the kinds of knowledge

*Loosely level-based statements about the practice at each tier, ing's own, built up from the cards and the knowledge models, read through Anderson and Krathwohl's knowledge dimension (`ing:doc:bloom-anderson-krathwohl-2001`), with Biggs (`ing:doc:constructive-alignment-biggs-1996`) and Marzano and Kendall (`ing:doc:new-taxonomy-marzano-kendall-2007`). Kept beside section 4a, not merged with it (D-ing-0059).*

| Tier | Statement about the practice | Knowledge type | Cognitive process | What changes |
|---|---|---|---|---|
| | | | | |

**How the learner moves to mastery.** *One paragraph: the shift from declarative to procedural to metacognitive knowledge across the tiers for this practice, ending on the core's A11 ladder.*

## 4a. The tier map: the pathway model as used

*The tier map of the pathway model as used, quoted as it stands, built down from the guide; kept beside section 3a, not merged (D-ing-0059). Say that the file is the first of three parts, the Introductory course first. Sources: `pathway-tier-mapping.md` and `catalogue_pathways_<pathway-id>.json`, with the mirror commit read. Leave out the voice-band anchor.*

**The catalogue's tier focus**

| Tier | Focus | Course | Status |
|---|---|---|---|
| Introductory | | | |
| Intermediate | | | |
| Advanced | | | |

**The map's text (Pathway <n>, <Pathway name>)**

> *Source, the three tier paragraphs, progression logic and cross-links, quoted.*

**Where the two directions differ** (ing's reading, recorded, not resolved): *where section 3a and the map place something at different tiers, or "none found".*

## 5. Table of correspondences

*One line: each card with its tier, kind of knowledge and loose indicative level, and the qualification-framework statements at that level from section 2c, by id and a short extract.*

| Card | Tier | Statement | Kind of knowledge | Indicative level | Qualification frameworks at that level |
|---|---|---|---|---|---|
| i1 | Introductory | | | L3 | |
| i2 | Introductory | | | L4 | |
| i3 | Introductory | | | L5 | |
| d1 | Intermediate | | | L4 | |
| d2 | Intermediate | | | L5 | |
| d3 | Intermediate | | | L6 | |
| e1 | Advanced | | | L5 | |
| e2 | Advanced | | | L6 | |
| e3 | Advanced | | | L7 | |

*One line: what the frameworks add or leave out, ing's reading.*

## 6. For review

*Numbered: proposed cards, corrections for the guide's map, searches owed, sources wanted, stale prefixes.*

---

## Change notes
- 0.1.0: <date>, <time>: created from the golden template (D-ing-0061); crosswalk from the core's ids: *old to new, every card* (ing N-<nnnn>).
