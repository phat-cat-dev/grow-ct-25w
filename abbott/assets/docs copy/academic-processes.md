# Universal Undergraduate Academic Processes

Twenty core academic *skills*, modelled as **processes** (ordered moves), documented
as SKOS and built as interactive **context-pack activities**. Because each item is a
process rather than a static term, its `skos:definition` holds an **ordered sequence
of steps** (`ProcessSteps`) — which is exactly what the activity reveals, one move at
a time, on click.

- **Human list + model:** this file.
- **Machine graph:** [`academic-processes.skos.jsonld`](./academic-processes.skos.jsonld) — all 20 as `skos:Concept`s with `ProcessSteps` definitions, grouped and cross-linked.
- **Activities (data):** [`tools/context-packs/packs/processes/`](../../tools/context-packs/packs/processes/) — one `process`-stage pack per skill, plus [`manifest.json`](../../tools/context-packs/packs/processes/manifest.json).
- **Launch them:** [`tools/context-packs/processes.html`](../../tools/context-packs/processes.html) (serve over `http://`).
- **Regenerate:** `node tools/context-packs/packs/processes/_build.cjs` (packs + SKOS + manifest from one data table).

## The three groups

| group | focus |
| --- | --- |
| **Intellectual Depth** (Thinking) | critical analysis, argument mapping, problem decomposition, hypothesis generation, counter-argumentation |
| **Research & Retrieval** (Doing) | literature reviewing, source evaluation, research design, data interpretation, literature search |
| **Communication & Reflection** (Applying) | academic writing, peer reviewing, oral presentation, synthesis, self-directed learning, ethical reasoning, time management, reflective practice, active listening, presentation storytelling |

## The 20 processes

### A · Intellectual Depth (Thinking)
1. **Critical Analysis** — test a source's central claim, hidden assumptions and evidence.
2. **Argument Mapping** — separate thesis, supporting premises, counter-arguments and logical gaps.
3. **Problem Decomposition** — break a huge, ill-defined problem into testable sub-components.
4. **Hypothesis Generation** — turn observation/theory into a specific, falsifiable prediction.
5. **Counter-argumentation** — seek and answer the strongest case against your own thesis.

### B · Research & Retrieval (Doing)
6. **Literature Reviewing** — synthesise sources, map what's known, find the gap.
7. **Source Evaluation** — apply a framework (CRAAP / RADAR / ROBOT) to judge credibility.
8. **Research Design** — move from a vague question to a testable plan before collecting data.
9. **Data Interpretation & Visualisation** — turn raw data into an honest narrative with the right picture.
10. **Literature Search Strategy** — find sources efficiently and ethically (Boolean mastery).

### C · Communication & Reflection (Applying)
11. **Academic Writing** — build a persuasive paper from thesis to conclusion.
12. **Peer Reviewing** — return honest, specific, actionable feedback on others' work.
13. **Oral Presentation & Communication** — structure complex information for an audience, in time.
14. **Synthesis of Diverse Fields** — connect two domains through a bridge variable for novel insight.
15. **Self-Directed Learning** — diagnose gaps, find resources, plan and check your own learning.
16. **Ethical Reasoning & Integrity** — recognise the moral stakes in how knowledge is used.
17. **Time Management & Project Sequencing** — milestones, dependencies and contingency.
18. **Reflective Practice** — turn experience into formalised, reusable learning.
19. **Active Listening (in lectures)** — listen for structure, emphasis and open questions, not transcription.
20. **Presentation Storytelling** — structure data as an unfolding narrative with tension and resolution.

Three of these have **worked companion activities** that show the process on a real artefact:
Source Evaluation → the [CRAAP](../../tools/context-packs/packs/craap.json), [RADAR](../../tools/context-packs/packs/radar.json)
and [ROBOT](../../tools/context-packs/packs/robot.json) checklists; Peer Reviewing → the
[Marking & feedback](../../tools/context-packs/packs/marking-feedback.json) annotation; and a
[Referencing](../../tools/context-packs/packs/referencing.json) assembly.

## The data model (SKOS ↔ context-pack)

Each process is a `skos:Concept` whose `skos:definition` is **not plain text** but an
ordered `ProcessSteps` array — the interactivity. That maps one-to-one onto a context
pack whose `stage.type` is `process`:

| SKOS / ProcessSteps | context-pack field |
| --- | --- |
| `@id` | `uri` |
| `skos:prefLabel` | `title` |
| `skos:altLabel` | `altLabel` |
| `skos:scopeNote` | `statement` (the goal, shown first) |
| `skos:broader` (group) | `broader` / `process` |
| `skos:related` | `related` (sibling ids) |
| `skos:definition.steps[].step_title` | `steps[].title` (the move) |
| `skos:definition.steps[].description` | `steps[].text` (the move **and why**) |

```json
{
  "@id": "https://grow.local/process/critical-analysis",
  "@type": "skos:Concept",
  "skos:prefLabel": "Critical Analysis",
  "skos:altLabel": "Evaluation of Arguments",
  "skos:broader": { "@id": "https://grow.local/process/intellectual-depth" },
  "skos:definition": {
    "@type": "ProcessSteps",
    "steps": [
      { "@id": ".../critical-analysis#step1", "step_title": "Identify the core claim",
        "description": "Find the single main point you are being asked to accept." }
    ]
  },
  "skos:related": [ { "@id": "https://grow.local/process/argument-mapping" } ]
}
```

The same concept as a renderable activity:

```json
{
  "version": 1, "id": "critical-analysis", "title": "Critical Analysis",
  "uri": "https://grow.local/process/critical-analysis",
  "broader": "intellectual-depth", "altLabel": "Evaluation of Arguments",
  "related": ["argument-mapping", "source-evaluation"],
  "statement": "Move past summarising to judging a source: test its central claim, …",
  "stage": { "type": "process" },
  "steps": [
    { "title": "Identify the core claim", "text": "Find the single main point you are being asked to accept. …" }
  ],
  "feedForward": { "badge": "Try it", "text": "Now do it on your own reading: …" }
}
```

### The `process` stage type

A new stage type in the context-pack renderer. It needs no artefact: the pack's
`steps` **are** the content. Each step becomes a numbered card, revealed cumulatively;
the active card is highlighted and the caption carries the "why". This is the direct
rendering of `ProcessSteps` — statement (goal) first, then one move per click, with a
closing feed-forward that turns the watch into a do. See the renderer in
[`assets/components/context-pack/`](../../assets/components/context-pack/) (the
`<context-pack>` custom element) and the schema in
[`context-pack-schema.json`](../../tools/context-packs/context-pack-schema.json).

## Relationships

Beyond `skos:broader` (to the group) and `skos:related` (to siblings), the richer
graph the vocabulary enables: `requires` (a process depends on another, e.g. Literature
Reviewing *requires* Source Evaluation), `is_derived_from`, and `uses_term` (linking a
process to the concepts it operates on). The current graph ships `broader` + `related`;
the others are the natural next layer.

## Authoring a new process activity

Add a row to the data table in [`_build.cjs`](../../tools/context-packs/packs/processes/_build.cjs)
(`[id, title, group, altLabel, related[], statement, steps[], feedForward]`) and re-run
it — the pack, the SKOS node and the manifest regenerate together. For prose/checklist/
assembly activities (worked examples on an artefact), use the author prompts in
[`tools/context-packs/prompts/author-context-pack.md`](../../tools/context-packs/prompts/author-context-pack.md).
