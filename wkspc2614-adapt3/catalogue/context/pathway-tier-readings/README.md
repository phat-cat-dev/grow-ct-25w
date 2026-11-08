# catalogue/context/pathway-tier-readings/

Generated output of `tools/build-pathway-tier-readings.py` (13 files, one
per pathway). Fills the universal benchmark's nine tier-statement formulas
(see `../subject/benchmarks/universal-reference.json` ->
`statementFormulas.u-intro/u-inter/u-adv`) with each pathway's own
capability vocabulary and voice band.

**Deterministic and programmatic**: the same inputs always produce
byte-identical output. Nothing here is hand-authored or hand-edited —
do not edit these files directly; regenerate them instead.

## Shape

Per file: `{ "pathway": "<id>", "tierReadings": [...] }`, one entry per
tier with:

- `tier`, `fheqLevel`, `universalRowId` (e.g. `"u-intro"`)
- `statements.practice/knowledge/identity`, each carrying:
  - `universalStatement` — the unfilled formula text, read from
    universal-reference
  - `template`, `fill` — the formula's named slots filled with this
    pathway's vocabulary
  - `slotProvenance[]` — per-slot record of where each fill came from
    (`capabilityVocabulary` vs `universalSourceFill`)

## Regenerating / checking

```
python3 tools/build-pathway-tier-readings.py --self-test
python3 tools/check-pathway-tier-readings.py
```

A rebuild should be a no-op (`git diff --exit-code`) unless `../pathway/`
or the universal benchmark changed.

## Consumers

Read by `tools/build-pathway-views.py` as one of the four joined stores.
