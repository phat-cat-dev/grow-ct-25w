---
document:  integration: how ADAPT uses the Academic Writing pathway
core:      `pathways/ingest-path-academic-writing.md` 0.1.22 (`ing:doc:pathway-academic-writing`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.20, 4 October 2026, 10:37, core pointer (ing N-0119); 0.1.19, 4 October 2026, 10:03, core pointer (ing N-0113); 0.1.18, 3 October 2026, 11:10, benchmark search patterns (ing N-0100); 0.1.17, 3 October 2026, 06:19, report writing amended (ing N-0093); 0.1.16, 3 October 2026, 06:04, report writing (ing N-0091); 0.1.15, 3 October 2026, 05:52, core pointer updated (ing N-0089); 0.1.14, 3 October 2026, 04:41, renamed; core pointer updated (ing N-0083); 0.1.13, 3 October 2026, 02:00, point 8 added (ing N-0072; G-ing-0125); 0.1.12, 3 October 2026, 01:17, point 7 renamed (ing N-0063; G-ing-0102); 0.1.11, 3 October 2026, 01:07, point 7 added (ing N-0062; G-ing-0099); 0.1.10, 3 October 2026, 00:57, core pointer updated (ing N-0061; G-ing-0096); 0.1.9, 3 October 2026, 00:41, core pointer updated (ing N-0060; G-ing-0093); 0.1.8, 3 October 2026, 00:38, core pointer updated (ing N-0059; G-ing-0090); 0.1.7, 3 October 2026, 00:21, core pointer; duplicated words in point 4 removed (ing N-0058; G-ing-0086); 0.1.6, 3 October 2026, 00:03, core pointer updated (ing N-0057; G-ing-0082); 0.1.5, 3 October 2026, 00:02, scope redefined (ing N-0056; G-ing-0079); 0.1.4, 2 October 2026, 23:53, reflective writing to Pathway 10 (ing N-0055; G-ing-0075); 0.1.3, 2 October 2026, 23:49, points 2 and 3 updated (ing N-0051; G-ing-0068); 0.1.2, 2 October 2026, 23:38, point 2 updated (ing N-0050; G-ing-0064); 0.1.1, 2 October 2026, 23:29, point 1 updated (ing N-0049; G-ing-0059); 0.1.0, 2 October 2026, 23:23 (ing N-0047; G-ing-0056)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror at commit `89ee9c4`; not evidence of repo state
---

# Academic Writing in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 6, chapters [8, 9]; `routes` feeds and drawsOn both null | `catalogue/context/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers | `catalogue/context/pathways/academic-writing.json` | `planned`; no course slug or context built in the mirror |
| The teaching prose | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 6, marked "Pilot candidate" | draft, for SME review |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053) | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 10 patterns for this pathway | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 6"; the core uses only `path:academic-writing`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "Academic Writing: <Tier> Stage" (TN-1), from a shell and subject context packs (PKS-1). None built in the mirror.
2. **Pilot candidate.** The mapping names this pathway the pilot candidate and asks for the placing of discipline conventions at Advanced to be confirmed at the pilot pressure-test (`pathway-tier-mapping.md`, Pathway 6). Whether the pilot has moved since `89ee9c4` is unchecked here; `referencing-introductory` is the course with a Phase A run.
3. **Voice band.** Default anchor, bands 2 to 4, "Confirmed: validated against L01/L02 at tier-spec STEP 5" (`pathway-tier-mapping.md`, Pathway 6).
4. **Scope and signposts.** Essay and assignment writing and the academic conventions and style (D-ing-0023). Signposted, not taught: reflective writing (Pathway 10), critical research writing and the research genres (Pathway 9), report writing (home held). The critical edge is taught in Pathway 5 and applied here (D-ing-0020 (a)). The pathway draws on Pathways 3 and 4 (cross-links in the mapping); the catalogue's `routes` are null, so the links live only in the prose.
5. **Benchmark mapping.** The 10 patterns are the word test for QV-TAG-2 part (e). `writing` and `assignment` are broad; `research report`, `lab report` and `report writing` name genres the mapping hands to Pathway 9 (core Part E item 6). Whether D-0028's v2 changes them is unchecked here.
6. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards. Abbott added two at 23:29 (D-ing-0019 (a)): "Follow the writing cycle to plan and complete a first draft" (Introductory) and "Integrate sources actively, putting one's own point first and using sources to support it" (Intermediate); for nts to land in `path` (ing N-0049).
2. The split with Criticality: settled (D-ing-0020 (a), 23:38); the Academic Writing courses apply the critical edge and refer to Criticality. The split with Researching: settled (D-ing-0021 (a), 23:49): `academic-writing/02` narrows to the essay and reflective writing.
3. The report patterns: D-ing-0021 (a) moves `research report`, `lab report` and `report writing` to Pathway 9's list, for RJ-0033 when it commits v2 (ing N-0051).
4. Whether the catalogue's null `routes` should carry the mapping's cross-links.
5. Reflective writing: D-ing-0022 (b), amended by D-ing-0023, moves it from Pathway 6's Intermediate tier to Pathway 10; `academic-writing/02` reads "Identify and structure the essay and other argued assignments"; `reflective` and `reflective report` leave this pathway's term list for Pathway 10's. The mapping's Pathway 6 text ("the essay in depth, and reflective writing") needs the same change; for nts (ing N-0055). An optional contrast of academic, reflective and report writing is a candidate only.
6. Report writing: settled (D-ing-0024 (a), 06:04): the Academic Writing courses signpost the research and laboratory report (Pathway 9's courses) and the business and incident report (Pathway 11's). [Was: held (D-ing-0023); probably signposted.] The mapping's Pathway 6 text needs D-ing-0023's scope; for nts (ing N-0056). [Amended 06:19, D-ing-0044: the courses refer to all three homes: the research and laboratory report (Pathway 9), the professional-practice reflective report (Pathway 10) and the context-defined report writing lesson (Pathway 11).]
7. Teaching the writing cycle and the four pillars (D-ing-0029): the mapping already places the writing cycle at Introductory and "The four pillars as a self-review lens" at Intermediate (`pathway-tier-mapping.md`, Pathway 6, mirror at `89ee9c4`, checked 01:07). Abbott wants each taught substantially, close to a lesson per pillar, with the four pillars self-review as the student's tool (named by D-ing-0030); his tier is "probably the middle", not ruled. For nts and prm when the Academic Writing courses are designed (ing N-0062).
8. Paraphrase (D-ing-0034 (b), 02:00): taught here as a writing skill under c2, with a paraphrase frame; Pathway 4 keeps acknowledgement and patchwriting. The mapping's Pathway 4 Intermediate text ("quotation vs paraphrase") needs the same change; for nts (ing N-0072).

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 10 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\bessay\w*
\bdissertation\w*
\bwritten[\s-]+work\b
\bwriting\b
\bassignment\w*
\breflective\b
\bresearch[\s-]+report\w*
\breflective[\s-]+report\w*
\blab[\s-]+report\w*
\breport[\s-]+writing\b
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): the 9 corrected patterns are not identified in ing's files (RJ-0031's report is not held here).

The core moves `research report`, `lab report` and `report writing` to Researching (D-ing-0021 (a)) and `reflective` and `reflective report` to Reflective Practice (D-ing-0022 (b)), proposals for the term list's owner.

## Sources

ADAPT's own files at the paths above, read in the Project mirror at `89ee9c4`; the card drafts from `mta-nts-ho-adp-nts-0007` (`adp-0212-capability-cards.md`); the tier notes from `adp-relay/threads/prm/reviews/adp-0213-tier-notes.md`; ADAPT's registers as of 2 October 2026, 23:23.

---

## Change notes
- 0.1.20: 4 October 2026, 10:37: core pointer to 0.1.22 (ing N-0119).
- 0.1.19: 4 October 2026, 10:03: core pointer to 0.1.21 (ing N-0113).
- 0.1.18: 3 October 2026, 11:10: core pointer to 0.1.20; section 4, the benchmark search patterns, v1.0 and the v2 changes known (D-ing-0050; ing N-0100).
- 0.1.17: 3 October 2026, 06:19: core pointer to 0.1.19; point 6 amended (D-ing-0044; ing N-0093).
- 0.1.16: 3 October 2026, 06:04: core pointer; report writing (D-ing-0024 (a); ing N-0091).
- 0.1.15: 3 October 2026, 05:52: core pointer to 0.1.17 (ing N-0089).
- 0.1.14: 3 October 2026, 04:41: file renamed from `adp-ing-pd-pathway-academic-writing-adapt.md` to `ingest-path-academic-writing-adapt.md`; core pointer to `ingest-path-academic-writing.md` 0.1.16 (ing N-0083).
- 0.1.13: 3 October 2026, 02:00: core pointer to 0.1.13; point 8, paraphrase (D-ing-0034 (b); ing N-0072; G-ing-0125).
- 0.1.12: 3 October 2026, 01:17: core pointer to 0.1.12; the tool named the four pillars self-review (D-ing-0030; ing N-0063; G-ing-0102).
- 0.1.11: 3 October 2026, 01:07: core pointer to 0.1.11; point 7, the teaching of the writing cycle and four pillars (D-ing-0029; ing N-0062; G-ing-0099).
- 0.1.10: 3 October 2026, 00:57: core pointer to 0.1.10 (ing N-0061; G-ing-0096).
- 0.1.9: 3 October 2026, 00:41: core pointer to 0.1.9 (ing N-0060; G-ing-0093).
- 0.1.8: 3 October 2026, 00:38: core pointer to 0.1.8 (ing N-0059; G-ing-0090).
- 0.1.7: 3 October 2026, 00:21: core pointer to 0.1.7; a duplicated phrase in section 2 point 4, written at 0.1.5, removed (ing N-0058; G-ing-0086).
- 0.1.6: 3 October 2026, 00:03: core pointer to 0.1.6 (ing N-0057; G-ing-0082).
- 0.1.5: 3 October 2026, 00:02: core pointer to 0.1.5; scope and signposts (D-ing-0023; ing N-0056; G-ing-0079).
- 0.1.4: 2 October 2026, 23:53: core pointer to 0.1.4; reflective writing to Pathway 10 (D-ing-0022 (b); ing N-0055; G-ing-0075).
- 0.1.3: 2 October 2026, 23:49: core pointer to 0.1.3; points 2 and 3 updated for D-ing-0021 (a) (ing N-0051; G-ing-0068).
- 0.1.2: 2 October 2026, 23:38: core pointer to 0.1.2; point 2 updated for D-ing-0020 (a) (ing N-0050; G-ing-0064).
- 0.1.1: 2 October 2026, 23:29: point 1 updated for D-ing-0019 (a) (ing N-0049; G-ing-0059).
- 0.1.0: 2 October 2026, 23:23: created with the core 0.1.0 (ing N-0047; G-ing-0056).
