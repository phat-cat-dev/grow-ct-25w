---
document:  integration: how ADAPT uses the Reflective Practice pathway
core:      `pathways/ingest-path-reflective-practice.md` 0.2.21 (`ing:doc:pathway-reflective-practice`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.7, 4 October 2026, 10:37, core pointer (ing N-0119); 0.1.6, 4 October 2026, 10:03, core pointer (ing N-0113); 0.1.5, 3 October 2026, 11:10, benchmark search patterns (ing N-0100); 0.1.4, 3 October 2026, 06:37, the reflective report card (ing N-0094); 0.1.3, 3 October 2026, 06:19, report writing amended (ing N-0093); 0.1.2, 3 October 2026, 05:52, core pointer updated (ing N-0089); 0.1.1, 3 October 2026, 04:41, renamed; core pointer updated (ing N-0083); 0.1.0, 2 October 2026, 21:01 (ing N-0012; G-ing-0006)
status:    drafted; never ingested into any store (ing N-0010 to N-0012)
read from: ADAPT's Project mirror at commit `89ee9c4`; not evidence of repo state
---

# Reflective Practice in ADAPT

What ADAPT does with the pathway, kept out of the core so the core stays generic. Every item here is ADAPT's; the core holds what the pathway is.

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 10, chapters [4] | `catalogue/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers, each with focus, voice band and a pointer to the teaching prose | `catalogue/pathways/reflective-practice.json` | all three `planned`, no course slug |
| The teaching prose for each tier | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 10 | draft, for SME review |
| The tier definitions | `docs/curriculum/tier-specification.md` v1.0 | validated on Academic Writing only |
| The capability cards and tier notes | adp-0212 (RJ-0047) and adp-0213 (RJ-0053); `adp-relay/threads/prm/reviews/adp-0213-tier-notes.json` | drafts; ADAPT D-0058 owed; the cards file is not in the Project |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 7 patterns for this pathway | v2 ruled (D-0028), committed by RJ-0033, held |

ADAPT calls the pathway "Pathway 10"; the core uses only `path:reflective-practice`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier in Moodle, titled "Reflective Practice: <Tier> Stage" (TN-1), each built from a shell and subject context packs (PKS-1). None built.
2. **Voice band.** Default anchor, bands 2 to 4: Introductory takes the voice specification's Beginner band, Intermediate its Intermediate band, Advanced its Advanced band (`pathway-tier-mapping.md`, Pathway 10; tier specification section 3). This sets register, sentence length and outcome verbs.
3. **Outcome verbs.** Drawn from the anchored band of `reference/excelling-voice-specification.md` section 16 (tier specification section 6): Introductory from Beginner (describe, identify, recognise, explain, distinguish and so on), never evaluate or critique; Intermediate from Intermediate; Advanced from Advanced. Moved here from the core's B5 because the bands are ADAPT's.
4. **Reflective prompt in every lesson.** ADAPT's pedagogy log, P11 (Schön, 1983), "in use": a reflective prompt in every lesson; that it is always shell, with a subject angle, is proposed, not ruled (log D2). P12 (Gibbs, 1988) is "to consider" as a structure for the prompts; question T2 asks whether prompts should follow a named cycle (`docs/design/pedagogy-log.md`). This is why the core links Schön though the tiers do not name him.
5. **Benchmark mapping.** The term list's patterns are a word test: a QAA benchmark statement whose extract matches a pattern is tagged `direct` for this pathway, otherwise `indirect` (QV-TAG-2 part (e); rules v1.2 to come). The core uses the same patterns only as entry terms.
6. **Practice connection.** The capabilities' student-facing statements fill the opening and closing wrappers of each course, filtered by tier (D-0047; RJ-0050, held on D-0058).
7. **Summative parity.** The end-of-tier summative is calibrated to the tier specification section 7 row; parity holds across contexts within a pathway and tier, not across pathways.
8. **Vocational packs.** The pathway serves nursing, teaching and social work heavily and needs authored, discipline-aware examples beyond the book (`pathway-tier-mapping.md`, cross-cutting notes); those packs are Phase D work.

## 3. Points open for ADAPT

1. D-0058: rule the cards and tier notes. The core's coverage gap (its Part E item 3: no card for critical reflection, action planning or choosing a fuller model; the only Intermediate card borrowed from Pathway 2) is for this ruling (ing N-0008 to nts).
2. Whether the pedagogy log's reflective prompt should follow the pathway's ERA cycle (T2).
3. The guide map for *Excelling at University*: adp-0212's draft book map, to be redone once the book profile exists (D-0043; `path` spec 0.4.1-draft, section 5). The core points at it; it lives with `path`.
4. The professional-practice reflective report (D-ing-0044, 06:19): Pathway 10's courses teach reflection written in report format, so report writing is taught here; the core's Part E item 12 gives the example structure (after Gibbs, 1988). Its card is `reflective-practice/c5`, Intermediate (D-ing-0045, 06:37), so the Intermediate course carries it; for nts to land under D-0058. [Was: the tier and the card owed.]

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 7 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\breflect\w*[\s-]+on\b
\breflectiv\w*
\breflection\w*
\breflexiv\w*
\bself[\s-]+reflect\w*
\bCPD\b
\bcontinuing[\s-]+professional[\s-]+development\b
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): the 9 corrected patterns are not identified in ing's files (RJ-0031's report is not held here).

## Sources

ADAPT's own files at the paths above, read in the Project mirror at `89ee9c4`; ADAPT's registers (`adp-relay/notes/adp-rg-decisions.md`, `adp-rg-jobs.md`) as of 2 October 2026, 20:30.

---

## Change notes
- 0.1.7: 4 October 2026, 10:37: core pointer to 0.2.21 (ing N-0119).
- 0.1.6: 4 October 2026, 10:03: core pointer to 0.2.20 (ing N-0113).
- 0.1.5: 3 October 2026, 11:10: core pointer to 0.2.19; section 4, the benchmark search patterns, v1.0 and the v2 changes known (D-ing-0050; ing N-0100).
- 0.1.4: 3 October 2026, 06:37: core pointer to 0.2.18; point 4: c5 at Intermediate (D-ing-0045; ing N-0094).
- 0.1.3: 3 October 2026, 06:19: core pointer to 0.2.17; point 4: the reflective report (D-ing-0044; ing N-0093).
- 0.1.2: 3 October 2026, 05:52: core pointer to 0.2.16 (ing N-0089).
- 0.1.1: 3 October 2026, 04:41: file renamed from `adp-ing-pd-pathway-reflective-practice-adapt.md` to `ingest-path-reflective-practice-adapt.md`; core pointer to `ingest-path-reflective-practice.md` 0.2.15 (ing N-0083).
- 0.1.0: 2 October 2026, 21:01: created from the ADAPT content taken out of the core at its 0.2.0 (ing N-0012; G-ing-0006).
