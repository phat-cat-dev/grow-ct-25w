# Query layers + the distil/proliferate generation flow

**Status: design scope (not wired).** Branch `gates/tri-tier`. This is the target
shape for the reworked onboarding + tri-tier generation; it reconciles the
intended flow with what is actually in the repo today (see "Where we got to").

## 1. The complete query layers (onboarding)

The onboarding resolves context top-down. Each layer narrows the next:

```
THEME (pathway)
  > TIER (introductory | intermediate | advanced | none)
    > LEVEL(S)
      > QUAL FRAMEWORKS + UNIVERSAL BENCHMARKS
        > FORK01  (shell vs context slot)
          > FORK02 (cross-cutting qualifiers)
```

- **THEME** - one of the academic-practice pathways (the 13, soon 14). Gate `onb-02_course-theme`.
- **TIER** - the pitch band. Gate `onb-03_pitch`. `none` is allowed (defer to LEVEL).
- **LEVEL(S)** - either **auto-decided by the tier bands** (`design-kb.tier-bands.json`), OR, when TIER is `none`, the human defines one or more FHEQ levels here.
  - Multiple levels are generally **adjacent** (e.g. L3 / L4).
  - **Exception: L7 crosses all tiers** - a "L7 introductory / intermediate / advanced" takes the same concepts and pitches them at PG level. So L7 is a cross-cutting level, not a rung on the same ladder.
- **QUAL FRAMEWORKS + UNIVERSAL BENCHMARKS** - FHEQ / CQFW (WCFQ) generic level descriptors, plus `universal-reference.json` (the `graduate_competency` shared core) as the generic grounding every build can stand on.
- **FORK01 - SHELL vs CONTEXT SLOT** *(still to define precisely)*. Which source corpus the agent analyses:
  - **A) BASELINE SHELL** - use the universal statements and run the same analysis from a **generic, subject-neutral** perspective. (`cxp-01 = baseline` already routes `cxp-04` to `universal-reference.json`.)
  - **B) GROUP** - a group context set by the human: (a) a **group identity** (e.g. School of Sport, School of Health Sciences), and (b) a **group of HESA subjects** under it, so relevant benchmark data can be searched. *Needs the CMET data tree of courses brought in.*
  - **C) SPECIFIC** - either a specific **HESA subject**, or a general **topic area** given by the user.
- **FORK02 - cross-cutting themes** - any **qualifiers** selected (the <=3 CXP qualifiers; the graduate-competency subset is one such category). Gate `cxp-02_qualifiers`.

> **To define:** the SHELL vs CONTEXT-SLOT mechanics - a "shell" is the generic
> analysis structure; a "context slot" is what a group/specific context fills it
> with. Pin down how a slot overrides/extends the shell, and bring in the CMET
> course tree + HESA grouping for FORK01-B.

## 2. The distil -> proliferate flow (symmetric)

The core move is **distil the pathway down to 3 course outcomes per tier, then
proliferate back out to lesson outcomes** - the same ladder, run in both
directions.

**Distil (pathway -> course):**
```
9 pathway generics (capabilities, 3 per tier)
  -> 18 benchmarks            (3 tiers x 6; grouped by complexity; "fuzzy/blurry tops" co-tagged across adjacent tiers)
  -> 6 course outcomes per tier
  -> [AGENT SUGGESTS / HUMAN CHOOSES]
  -> 3 course outcomes per tier
```

**Proliferate (course -> lessons)** - the distillation expanded back out:
```
3 course outcomes (per tier)
  -> 6 -> 18 lesson-level, ACTIVE-VERB learning outcomes   (expand back out, mirroring the distillation in reverse)
  -> grouped across 4 / 5 / 6 lessons    (count by the shape of the content)
```
Each lesson addresses a **group** of these outcomes and, together, the lessons
deliver an **overarching course objective**. Proliferation is **constrained by
the tier and/or level qualifiers** chosen in layer 1.

**Alignment inputs at every step:** pathway benchmarks + universal benchmarks +
subject context (if FORK01 = group/specific) + cross-cutting qualifiers. The
agent breaks the outcomes down **ensuring alignment** across all of these, and at
each gate first **reviews the ingested data it is pointed at** (see each gate's
`agentContext` in `design-kb.gates.json`).

## 3. All three tiers at once

The `18 = 3 x 6` analysis is produced **once per pathway**; the generator then
emits **introductory, intermediate and advanced in parallel** (not one
level-selected tier), each with its own `6 -> 3` distil and `3 -> 6 -> 18`
proliferate, pitched by the tier bands and the L7-crosses-all rule. Deciders stay
`AGENT SUGGESTS / HUMAN GATE / AUTO` and the flow is the same whichever is used.

## 4. Where we got to (current repo state)

- **Pathways:** all 13 carry exactly **9 capabilities = 3 per tier** (`catalogue/context/pathway/*.json`, each capability has `capabilityId`, `tier`, `fheqLevel`, `qf`, `competency{}`). This is the "9 definitive generics". OK.
- **The 18 = 3x6 distillation:** prototyped (`tiers.json` - ran on ai-technology, reproduced 3 of the real intro course's 4 lessons) but the artifact is **NOT in the current repo** (lost in the VM-transfer snapshot). Needs rebuilding as a tool.
- **Universal:** `graduate_competency` (20 shared-core) + `pathwayMapping` + `tier-bands` (3 tiers). Benchmarks key into pathways at **pathway level**; **pathway+tier** is the agreed next granularity.
- **Gates:** every gate carries `agentContext { fieldDescription, authoringReview { instruction, pointers } }` so the agent reviews a gate's ingested sources before authoring.

## 5. Open definitions to resolve

1. **FORK01 shell vs context slot** - precise mechanics (how a context slot fills/overrides the generic shell).
2. **GROUP context** - bring in the **CMET data tree of courses** + HESA subject groupings so group benchmark data can be searched.
3. **The 18-grouping method** - how `9 -> 18`, grouped by complexity, and how the **fuzzy/blurry tops** are encoded (co-tag across adjacent tiers).
4. **L7 cross-tier handling** in the level model (same concepts, PG pitch, across all three tiers).
5. **The exact `6 -> 3` distil and `3 -> 6 -> 18` proliferate rules** (keep them symmetric so provenance is traceable both ways).

## 6. Next implementation (this branch)

1. Add the **tier dimension** to the benchmark keys (pathway -> pathway+tier) on the universal `graduate_competency` + `pathwayMapping` and on `psychology-2023.json`.
2. **Pathway reverse-index** - each `pathway/*.json` lists the benchmarks that key into it, by tier.
3. Rebuild the **`9 -> 18 -> tiers` distiller** as a tool (mirror `tools/build-universal-benchmark.py`).
4. Wire the **tri-tier benchmark -> outcome generator** (all three tiers at once) reading the keys + each gate's `agentContext`.
