---
document:  integration: how ADAPT uses the Self-Development pathway
core:      `pathways/ingest-path-self-development.md` 0.1.0 (`ing:doc:pathway-self-development`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.0, 4 October 2026, 13:37 (ing N-0146)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror (`adp/adp-mirror/`, generated from `b22b1c3`); not evidence of repo state
---

# Self-Development in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, a fourteenth pathway, "Self-Development" | `catalogue/context/pathways.json` | not in the catalogue: added by Abbott on 4 October 2026 (D-ing-0064); a catalogue entry is owed |
| Its three tiers | `catalogue/context/pathways/self-development.json` | no file; the tiers are ing's draft (the core's A3; the card integration's section 4a) |
| The teaching prose | `docs/curriculum/pathway-tier-mapping.md` | no Pathway 14 section; ing's draft tier text is in the card integration's section 4a, for Abbott to rule |
| The capability cards | `integrations/cards/ing-cards-self-development.md` 0.1.0 | nine proposed cards, i1 to e3 (D-ing-0060, D-ing-0064); no adp-0212 drafts exist for this pathway |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0 | no entry; candidate patterns in section 4 |

ADAPT would call it "Pathway 14"; the core uses only `path:self-development`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "Self-Development: <Tier> Stage" (TN-1), from a shell and context packs (PKS-1), once the catalogue holds the pathway. None planned yet.
2. **The academic practitioner first.** These courses are for the student; the professional practitioner's version follows (D-ing-0064), and fits context packs for vocational subjects (nursing, teaching, social work).
3. **Assessment.** A learner's identity or values are never assessed as the person; tasks assess the practice of naming, organising, articulating and examining them (the core's A5d and B5). This bears on summative parity (tier specification section 7).
4. **Cross-links.** Starting, Progressing and Succeeding (Pathway 1) for disposition and graduate identity; Reflective Practice (10) for the method; Referencing (4) for integrity's values; Work-Based Learning (11) for identity in practice. A course here would cross-reference, not repeat, their material.
5. **Practice connection** as for every pathway (D-0047).

## 3. Points open for ADAPT

1. A catalogue entry, a tier map section and a voice-band anchor for Pathway 14, for Abbott to rule; ing's draft is in the card integration.
2. Key theory open (core Part E item 4); the uningested sources (Baxter Magolda, Holmes, Wenger, Maslow) go to META's ing as a handover once ruled.
3. Benchmark evidence: none searched (D-ing-0063 open).
4. Care in task design: examining one's identity and background can touch difficult personal ground (the core's A7b).

## 4. Benchmark search patterns

None: the term list v1.0 holds thirteen pathways. Candidate patterns for a term list entry, ing's proposal, untested against the benchmarks:

```
\bidentit\w*
\bvalues?\b
\breflexiv\w*
\bself[\s-]+(awareness|development|authorship|reflection)\b
\bpersonal[\s-]+development\b
\bprofessional[\s-]+identit\w*
```

`\bvalues?\b` will match statistical and moral senses alike and would need the mapper's reading; `\bidentit\w*` will match subject content (national identity, identity politics). Both are candidates for the provisional list (D-0031's approach).

## Sources

ADAPT's own files at the paths above, read in the Project mirror; the card integration and the core; ADAPT's registers as of 4 October 2026, 13:37.

---

## Change notes
- 0.1.0: 4 October 2026, 13:37: created with the core 0.1.0 (ing N-0146).
