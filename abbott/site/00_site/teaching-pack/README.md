# Teaching meta-processes: a SKOS based lesson pack

A six-lesson course for early career educators on the processes that sit under
teaching: planning, delivering, evaluating and reflecting. The course vocabulary
is a SKOS concept scheme, and each lesson ("session") is a SKOS collection of the
concepts it introduces. The records follow `course_frontmatter_spec.md` and
`frontmatter_spec.md`.

## Contents

| Path | What it is |
|---|---|
| `skos/concepts.json` | Source of truth for the vocabulary: 34 concepts with definition, scope note, example, source, hierarchy and links. |
| `skos/teaching-meta.ttl` | Generated SKOS (Turtle): one scheme, 5 top concepts, 34 concepts, 6 session collections, 1 ordered collection for the pack. |
| `course/course.json` | The course record (Level 0 concept node). |
| `content/lessons.js` | The six lesson records and their authored text. |
| `dist/course.md`, `dist/lesson-01.md` to `lesson-06.md` | Generated Markdown with YAML front matter and a full body. |
| `dist/report.json` | Build summary. |
| `build-pack.js`, `tools/` | The build. `tools/` is a copy of the Handlebars stubs and `render-stubs.js`. |

## Build

```
npm install
node build-pack.js
```

The build stops with a list of problems if any check fails. It runs the ten course
coherence checks, the lesson-to-course consistency checks and SKOS integrity checks
(labels, notations, hierarchy cycles, related versus broader conflicts). It then
renders each Markdown file and confirms the front matter parses back to the same data.

## How SKOS is used

- **Concept scheme:** `tm:scheme`, with five top concepts (Teaching cycle, Planning learning, Delivering learning, Evaluating learning, Reflective practice).
- **Hierarchy:** `skos:broader` and `skos:narrower`, kept to true generic links (for example Peer observation sits under Evaluating teaching, and Kolb cycle under Reflective cycle).
- **Cross links:** `skos:related`, stated once in the source and written in both directions in the Turtle.
- **Documentation:** `skos:definition`, `skos:scopeNote` (what to do in practice), `skos:example`, `skos:altLabel` and `dct:source`.
- **Sessions:** `tm:session-01` to `tm:session-06` are `skos:Collection`s. `tm:pack` is a `skos:OrderedCollection` of the six.
- **Front matter link:** the course `key_terms` (T1 to T34) are generated from the scheme, and each lesson carries the notations it introduces in `tags` (for example `teaching-meta:PL.01`).

## Things to settle before you publish

1. The base URI `https://example.org/skos/teaching-meta/` is a placeholder.
2. The four relation targets in the course record (`concept-educational-practice`, `concept-curriculum-design`, `concept-teaching-techniques`, `concept-learning-science`) do not exist yet. Point them at real nodes in your graph or remove them.
3. `owner`, `authors` and `reviewers` are placeholders. Review status is `pending`.
4. Citations in `dct:source` are given from memory of the standard literature and have not been checked page by page. Verify each before use.
5. The course spec section 10 decisions still stand: one concept node per course, the relation vocabulary, the lesson roles and guided order. This pack assumes the defaults.
6. Nothing here configures Adapt or SCORM. The portfolio is a design intention for self-checking, not tracked or marked.
