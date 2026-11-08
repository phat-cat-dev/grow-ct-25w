# catalogue/context/subject/benchmarks/

54 per-subject QAA Subject Benchmark Statement files (e.g.
`accounting-2025.json`, `law-2023.json`, ...), plus the cross-subject
`universal-reference` sibling set (`.json` / `.md` / `.yaml`).

## Per-subject files

Built by `tools/build-subject-benchmark.py` from two sources per subject:

1. The QAA ingest markdown (`source-kb/.../ingested/standards/ingest-std-
   qaa-<id>-benchmarks/...`), carrying the actual benchmark statements,
   metadata and framework alignment
2. The subject's Adapt pathway map (`tools/pathways/core/mapping/
   <id>.adapt-map.json`, optional — only `psychology-2023` has one today),
   carrying how that subject's benchmark relates to each of the 13 Adapt
   pathways (`pathwayMapping`)

## universal-reference.{json,md,yaml}

Built by `tools/build-universal-benchmark.py`, which reads every file in
this folder and distils the shared core across all of them: what an
honours graduate is expected to know, do and be, regardless of subject.

Method: a 20-concept / 5-strand keyword rule is matched against each
statement's `about` + `paraphrase` + `verbs` + `themes`. A subject
"carries" a concept at a rung (introductory/intermediate/advanced) when it
has at least one matching statement at that rung; `sharedBy` counts
subjects out of the full set of 54.

```
python3 tools/build-universal-benchmark.py               # JSON + Markdown
python3 tools/build-universal-benchmark.py --format all   # + YAML
```

The JSON (`universal-reference.json`) is the machine-readable form that
`tools/build-pathway-tier-readings.py` and the resolver/context-pack flow
consume (via its `pathwayMapping` and `statementFormulas`); the `.md` and
`.yaml` siblings are the same content for a human or authoring agent to
read.

## Consumers

`universal-reference.json` is the root grounding for
`../pathway-evidence/`, `../pathway-tier-readings/`, and `../pathway-views/`
— see their README files for how each one joins back to it.
