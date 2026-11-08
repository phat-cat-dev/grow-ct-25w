# catalogue/context/pathways/

Per-pathway tier stubs, one file per academic-practice pathway (13 files,
e.g. `academic-writing.json`). Indexed by the sibling `../pathways.json`,
whose `pathways[].file` field points here.

## Shape

Each file is `{ "pathwayId": "<id>", "tiers": [...] }` with one entry per
tier (introductory / intermediate / advanced):

- `tierId`, `displayName`
- `focus` — one-line description of what that tier covers
- `courseSlug`, `status`, `contextsBuilt`, `assumesFromPrevious` — course
  build/tracking fields (currently `null` / `"planned"` for all tiers)
- `voiceBand` — pointer into `docs/curriculum/pathway-tier-mapping.md`
  recording the confirmed voice band for that tier
- `teachingProsePointer` — pointer into the same mapping doc for the
  tier's teaching-prose section

## What this is not

This is a thin stub/registry layer, not the authoring source. The
substantive capability content for each pathway lives in
`../pathway/<id>.json`. Nothing here references subject or universal
benchmarks directly.
