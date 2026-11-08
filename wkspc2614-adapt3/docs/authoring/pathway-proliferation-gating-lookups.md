# Pathway-proliferation gating — full lookup survey

Companion to `original-pathway-gating-lookups.md` (the live system). This
file covers the **design-status** redesign held in
`design-kb/design-kb.gate-profiles.json` (kbVersion 0.1.1) — the profile the
user's shorthand "multiplies the old one by three" refers to
(`pathway-distillation`: all three tiers built together, from the pathway's
own benchmarks rather than free thematic strands) — plus the
`single-course` profile it shares its machinery with, and the
`built-course-shape` profile, which is `status: "live"` and documents, for
comparison, what the current 4-gate `original-pathway-gating-lookups.md`
flow actually produces.

**None of this is wired into `design-kb/design-kb.gates.json`.** Both
`single-course` and `pathway-distillation` are `status: "design"`. Treat
every lookup below as a documented intention, not a running gate, unless
stated otherwise.

## The underlying data: the 9 capabilities and the 18 evidence statements

Before any gate-profile step runs, two generated catalogue files ground the
whole redesign:

**The 9 — `catalogue/context/pathway/<pathway>.json`, `capabilities[]`.**
3 per tier (`i1-i3` introductory, `d1-d3` intermediate, `e1-e3` advanced).
Each entry carries `rowId`, `capabilityId`, `tier`, `fheqLevel`, `statement`,
`knowledgeKind`, `qf`, `book`, `competency`, `vocabulary`, `bookGrounding`.
**Correction to a common assumption:** these are *not* uniformly pitched at
FHEQ L5/L6. Verified directly on `criticality.json`: `i1=L3, i2=L4, i3=L5,
d1=L4, d2=L5, d3=L6, e1=L5, e2=L6, e3=L7` — a spread of L3 to L7, FHEQ levels
are indicative and cross-cutting (a tier can span several levels and a level
several tiers), not a bucket. Only 4 of the 9 (`i3, d2, e1, e2` — plus
`d3`/`e1` depending on how the L5/L6 band is drawn) actually sit at L5/L6.
The file also carries a `benchmarkKeys` block (`note, sources, byTier,
attribution`, built by `tools/key-benchmark-tiers.py`) and a `source` block
recording the off-repo ingest files it was built from (`core, plan, wide,
vocab, eau, adapt`, all under a path beginning `/home/user/wkspc2614-adapt`
— **confirmed absent on this machine**; the raw ingest cannot currently be
re-derived or audited from this repo, only the already-built
`capabilities[]` output can).

**The 18 — `catalogue/context/pathway-evidence/<pathway>.json`.** Exactly 2
evidence examples per capability (one `conceptual`, one `applied`) × 9
capabilities = 18, 6 per tier. Each pair: `{kind, title, example, artefact,
grounding[]}`. Validated by `tools/check-pathway-evidence.py` — rules taken
directly from its docstring: exactly 1 conceptual + 1 applied per capability;
conceptual grounding must cite the capability's own ingested theory id or
`"model: <name>"`; word-count bounds (title ≤12, example 35-90, artefact
8-30); no em dash; never the phrase "academic skills". Directly re-run: **all
13 pathways pass**, not just criticality (files are marked
`"status": "drafted"`, i.e. authored and validated but not yet gate-closed
anywhere).

**An .md export of the 9+18 already exists.** `tools/
render-pathway-benchmarks-md.py` writes `gate-experiment/
pathway-capabilities-and-benchmark-keys.md` (242,505 bytes, 1,307 lines,
re-run directly, exit 0) — one file covering all 13 pathways' capabilities
and benchmark keys in one place. A separate, related tool,
`tools/build-prompt-sets.py`, generates RTCF student-facing chat-prompt
starters from the same benchmark keys into
`src/components/adapt-grow-promptbuilder/libraries/
academic-practice-prompts.json` — not a generation formula for the 18
itself, but downstream of it.

## The generation "formula"

Two distinct things answer "what was the 18 generated from":

1. **Generating the 18 itself** — governed by `check-pathway-evidence.py`'s
   validation rules above. There is no separate, reusable prompt string
   recorded in the repo for this step; the rules are the closest thing to a
   formula.
2. **Distilling the 18 into learning outcomes** — the **book-first,
   two-layer method**, settled 2 Nov 2026, documented in full in
   `gate-experiment/crs-redesign.md`. Layer 1 (primary): one LO per real
   section of the pathway's own book chapter
   (`source-kb/source-maps/book-excelling-at-university-2026.json`), book
   cross-references and definitions taking precedence over external theory.
   Layer 2 (secondary, fill-to-minimum only): where Layer 1 falls short of 5
   LOs, fill using (a) the pathway's own applied/professional benchmark
   evidence, and/or (b) at most one named theory lesson **per tier** (each
   tier is its own Adapt course, so each tier carries its own theory
   budget), anchored inside an existing book-grounded lesson's context, never
   freestanding.

   This explicitly **supersedes an earlier "merge rule"** (merge two adjacent
   benchmark statements into one outcome where they cluster), which was
   hand-tested against all 9 capabilities of two real pathways (criticality,
   referencing) and never fired once — 6/6/6 in both, because every
   pathway-evidence pair is deliberately authored as one theory-grounded
   example plus one distinct professional-practice example, so the two
   members of a pair almost never cluster.

   **Worked trace (criticality, settled 2 Nov 2026).** Book chapter 8 splits
   3 introductory / 3 intermediate / 5 advanced sections (not the even 3/3/3
   the capability model assumed — advanced under-represents the book:
   capability `/05` alone maps to 4 of the 5 advanced sections, and `#e3`
   has no book section at all, a pure Hyland-theory import). Applying the
   method settles criticality at **5 / 5 / 6 lessons**
   (introductory/intermediate/advanced), within the 5-floor/6-ceiling per
   tier:

   | Tier | # | LO source | Traces to |
   |---|---|---|---|
   | Intro | 1 | Book: defining critical thought | `ch8/defining-critical-thought`, `#i3` |
   | Intro | 2 | Book: thinking critically about academic sources | `ch8/thinking-critically-about-academic-sources`, `c1` |
   | Intro | 3 | Book: opening up the discourse in practice | `ch8/opening-up-the-discourse-in-practice`, `/02` |
   | Intro | 4 | **Theory** — Bloom's full taxonomy ladder, orienting preview | Anderson & Krathwohl 2001 |
   | Intro | 5 | Benchmark fill — stakeholder mapping (food bank) | `/02` applied evidence |
   | Inter | 1 | Book: analysing an interpretation | `ch8/analysing-an-interpretation`, `/01` |
   | Inter | 2 | Book: evaluating interpretations | `ch8/evaluating-interpretations`, `/03` |
   | Inter | 3 | Book: engaging with journal articles (Table 8.1) | `ch8/engaging-with-journal-articles`, `/04` |
   | Inter | 4 | Benchmark fill — recognising analysis/evaluation without steer words | `/01` applied |
   | Inter | 5 | Benchmark fill — method-check/briefing (software internship) | `/04` applied |
   | Adv | 1 | Book: active vs passive approaches | `ch8/active-and-passive-approaches` |
   | Adv | 2 | Book: forming judgements | `ch8/forming-judgements`, `c2` |
   | Adv | 3 | Book: applying synthesis | `ch8/applying-synthesis` |
   | Adv | 4 | Book: the language of criticality | `ch8/language-of-criticality`, `/05` |
   | Adv | 5 | Book: discipline-specific vocabulary | `ch8/discipline-specific-vocabulary`, `/05` |
   | Adv | 6 | **Theory** — Hyland's 2005 stance model, built on LO3 | Hyland 2005, restores `#e3` |

   Status: agreed with human gate 2 Nov 2026; not yet run on a second or
   third pathway, so it is open whether 5/5/6 is typical or specific to
   criticality's own chapter shape.

## Part A — the 3 gate profiles, step by step

### `single-course` (status: design) — one tier, query-layer build

| step id | gates | decider | inputs | produces |
|---|---|---|---|---|
| `theme` | onb-01, onb-02 | agent+human | `catalogue/context/pathways.json` | the pathway |
| `tier` | onb-03 | agent+human | `design-kb.tier-bands.json` | intro\|inter\|advanced\|none |
| `levels` (planned) | — | agent+human | tier-bands, `pathway/<p>.json` `tierProgression.levels` | one or adjacent levels |
| `ctx-shell` (CXS, pre) | cxs-01..04, cxs-06 | auto | reserved placeholders, all auto-pass | the context shell, in place before authoring starts |
| `fork01-frameworks` | cxs-05 | human (change: was auto) | `catalogue/context/shared/cross-cutting.json` `frameworks` (FHEQ, CQFW, FQHEIS/SCQF, QF-EHEA) | chosen framework(s) |
| `fork01-benchmarks` (planned) | — | human | `pathway/<p>.json` capabilities+benchmarkKeys, `universal-reference.json` | 0-9 of the pathway's 9 benchmarks selected |
| `ao-01` (planned) | — | agent+human | chosen frameworks+benchmarks, `pathway-evidence/<p>.json` (the 18), the tier | the tier's flat LOs, typically 4-6, straight from its 6 benchmark statements — no further distillation |
| `ao-04` (planned) | — | agent+human | AO-01, `tools/voice-lint.js` | the ONB shell context statement (voice-linted) |
| `lessons` | crs-04 | agent+human | AO-04's flat LOs, `design-kb.content-shapes.json` | up to 6 lessons, one LO each |
| `fork02-shell` | cxp-01 | agent+human | baseline (`universal-reference.json`) \| group (CAH1/2 via `tools/resolve-subject-benchmark.js`, `docs/contexts/cmet/cardiff_met_school_hesa_shortlist.json`) \| specific (HECoS/CAH3) | the shell's subject grounding |
| `fork03-qualifiers` | cxp-02 | human | `docs/authoring/qualifier-list-2026-10-04.md`, `universal-reference.json` `graduate_competency`, Advance HE ingests | up to 6 qualifiers, 4 categories |
| `ao-02` | cxp-04 | agent+human | fork02-shell's resolved benchmark, AO-01 | context-specific competency attributes + worked examples, merged via `merge-context.js` |
| `ao-03` (planned) | — | agent+human | each chosen qualifier's ingest | qualifier-specific competency attributes added to the context pack |

`continuesWith`: `crs-05_course-spec`, `les-01_lesson-proposal`,
`wra-01..04`.

### `pathway-distillation` (status: design) — all three tiers at once

Same `theme` and `ctx-shell` steps as `single-course` (CXS runs once, shared
across tiers). Then diverges:

| step id | gates | decider | inputs | produces |
|---|---|---|---|---|
| `pathway-statements` (planned) | — | auto | `pathway/<p>.json` capabilities(9)+benchmarkKeys, `pathway-evidence/<p>.json` (the 18) | the 18 statements, 6/tier, with capability+attribution+key |
| `tiered-outcomes` (planned) | — | agent+human | `source-kb/source-maps/book-excelling-at-university-2026.json`, the tier's 6 statements, tierReadings, tier-keyed benchmarks | the tier's flat LOs, book-first two-layer method (see above) |
| `lessons` | crs-04 | agent+human | the tier's flat LOs (5-6), content shapes | 5-6 lessons per tier (hard floor 5, ceiling 6), one LO each |
| `progression-signposting` (planned, no generator yet) | — | agent+human | all three tiers' LOs + lesson maps together | forward/backward signposts between tiers — annotation, not new gate content |
| `fork02-shell` | cxp-01 | agent+human | same as single-course, run **once**, shared | subject grounding shared across all 3 tiers |
| `fork03-qualifiers` | cxp-02 | human | same as single-course | up to 6 qualifiers, shared |
| `ao-02` | cxp-04 | agent+human | fork02-shell's resolved benchmark, each tier's LOs | context-specific attributes, generated once, merged into all 3 tiers' shells |
| `ao-03` (planned) | — | agent+human | qualifier ingests | qualifier-specific attributes, shared across all 3 tiers |

`continuesWith`: `les-01_lesson-proposal`, `wra-01..04` (no `crs-05` listed
for this profile).

### `built-course-shape` (status: live) — what actually ran

Kept in `gate-profiles.json` as its own named profile specifically so the
two redesigns above can be compared against, or fallen back to, what is
really live. Matches `original-pathway-gating-lookups.md` Part A exactly for
`onb-01..03`, `crs-02..04`: free thematic strands (5-10, human-authored) are
the structural source, not pathway benchmarks; no query layers
(TIER/LEVEL(S)/FORK01-03/AO-01-04) exist; 4 course outcomes (gate allows
3-5, built courses all chose 4); 4 parallel lessons, one course outcome +
3 lesson outcomes each (12 total), no synthesis lesson. Checked against the
real built courses (criticality, ai-technology, academic-writing,
presenting) on 29 Oct 2026.

## Part B — the query-layer chain (onboarding side, `single-course`/`pathway-distillation` shared)

From `gate-experiment/query-layers-and-generation.md` (status: design scope,
branch `gates/tri-tier`):

```
1  TIER          intro | inter | advanced | none                    (optional)
2  LEVEL(S)      auto from tier bands | human: single or grouped | none
     FORK01  GENERIC STATEMENTS
       1  qualification frameworks (user selects)
       2  universal / pathway benchmarks (0-9 of the pathway's 9)
          -> AO-01  GENERIC COMPETENCY ATTRIBUTES CONTEXT: 6 generic benchmarks
     FORK02  SHELL vs CONTEXT SLOT
       1  baseline shell | 2  group context shell | 3  specific context shell
          -> AO-02  CONTEXT SPECIFIC COMPETENCY ATTRIBUTES CONTEXT
     FORK03  QUALIFIERS (up to 6, four categories)
          -> AO-03  QUALIFIER SPECIFIC COMPETENCY ATTRIBUTES CONTEXT
4  AO-04  ONB SHELL CONTEXT STATEMENT (academic prose, voice-linted)
5  flat tiered learning outcomes (settled 2 Nov 2026 — see "flat 6" below), then the lesson map
```

Layer → gate-today → data-it-reads → status table (reproduced from the
source doc, all verified against the live store):

| Layer | Gate today | Data it reads | Status |
|---|---|---|---|
| THEME | onb-01, onb-02 | `catalogue/context/pathways.json` | exists |
| 1 TIER | onb-03 | `design-kb.tier-bands.json` | exists, `none` option to add |
| 2 LEVEL(S) | none | tier bands; `pathway/<p>.json` `tierProgression.levels` (L3-L8) | gap: tier bands list L3-L7 only, no L8 |
| FORK01.1 frameworks | cxs-05 (auto, reserved) | `cross-cutting.json` `frameworks` | data exists, needs human-select change |
| FORK01.2 benchmarks | none | capabilities + benchmarkKeys + pathway-evidence (18) + universal-reference.json | data exists, gate to build |
| AO-01 | none | the above | to build |
| FORK02 shell | cxp-01 (+ baseline routing) | baseline: universal-reference.json; group: CAH1/2 via `tools/subject/core/vocab/cah.json`; specific: HECoS/CAH via `tools/resolve-subject-benchmark.js` | now available, not yet consumed here: `tools/cmet-context.js` (added 5 Nov 2026) resolves School/Faculty→HESA-subject grouping against the `tools/context-cmet` submodule's HECoS/CAH-tagged course data; FORK02/cxp-01 itself stays design-status and unwired this session (see Part C) |
| AO-02 | cxp-04 | subject benchmark corpus, pathway mappings, **+ context-cmet's HECoS/CAH-to-pathway mapping (`tools/cmet-context.js`, wired live 5 Nov 2026)** | partial — the CMET source is live and additive (fills the empty `pathwayMapping` in 53 of 55 host benchmark files); AO-02 as a whole is still design-status |
| FORK03 qualifiers | cxp-02 (max 3/3 today), cxs-03 (reserved) | `qualifier-list-2026-10-04.md`, `graduate_competency` (20, in universal), Advance HE ingests | gap: no qualifier JSON mapping each qualifier to its ingest yet |
| AO-03 | none | qualifier ingests | to build |
| AO-04 | none | AO-01 to AO-03, `tools/voice-lint.js` | to build |
| 5 outcomes | crs-04 | AO-04 | exists (crs-04); crs-03 has no job left under flat-6 |

**"Flat 6" ruling (settled 2 Nov 2026, supersedes a 29 Oct 2026 "3 course + 6
lesson outcomes" draft):** AO-01's generic benchmarks (contextualised by
AO-02+AO-03 into AO-04) ARE the tier's final learning outcomes, flat — not
distilled to 3 and proliferated back to 6. They map one-to-one onto up to 6
lessons (single-course) or 5-6 (pathway-distillation), each ~4-6 pages.

## Part C — open structural blockers (none of this is wired live)

- **`crs-03_course-outcomes` loses its job entirely** under flat-6 — there
  is no course-outcome tier left to populate. This is a bigger live-gate
  change than demoting `crs-02_thematic-scope`: `crs-04_lesson-map`'s
  dependency note and every lesson's `serves` field assume a course-outcome
  id (`design-kb.gates.json:748-755`), and `wra-03_summative`'s AL-3 rule
  ("two summative questions per course outcome",
  `design-kb.gates.json:1361-1366`) has nothing to count against — open
  whether it becomes two-per-LO or one-per-LO. Needs explicit sign-off
  before `crs-03` is touched live.
- **`crs-02_thematic-scope` is demoted** to optional colour under both
  design profiles — benchmarks drive structure instead of free strands.
  Also needs explicit sign-off.
- **The 9 capabilities' own off-repo ingest sources are inaccessible from
  this workspace** (`/home/user/wkspc2614-adapt`, confirmed absent) — the
  generated `capabilities[]`/`benchmarkKeys` output can be read and used,
  but not re-derived or audited against its raw ingest from here.
- **L8** is not yet in the tier bands (only L3-L7), despite
  `tierProgression.levels` elsewhere documenting it as cross-cutting
  alongside L7.
- **A CMET course-data tree now exists and is wired for lookup, but not yet
  consumed at FORK02.** `tools/cmet-context.js` (added 5 Nov 2026) wraps the
  private `tools/context-cmet` submodule (not the flat
  `docs/contexts/cmet/cardiff_met_courses.csv` the host already holds, which
  carries no HECoS/CAH tags) and resolves a HECoS/CAH code or subject text to
  its School/Faculty grouping, Cardiff Met course and school data, and
  pathway mapping, by shelling out to the submodule's own CLI. It is live
  only at `cxp-04_context-generation` (AO-02) this session, as an additive
  source alongside the existing baseline/fork02-shell resolver, and carried
  as a shape (not a live selector) on the still-reserved
  `cxs-02_subject-context` for when it is un-reserved — confirmed 5 Nov 2026
  that un-reserving, if it happens, is human-select only, never
  auto-derived. **FORK02/cxp-01 itself — the design-status site in this doc
  for an actual School→HESA-subjects grouping choice — has not been
  touched**, so the specific gap this bullet names (a bare CAH1/CAH2 pick for
  sport/exercise science, nursing, midwifery, physiotherapy, podiatry,
  dietetics or speech and language therapy silently falling back to an
  unrelated entry sharing only the same CAH2 ancestor) is not yet closed;
  closing it means wiring `cmet-context.js` into FORK02 itself, a follow-on,
  not done here. Two deliberate non-translations, confirmed rather than
  invented: context-cmet's extra `self-development` pathway has no host
  course-slug counterpart and is not synthesised one; and tier→row (the host
  records tier, not FHEQ level) is never guessed — `--row` is passed through
  only when a caller supplies one explicitly.
- **No qualifier JSON** yet mapping each of the (proposed) 6 qualifiers
  across 4 categories to its own ingest.
- **The book-first two-layer LO method has been run on exactly one
  pathway** (criticality). It is not yet known whether its 5/5/6 lesson
  split is typical or specific to that pathway's chapter shape.
- **Phase-order note, same as doc 1:** neither design profile introduces a
  `CONF`, `SUMM`, or `GLOS` phase. Both profiles tag steps with a `stage`
  field (`pre` / `course-body` / `post`) instead — `pre` = CXS before
  authoring starts, `course-body` = the tier/LO/lesson build, `post` = CXP
  after the lessons exist. This is a different organising axis from an
  8-phase list, not a renamed version of it.
