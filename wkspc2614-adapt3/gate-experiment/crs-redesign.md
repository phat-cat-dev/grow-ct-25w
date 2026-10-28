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

## Flow (per the whole-pathway model)
```
pathway capabilities + generic descriptors (FHEQ/CQFW)
      │  (analyse, like universal-reference did the 54 benchmarks)
      ▼
18 benchmarks  =  3 tiers × 6, grouped by type/action, fuzzy "blurry tops"      ← tiers.json
      │  level (onb-04_level) selects the course's tier
      ▼
6 tier benchmarks  →  narrow/merge  →  3 course outcomes                          { AGENT SUGGESTS / HUMAN GATE / AUTO }
      ▼
each outcome ×3  →  9 lesson outcomes   (ref the tier benchmarks + blurry tops)
      ▼
9 lesson outcomes  →  divide across 4–6 lessons   (by content + activity opportunity; each tier its own steer + book ref)
      ▼
agent drafts the lesson map (titles + lesson plans)  →  scaffold
```

## Proposed CRS gates (benchmark-first)

| gate | vs live | decider | produces |
|---|---|---|---|
| `crs-01_sources` | keep | human | themed source set (book) — feeds every agent search |
| `crs-02_benchmarks` | **NEW** (takes the structural role of `crs-02_thematic-scope`) | agent+human (suggest / gate / auto) | the pathway's 18-benchmark `tiers.json` (3×6, grouped, fuzzy tops) |
| `crs-03_tier-outcomes` | reworks `crs-03_course-outcomes` | agent+human | the resolved tier's **6 → 3 course outcomes** (+ per-outcome banks, as now) |
| `crs-04_lesson-outcomes` | **NEW** | agent+human | each outcome **×3 → 9 lesson outcomes** |
| `crs-05_lesson-map` | reworks `crs-04_lesson-map` | agent+human | **9 → 4–6 lessons** (title, topic, outcomes, source section, steer) |
| `crs-06_course-spec` | = `crs-05_course-spec` | advisory, auto-stands | rollup |

### `crs-02_benchmarks` (NEW) — the structural source
```yaml
decider: agent+human            # agent proposes, human gates, or AUTO
hardness: hard-stop
produces: tiers.json            # 18 benchmarks = 3 tiers × 6
sources:
  - catalogue/context/pathway/<pathway>.json  (capabilities: tier, fheqLevel, statement, qf)
  - catalogue/context/pathway-student-facing.json  (the "you can…" rewrites)
  - catalogue/context/subject/benchmarks/universal-reference.json  (shared-core + pathwayMapping)
  - FHEQ + CQFW/WCFQ generic level descriptors  (generic phrase sources)
method: mirror tools/build-universal-benchmark.py — tier, group by type/action, co-tag the fuzzy tops
feeds: [crs-03_tier-outcomes, crs-04_lesson-outcomes, crs-05_lesson-map]
dependsOn: [onb-02_course-theme (pathway), onb-04_level (which tier), crs-01_sources]
```

### `crs-03_tier-outcomes` — 6 → 3
```yaml
decider: agent+human            # AGENT SUGGESTS / HUMAN GATE / AUTO
produces: 3 course outcomes for the resolved tier (merged from the 6 benchmarks, with provenance)
rule: review the tier's 6 benchmarks; merge duplicates/overlaps down to 3 (one idea each)
dependsOn: [crs-02_benchmarks, onb-04_level]
```

### `crs-04_lesson-outcomes` (NEW) — 3 → 9
```yaml
decider: agent+human
produces: 9 lesson outcomes (each of the 3 course outcomes proliferated ×3)
rule: proliferate with reference to the tier benchmarks + the blurry-top benchmarks reaching up from the next tier
dependsOn: [crs-03_tier-outcomes, crs-02_benchmarks]
```

### `crs-05_lesson-map` — 9 → 4–6 lessons
```yaml
decider: agent+human
produces: 4–6 lessons (key, title, topic, lesson outcomes, source section(s), steer)
rule: divide the 9 outcomes across lessons by content + activity opportunity; each tier carries its own steer + book/source refs; agent drafts titles + lesson plans
dependsOn: [crs-04_lesson-outcomes, crs-01_sources]
```

## How it maps onto the live gates
- `crs-02_thematic-scope` (free strands) is **demoted**: strands become optional colour, not the structural source. The benchmarks drive structure instead. *(Biggest downstream change — flagged in the tiers.json fork's assessment; needs your sign-off before it ever touches live.)*
- `crs-03`/`crs-04` keep their jobs (outcomes, lesson map) but are now **benchmark-derived**, and a new `crs-04_lesson-outcomes` sits between them to carry the 3→9 proliferation.
- `onb-04_level` (the level data object) is what picks the tier whose 6 benchmarks seed the outcomes.

## Proven already (in this experiment)
- `tiers.json` — benchmarks → 3×6 (fuzzy tops) → 3 outcomes → 9 → lessons (ran on ai-technology; reproduced 3 of the real intro course's 4 lessons).
- `level.js` — the pitch/explicit-L resolver that selects the tier.
- `capabilities-to-growlevels.js` — one knowledge→component generator built on the same capability data.

## Open decisions (carried from the fork)
1. Where the 18 come from (capabilities + generic descriptors) — and the real FHEQ/CQFW corpus is not yet in the repo.
2. How the fuzzy tops are encoded (co-tagging across adjacent tiers).
3. The exact 3→9 proliferation rule.
4. **Demoting `crs-02_thematic-scope`** — the one that reshapes the live front gates; needs explicit approval.
