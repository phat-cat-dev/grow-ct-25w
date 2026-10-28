---
document:  integration: how ADAPT uses the Researching and Research Methods pathway
core:      `pathways/ingest-path-researching-research-methods.md` 0.1.16 (`ing:doc:pathway-researching-research-methods`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.9, 4 October 2026, 10:37, core pointer (ing N-0119); 0.1.8, 4 October 2026, 10:03, core pointer (ing N-0113); 0.1.7, 3 October 2026, 11:10, benchmark search patterns (ing N-0100); 0.1.6, 3 October 2026, 06:19, report writing amended (ing N-0093); 0.1.5, 3 October 2026, 06:04, report writing (ing N-0091); 0.1.4, 3 October 2026, 05:52, core pointer updated (ing N-0089); 0.1.3, 3 October 2026, 04:41, renamed; core pointer updated (ing N-0083); 0.1.2, 2 October 2026, 22:07 (ing N-0028; G-ing-0021); 0.1.1, 21:51 (ing N-0026; G-ing-0018); 0.1.0, 21:45 (ing N-0024; G-ing-0014)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror at commit `89ee9c4`; not evidence of repo state
---

# Researching and Research Methods in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 9, chapters [3, 5, 9, 10] | `catalogue/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers: focus, voice band, pointer to the teaching prose | `catalogue/pathways/researching-research-methods.json` | all three `planned`, no course slug |
| The teaching prose | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 9 | draft, for SME review |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053); `adp-relay/threads/prm/reviews/adp-0213-tier-notes.json` | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 15 patterns for this pathway | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 9"; the core uses only `path:researching-research-methods`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "Researching & Research Methods: <Tier> Stage" (TN-1), from a shell and subject context packs (PKS-1). None built.
2. **Voice band, up-skewed.** Bands 3 to 5: Introductory takes the voice specification's Intermediate band, Intermediate its Advanced band, Advanced its Masters band (`pathway-tier-mapping.md`, Pathway 9; tier specification section 3, marked "illustrative, confirm at authoring"). It is the only pathway not on the default anchor.
3. **Outcome verbs.** From the anchored band of `reference/excelling-voice-specification.md` section 16: Introductory from Intermediate (analyse, compare, apply, evaluate and so on), Intermediate from Advanced, Advanced from Masters.
4. **Hand-off from Academic Writing.** The research proposal, literature review and report moved out of Pathway 6 into this pathway in the model's v2; ADAPT's Academic Writing courses must not teach them.
5. **Shared ethics with Referencing.** Pathway 4's Advanced tier covers integrity values and plagiarism; this pathway covers ethics in practice. ADAPT's courses cross-reference, never duplicate.
6. **Benchmark mapping.** The 15 patterns are the word test that tags a QAA benchmark statement `direct` for this pathway (QV-TAG-2 part (e)); three of them (`qualitative`, `quantitative`, `empirical`) are broad, and may tag statements that are not about research skills.
7. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards. Abbott added two at 21:51 (D-ing-0007 (a)): the proposal as a whole document (Intermediate) and methodology (Advanced); for nts to land in `path` (ing N-0026).
2. The Researching voice-band anchor is "illustrative, confirm at authoring": not yet confirmed.
3. The up-skewed Introductory tier stays (D-ing-0009 (c), 22:07); ADAPT's catalogue and course pages should send a learner new to research to Finding & Using Sources and Criticality first. Where that pointer lives (the catalogue's `routes`, W-OPEN's copy or both) is ADAPT's to decide.
4. Report writing (D-ing-0024 (a), 06:04): Pathway 9's courses teach the research and laboratory report; the term list's `report writing` pattern now spans Pathways 9 and 11, for RJ-0033 when it commits v2. (ing N-0091). [Amended 06:19, D-ing-0044: the term list's `report writing` pattern now spans Pathways 9, 10 and 11.]

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 15 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\bresearch[\s-]+method\w*
\bresearch[\s-]+design\b
\bresearch[\s-]+ethic\w*
\bresearch[\s-]+skill\w*
\bresearch[\s-]+project\w*
\bresearch[\s-]+question\w*
\bmethods[\s-]+of[\s-]+enquiry\b
\bmethods[\s-]+of[\s-]+inquiry\b
\bempirical\b
\bdata[\s-]+analys\w*
\bdata[\s-]+collection\b
\bqualitative\b
\bquantitative\b
\bhypothes\w*
\bdissertation\w*
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): the 9 corrected patterns are not identified in ing's files (RJ-0031's report is not held here).

## Sources

ADAPT's own files at the paths above, read in the Project mirror at `89ee9c4`; ADAPT's registers as of 2 October 2026, 21:40.

---

## Change notes
- 0.1.9: 4 October 2026, 10:37: core pointer to 0.1.16 (ing N-0119).
- 0.1.8: 4 October 2026, 10:03: core pointer to 0.1.15 (ing N-0113).
- 0.1.7: 3 October 2026, 11:10: core pointer to 0.1.14; section 4, the benchmark search patterns, v1.0 and the v2 changes known (D-ing-0050; ing N-0100).
- 0.1.6: 3 October 2026, 06:19: core pointer to 0.1.13; point 4 amended (D-ing-0044; ing N-0093).
- 0.1.5: 3 October 2026, 06:04: core pointer; report writing (D-ing-0024 (a); ing N-0091).
- 0.1.4: 3 October 2026, 05:52: core pointer to 0.1.11 (ing N-0089).
- 0.1.3: 3 October 2026, 04:41: file renamed from `adp-ing-pd-pathway-researching-research-methods-adapt.md` to `ingest-path-researching-research-methods-adapt.md`; core pointer to `ingest-path-researching-research-methods.md` 0.1.10 (ing N-0083).
- 0.1.2: 2 October 2026, 22:07: point 3 settled by D-ing-0009 (c) (ing N-0028; G-ing-0021).
- 0.1.1: 2 October 2026, 21:51: point 1 updated for D-ing-0007 (a) (ing N-0026; G-ing-0018).
- 0.1.0: 2 October 2026, 21:45: created with the core 0.1.0 (ing N-0024; G-ing-0014).
