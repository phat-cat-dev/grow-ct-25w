---
document:  integration: how ADAPT uses the Creativity pathway
core:      `pathways/ingest-path-creativity.md` 0.1.0 (`ing:doc:pathway-creativity`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.0, 4 October 2026, 10:06 (ing N-0114)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror (`adp/adp-mirror/`, generated from `d9cf3af`); not evidence of repo state
---

# Creativity in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 13, "Creativity", no chapter (authored, Track B) | `catalogue/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers, focus creativity as a foundational academic skill, creative methods in academic work, creativity as innovation, enterprise and professional attribute | `catalogue/pathways/creativity.json` | all `planned`; no course slug; voice band "Provisional: confirm at SME sign-off." |
| The teaching prose, with its sources, framing decision, cross-links and notes | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 13 | draft; needs SME approval before authoring |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053): seven cards, two introduced, four developed, one extended | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 7 patterns for this pathway, one held twice | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 13"; the core uses only `path:creativity`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "Creativity: <Tier> Stage" (TN-1), from a shell and context packs (PKS-1). None built in the mirror.
2. **SME sign-off first.** The mapping requires subject expert approval before authoring.
3. **Context coupling.** The institutional source is Cardiff Met Library's own guide, with discipline pages (business, art and design, health, sport, education, social policy, technology): ready-made material for subject context packs (PKS-1).
4. **Cross-links.** Criticality (Pathway 5) throughout; Reflective Practice (10) for awareness of one's own creative process; Work-Based Learning (11) and Starting, Progressing and Succeeding (1) for the enterprise strand. The catalogue's `routes` are null.
5. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards (seven, every tier covered), for nts to land in `path`.
2. Key theory open (core Part E item 4); once ruled, the uningested sources go to META's ing as a handover.
3. Benchmark evidence for the cards (adp-0212's drafts): `/01` 457 chunks across 53 texts; `/06` 428 across 54; `/04` 170 across 51; `/02` 13 across 11; `/03` 5 across 4; `/05` 5 across 2; `/07` 3 across 3. `\bcreativ\w*`, `\binnovat\w*` and the enterprise patterns match nearly every benchmark: enterprise and entrepreneurship education is a QAA cross-cutting theme, so these hits mark the theme rather than the skill (the tagging review, ing N-0105).
4. The term list holds `problem[\s-]+solving` twice; D-0028's v2 drops the duplicate.

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 7 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\bcreativ\w*
\binnovat\w*
\bproblem[\s-]+solving\b
\bproblem[\s-]+solving\b
\benterprise\b
\bentrepreneur\w*
\bimaginat\w*
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): drops the duplicate `problem solving`; holds `creativ*` provisional (over 10% of chunks), to be narrowed after the pilot if the mapper rejects many hits (D-0031); the 9 corrected patterns are not identified in ing's files.

## Sources

ADAPT's own files at the paths above, read in the Project mirror; the card drafts and their benchmark evidence from `mta-nts-ho-adp-nts-0007` (`adp-0212-capability-cards.md`); the tier notes from `adp-relay/threads/prm/reviews/adp-0213-tier-notes.json`; ADAPT's registers as of 4 October 2026, 10:06.

---

## Change notes
- 0.1.0: 4 October 2026, 10:06: created with the core 0.1.0 (ing N-0114).
