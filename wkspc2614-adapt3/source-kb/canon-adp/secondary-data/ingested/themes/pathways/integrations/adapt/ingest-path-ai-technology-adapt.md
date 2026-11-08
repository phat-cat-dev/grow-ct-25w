---
document:  integration: how ADAPT uses the AI and Technology pathway
core:      `pathways/ingest-path-ai-technology.md` 0.1.0 (`ing:doc:pathway-ai-technology`)
consumer:  ADAPT (the academic skills e-learning programme in the Adapt Framework, SCORM in Moodle)
owner:     adp ing (drafts); ADAPT rules
version:   0.1.0, 4 October 2026, 10:06 (ing N-0114)
status:    drafted; never ingested into any store
read from: ADAPT's Project mirror (`adp/adp-mirror/`, generated from `d9cf3af`); not evidence of repo state
---

# AI and Technology in ADAPT

## 1. Where the pathway lives in ADAPT

| What | Where | State |
|---|---|---|
| The pathway's entry, Pathway 12, "AI & Technology", no chapter (authored, Track B) | `catalogue/context/pathways.json` 1.0.0 | in the catalogue |
| Its three tiers, focus understand AI, use AI critically, evaluate, create with and act ethically around AI | `catalogue/context/pathways/ai-technology.json` | all `planned`; no course slug; voice band "Provisional: confirm at SME sign-off." |
| The teaching prose, with its sources, framing decision, cross-links and notes | `docs/curriculum/pathway-tier-mapping.md` Draft v3 (v3.1), Pathway 12 | draft; needs SME approval before authoring |
| The capability cards and tier notes | adp-0212 (RJ-0047), adp-0213 (RJ-0053): six cards, three developed, two extended, one unplaced, none introduced | drafts; D-0058 owed |
| The term list | `tools/pathways/core/rules/pathway-term-lists.json` v1.0, 8 patterns for this pathway | v2 ruled (D-0028), held on RJ-0033 |

ADAPT calls it "Pathway 12"; the core uses only `path:ai-technology`.

## 2. How ADAPT uses it

1. **Courses.** One SCORM course per tier, "AI & Technology: <Tier> Stage" (TN-1), from a shell and context packs (PKS-1). None built in the mirror.
2. **SME sign-off first.** The mapping requires subject expert approval before authoring, not just a pressure-test.
3. **Context coupling, heavily.** The mapping's examples are the University of Sheffield's; Cardiff Met's approved tools, local policy and disclosure process are to be supplied by the SME at authoring and replace them. The Cardiff Met AI Hub is login-walled. This is institutional context: in ADAPT's terms an institutional context pack, and an ORGDAT matter once that project exists.
4. **Currency.** The fastest-moving pathway: courses are to be built to be updated; every policy statement needs a date and an owner.
5. **Cross-links.** Referencing (Pathway 4) carries integrity; this pathway is its AI-specific extension, to be coordinated so the two reinforce rather than repeat. Also Criticality (5), Finding and Using Sources (3), Academic Writing (6) and Revising and Exams (8). The catalogue's `routes` are null.
6. **Practice connection and summative parity** as for every pathway (D-0047; tier specification section 7).

## 3. Points open for ADAPT

1. D-0058: the cards. No Introductory card; `/04` describes the pathway's design. The core proposes c1 at Introductory and `/04` as a design note (core Part E item 3), for Abbott and then nts to land in `path`.
2. Key theory open (core Part E item 4); once ruled, the uningested sources go to META's ing as a handover.
3. Who supplies Cardiff Met's AI policy, tools and disclosure process, and when.
4. Benchmark evidence for the cards (adp-0212's drafts): `/01` 165 chunks across 45 texts; `/02` 118 across 22; `/05` 46 across 28; `/04` 29 across 23; `/03` 14 across 12; `/06` 3 across 3. `\btechnolog\w*` is one of the nine broad terms D-0028 holds provisional; most hits are about subject technology, not AI. From the 2026 editions, generative AI is a cross-cutting theme of QAA benchmark statements (META's benchmark statements run), so new editions will carry direct statements.

## 4. Benchmark search patterns

The term list v1.0 (`tools/pathways/core/rules/pathway-term-lists.json`, from QAAVector's `STRENGTH_TERMS` at `066c17ff`), 8 patterns for this pathway, case-insensitive; a benchmark statement whose extract matches one is tagged `direct` (QV-TAG-2 part (e)). The core keeps them as words in A10; the patterns are ADAPT's tool and live here (D-ing-0050).

```
\bartificial[\s-]+intelligence\b
\bAI\b
\bGenAI\b
\bgenerative[\s-]+AI\b
\btechnolog\w*
\bdigital[\s-]+skills\b
\bdigital[\s-]+literacy\b
\bdigital[\s-]+tools\b
```

Term list v2 (D-0028, ruled 18:51, not committed; RJ-0033 commits it): holds `technolog*` provisional (over 10% of chunks), to be narrowed after the pilot if the mapper rejects many hits (D-0031); the 9 corrected patterns are not identified in ing's files.

## Sources

ADAPT's own files at the paths above, read in the Project mirror; the card drafts and their benchmark evidence from `mta-nts-ho-adp-nts-0007` (`adp-0212-capability-cards.md`); the tier notes from `adp-relay/threads/prm/reviews/adp-0213-tier-notes.json`; ADAPT's registers as of 4 October 2026, 10:06.

---

## Change notes
- 0.1.0: 4 October 2026, 10:06: created with the core 0.1.0 (ing N-0114).
