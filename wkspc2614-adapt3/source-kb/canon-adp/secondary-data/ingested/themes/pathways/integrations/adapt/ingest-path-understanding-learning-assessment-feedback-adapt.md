---
document:  integration: how ADAPT uses the Understanding Learning, Assessment and Feedback pathway
core:      `pathways/ingest-path-understanding-learning-assessment-feedback.md` 0.1.8 (`ing:doc:pathway-understanding-learning-assessment-feedback`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.8, 4 October 2026, 10:37, core pointer (ing N-0119); 0.1.7, 4 October 2026, 10:19, core pointer (ing N-0115); 0.1.6, 4 October 2026, 10:03, core pointer (ing N-0113); 0.1.5, 3 October 2026, 11:10, benchmark search patterns (ing N-0100); 0.1.4, 3 October 2026, 05:52, core pointer updated (ing N-0089); 0.1.3, 3 October 2026, 05:28, point 2 refined (ing N-0088; G-ing-0181); 0.1.2, 3 October 2026, 05:27, points 1 and 2 (ing N-0087; G-ing-0178); 0.1.1, 3 October 2026, 05:11, point 1 settled (ing N-0086; G-ing-0175); 0.1.0, 3 October 2026, 04:48 (ing N-0084; G-ing-0172)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror at commit `89ee9c4`; not evidence of repo state
---

# Understanding Learning, Assessment and Feedback in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 2, "Understanding Learning, Assessment & Feedback", chapters [3, 4, 5, 6]; `routes` feeds and drawsOn both null | `catalogue/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers | `catalogue/pathways/understanding-learning-assessment-feedback.json` | all `planned`; no course slug |
| The teaching prose | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 2 | draft, for SME review |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053): six cards, three introduced, three developed, none extended | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 26 patterns for this pathway | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 2"; the core uses only `path:understanding-learning-assessment-feedback`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "Understanding Learning, Assessment & Feedback: <Tier> Stage" (TN-1), from a shell and subject context packs (PKS-1). None built in the mirror.
2. **Voice band.** Introductory, Intermediate and Advanced anchored to tier specification section 16, bands 2 to 4, default (`pathway-tier-mapping.md`, Pathway 2).
3. **Context coupling.** Marking criteria, mark bands, module handbooks and the virtual learning environment are institutional: the book's Table 5.1 is simplified Level 4 criteria, and the courses need each context pack's own criteria and handbook conventions (PKS-1).
4. **Cross-links.** The self-regulation mechanics here are the operational counterpart to Pathway 1's dispositional material; Reflective Practice (Pathway 10) is the engine beneath the feedback cycle and self-assessment. The catalogue's `routes` are null, so the links live only in the prose.
5. **Benchmark mapping.** The 26 patterns are the word test for QV-TAG-2 part (e). `assessment\w*`, `feedback` and `marking` are broad; `\b\w+[\s-]+based[\s-]+learning\b` also matches "work-based learning", Pathway 11's ground. The draft card evidence ranges from 244 chunks across 51 texts (`/03`, learning outcomes) to 1 chunk in 1 text (`/06`, feedback into an action plan). Whether D-0028's v2 changes them is unchecked here.
6. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards. Abbott added three at Advanced at 05:10 (D-ing-0041 (a)): "Assess one's own and peers' work against marking criteria", "Use feedback diagnostically and in dialogue with tutors to sustain development across a degree" and "Adapt to the demands of different types of assessment" (renamed by D-ing-0042); for nts to land in `path` (ing N-0086).
2. Theory (D-ing-0042, 05:27): no single key theory; every theorist the book cites in Chapters 3 to 6 and the field's main accounts of assessment and feedback cycles, by strand (core A9); the uningested ones queued at META's ing (`adp-ing-ho-mta-ing-0011`). Refined by D-ing-0043 (05:28): the courses' spine is Zimmerman for learning, Biggs's constructive alignment for the learning, assessment and feedback cycle, Carless and Boud as the key theory for feedback literacy, and Nicol and Macfarlane-Dick to explain the cycle.
3. Whether the catalogue's null `routes` should carry the mapping's cross-links.
4. The term pattern for "-based learning" and its overlap with Pathway 11, for RJ-0033 when it commits v2.
5. Cardiff Met's generic assessment criteria are now ingested at META (`std:doc:cardiffmet-generic-2020-assesscriteria`, SHA-256 prefix ce6386ad868a), with Bristol's (`std:doc:bristol-generic-2024-assesscriteria`): the context packs' marking criteria (point 3 of section 2) can draw on them instead of the book's simplified Table 5.1.

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 26 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\bown[\s-]+learning\b
\bindependent[\s-]+learning\b
\bself[\s-]+directed[\s-]+learning\b
\blearning[\s-]+outcome\w*
\blearning[\s-]+theor\w*
\bself[\s-]+regulat\w*
\bassessment\w*
\bsummative\b
\bformative\b
\bfeedback\b
\bfeed[\s-]+forward\b
\bassessment[\s-]+criteria\b
\bmarking[\s-]+criteria\b
\bgrading[\s-]+criteria\b
\bassessment[\s-]+brief\w*
\bassignment[\s-]+brief\w*
\bmarking[\s-]+scheme\w*
\bmark[\s-]+scheme\w*
\brubric\w*
\bgrade[\s-]+descriptor\w*
\bassessment[\s-]+task\w*
\bassessment[\s-]+literacy\b
\bmarking\b
\bgrading\b
\bPBL\b
\b\w+[\s-]+based[\s-]+learning\b
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): drops `grading criteria`; holds `assessment*` provisional (over 10% of chunks), to be narrowed after the pilot if the mapper rejects many hits (D-0031); the 9 corrected patterns are not identified in ing's files (RJ-0031's report is not held here).

## Sources

ADAPT's own files at the paths above, read in the Project mirror at `89ee9c4`; the card drafts and their benchmark evidence from `mta-nts-ho-adp-nts-0007` (`adp-0212-capability-cards.md`); the tier notes from `adp-relay/threads/prm/reviews/adp-0213-tier-notes.md`; ADAPT's registers as of 3 October 2026, 04:48.

---

## Change notes
- 0.1.8: 4 October 2026, 10:37: core pointer to 0.1.8 (ing N-0119).
- 0.1.7: 4 October 2026, 10:19: core pointer to 0.1.7 (ing N-0115).
- 0.1.6: 4 October 2026, 10:03: core pointer to 0.1.6 (ing N-0113).
- 0.1.5: 3 October 2026, 11:10: core pointer to 0.1.5; section 4, the benchmark search patterns, v1.0 and the v2 changes known (D-ing-0050; ing N-0100).
- 0.1.4: 3 October 2026, 05:52: core pointer to 0.1.4; point 5, Cardiff Met's assessment criteria at META (ing N-0089).
- 0.1.3: 3 October 2026, 05:28: core pointer to 0.1.3; point 2 refined (D-ing-0043; ing N-0088; G-ing-0181).
- 0.1.2: 3 October 2026, 05:27: core pointer to 0.1.2; points 1 and 2 for D-ing-0042 (ing N-0087; G-ing-0178).
- 0.1.1: 3 October 2026, 05:11: core pointer to 0.1.1; point 1 settled (D-ing-0041 (a); ing N-0086; G-ing-0175).
- 0.1.0: 3 October 2026, 04:48: created with the core 0.1.0 (ing N-0084; G-ing-0172).
