---
document:  integration: how ADAPT uses the Referencing, Citation and Academic Integrity pathway
core:      `pathways/ingest-path-referencing.md` 0.1.13 (`ing:doc:pathway-referencing`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.11, 4 October 2026, 10:37, core pointer (ing N-0119); 0.1.10, 4 October 2026, 10:03, core pointer (ing N-0113); 0.1.9, 3 October 2026, 11:10, benchmark search patterns (ing N-0100); 0.1.8, 3 October 2026, 05:52, core pointer updated (ing N-0089); 0.1.7, 3 October 2026, 04:41, renamed; core pointer updated (ing N-0083); 0.1.6, 3 October 2026, 02:00, point 6 (ing N-0072; G-ing-0124); 0.1.5, 3 October 2026, 01:57, point 5 amended (ing N-0070; G-ing-0120); 0.1.4, 3 October 2026, 01:55, core pointer updated (ing N-0069; G-ing-0117); 0.1.3, 3 October 2026, 01:49, core pointer and point 5 (ing N-0068; G-ing-0114); 0.1.2, 3 October 2026, 01:45, point 2 corrected (ing N-0067; G-ing-0111); 0.1.1, 3 October 2026, 01:41, points 1 and 2 updated (ing N-0066; G-ing-0108); 0.1.0, 3 October 2026, 01:24 (ing N-0065; G-ing-0105)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror at commit `89ee9c4`; not evidence of repo state
---

# Referencing, Citation and Academic Integrity in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 4, "Referencing, Citation & Academic Integrity", chapters [10]; `routes` null | `catalogue/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers | `catalogue/pathways/referencing.json` | Introductory `in-design`, course slug `referencing-introductory`; Intermediate and Advanced `planned` |
| The teaching prose | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 4 | draft, for SME review |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053) | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 10 patterns for this pathway | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 4"; the core uses only `path:referencing`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "Referencing, Citation & Academic Integrity: <Tier> Stage" (TN-1), from a shell and subject context packs (PKS-1).
2. **The first course.** `referencing-introductory` is the only course with a design run: Phase A ran once and is retired by RRN-1, to be rerun after the fixes in backlog 5.154. Its gate records are the place where this core's Introductory content first meets a design; whether the rerun has happened since `89ee9c4` is unchecked here.
3. **Referencing style is context, not shell.** The core teaches author-date as the worked style and sends the learner to the required one. In ADAPT the style belongs to the context pack's phase (PKS-1, Option B of 26 September; the RS-1 amendment puts it in the context definition), and references are to be stored as data and formatted for each context (`mta-ho-adp-prm-02`). The shell's content stays style-neutral where it can.
4. **Voice band.** Introductory, Intermediate and Advanced anchored to tier specification section 16, bands 2 to 4, default (`pathway-tier-mapping.md`, Pathway 4).
5. **Cross-links.** Supports Academic Writing (Pathway 6), whose four pillars self-review carries the referencing checks (pillar 4); research ethics in practice is Researching's (Pathway 9); integrity connects to the graduate identity thread in Pathway 1. The catalogue's `routes` are null, so the links live only in the prose.
6. **Benchmark mapping.** The 10 patterns are the word test for QV-TAG-2 part (e). `references` and `cite` are broad. `academic integrity` and `plagiaris*` will meet few subject benchmark statements, which treat integrity in general terms. Whether D-0028's v2 changes them is unchecked here.
7. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards. Abbott added three at 01:41 (D-ing-0031 (a)): "Explain why academic work acknowledges the sources of its knowledge" and "Record and organise sources as they are found, so that every citation can be traced" (Introductory) and "Use citation to show the scope of research and engagement with the discourse" (Intermediate); for nts to land in `path` (ing N-0066).
2. The Manage pillar (D-ing-0014 (a)) is now a capability (c2). The guide grounds it in part (accuracy as honesty, the details each reference needs, efficient working, keeping a record while making notes); Abbott wants SCONUL's Seven Pillars model introduced in the lessons by name and cited in the course's sources (ing N-0067). This bears on `referencing-introductory`'s rerun (RRN-1) and its sources step (SIP-1).
3. The AI integrity material: the mapping puts it in Pathway 12 as the AI-specific extension of this pathway's values and plagiarism content, cross-referenced, not duplicated (`pathway-tier-mapping.md`, Pathway 12, cross-links). The two pathways' courses need to agree where each case sits.
4. Whether the catalogue's null `routes` should carry the mapping's cross-links.
5. Theory for the courses (D-ing-0033, 01:57, amending D-ing-0032 (a)): Hyland (1999) is the key theory and Howard (1995) sits beside it, with patchwriting possible at Advanced; the discourse community journey (Lave and Wenger, META run 0033) runs through the pathway; the ICAI values appear in passing. What the book teaches comes to the courses through its source map (`adp-ing-td-source-map-candidates-referencing.md` until `path` holds it). Hyland and the ICAI values are queued at META's ing (`adp-ing-ho-mta-ing-0007`), Howard by `adp-ing-ho-mta-ing-0008`.
6. Paraphrase (D-ing-0034 (b), 02:00): taught in the Academic Writing courses; the Referencing courses teach acknowledging quoted and paraphrased material and, at Advanced, patchwriting. `referencing/02` narrows accordingly; for nts to land in `path` (ing N-0072).

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 10 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\breferencing\b
\breferences\b
\breference[\s-]+list\b
\bcitat\w*
\bcite\b
\bcited\b
\bciting\b
\bacademic[\s-]+integrity\b
\bplagiaris\w*
\backnowledg\w*[\s-]+sources\b
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): the 9 corrected patterns are not identified in ing's files (RJ-0031's report is not held here).

## Sources

ADAPT's own files at the paths above, read in the Project mirror at `89ee9c4`; the card drafts from `mta-nts-ho-adp-nts-0007` (`adp-0212-capability-cards.md`); the tier notes from `adp-relay/threads/prm/reviews/adp-0213-tier-notes.md`; ADAPT's project instructions (PKS-1, RRN-1, RS-1 amendment); ADAPT's registers as of 3 October 2026, 01:18.

---

## Change notes
- 0.1.11: 4 October 2026, 10:37: core pointer to 0.1.13 (ing N-0119).
- 0.1.10: 4 October 2026, 10:03: core pointer to 0.1.12 (ing N-0113).
- 0.1.9: 3 October 2026, 11:10: core pointer to 0.1.11; section 4, the benchmark search patterns, v1.0 and the v2 changes known (D-ing-0050; ing N-0100).
- 0.1.8: 3 October 2026, 05:52: core pointer to 0.1.10 (ing N-0089).
- 0.1.7: 3 October 2026, 04:41: file renamed from `adp-ing-pd-pathway-referencing-adapt.md` to `ingest-path-referencing-adapt.md`; core pointer to `ingest-path-referencing.md` 0.1.9 (ing N-0083).
- 0.1.6: 3 October 2026, 02:00: core pointer to 0.1.6; point 6, paraphrase (D-ing-0034 (b); ing N-0072; G-ing-0124).
- 0.1.5: 3 October 2026, 01:57: core pointer to 0.1.5; point 5 amended for D-ing-0033 (ing N-0070; G-ing-0120).
- 0.1.4: 3 October 2026, 01:55: core pointer to 0.1.4 (ing N-0069; G-ing-0117).
- 0.1.3: 3 October 2026, 01:49: core pointer to 0.1.3; point 5, grounding order (D-ing-0032 (a); ing N-0068; G-ing-0114).
- 0.1.2: 3 October 2026, 01:45: core pointer to 0.1.2; point 2 corrected: SCONUL's model taught and cited (ing N-0067; G-ing-0111).
- 0.1.1: 3 October 2026, 01:41: core pointer to 0.1.1; points 1 and 2 updated for D-ing-0031 (a) (ing N-0066; G-ing-0108).
- 0.1.0: 3 October 2026, 01:24: created with the core 0.1.0 (ing N-0065; G-ing-0105).
