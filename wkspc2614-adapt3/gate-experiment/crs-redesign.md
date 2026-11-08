# Experiment — CRS redesign (benchmark-first course build)

**Not wired into the live gates.** `design-kb/design-kb.gates.json` is unchanged.
This proposes expanding the CRS phase to build the course structure **from the
pathway's defined benchmarks**, instead of from free thematic strands. Prototyped
in `gate-experiment/` (`tiers.json`, `level.js`, `capabilities-to-growlevels.js`).

## The idea
Today CRS derives outcomes from `crs-02_thematic-scope` (5–10 free strands). The
redesign makes the **pathway benchmarks** the structural source: analyse them once
(like `universal-reference.json` did the sector), tier them, and let outcomes and
lessons fall out of that — agent-proposed, human-gated, or auto.

## Flow (per the whole-pathway model, flat and un-distilled — settled 2 Nov
## 2026, supersedes the 6 → 3 → 9 chain below; outcome count revised 2 Nov
## 2026, same day: not fixed at 6 — content shape decides, typically 4-6)
```
pathway capabilities + generic descriptors (FHEQ/CQFW)
      │  (analyse, like universal-reference did the 54 benchmarks)
      ▼
18 benchmarks  =  3 tiers × 6, grouped by type/action, fuzzy "blurry tops"      ← tiers.json
      │  level (onb-04_level) selects the course's tier
      ▼
6 tier benchmark statements  →  the tier's learning outcomes, FLAT                { AGENT SUGGESTS / HUMAN GATE / AUTO }
      │  no distillation to 3, no expansion to 9 — but not mechanically 6 either:
      │  one outcome per statement by default; merge two adjacent statements into
      │  one outcome only where their content naturally clusters. Typically 4-6
      │  outcomes; the content's own shape decides the count, not a fixed target.
      ▼
4-6 LOs  →  up to 6 lessons, one LO each   (circa 4–6 pages per lesson; each tier its own steer + book ref)
      ▼
agent drafts the lesson map (titles + lesson plans)  →  scaffold
```

## Proposed CRS gates (benchmark-first, flat and un-distilled)

| gate | vs live | decider | produces |
|---|---|---|---|
| `crs-01_sources` | keep | human | themed source set (book) — feeds every agent search |
| `crs-02_benchmarks` | **NEW** (takes the structural role of `crs-02_thematic-scope`) | agent+human (suggest / gate / auto) | the pathway's 18-benchmark `tiers.json` (3×6, grouped, fuzzy tops) |
| `crs-03_course-outcomes` | **removed** — no distillation left to do; the tier's outcomes come straight from its 6 statements (merged to 4-6 where content shape clusters them) | — | — |
| `crs-04_lesson-outcomes` | **removed** — no expansion left to do; the tier's outcomes already ARE the lesson outcomes | — | — |
| `crs-05_lesson-map` (renumbered `crs-03` once the above are gone) | reworks `crs-04_lesson-map` | agent+human | **4-6 → up to 6 lessons** (title, topic, outcome, source section, steer) |
| `crs-06_course-spec` (renumbered accordingly) | = `crs-05_course-spec` | advisory, auto-stands | rollup |

### `crs-02_benchmarks` (NEW) — the structural source
```yaml
decider: agent+human            # agent proposes, human gates, or AUTO
hardness: hard-stop
produces: tiers.json            # 18 benchmarks = 3 tiers × 6
sources:
  - catalogue/context/pathway/<pathway>.json  (capabilities: tier, fheqLevel, statement, qf)
  - catalogue/context/pathway-student-facing/pathway-student-facing.json  (the "you can…" rewrites)
  - catalogue/context/subject/benchmarks/universal-reference.json  (shared-core + pathwayMapping)
  - FHEQ + CQFW/WCFQ generic level descriptors  (generic phrase sources)
method: mirror tools/build-universal-benchmark.py — tier, group by type/action, co-tag the fuzzy tops
feeds: [crs-05_lesson-map]
dependsOn: [onb-02_course-theme (pathway), onb-04_level (which tier), crs-01_sources]
```

**No distillation gate, and no fixed outcome count.** The tier's 6 benchmark
statements from `crs-02_benchmarks` become the tier's learning outcomes directly —
one outcome per statement by default, merged into one outcome only where two
adjacent statements naturally cluster (revised 2 Nov 2026: not every tier gets
mechanically 6; the content's own shape decides, typically 4-6). Nothing is
distilled down to 3 or expanded out to 9 — that structural rule still holds; only
the "always exactly 6" numeral was dropped.

### `crs-05_lesson-map` — 4-6 → up to 6 lessons
```yaml
decider: agent+human
produces: up to 6 lessons (key, title, topic, the one LO it carries, source section(s), steer)
rule: one lesson per LO by default; merge two adjacent LOs into one lesson only where content shape forces it. Each tier carries its own steer and book/source refs; agent drafts titles + lesson plans; each lesson runs circa 4–6 pages (the six-part flow) to develop its LO well.
dependsOn: [crs-02_benchmarks, crs-01_sources]
```

## How it maps onto the live gates
- `crs-02_thematic-scope` (free strands) is **demoted**: strands become optional colour, not the structural source. The benchmarks drive structure instead. *(Flagged in the tiers.json fork's assessment; needs your sign-off before it ever touches live.)*
- `crs-03_course-outcomes` **loses its job entirely** under the flat, un-distilled shape, not just a rework — there is no course-outcome tier to populate. This is now at least as big a live-gate change as the `crs-02` demotion: `crs-04_lesson-map`'s "Lessons serve the course outcomes" dependency note and every lesson outcome's `serves` field assume a course-outcome id (`design-kb.gates.json:748-755`), and `wra-03_summative`'s AL-3 rule ("two summative questions per course outcome", `design-kb.gates.json:1361-1366`) has no course outcome to count against — open whether it becomes two-per-LO or one-per-LO. None of this is resolved yet; it needs explicit sign-off before `crs-03` is touched live.
- `onb-04_level` (the level data object) is what picks the tier whose 6 benchmarks seed the lessons.

## Proven already (in this experiment)
- `tiers.json` — benchmarks → 3×6 (fuzzy tops) → 3 outcomes → 9 → lessons (ran on ai-technology; reproduced 3 of the real intro course's 4 lessons, under the superseded 6→3→9 shape — see `design-kb.gate-profiles.json`'s `built-course-shape` profile for that shape kept as its own named run).
- `level.js` — the pitch/explicit-L resolver that selects the tier.
- `capabilities-to-growlevels.js` — one knowledge→component generator built on the same capability data.

## Open decisions (carried from the fork)
1. Where the 18 come from (capabilities + generic descriptors) — and the real FHEQ/CQFW corpus is not yet in the repo.
2. How the fuzzy tops are encoded (co-tagging across adjacent tiers).
3. ~~The exact 3→9 proliferation rule~~ — moot under the flat, un-distilled shape (settled 2 Nov 2026); no 3→9 step exists in this profile.
4. **Demoting `crs-02_thematic-scope`** — the one that reshapes the live front gates; needs explicit approval.
5. **Removing `crs-03_course-outcomes`** — needs its own explicit approval, same weight as #4.
6. ~~The merge rule for 6→4-6~~ — **tested and dropped as the generative mechanism** (settled 2 Nov 2026, see "Worked example — criticality" below). The merge test was applied by hand to all 9 capabilities of two real pathways (criticality, referencing): it never fired once (6/6/6 in both). This is structural, not incidental — every pathway-evidence pair is deliberately authored as one theory-grounded conceptual example plus one distinct graduate-competency/professional-practice example, so the two items almost never cluster. **Book-section count replaced it as the generative mechanism** — see below.
7. **Book-first, two-layer outcome method** (settled 2 Nov 2026) — in place of the merge rule: Layer 1 reads the pathway's own book chapter (`source-kb/source-maps/book-excelling-at-university-2026.json`) and takes one LO per real section, book cross-references and definitions ahead of named theory. Layer 2 fills any tier short of 5 LOs using (a) the pathway's own applied/professional benchmark evidence, and/or (b) at most one named theory lesson **per tier** (each tier is its own Adapt course, so each tier gets its own theory budget, delivered anchored inside a book-grounded lesson's context, never freestanding). Hard floor 5 lessons per tier, ceiling remains 6. Still open: the exact Layer-2 trigger logic where a tier is short by more than one LO (benchmark fill vs theory lesson vs both) is an agent judgement call per run, not yet a rule; needs a second and third worked pathway to see if a pattern emerges.

## Worked example — criticality (settled 2 Nov 2026)

Chapter 8 (criticality) of the book naturally splits into 3 introductory / 3
intermediate / 5 advanced sections (not the even 3/3/3 the capability model
assumed) — advanced is where the pathway's existing capability authoring
under-represents the book: one capability (`/05`) alone maps to 4 of the 5
advanced sections, and one capability (`#e3`) has no book section at all (a
pure Hyland-theory import with no book grounding).

Applying the book-first, two-layer method (Layer 1 book, Layer 2 benchmark
evidence + one theory lesson per tier) settles criticality at **16 lessons: 5
introductory / 5 intermediate / 6 advanced** — within the 5-floor/6-ceiling
per tier.

| Tier | # | LO source | Traces to |
|---|---|---|---|
| Introductory | 1 | Book: defining critical thought | `ch8/defining-critical-thought`, capability `#i3` (previously had no bookGrounding; this sweep gives it one) |
| Introductory | 2 | Book: thinking critically about academic sources | `ch8/thinking-critically-about-academic-sources`, capability `c1` |
| Introductory | 3 | Book: opening up the discourse in practice | `ch8/opening-up-the-discourse-in-practice`, capability `/02` |
| Introductory | 4 | **Theory** — Bloom's full taxonomy ladder (remember→create) as an orienting preview, not yet tested at analyse/evaluate | Anderson & Krathwohl 2001; anchored in the "habit of mind" context of LO1 |
| Introductory | 5 | Benchmark fill — stakeholder mapping (food bank) | `/02` applied evidence |
| Intermediate | 1 | Book: analysing an interpretation | `ch8/analysing-an-interpretation`, capability `/01` |
| Intermediate | 2 | Book: evaluating interpretations | `ch8/evaluating-interpretations`, capability `/03` |
| Intermediate | 3 | Book: engaging with journal articles (Table 8.1) | `ch8/engaging-with-journal-articles`, capability `/04` |
| Intermediate | 4 | Benchmark fill — recognising analysis/evaluation without academic steer words | `/01` applied evidence |
| Intermediate | 5 | Benchmark fill — method-check/briefing (software internship) | `/04` applied evidence |
| Advanced | 1 | Book: active vs passive approaches (Susie exemplar) | `ch8/active-and-passive-approaches` |
| Advanced | 2 | Book: forming judgements | `ch8/forming-judgements`, capability `c2` |
| Advanced | 3 | Book: applying synthesis | `ch8/applying-synthesis` |
| Advanced | 4 | Book: the language of criticality | `ch8/language-of-criticality`, capability `/05` (narrowed — previously absorbed 4 sections) |
| Advanced | 5 | Book: discipline-specific vocabulary | `ch8/discipline-specific-vocabulary`, capability `/05` (narrowed, second half) |
| Advanced | 6 | **Theory** — Hyland's 2005 stance model, built on LO3's synthesis work | Hyland 2005; restores capability `#e3`, which Layer 1 alone left homeless |

No merge, no distillation: every LO traces to exactly one book section,
exactly one piece of benchmark evidence, or exactly one named theory source.
`#e3` (Hyland) is the one capability with no book-section home; the method
restores it via the advanced tier's own theory-lesson budget rather than
dropping it, which an earlier (superseded) draft of this run did by mistake
when it treated the theory budget as shared across the whole pathway instead
of per tier.

**Status: agreed with the human gate 2 Nov 2026.** Not yet run on a second or
third pathway to see whether the 5/5/6 split (vs. e.g. 5/6/5, or 6/5/5) is
typical or specific to criticality's own chapter shape.
