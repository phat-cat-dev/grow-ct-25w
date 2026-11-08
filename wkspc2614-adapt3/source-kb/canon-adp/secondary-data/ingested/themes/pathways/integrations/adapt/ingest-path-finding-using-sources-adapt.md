---
document:  integration: how ADAPT uses the Finding and Using Sources pathway
core:      `pathways/ingest-path-finding-using-sources.md` 0.1.11 (`ing:doc:pathway-finding-using-sources`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.9, 4 October 2026, 10:37, core pointer (ing N-0119); 0.1.8, 4 October 2026, 10:03, core pointer (ing N-0113); 0.1.7, 3 October 2026, 11:10, benchmark search patterns (ing N-0100); 0.1.6, 3 October 2026, 05:52, core pointer updated (ing N-0089); 0.1.5, 3 October 2026, 04:41, renamed; core pointer updated (ing N-0083); 0.1.4, 2 October 2026, 22:50, core pointer updated (ing N-0039; G-ing-0041); 0.1.3, 2 October 2026, 22:48, core pointer updated (ing N-0038; G-ing-0038); 0.1.2, 2 October 2026, 22:44, core pointer updated (ing N-0037; G-ing-0036); 0.1.1, 2 October 2026, 22:42, point 1 updated (ing N-0036; G-ing-0032); 0.1.0, 2 October 2026, 22:37 (ing N-0034; G-ing-0029)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror at commit `89ee9c4`; not evidence of repo state
---

# Finding and Using Sources in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 3, chapters [7]; `routes` feeds and drawsOn both null | `catalogue/context/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers | `catalogue/context/pathways/finding-using-sources.json` | `planned` |
| The teaching prose | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 3 | draft, for SME review |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053) | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 8 patterns for this pathway | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 3"; the core uses only `path:finding-using-sources`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "Finding & Using Sources: <Tier> Stage" (TN-1), from a shell and subject context packs (PKS-1). None built.
2. **Voice band.** Default anchor, bands 2 to 4, with no provisional mark (`pathway-tier-mapping.md`, Pathway 3).
3. **Cross-links.** The mapping says the pathway feeds Criticality (evaluating sources), Academic Writing (integrating them) and Researching (the search phase of a project); the catalogue's `routes` are null, so the links live only in the prose. D-ing-0009 (c) makes it, with Criticality, the on-ramp for a learner new to research.
4. **Library context.** "The library discovery service" is generic in the core; each institution's pack names its own service, subject guides and databases (Phase D).
5. **Benchmark mapping.** The 8 patterns are the word test for QV-TAG-2 part (e). Several are broad (`source`, `search`, `reading`, `literature`) and may tag statements that are not about finding sources, for example a benchmark's "sources of error" or "reading" as a skill in a language subject; whether D-0028's v2 narrows them is unchecked here.
6. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards. Abbott added one at 22:42 (D-ing-0012 (a)): "Follow a staged search strategy, starting from the reading list and what one already knows" (Introductory), beside `finding-using-sources/02`; for nts to land in `path` (ing N-0036).
2. Whether the catalogue's null `routes` should carry the mapping's cross-links.
3. The broad term patterns, for RJ-0033 when it commits v2.

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 8 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\bliterature\b
\bliterature[\s-]+review\w*
\bsource\w*
\bsearch\w*
\bretriev\w*
\bdatabase\w*
\binformation[\s-]+literacy\b
\breading\b
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): the 9 corrected patterns are not identified in ing's files (RJ-0031's report is not held here).

## Sources

ADAPT's own files at the paths above, read in the Project mirror at `89ee9c4`; ADAPT's registers as of 2 October 2026, 22:36.

---

## Change notes
- 0.1.9: 4 October 2026, 10:37: core pointer to 0.1.11 (ing N-0119).
- 0.1.8: 4 October 2026, 10:03: core pointer to 0.1.10 (ing N-0113).
- 0.1.7: 3 October 2026, 11:10: core pointer to 0.1.9; section 4, the benchmark search patterns, v1.0 and the v2 changes known (D-ing-0050; ing N-0100).
- 0.1.6: 3 October 2026, 05:52: core pointer to 0.1.8 (ing N-0089).
- 0.1.5: 3 October 2026, 04:41: file renamed from `adp-ing-pd-pathway-finding-using-sources-adapt.md` to `ingest-path-finding-using-sources-adapt.md`; core pointer to `ingest-path-finding-using-sources.md` 0.1.7 (ing N-0083).
- 0.1.4: 2 October 2026, 22:50: core pointer to 0.1.4 (ing N-0039; G-ing-0041).
- 0.1.3: 2 October 2026, 22:48: core pointer to 0.1.3 (ing N-0038; G-ing-0038).
- 0.1.2: 2 October 2026, 22:44: core pointer to 0.1.2 (ing N-0037; G-ing-0036).
- 0.1.1: 2 October 2026, 22:42: point 1 updated for D-ing-0012 (a) (ing N-0036; G-ing-0032).
- 0.1.0: 2 October 2026, 22:37: created with the core 0.1.0 (ing N-0034; G-ing-0029).
