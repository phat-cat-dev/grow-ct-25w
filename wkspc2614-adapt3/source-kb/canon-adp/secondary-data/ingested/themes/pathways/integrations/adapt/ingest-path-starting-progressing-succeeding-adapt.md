---
document:  integration: how ADAPT uses the Starting, Progressing and Succeeding pathway
core:      `pathways/ingest-path-starting-progressing-succeeding.md` 0.1.7 (`ing:doc:pathway-starting-progressing-succeeding`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.7, 4 October 2026, 10:37, core pointer (ing N-0119); 0.1.6, 4 October 2026, 10:19, core pointer (ing N-0115); 0.1.5, 4 October 2026, 10:03, core pointer (ing N-0113); 0.1.4, 3 October 2026, 11:10, benchmark search patterns (ing N-0100); 0.1.3, 3 October 2026, 09:25, point 2 extended (ing N-0098); 0.1.2, 3 October 2026, 08:04, c2 reworded (ing N-0097); 0.1.1, 3 October 2026, 07:13, points 1 and 2 settled (ing N-0096); 0.1.0, 3 October 2026, 06:58 (ing N-0095)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror at commit `89ee9c4`; not evidence of repo state
---

# Starting, Progressing and Succeeding in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 1, "Starting, Progressing & Succeeding", chapters [2, 14]; `routes` feeds and drawsOn both null | `catalogue/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers, focus Starting, Progressing and Succeeding | `catalogue/pathways/starting-progressing-succeeding.json` | all `planned`; no course slug |
| The teaching prose | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 1 | draft, for SME review |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053): four cards, one introduced, two developed, one extended | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 17 patterns for this pathway | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 1"; the core uses only `path:starting-progressing-succeeding`.

## 2. How ADAPT uses it

1. **Programme entry point.** The mapping makes it the programme's entry point: surfaced first, it introduces the other pathways and carries the orientation tone. The Introductory course is the natural first course a student meets.
2. **Courses.** One SCORM course per tier, "Starting, Progressing & Succeeding: <Tier> Stage" (TN-1), from a shell and subject context packs (PKS-1). None built in the mirror.
3. **Voice band.** Introductory, Intermediate and Advanced anchored to tier specification section 16, bands 2 to 4, default (`pathway-tier-mapping.md`, Pathway 1).
4. **Context coupling.** Graduate attributes frameworks, support services (personal tutors, wellbeing, careers, academic skills) and employability provision are institutional: the courses need each context pack's own graduate attributes and support routes (PKS-1). The book directs students to their own university's graduate attributes framework (p. 15).
5. **Cross-links.** Every other pathway leans on this one for the motivational and dispositional layer; Pathway 2's self-regulation mechanics are its mechanical counterpart. Referencing's integrity tier links to graduate identity here (mapping, Pathway 4). The catalogue's `routes` are null, so the links live only in the prose.
6. **Benchmark mapping.** The 17 patterns are the word test for QV-TAG-2 part (e). Several are very broad: `\bprogress\w*`, `\bgraduat\w*`, `\bemploy\w*`, `\bprofession\w*`, `\bgoal\w*` and the four level patterns (`level 4` to `level 7`) will match statements about qualification structure rather than disposition, and `\bprofession\w*` is also Pathway 11's ground. The draft card evidence ranges from 229 chunks across 53 texts (`/04`, graduate capital) to 9 chunks across 6 texts (`/02`, self-efficacy and anxiety). Whether D-0028's v2 changes them is unchecked here.
7. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards. Abbott added three at 07:13 (D-ing-0046), temporary ids: c1 "Recognise and follow the conventions of academic practice" (Introductory), c2 "Invest in strategic personal development as an academic practitioner" (Intermediate), c3 "Direct one's own academic practice, learning and development independently, as a lifelong learner" (Advanced); the Introductory course is about the conventions of academic practice, conforming and then expressing oneself within them, and the learner's identity as an academic practitioner evolves across the three courses; for nts to land in `path`. [Was: the core's candidates, which Abbott did not take.] [c2 reworded 08:04 (D-ing-0048): "Develop an academic voice, and the confidence and sense of capability to own one's practice within its conventions"; the Intermediate course is where the learner moves beyond conforming to an academic voice.]
2. Theory (D-ing-0047, 07:13): Dweck, Bandura, Pintrich and Tomlinson, queued at META's ing (`adp-ing-ho-mta-ing-0012`). [Was: the key theory open.] The evolution of the learner's identity across the three courses is framed by Baxter Magolda's self-authorship, with SOLO beside it and Ivanič for voice in the Intermediate course (D-ing-0049, 09:25); Baxter Magolda and Ivanič queued at META's ing (`adp-ing-ho-mta-ing-0013`).
3. Whether the catalogue's null `routes` should carry the mapping's cross-links.
4. The broad term patterns (section 2, point 6), for RJ-0033 when it commits v2.
5. The Intermediate tier's setbacks, help-seeking and perfectionism have little source in the book (core Part E item 7): its content will come from outside the book and from each context pack's support routes.

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 17 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\bprogress\w*
\btransition\w*
\bmotivat\w*
\bmindset\b
\bgoal\w*
\bgraduate[\s-]+identity\b
\blifelong[\s-]+learning\b
\bfurther[\s-]+study\b
\bindependent[\s-]+study\b
\blevel[\s-]+4\b
\blevel[\s-]+5\b
\blevel[\s-]+6\b
\blevel[\s-]+7\b
\bgraduat\w*
\bemploy\w*
\bprofession\w*
\bpostgraduate\b
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): drops `graduate identity`; holds `profession*`, `graduat*`, `employ*` provisional (over 10% of chunks), to be narrowed after the pilot if the mapper rejects many hits (D-0031); the 9 corrected patterns are not identified in ing's files (RJ-0031's report is not held here).

## Sources

ADAPT's own files at the paths above, read in the Project mirror at `89ee9c4`; the card drafts and their benchmark evidence from `mta-nts-ho-adp-nts-0007` (`adp-0212-capability-cards.md`); the tier notes from `adp-relay/threads/prm/reviews/adp-0213-tier-notes.md`; ADAPT's registers as of 3 October 2026, 06:58.

---

## Change notes
- 0.1.7: 4 October 2026, 10:37: core pointer to 0.1.7 (ing N-0119).
- 0.1.6: 4 October 2026, 10:19: core pointer to 0.1.6 (ing N-0115).
- 0.1.5: 4 October 2026, 10:03: core pointer to 0.1.5 (ing N-0113).
- 0.1.4: 3 October 2026, 11:10: core pointer to 0.1.4; section 4, the benchmark search patterns, v1.0 and the v2 changes known (D-ing-0050; ing N-0100).
- 0.1.3: 3 October 2026, 09:25: core pointer to 0.1.3; point 2: the identity frame (D-ing-0049; ing N-0098).
- 0.1.2: 3 October 2026, 08:04: core pointer to 0.1.2; c2 reworded (D-ing-0048; ing N-0097).
- 0.1.1: 3 October 2026, 07:13: core pointer to 0.1.1; points 1 and 2 settled (D-ing-0046, D-ing-0047; ing N-0096).
- 0.1.0: 3 October 2026, 06:58: created with the core 0.1.0 (ing N-0095).
