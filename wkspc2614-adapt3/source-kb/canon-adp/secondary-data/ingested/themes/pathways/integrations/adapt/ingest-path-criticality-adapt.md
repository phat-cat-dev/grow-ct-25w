---
document:  integration: how ADAPT uses the Criticality pathway
core:      `pathways/ingest-path-criticality.md` 0.1.13 (`ing:doc:pathway-criticality`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.11, 4 October 2026, 10:37, core pointer (ing N-0119); 0.1.10, 4 October 2026, 10:03, core pointer (ing N-0113); 0.1.9, 3 October 2026, 11:10, benchmark search patterns (ing N-0100); 0.1.8, 3 October 2026, 05:52, core pointer updated (ing N-0089); 0.1.7, 3 October 2026, 04:41, renamed; core pointer updated (ing N-0083); 0.1.6, 3 October 2026, 00:21, core pointer updated (ing N-0058; G-ing-0087); 0.1.5, 2 October 2026, 23:51, core pointer updated (ing N-0052; G-ing-0071); 0.1.4, 2 October 2026, 23:38, points 2 and 3 settled (ing N-0050; G-ing-0063); 0.1.3, 2 October 2026, 23:16, core pointer updated (ing N-0045; G-ing-0053); 0.1.2, 2 October 2026, 23:14, core pointer updated (ing N-0044; G-ing-0050); 0.1.1, 2 October 2026, 23:10, point 1 updated (ing N-0043; G-ing-0047); 0.1.0, 2 October 2026, 23:02 (ing N-0041; G-ing-0044)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror at commit `89ee9c4`; not evidence of repo state
---

# Criticality in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 5, chapters [8]; `routes` feeds and drawsOn both null | `catalogue/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers | `catalogue/pathways/criticality.json` | `planned` |
| The teaching prose | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 5 | draft, for SME review |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053) | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 7 patterns for this pathway | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 5"; the core uses only `path:criticality`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "Criticality: <Tier> Stage" (TN-1), from a shell and subject context packs (PKS-1). None built.
2. **Voice band.** Default anchor, bands 2 to 4, with no provisional mark (`pathway-tier-mapping.md`, Pathway 5).
3. **Overlap with Academic Writing.** The mapping says the Advanced tier bridges into Academic Writing and the "writing critically" material is shared. Settled by D-ing-0020 (a): the Criticality courses teach the critical edge; the Academic Writing courses apply it and refer here.
4. **On-ramp.** D-ing-0009 (c) makes Criticality, with Finding and Using Sources, the start for a learner new to research.
5. **Benchmark mapping.** The 7 patterns are the word test for QV-TAG-2 part (e). They are among the broadest in the list: `critical`, `evaluat`, `analys` and `synthesi` appear in most benchmark statements' skills sections, and the draft card evidence already shows 866 chunks across 54 texts for `criticality/01`. Whether D-0028's v2 narrows them is unchecked here.
6. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards. Abbott added two at 23:10 (D-ing-0016 (a)): "Apply critical thought to the choices made when searching, reading and planning" (Introductory) and "Form and justify judgements on the relative importance of factors" (Advanced); for nts to land in `path` (ing N-0043).
2. The split of the Advanced material with Academic Writing: settled (D-ing-0020 (a), 23:38).
3. Whether the catalogue's null `routes` should carry the mapping's cross-link to Academic Writing.
4. The broad term patterns, for RJ-0033 when it commits v2.

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 7 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\bcritical\w*
\bcritique\w*
\bevaluat\w*
\banalys\w*
\banalyz\w*
\bapprais\w*
\bsynthesi\w*
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): holds `critical*`, `analys*`, `evaluat*` provisional (over 10% of chunks), to be narrowed after the pilot if the mapper rejects many hits (D-0031); the 9 corrected patterns are not identified in ing's files (RJ-0031's report is not held here).

## Sources

ADAPT's own files at the paths above, read in the Project mirror at `89ee9c4`; the card drafts and their benchmark evidence from `mta-nts-ho-adp-nts-0007` (`adp-0212-capability-cards.md`); the tier notes from `adp-relay/threads/prm/reviews/adp-0213-tier-notes.md`; ADAPT's registers as of 2 October 2026, 23:02.

---

## Change notes
- 0.1.11: 4 October 2026, 10:37: core pointer to 0.1.13 (ing N-0119).
- 0.1.10: 4 October 2026, 10:03: core pointer to 0.1.12 (ing N-0113).
- 0.1.9: 3 October 2026, 11:10: core pointer to 0.1.11; section 4, the benchmark search patterns, v1.0 and the v2 changes known (D-ing-0050; ing N-0100).
- 0.1.8: 3 October 2026, 05:52: core pointer to 0.1.10 (ing N-0089).
- 0.1.7: 3 October 2026, 04:41: file renamed from `adp-ing-pd-pathway-criticality-adapt.md` to `ingest-path-criticality-adapt.md`; core pointer to `ingest-path-criticality.md` 0.1.9 (ing N-0083).
- 0.1.6: 3 October 2026, 00:21: core pointer to 0.1.6 (ing N-0058; G-ing-0087).
- 0.1.5: 2 October 2026, 23:51: core pointer to 0.1.5 (ing N-0052; G-ing-0071).
- 0.1.4: 2 October 2026, 23:38: core pointer to 0.1.4; the split with Academic Writing settled (ing N-0050; G-ing-0063).
- 0.1.3: 2 October 2026, 23:16: core pointer to 0.1.3 (ing N-0045; G-ing-0053).
- 0.1.2: 2 October 2026, 23:14: core pointer to 0.1.2 (ing N-0044; G-ing-0050).
- 0.1.1: 2 October 2026, 23:10: point 1 updated for D-ing-0016 (a) (ing N-0043; G-ing-0047).
- 0.1.0: 2 October 2026, 23:02: created with the core 0.1.0 (ing N-0041; G-ing-0044).
