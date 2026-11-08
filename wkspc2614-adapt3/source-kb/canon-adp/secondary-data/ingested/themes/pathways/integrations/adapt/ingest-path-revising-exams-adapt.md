---
document:  integration: how ADAPT uses the Revising and Exams pathway
core:      `pathways/ingest-path-revising-exams.md` 0.1.1 (`ing:doc:pathway-revising-exams`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.1, 4 October 2026, 10:37, core pointer (ing N-0119); 0.1.0, 4 October 2026, 10:06 (ing N-0114)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror (`adp/adp-mirror/`, generated from `d9cf3af`); not evidence of repo state
---

# Revising and Exams in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 8, "Revising & Exams", chapter 13 | `catalogue/context/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers, focus understanding exams and the need for strategy, building a revision strategy, active techniques and exam-day performance | `catalogue/context/pathways/revising-exams.json` | all `planned`; no course slug; voice band "§16 Beginner (bands 2-4, default). Provisional: confirm at pathway pressure-test." |
| The teaching prose | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 8, with its flag | draft, for SME review |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053): four cards, one introduced, three extended, none developed | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 7 patterns for this pathway | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 8"; the core uses only `path:revising-exams`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "Revising & Exams: <Tier> Stage" (TN-1), from a shell and subject context packs (PKS-1). None built in the mirror.
2. **Voice band.** Introductory, Intermediate and Advanced anchored to tier specification section 16, bands 2 to 4, default; provisional until the pressure-test (`pathway-tier-mapping.md`, Pathway 8).
3. **Pressure-test first.** The mapping flags the pathway as less writing-centric and asks for a pressure-test before building (CLAUDE.md guardrail).
4. **Context coupling.** The form of exam, past papers, exam regulations and support for exam anxiety are module and institution specific: each context pack needs its exam forms and its support routes (PKS-1). Exams thin out in some disciplines; a pack for a coursework-only programme may not need this pathway.
5. **Media and interaction.** Self-testing is the pathway's best-evidenced technique; Adapt's question components can model retrieval practice inside the course itself, not only describe it. Candidate components belong to the component register, not here.
6. **Cross-links.** Exams as one form of assessment link to Understanding Learning, Assessment and Feedback (Pathway 2); anxiety and resilience to Starting, Progressing and Succeeding (Pathway 1); essay exams to Academic Writing (Pathway 6). The catalogue's `routes` are null.
7. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards. No Intermediate card; the core proposes c1, a revision strategy card (core Part E item 3), for Abbott and then nts to land in `path`.
2. Key theory open (core Part E item 4); once ruled, the uningested sources go to META's ing as a handover.
3. The book's visual, auditory and kinaesthetic framing as learning preferences conflicts with the learning styles research (core Part E item 6); the courses should not teach preference matching until ruled.
4. Benchmark evidence for the cards (adp-0212's drafts): `/04` 23 chunks across 20 texts; `/03` 21 across 18; `/02` 2 across 2; `/01` 2 across 1. Exam vocabulary in benchmarks is mostly about assessment design, not student revision.

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 7 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\bexamination\w*
\bexam\b
\bexams\b
\brevision\b
\brevising[\s-]+for\b
\bunseen\b
\btimed[\s-]+assessment\w*
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): no change to this pathway is known in ing's files; the 9 corrected patterns are not identified (RJ-0031's report is not held here). `\brevision\b` will also match revision in the sense of revising a draft or a curriculum.

## Sources

ADAPT's own files at the paths above, read in the Project mirror; the card drafts and their benchmark evidence from `mta-nts-ho-adp-nts-0007` (`adp-0212-capability-cards.md`); the tier notes from `adp-relay/threads/prm/reviews/adp-0213-tier-notes.json`; ADAPT's registers as of 4 October 2026, 10:06.

---

## Change notes
- 0.1.1: 4 October 2026, 10:37: core pointer to 0.1.1 (ing N-0119).
- 0.1.0: 4 October 2026, 10:06: created with the core 0.1.0 (ing N-0114).
