# Benchmark ingest inputs (`source-kb/canon-adp`)

`tools/build-subject-benchmark.py` assembles each
`catalogue/context/subject/benchmarks/<id>.json` from **three inputs** (per
subject). Drop them here, then run the build. `<id>` = the QAA ingest dir name
with the `ingest-std-qaa-` prefix and `-benchmarks` suffix removed
(e.g. `law-2023`).

| Input | Path |
|---|---|
| 1. Ingested QAA statement (markdown) | `secondary-data/ingested/standards/ingest-std-qaa-<id>-benchmarks/ingest-std-qaa-<id>-benchmarks.md` |
| 2. Tier-readings card (per-tier practice/knowledge/identity) | `secondary-data/ingested/themes/pathways/integrations/cards/wide/benchmarks/<id>.yaml` |
| 3. Pathway adapt-map (optional) | `../../tools/pathways/core/mapping/<id>.adapt-map.json` |

## Build

```sh
python tools/build-subject-benchmark.py --subject <id>     # one subject
python tools/build-subject-benchmark.py --all              # every ingested subject
python tools/build-subject-benchmark.py --subject <id> --dry-run
```

Writes `catalogue/context/subject/benchmarks/<id>.json` and rebuilds
`benchmarks.json`. Copyright-held fields (`source`/`quote`) are dropped — the
catalogue holds only the processed statements, `tierReadings`, `pathwayMapping`
and `digest`.

## Notes
- Needs Python + **PyYAML** (`pip install pyyaml`). On this Windows host use
  `python` or `py`, **not** `python3` (that's the Store alias and fails).
- The paths above are now **repo-relative** (were hardcoded to the original
  `/home/user/…` repos). Override with `--ingest-root` / `--card-root` /
  `--adapt-map-root` / `--out-dir` / `--index` if the inputs live elsewhere.
- The **54 subjects already in `catalogue/context/subject/benchmarks/`** were
  built this way upstream; their raw inputs were not copied here. You only need
  these inputs to ingest a NEW subject (or re-build from an updated statement).
- The step that *creates* input (1) from a raw QAA statement, and inputs (2)/(3),
  is upstream tooling that is not in this repo.
