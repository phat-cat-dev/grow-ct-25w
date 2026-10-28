# tools/pathways/core/

The pathways model itself, under the `tools/<module>/` layout (TLS-1, 30 September 2026), moved here by RJ-0048 (D-0041, D-0044, 2 October 2026, adp-0213). It documents and structures the pathways model and develops it as a model of academic skills practice, apart from any consuming project's own generation side, and serves any use, documentation included (PTH-1). It holds no ingestion.

This folder names no consuming project (PCP-1). A search of this folder for `adapt` is expected to return three kinds of hit, each already explained and left for a later job to close: the `adapt-` pathway-tag prefix, still in use here and inside the maps pending RJ-0033's move to `path-<pathway-id>` (D-0045); the `"project": "adapt"` field inside the same maps, pending the same move (PCP-1); and the `[ADAPT]` markers in `rules/source-mapping-rules.md`, which mark the parts specific to one consuming project, not a dependency on it. Any other hit is a purity breach (PCP-1).

## What is here

- `pathways.json`: the catalogue's pathway ids and names only, kept in agreement with a consuming project's own catalogue copy (which keeps that project's own fields: chapters, routes, file).
- `mapping/`: one benchmark-to-pathway map per QAA subject benchmark statement, plus `index.json`.
- `rules/pathway-term-lists.json`: the word test for strength, one list per pathway.
- `rules/source-mapping-rules.md`: tells a mapping agent how to map one benchmark statement against the pathways. Renamed by RJ-0048 from a project-qualified filename under TLS-1's naming convention; its `[ADAPT]`-marked parts are unchanged.
- `tools/validate-map.js`: validates a map against the mapping rules; `tools/test/` holds its tests and fixtures.
