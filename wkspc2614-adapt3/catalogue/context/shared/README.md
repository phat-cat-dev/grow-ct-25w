# catalogue/context/shared/

`cross-cutting.json` — the generic, pathway- and subject-independent
scaffolding that the per-pathway and per-subject tier readings specialise.
Built by `tools/build-cross-cutting-store.py`. This is infrastructure, not
benchmark content: it carries no statements or evidence of its own.

## Shape

Concept-ordered, one file:

1. `tierModel` — the tier<->level spine: the three tiers
   (introductory/intermediate/advanced), the overlap formula, the edge
   rows (F, L8), and the full row grid (`i1`/`i2`/`i3`, `d1`/`d2`/`d3`,
   `e1`/`e2`/`e3`), each row carrying both its tier and its indicative
   FHEQ level
2. `genericLadder` — the practitioner F->L8 readings (practice / knowledge
   / identity), the generic spine the subject and pathway readings
   specialise
3. `frameworks` — FHEQ / CQFW / FQHEIS / QF-EHEA, each with its dimensions
   and per-row level alignment

## Consumers

Read by every tier-aware builder (via `tools/pathway_tiers.py`) and by
`tools/build-pathway-tier-readings.py` when filling universal formulas, as
the single source of truth for the tier/row/FHEQ-level model used
everywhere else under `catalogue/context/`.
