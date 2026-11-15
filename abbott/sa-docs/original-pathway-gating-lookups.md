# Original (live) pathway gating — full lookup survey

Hand-maintained, not generated (unlike `gate-process.md`, which
`scratchpad/gate-to-md.js` regenerates from `design-kb.gates.json`'s gate
*definitions*). This file records a different thing: every JSON/file **lookup**
each gate and each enforcement tool actually makes, as verified directly
against the live store on 2 Nov 2026 (`design-kb/design-kb.gates.json`
kbVersion 0.10.5, 24 gates). Regenerate Part A from the store if it changes;
re-grep Part B's tool sections if `manifest-completeness.js` or
`validate-design-schemas.py` change.

Companion file: `pathway-proliferation-gating-lookups.md` covers the same
survey for the design-status redesign in `design-kb.gate-profiles.json`.

## Scope and a phase-order note

The live system runs **6 phases, in strict `sequence` order**: `ONB` (0-3) →
`CXS` (4-9) → `CRS` (10-14) → `LES` (15) → `WRA` (16-19) → `CXP` (20-23).

This does **not** match the 8-phase order quoted when this survey was
commissioned (`ONB > CXS > CRS > LES > CONF > SUMM > WRA > GLOS`). Concretely:

- There is no `CONF` or `SUMM` phase. The 4 gates that plausibly map onto
  those labels — `wra-01_wrapper-open`, `wra-02_wrapper-close`,
  `wra-03_summative`, `wra-04_confidence` — all sit inside the single `WRA`
  phase (sequence 16-19), run *after* `LES`, not as two separate phases
  sitting between `LES` and `WRA`.
- There is no `GLOS` phase at all. Glossary is tracked as its own open task
  (#20, "Design + build glossary system"), not yet a gate in the store.

So the live store's phase set is a strict subset of, and differently grouped
than, the 8-phase expectation. This is not something this survey can fix —
it only records what `design-kb.gates.json` actually contains.

## Part A — per-gate lookup table (all 24 gates, live store)

Columns: `deps` = `dependsOn`; `generation.sources` = the gate's own
(pre-existing) `generation.sources` field, often descriptive prose rather
than a literal path; `pointers` = `agentContext.authoringReview.pointers`
(tightened to explicit file/field references on exactly 4 gates — crs-02,
crs-03, crs-04, crs-05 — during the 0.10.2-0.10.5 agentContext build; every
other gate's `pointers` is original and loosely mirrors `generation.sources`,
not independently re-verified beyond what is reproduced here); `checks` =
`agentContext.validation.checks` ids (declared, see Part C for enforcement
status); `sourceConsultation` = the gate's `sourceConsultation` object,
where set.

| seq | gate id | phase | hardness | kind | deps | generation.sources / pointers | checks | sourceConsultation |
|---|---|---|---|---|---|---|---|---|
| 0 | `onb-01_theme-preset` | ONB | hard-stop | human | — | — | — | — |
| 1 | `onb-02_course-theme` | ONB | hard-stop | agent+human | onb-01 | `catalogue/pathways.json` \| crs-01 source set (no-preset path) | — | — |
| 2 | `onb-03_pitch` | ONB | hard-stop | agent+human | onb-02 | `design-kb/design-kb.tier-bands.json` (tier↔FHEQ relation, cognitive-demand notes) \| `catalogue/context/pathway/<pathway>.json` (both axes independently: `tierProgression.levels` L3-L8, `tierProgression.tierStatements`, `masteryNote`, `capabilities[]` each with tier+fheqLevel) \| same file's `bookGrounding` \| `catalogue/context/subject/benchmarks/universal-reference.json` (`tierReadings.rows`, `pathwayMapping['adapt-<pathway>']`) | — | — |
| 3 | `onb-04_naming` | ONB | hard-stop | agent+human | onb-02, onb-03 | — | — | — |
| 4 | `cxs-01_institutional-context` | CXS | advisory | auto | — | — | — | — |
| 5 | `cxs-02_subject-context` | CXS | advisory | auto | — | — | — | — |
| 6 | `cxs-03_qualifiers` | CXS | advisory | auto | — | — | — | — |
| 7 | `cxs-04_referencing-style` | CXS | advisory | auto | — | — | — | — |
| 8 | `cxs-05_external-standards` | CXS | advisory | auto | — | — | — | — |
| 9 | `cxs-06_resources` | CXS | advisory | auto | — | — | — | — |
| 10 | `crs-01_sources` | CRS | hard-stop | human | onb-02 | — | — | — |
| 11 | `crs-02_thematic-scope` | CRS | hard-stop | agent+human | crs-01 | sources: `crs-01 source set: pathway core Part A + source-map` (prose). pointers (tightened): `crs-01_sources` ;; `design-kb.pathways.json` (`pathways[].chapters`, `bookChunks.primary/shared`, `tiers.<tier>.voiceBand`) | SCP-1, STR-1, TW-1 | `{triggeringFacets:["level"], authorityLevels:["sector"]}` |
| 12 | `crs-03_course-outcomes` | CRS | hard-stop | agent+human | crs-02 | sources: `thematic scope \| pathway core A10 capabilities` (prose). pointers (tightened): `crs-02_thematic-scope` ;; `catalogue/context/pathway/<pathway-id>.json` (`capabilities[].capabilityId`, the A10 core-capability crosswalk) | AL-2, AL-4 | — |
| 13 | `crs-04_lesson-map` | CRS | hard-stop | agent+human | crs-03, crs-02 | sources: `course outcomes \| thematic strands \| source search` (prose, not paths). pointers (tightened): `crs-01_sources` ;; `crs-02_thematic-scope` ;; `crs-03_course-outcomes` | AL-1, AL-2, MCO-1 | — |
| 14 | `crs-05_course-spec` | CRS | advisory | agent+human | crs-04 | sources: `all closed ONB+CRS records` (prose). pointers (tightened): `onb-01_theme-preset` ;; `onb-02_course-theme` ;; `onb-03_pitch` ;; `onb-04_naming` ;; `cxs-04_referencing-style` ;; `crs-01_sources` ;; `crs-02_thematic-scope` ;; `crs-03_course-outcomes` ;; `crs-04_lesson-map` | AL-1, AL-2 | — |
| 15 | `les-01_lesson-proposal` | LES | soft | agent+human | crs-04, crs-02 | pathway core A10 templates + Part C process \| crs-01 source set | — | `{triggeringFacets:["activity"], authorityLevels:["institutional"]}` |
| 16 | `wra-01_wrapper-open` | WRA | soft | agent+human | crs-03, crs-04 | crs-01 source set \| pathway core A10 professional equivalences | — | — |
| 17 | `wra-02_wrapper-close` | WRA | soft | agent+human | crs-03, crs-04 | crs-01 source set \| pathway core A9 Relations + adapt-integration overlap \| `catalogue/pathways.json` (tier ladder) | — | — |
| 18 | `wra-03_summative` | WRA | soft | agent+human | crs-03, crs-04 | crs-03 `courseOutcomeBanks` (the 3 `mcqSet` specs per outcome) \| crs-01 source set \| pathway core | — | — |
| 19 | `wra-04_confidence` | WRA | soft | agent+human | crs-03 | crs-03 `courseOutcomeBanks` (`confidenceStatement` per outcome) | — | — |
| 20 | `cxp-01_subject` | CXP | hard-stop | human | — | — | — | — |
| 21 | `cxp-02_qualifiers` | CXP | hard-stop | human | — | — | — | — |
| 22 | `cxp-03_exemplar-programmes` | CXP | advisory | auto | — | — | — | — |
| 23 | `cxp-04_context-generation` | CXP | soft | agent+human | cxp-01, les-01, wra-01, wra-02, wra-03 | subject benchmark corpus (adapt-integration benchmark search patterns) \| baseline subject (cxp-01=baseline): `catalogue/context/subject/benchmarks/universal-reference.json` \| standing standards registry \| cxs-04 referencing \| crs-01 source set | — | `{triggeringFacets:["level","institution","faculty","activity"], authorityLevels:["sector","institutional"]}` |

## Part B — tool-level lookups

### `tools/manifest-completeness.js`

`ROOT = path.resolve(__dirname, '..')` (repo root). Direct file/dir reads
(grep-verified, `path.join(ROOT, ...)` call sites):

- `content/context-packs/` — directory scan, clause 3 ("context packs imply
  cxp-04 record").
- `design-kb/design-kb.skeletons.json` — read at **4 separate call sites**
  (`loadArchetypePositionRules`, `loadSkeletonBlockKeys`,
  `loadWrapperBaseKeys`, and one earlier inline check), each with its own
  cache variable — not a single shared load.
- `source-kb/source-maps/` — directory scan (`loadSourceMaps`), one file per
  source, cached as `sourceId -> Map(chunkId -> chunk)`.
- The course-design manifest itself (passed as the tool's argument), via
  `lib/course-resolve.js`'s `resolveCourse`.
- Local helper modules: `./lib/page-match.js` (`matchesPageKey`),
  `./lib/course-resolve.js` (`resolveCourse`), `./lib/phase-gate.js`
  (`scaffoldBoundaryStatus`).

Check ids actually implemented in code (grep-verified, authoritative —
supersedes any earlier recollection of this list): `AL-3a`, `AL-3b`, `AL-4`,
`BKS-1`, `CK-1`, `CO-1`, `CP-1h`, `CP-1i`, `LPG-1`, `MK-1`, `OC-1`, `PLR-1`,
`PSR-1`, `RP-1`.

**`AL-1` and `AL-2` are absent from this list.** They exist only as
*declared* `agentContext.validation.checks` ids on 4 gates (crs-03, crs-04,
crs-05) — there is no automated code check for either in
`manifest-completeness.js`. Enforcement today is agent-instruction-only.

### `tools/validate-design-schemas.py`

Stores it can validate, one CLI flag per store: `--course-design`, `--gates`,
`--course-design-gates` (an *alternate* gates store to resolve a
`--course-design`'s gate ids/shapes against — distinct from `--gates`, which
validates the gates file itself; used by `phase-confirm.js`'s read-back or a
test fixture that was written against a non-default store), `--source-kb`,
`--institutional-kb`, `--vocab-kb`, `--hecos-kb`, `--skeletons`, `--palette`,
`--name-bank`, `--gate-profiles`, `--tier-bands`, `--activity-patterns`,
`--content-shapes`, `--pathways`, `--source-maps` (directory scan),
`--catalogue` (`catalogue.json` + `catalogue/pathways.json` + every
`catalogue/pathways/<pathway>.json`), `--test-fixtures`, `--all-defaults`
(validates every store above at its fixed repo path; `--course-design` is
excluded since it has no fixed default — PR-S-35).

Structural-invariant ids found in the file (grep-verified; each tied to a
named prompt/decision in its own comment trail): `CS-1` (book content
shapes, 7 anchored on Horn's taxonomy), `SMAP-1` + amendment (source maps:
one file per source, pathwayTag rules), `BM-1` + amendment (source-map
block-type list, QAAVector), `CAT-1` + amendment (`catalogue.json`/
`catalogue/pathways.json`), `HSV-1` (hecos-kb vs `vocab-kb/cah.json`),
`TLS-1`/`HMD-1` (vocab-kb/ layout), `LCR-1`/`GF-1` (per-gate record shape,
bare Phase-A gate ids), `CPL-1` (skeleton slot/depth), `SHP-1` (closed
record vs its resolved shape — prints `PASS`/`FAIL` per record), `GI-2`
(provenance vs hardness/defaultType — prints `PASS`/`FAIL` per record),
`NSK-1` (crs-04/after-outcomes gate-id typing), `LK-1` (`crs-04_lesson-map`
`decidedValue.lessons[].key` dedup), `AL-4` (crs-03 `courseOutcomeBanks[]
.outcomeId`, confidence).

Resolves a `--course-design`'s gates against `design-kb/design-kb.gates.json`
by default, or `--course-design-gates` for an alternate store.

## Part C — honest caveats

- **`generation.sources` is descriptive prose on most gates, not a
  machine-readable path list.** E.g. `crs-04_lesson-map`'s
  `generation.sources` reads `"course outcomes | thematic strands | source
  search"` — three phrases, no file path among them. Only the 4 gates edited
  2 Nov 2026 (crs-02, crs-03, crs-04, crs-05) have an
  `agentContext.authoringReview.pointers` field deliberately tightened to
  explicit file+field references; every other gate's `pointers` is original
  and was not independently re-verified beyond the literal string reproduced
  in Part A.
- **`AL-1` and `AL-2` have zero automated enforcement.** They are declared on
  4 gates' `agentContext.validation.checks` and are enforced only by asking
  the agent to check them at the gate (`gate.md` step 1b) — not by any code
  path in `manifest-completeness.js` or `validate-design-schemas.py`.
- **Phase-order mismatch**, restated from above: live is `ONB → CXS → CRS →
  LES → WRA → CXP`. There is no `CONF`, `SUMM`, or `GLOS` phase; `WRA`'s 4
  gates cover what `CONF`+`SUMM` likely meant, as one phase not two; glossary
  does not exist as a gate at all yet (open task #20).
