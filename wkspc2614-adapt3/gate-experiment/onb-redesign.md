# Experiment — ONB redesign + the `level` data object

**Not wired into the live gates.** `design-kb/design-kb.gates.json` is unchanged;
this is the proposed shape, prototyped in `gate-experiment/`.

## Revised ONB phase (5 gates)

| gate | status | decides |
|---|---|---|
| `onb-01_theme-preset` | unchanged | use a preset, or custom |
| `onb-02_course-theme` | unchanged | **pick a pathway** (the 13) |
| `onb-03_pitch` | unchanged | tier: introductory / intermediate / advanced / **none** |
| `onb-04_level` | **NEW** | the `level` data object |
| `onb-05_naming` | renamed from `onb-04_naming` | name + slug |

## `onb-04_level` — the level data object
Decider: **auto**, with human override. Produces `level`.

**Rule** (`level.js`): the level is **set by pitch** (`onb-03`). **If pitch is
`none`/`no-tier`, a specific explicit `L` setting takes precedence.**

```
pitch set (not none)      -> level from pitch   (introductory→L4, intermediate→L5, advanced→L6)
pitch none + explicitL    -> level from the explicit L   (PRECEDENCE)
neither                   -> unresolved (flagged)
```

`decidedValue`:
```yaml
setBy: pitch | explicit | none
pitch: <onb-03 value>
explicitL: <e.g. "fheq:5" | null>   # only used when pitch is none
resolvedFheq: <3..7 | null>
resolvedTier: <introductory|intermediate|advanced | null>
```

## Why it exists
`level` is consumed downstream to **pitch generated content**. Proven in
`capabilities-to-growlevels.js`: the capabilities→growLevels generator uses
`resolvedTier` (pitch path) to pick a tier's 3-rung ladder, or `resolvedFheq`
(explicit-L path) to pick capabilities at that exact FHEQ level across tiers.
See `growlevels-sample.json` for the two worked outputs.

## First knowledge→component mapping proven
`pathway capabilities → growLevels` (the first row of the knowledge→component
table). `tiers.json` already proved `benchmarks → outcomes/lessons`. Remaining
rows to prototype: `_definitions → keyTerm/glossary`, `academic → annotate/Citation`,
taxonomies → `sortable/matching`, decisions → `branching`.
