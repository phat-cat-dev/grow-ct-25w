# catalogue/context/pathway-views/

Generated, read-only **view** of each pathway's full benchmark chain (13
files as `.json`, mirrored as `.yaml`, plus `pathway-views.md`). Produced
by `tools/build-pathway-views.py`.

This is a view, not a store: nothing here is invented, filled or
authored. It only joins, read-only, across four existing stores, per
pathway:

```
benchmark statement text
  (../subject/benchmarks/<source>.json)
    -> the 9 capabilities
       (../pathway/<pathway>.json)
         -> the 18 generic learning outcomes
            (../pathway-evidence/<pathway>.json)
              -> the 9 tier readings (practice/knowledge/identity)
                 (../pathway-tier-readings/<pathway>.json)
```

## Shape

Per file: `{ "pathway": "<id>", "note": "...read-only view...", "tiers": [...] }`,
with each tier's `capabilities[]` carrying the joined `statement`,
`knowledgeKind`, `benchmarks[]` (each with `source: "universal-reference"`
and a `statementId` such as `qaa-universal/threshold/written-communication`),
`genericOutcomes[]`, and the matching `tierReadings` entry.

**Deterministic**: the same four source stores always give byte-identical
output, so a rebuild is a no-op and determinism is itself checkable via
`git diff --exit-code`. Do not hand-edit these files.

## Consumers

Reference/verification only — not read by any further build step. Useful
for seeing a pathway's complete benchmark-to-tier-reading chain in one
place without cross-referencing four separate stores.
