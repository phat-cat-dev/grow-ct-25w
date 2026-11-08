# catalogue/context/pathway-evidence/

Hand-authored evidence examples and generic learning outcomes for each
pathway's 9 capabilities (13 files + `_theory-refs.json`). Kept apart from
`../pathway/`, which `tools/build-pathway-reference.py` regenerates —
this store is never touched by that script.

## Shape

Per file: `{ "pathway": "<id>", "capabilities": [...] }`, one entry per
capability (`academic-writing/05` etc.) with:

- `evidence[]` — exactly two items per capability: one **conceptual**
  (theory/concept/model) and one **applied** (practice/real world)
- `genericOutcomes[]` — two outcome variants (conceptual + applied), each
  carrying `origin: "from-benchmark"` and a `grounding[]` entry such as
  `"benchmark: qaa-universal/threshold/written-communication"` — this is
  the explicit join to the universal benchmark (see
  `../subject/benchmarks/universal-reference.json`), not to any single
  subject's benchmark.

9 capabilities x 2 evidence items = 18 per pathway, 6 per tier.

## Validation

`tools/check-pathway-evidence.py` checks, per file: every capability
appears exactly once with the right tier, exactly one conceptual + one
applied evidence item, grounding rules (ingested theory ids where
available, else `"model: <named model>"`), and length bounds (title <= 12
words; example 35-90 words; artefact 8-30 words).

## Consumers

Read by `tools/build-pathway-views.py` as the source of the generic
learning outcomes in the joined per-pathway benchmark view.
