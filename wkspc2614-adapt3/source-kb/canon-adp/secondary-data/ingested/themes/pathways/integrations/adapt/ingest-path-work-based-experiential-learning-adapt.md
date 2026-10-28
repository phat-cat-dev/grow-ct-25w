---
document:  integration: how ADAPT uses the Work-Based and Experiential Learning pathway
core:      `pathways/ingest-path-work-based-experiential-learning.md` 0.1.11 (`ing:doc:pathway-work-based-experiential-learning`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.8, 4 October 2026, 10:37, core pointer (ing N-0119); 0.1.7, 4 October 2026, 10:03, core pointer (ing N-0113); 0.1.6, 3 October 2026, 11:10, benchmark search patterns (ing N-0100); 0.1.5, 3 October 2026, 06:19, report writing amended (ing N-0093); 0.1.4, 3 October 2026, 06:04, report writing (ing N-0091); 0.1.3, 3 October 2026, 05:52, core pointer updated (ing N-0089); 0.1.2, 3 October 2026, 04:41, renamed; core pointer updated (ing N-0083); 0.1.1, 2 October 2026, 22:14 (ing N-0031; G-ing-0026); 0.1.0, 22:12 (ing N-0029; G-ing-0023)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror at commit `89ee9c4`; not evidence of repo state
---

# Work-Based and Experiential Learning in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 11, chapters [12] | `catalogue/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers | `catalogue/pathways/work-based-experiential-learning.json` | `planned` |
| The teaching prose | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 11 | draft, for SME review |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053) | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 20 patterns for this pathway | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 11"; the core uses only `path:work-based-experiential-learning`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "Work-Based & Experiential Learning: <Tier> Stage" (TN-1), from a shell and subject context packs (PKS-1). None built.
2. **Voice band.** Default anchor, bands 2 to 4, marked "Provisional: confirm at pathway pressure-test" (`pathway-tier-mapping.md`, Pathway 11).
3. **Pressure-test first.** The mapping names this as one of the three less writing-centric pathways to pressure-test against its chapter before content is built (`pathway-tier-mapping.md`, cross-cutting notes).
4. **Vocational packs.** Nursing, teaching and social work packs need authored, discipline-aware examples beyond the book; they sit between "convert" and "author new" (cross-cutting notes); Phase D work.
5. **Leans on Reflective Practice.** ADAPT's courses cross-reference Pathway 10 for the method rather than re-teach it.
6. **Benchmark mapping.** The 20 patterns are the word test for QV-TAG-2 part (e); `real world` appears twice, and broad patterns (`in practice`, `real world`, `laboratory`) may tag statements that are not about work-based learning.
7. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards. Abbott added two at 22:14 (D-ing-0010 (a)): professional conduct and testing theory in practice (Intermediate); for nts to land in `path` (ing N-0031).
2. The pressure-test of Pathway 11 against Chapter 12, and the voice-band anchor it would confirm.
3. The duplicated `real world` pattern in the term list, for RJ-0033 when it commits v2.
4. Report writing (D-ing-0044, 06:19): one lesson somewhere in Pathway 11's series, defined in ADAPT's content rather than the core: a brief outer shell describing the characteristics of report writing, then the context does its job and defines the report, generally or subject-specifically, from the context pack (PKS-1). Where in the series, and whether a card names it, are for nts under D-0058. [Was, 06:04 to 06:19: Report writing (D-ing-0024 (a), 06:04): Pathway 11's courses teach the business report and the incident report; the incident report has no source in the book and no card, so its content comes from outside the book; candidate card for nts under D-0058. (ing N-0091).]

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 20 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\bplacement\w*
\bfieldwork\b
\bfield[\s-]+work\b
\blab[\s-]+work\b
\blaboratory\b
\bwork[\s-]+based\b
\bexperiential\b
\bwork[\s-]+experience\b
\bpracticum\b
\binternship\w*
\blive[\s-]+project\w*
\bapprenticeship\w*
\bpractice[\s-]+based\b
\breal[\s-]+world\b
\breal[\s-]+world\b
\bin[\s-]+practice\b
\bapplied[\s-]+practice\b
\bpractice[\s-]+setting\w*
\bprofessional[\s-]+practice\b
\bin[\s-]+the[\s-]+workplace\b
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): drops `practicum`; drops the duplicate real world (listed twice in v1); the 9 corrected patterns are not identified in ing's files (RJ-0031's report is not held here).

## Sources

ADAPT's own files at the paths above, read in the Project mirror at `89ee9c4`; ADAPT's registers as of 2 October 2026, 22:10.

---

## Change notes
- 0.1.8: 4 October 2026, 10:37: core pointer to 0.1.11 (ing N-0119).
- 0.1.7: 4 October 2026, 10:03: core pointer to 0.1.10 (ing N-0113).
- 0.1.6: 3 October 2026, 11:10: core pointer to 0.1.9; section 4, the benchmark search patterns, v1.0 and the v2 changes known (D-ing-0050; ing N-0100).
- 0.1.5: 3 October 2026, 06:19: core pointer to 0.1.8; point 4: the report writing lesson (D-ing-0044; ing N-0093).
- 0.1.4: 3 October 2026, 06:04: core pointer; report writing (D-ing-0024 (a); ing N-0091).
- 0.1.3: 3 October 2026, 05:52: core pointer to 0.1.6 (ing N-0089).
- 0.1.2: 3 October 2026, 04:41: file renamed from `adp-ing-pd-pathway-work-based-experiential-learning-adapt.md` to `ingest-path-work-based-experiential-learning-adapt.md`; core pointer to `ingest-path-work-based-experiential-learning.md` 0.1.5 (ing N-0083).
- 0.1.1: 2 October 2026, 22:14: point 1 updated for D-ing-0010 (a) (ing N-0031; G-ing-0026).
- 0.1.0: 2 October 2026, 22:12: created with the core 0.1.0 (ing N-0029; G-ing-0023).
