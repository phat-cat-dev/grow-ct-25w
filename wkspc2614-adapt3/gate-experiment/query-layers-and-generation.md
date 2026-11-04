# Query layers + the onboarding generation flow

**Status: design scope (not wired).** Branch `gates/tri-tier`. Revised 29 Oct 2026 to
Abbott's restated layers (`abbott/# TODOs.md`, "SCOPE THE COMPLETE QUERY LAYERS"). Each
layer is mapped to the gate that holds it today, the data it reads, and what is missing
(section 3).

## 1. The query layers (onboarding)

The pathway (THEME) is already chosen by `onb-01_theme-preset` / `onb-02_course-theme`.
The layers below then resolve the context top-down; each narrows the next, and four agent
outcomes (AO-01 to AO-04) accumulate into the SHELL context.

```
1  TIER          intro | inter | advanced | none                       (optional)
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
5  3 course outcomes + 6 lesson outcomes (2 each), then the lesson map (section 2)
```

**1. TIER** (optional): introductory, intermediate, advanced, or none (defer to LEVEL).

**2. LEVEL(S)** (auto or optional, depending on TIER: single, grouped or none).
- With a tier: levels are auto-decided by the tier bands (`design-kb.tier-bands.json`).
- With no tier: the human defines one or more levels. Grouped levels are generally
  **adjacent** (e.g. L3 / L4).
- **Exception: L7 and L8 cross all tiers.** An L7 or L8 introductory / intermediate /
  advanced course takes the same concepts and pitches them at postgraduate or doctoral
  level. L7 and L8 are cross-cutting levels, not rungs on the same ladder.

**FORK01: GENERIC STATEMENTS**
1. **Qualification frameworks:** the user selects a specific one (FHEQ, CQFW, the Scottish
   FQHEIS within SCQF, QF-EHEA / Bologna).
2. **Universal benchmarks:** auto-generated from the previous decisions. If neither TIER
   nor LEVEL was set, the user is offered the pathway's **9 generic pathway benchmarks** (its
   capabilities) and selects from 0 to 9. Both 0 and 9 treat all nine equally.
- **AO-01 = GENERIC COMPETENCY ATTRIBUTES CONTEXT.** The agent refers to the chosen
  ingested frameworks, universal and pathway benchmarks and the tier (including the fuzzy
  tops), groups candidates, and with agent suggestion plus human confirmation or amendment
  boils them down to **6 generic benchmarks** for the pathway. These are the initial
  generic basis for the course learning outcomes.

**FORK02: SHELL vs CONTEXT SLOT**
1. **Baseline shell:** the universal statements, analysed as a subject benchmark would be,
   authored from a generic perspective.
2. **Group context shell:** (a) a group identity (e.g. School of Sport, School of Health
   Sciences, Faculty of Aeronautics) and (b) the group of HESA subjects under it, so the
   relevant benchmark data can be searched. Set by the human.
3. **Specific context shell:** one HESA subject or code, or a general topic area given by
   the user.
- **AO-02 = CONTEXT SPECIFIC COMPETENCY ATTRIBUTES CONTEXT.**

**FORK03: QUALIFIERS:** the earlier ONB qualifiers plus the graduate competencies from
the universal JSON, in four categories:
1. pedagogical
2. professionally oriented
3. cross-cutting agendas
4. graduate competencies / capital

Each chosen qualifier directs the agent to the ingested context for that qualifier, which
adds to the developing SHELL context. The user applies **up to 6** (the number may vary).
- **AO-03 = QUALIFIER SPECIFIC COMPETENCY ATTRIBUTES CONTEXT.**

**By this stage the agent holds:** level(s) + chosen frameworks + chosen universal
benchmarks + AO-01 (6 course / pathway benchmarks) + the chosen shell (baseline; group,
i.e. HESA subject groups and / or codes under a user-given identity; or specific, one HESA
subject or code) + AO-02 + up to 6 qualifiers + AO-03.

**4. AO-04 = ONB SHELL CONTEXT STATEMENT:** the product of ONB. A context statement that
restates the SHELL context in academic prose, voice-linted.

**5. The course's learning outcomes**, generated from AO-04 by the proliferation in
section 2: 3 course outcomes, each with 2 supporting lesson outcomes (6 learning outcomes
beneath the 3), then the lesson map.

## 2. Distil (flat 6 - settled 2 Nov 2026, supersedes the 6 -> 3 -> 6 draft below)

**Ruling:** no separate course-outcome tier. AO-01's 6 generic benchmarks (set in
context by AO-02 + AO-03 -> AO-04) are the tier's 6 final learning outcomes, flat -
not distilled further to 3 and proliferated back out to 6. Every outcome still traces
to its source statement(s) in the 18, one level closer than before.

```
DISTIL    18 pathway statements (the 9 capabilities x 2 evidence examples, 6 per tier)
          -> 6 tiered outcomes (single course: AO-01's 6 generic benchmarks,
             set in context by AO-02 + AO-03 -> AO-04)
          = the tier's 6 learning outcomes. FLAT. No further distillation to 3.
(CRS onwards)
          6 LOs -> up to 6 lessons, one LO each, inside the existing 4-6 lesson band.
          A synthesis lesson is optional colour (content-shape driven) when the
          content calls for one, not a structural slot reserved against a 3-vs-6 split.
```
**Lesson interior size (2 Nov 2026):** one LO per lesson is not thin - each lesson
carries circa 4-6 pages to develop its one LO well (orientation, concept, worked
example, analysis, practical guidance, reflective prompt - the six-part flow in
`CLAUDE.md`), not a single page per outcome.
Proliferation is constrained by the tier and / or level choices. At every gate the
agent first reviews the ingested data it is pointed at (`agentContext` on each gate in
`design-kb.gates.json`). Both runs are defined as gate profiles in
`design-kb/design-kb.gate-profiles.json`: `single-course` and `pathway-distillation`
(all three tiers at once).

**Live-gate impact (not yet resolved, flagged for sign-off alongside the `crs-02`
demotion):** `crs-03_course-outcomes` loses its job - there is no course-outcome tier
to distil to. `crs-04_lesson-map`'s dependency note ("Lessons serve the course
outcomes") and every lesson outcome's `serves: <course outcome id>` field
(`design-kb.gates.json:852-855`) need a flat-LO equivalent. `wra-03_summative`'s AL-3
rule - "exactly two summative questions per course outcome", sourced from `crs-03`'s
`courseOutcomeBanks` (`design-kb.gates.json:1361-1366`) - has no course outcome to
count two-per against; open whether it becomes two-per-LO (12 total) or one-per-LO (6).

### Superseded draft (6 -> 3 -> 6, settled 29 Oct 2026, replaced 2 Nov 2026)
```
DISTIL           18 pathway statements (6 per tier) -> 6 tiered outcomes -> 3 course
                 outcomes                            [AGENT SUGGESTS / HUMAN CHOOSES]
PROLIFERATE      3 course outcomes -> 6 lesson outcomes (2 per course outcome) = 9
(CRS onwards)    Lessons 1-3: one course outcome + its 2 lesson outcomes each
                 Lesson 4, and 5-6 where the content's shape needs them: synthesis
```

**What the built courses do today** (criticality, ai-technology, academic-writing and
presenting, checked 29 Oct 2026): 4 course outcomes, 4 parallel lessons with one course
outcome each, 3 lesson outcomes per lesson all serving that one outcome (12), and no
synthesis lesson.

**All three tiers at once.** When TIER is `none`, or when a whole pathway pack is
generated, AO-01 runs once per tier from the same 9 + 18, so introductory, intermediate and
advanced are produced in parallel, each pitched by its tier band and the L7 / L8 rule.

## 3. Layer -> gate -> data (where we are)

| Layer | Gate today | Change needed | Data it reads | Status |
|---|---|---|---|---|
| THEME | `onb-01_theme-preset`, `onb-02_course-theme` | none | `catalogue/pathways.json` | exists |
| 1 TIER | `onb-03_pitch` | add a `none` option | `design-kb.tier-bands.json` | exists, `none` to add |
| 2 LEVEL(S) | none | NEW gate: auto from tier bands, or human single / grouped with the adjacency rule; L7 / L8 cross-tier | tier bands; `pathway/<p>.json` `tierProgression.levels` (L3 to L8) | gap: tier bands list L3 to L7 only, no L8 |
| FORK01.1 frameworks | `cxs-05_external-standards` (auto, reserved) | make it a human select | `catalogue/context/shared/cross-cutting.json` `frameworks`: FHEQ, CQFW, FQHEIS / SCQF, QF-EHEA | data exists |
| FORK01.2 benchmarks | none | NEW: select 0 to 9 of the pathway's 9 (0 or 9 = equal weight) | pathway capabilities + `benchmarkKeys` (tiered keys, attribution) + `pathway-evidence/` (the 18) + `universal-reference.json` | data exists |
| AO-01 | none | NEW agent+human gate: 6 generic benchmarks | the above | to build |
| FORK02 shell | `cxp-01_subject` (+ `cxp-01 = baseline` routing) | reshape to baseline / group / specific | baseline: `universal-reference.json`; group: HESA groupings = CAH1 / CAH2 in `tools/subject/core/vocab/cah.json`; specific: HECoS / CAH codes on every benchmark, resolved by `tools/resolve-subject-benchmark.js`, or a free topic | gap: group **identity** (School / Faculty -> its HESA subjects) needs the CMET course data tree |
| AO-02 | `cxp-04_context-generation` | re-aim its product at context-specific competency attributes | subject benchmark corpus, pathway mappings | partial |
| FORK03 qualifiers | `cxp-02_qualifiers` (max 3, 3 categories), `cxs-03_qualifiers` (reserved) | max 6, 4 categories | `docs/authoring/qualifier-list-2026-10-04.md` (`ped:` / `theme:` / `pro:`), `graduate_competency` (20) in the universal, Advance HE framework ingests under `source-kb/.../ingested/standards/` | gap: no qualifier JSON mapping each qualifier to its ingest |
| AO-03 | none | NEW | the qualifier ingests | to build |
| AO-04 | none | NEW: shell context statement, voice-linted | AO-01 to AO-03; `tools/voice-lint.js` | to build |
| 5 outcomes | `crs-04_lesson-map` | 6 flat LOs from AO-04 map one-to-one onto up to 6 lessons; `crs-03_course-outcomes` has no job left | AO-04 | exists (`crs-04`), to remove or repurpose (`crs-03`) |

## 4. Rulings this changes (need sign-off)

1. **Qualifiers:** from at most 3 across 3 categories (rulings of 2 to 4 Oct 2026 in the
   qualifier list) to **up to 6 across 4**. `theme:` becomes "cross-cutting agendas", and
   graduate competencies / capital is a new category. `cxp-02`'s `decidedValueShape`
   (`maxItems: 3`) changes with it.
2. **Flat 6 (settled 2 Nov 2026, supersedes the 29 Oct 2026 "3 course + 6 lesson
   outcomes" ruling):** AO-04's 6 generic benchmarks ARE the tier's learning outcomes,
   flat - no distillation to 3 course outcomes, no expansion back out to 6 lesson
   outcomes. They map one-to-one onto up to 6 lessons, each circa 4-6 pages deep. Gate
   changes this needs: **`crs-03_course-outcomes` removed or repurposed** - it has no
   distillation left to do; `crs-04`'s dependency note ("Lessons serve the course
   outcomes", `design-kb.gates.json:748-751`) and every lesson outcome's `serves`
   field (`design-kb.gates.json:852-855`) need a flat-LO equivalent, not a course-
   outcome id; `wra-03`'s AL-3 rule (two summative questions per course outcome,
   `design-kb.gates.json:1361-1366`) needs a flat-LO equivalent too (two-per-LO = 12,
   or one-per-LO = 6 - still open); `les-01`'s formative check needs re-mapping from
   "1 course + 2 lesson outcomes" to "1 LO". Make these per profile, so the built
   4 x 3 courses (4 course outcomes, 3 LOs each, no synthesis) still validate under
   their own, unchanged shape.
3. **L8** joins L7 as cross-tier; the tier bands need L8 added.
4. Still open from before: demoting `crs-02_thematic-scope` to optional colour.

## 5. Open definitions

1. **SHELL vs CONTEXT SLOT mechanics:** how a group or specific slot fills, extends or
   overrides the baseline shell.
2. **CMET course data tree:** the source for group identities (School / Faculty -> courses
   -> HECoS codes). Needed for the group shell.
3. **AO-01 grouping method:** how the agent groups the selected capabilities (and their 18
   evidence examples) into 6, and how the fuzzy tops are encoded across adjacent tiers.
4. **Level adjacency:** the exact rule for grouped levels, and how L7 / L8 pitch each tier.
5. **Qualifier cap:** 6 now, "may vary". Fixed per course, or per category?

## 6. Next implementation (this branch)

Done: pathway + tier benchmark keys and the reverse index; capability attribution
(direct / indirect-only / unattributed); the 18 evidence examples; the academic-practice
prompt sets and activities.

1. **Qualifier JSON:** compile the four categories into one file, each qualifier mapped to
   its ingest (`ped:` / `pro:` from the qualifier list, cross-cutting agendas from the
   Advance HE ingests, graduate competencies from the universal).
2. **LEVEL(S) gate**, plus L8 in the tier bands.
3. **FORK01 gate + AO-01 generator:** 0 to 9 benchmark selection -> 6 generic benchmarks,
   reading the keys and the 18.
4. **FORK02 shell gate:** wire baseline / CAH group / HECoS specific through
   `resolve-subject-benchmark.js`; the group identity waits on the CMET tree.
5. **AO-02 / AO-03 / AO-04:** context, qualifier and shell statements, AO-04 voice-linted.
6. **Outcome generation** from AO-04: 3 course + 6 lesson outcomes, the lesson map with
   synthesis lessons, and the per-profile crs-03 / crs-04 / les-01 changes in section 4.
