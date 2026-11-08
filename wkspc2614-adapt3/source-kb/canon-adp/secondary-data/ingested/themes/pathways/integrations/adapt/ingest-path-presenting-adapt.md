---
document:  integration: how ADAPT uses the Presenting pathway
core:      `pathways/ingest-path-presenting.md` 0.1.7 (`ing:doc:pathway-presenting`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.7, 4 October 2026, 10:37, core pointer (ing N-0119); 0.1.6, 4 October 2026, 10:03, core pointer (ing N-0113); 0.1.5, 4 October 2026, 08:42, points 2 and 4 ruled (ing N-0109); 0.1.4, 4 October 2026, 06:49, core pointer (ing N-0108); 0.1.3, 3 October 2026, 15:19, core pointer (ing N-0104); 0.1.2, 3 October 2026, 14:50, point 2 (ing N-0103); 0.1.1, 3 October 2026, 14:06, point 1 settled (ing N-0102); 0.1.0, 3 October 2026, 13:34 (ing N-0101)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror (now `adp-mirror/`); not evidence of repo state
---

# Presenting in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 7, "Presenting", chapters [11]; `routes` feeds and drawsOn both null | `catalogue/context/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers | `catalogue/context/pathways/presenting.json` | all `planned`; no course slug; each tier's voice band "Confirmed 4 Sep 2026 at presenting-introductory A2 (f05d72d)" |
| The teaching prose | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 7, with the remap note of 3 September 2026 and two flags | draft, for SME review |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053): four cards, three developed, one extended, none introduced | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 11 patterns for this pathway | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 7"; the core uses only `path:presenting`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "Presenting: <Tier> Stage" (TN-1), from a shell and subject context packs (PKS-1). The catalogue records a design run of `presenting-introductory` (gate A2, commit `f05d72d`, 4 September 2026) that confirmed the voice band, but no course slug; whether that run's records still stand is not checked here.
2. **Voice band.** Introductory, Intermediate and Advanced anchored to tier specification section 16, bands 2 to 4, default, confirmed (`pathway-tier-mapping.md`, Pathway 7).
3. **Pressure-test first.** The mapping flags Presenting as less writing-centric and asks for a pressure-test before building (CLAUDE.md guardrail).
4. **Context coupling.** Presentation briefs, formats and marking criteria vary by module and discipline: vocational packs need practice-based formats (a pitch, a case presentation, a coaching plan), research packs posters and progress talks (PKS-1).
5. **Media.** Presenting is oral and visual: Adapt components for video, audio and slide examples matter more here than in writing pathways; candidate components belong to the component register, not here.
6. **Cross-links.** Group work's reflective element uses Reflective Practice (Pathway 10); academic voice links to Starting, Progressing and Succeeding (Pathway 1) and Academic Writing (Pathway 6). The catalogue's `routes` are null.
7. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards. Abbott added three at 14:06 (D-ing-0051), temporary ids: c1 "Build a presentation to a brief through the five steps, with a hook, a main body and a conclusion" (Introductory), c2 "Present and defend an argument with an academic voice under questioning" (Intermediate), c3 "Present in professional formats: the pitch, the conference poster and the viva-style interview" (Advanced); for nts to land in `path`. [Was: the core's candidates, open.]
2. Theory by strand (D-ing-0052, 14:50): five strands with researched theorists (core A9); leads proposed (Aristotle, Mayer, McCroskey, Ivanič, Tuckman), not ruled; once ruled, the uningested ones go to META's ing as a handover. [Was: the key theory open.] [08:42, ruled (D-ing-0053): leads as proposed, group work led by Gibbs and Healey with Tuckman beside, and Tufte beside Mayer for visual design; the uningested leads go to META's ing as a handover.]
3. Group work: stay as an Advanced card here, or spin out into its own pathway, as the mapping flags (core Part E item 5).
4. The book's OCEAN mapping conflicts with the five-factor model (core Part E item 6); the courses should not teach it as is until ruled. [08:42, ruled (D-ing-0054): the courses do not teach OCEAN; group work is taught through process. The tier prose in `pathway-tier-mapping.md` (Pathway 7, Advanced) names OCEAN: for nts to carry to `path`.]
5. Benchmark evidence for the cards (adp-0212's drafts): `/04` 494 chunks across 54 texts (group work is everywhere); `/03` 35 across 26; `/01` 13 across 12; `/02` none found.

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 11 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\bpresentation\w*
\bpresent\b
\bpresenting\b
\bpresented\b
\bposter\w*
\boral[\s-]+communication\b
\bgroup[\s-]+work\b
\baudience\w*
\bpitch\w*
\bpublic[\s-]+speaking\b
\bdisseminat\w*
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): no drop or provisional term for this pathway is recorded; the 9 corrected patterns are not identified in ing's files (RJ-0031's report is not held here). `\bpresent\b` and `\baudience\w*` are broad: "present" matches the ordinary verb.

## Sources

ADAPT's own files at the paths above, read in the Project mirror; the card drafts and their benchmark evidence from `mta-nts-ho-adp-nts-0007` (`adp-0212-capability-cards.md`); the tier notes from `adp-relay/threads/prm/reviews/adp-0213-tier-notes.md`; ADAPT's registers as of 3 October 2026, 13:34.

---

## Change notes
- 0.1.7: 4 October 2026, 10:37: core pointer to 0.1.7 (ing N-0119).
- 0.1.6: 4 October 2026, 10:03: core pointer to 0.1.6 (ing N-0113).
- 0.1.5: 4 October 2026, 08:42: core pointer to 0.1.5; points 2 and 4 ruled (D-ing-0053, D-ing-0054; ing N-0109).
- 0.1.4: 4 October 2026, 06:49: core pointer to 0.1.4 (ing N-0108).
- 0.1.3: 3 October 2026, 15:19: core pointer to 0.1.3 (ing N-0104).
- 0.1.2: 3 October 2026, 14:50: core pointer to 0.1.2; point 2, theory by strand (D-ing-0052; ing N-0103).
- 0.1.1: 3 October 2026, 14:06: core pointer to 0.1.1; point 1 settled (D-ing-0051; ing N-0102).
- 0.1.0: 3 October 2026, 13:34: created with the core 0.1.0, section 4 from the start (ing N-0101).
