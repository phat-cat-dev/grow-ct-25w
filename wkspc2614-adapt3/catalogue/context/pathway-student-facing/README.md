# catalogue/context/pathway-student-facing/

`pathway-student-facing.json` — one combined, hand-reviewed file covering
all 13 pathways' student-facing capability rewrites. Unlike every other
store under `catalogue/context/`, this one carries no benchmark references
at all; it is pure voice/register content.

## Shape

`{ "pathways": { "<pathwayId>": [ ... ] } }`, with 18 entries per pathway
(one per capability across all three tiers). Each entry carries:

- `id`, `tier`, `fheqLevel`
- `academic` — the original capability statement (as in `../pathway/`)
- `studentFacing` — the second-person, plain-register rewrite ("you can...")
- `origin` — `"identified"` or `"proliferated"`
- `status` — `"confirmed"` or `"drafted"`

## Consumers

Read by `gate-experiment/capabilities-to-growlevels.js` and built/merged
by the scripts in `scratchpad/` (`build-student-facing.js`,
`merge-proliferation.js`). Intended for student-facing UI/messaging, not
for authoring or benchmark grounding.
