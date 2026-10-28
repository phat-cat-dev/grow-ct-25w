<!--
  SKOS Concept-Map Template — field-definition edition
  Conforms to the node model in skos-structure-accordion.html and the source
  vocabulary academic-processes.skos.jsonld. This is a BLANK template: every slot
  is a definition of the field (its SKOS property + how it applies on the page),
  not example content. Copy the blocks, replace each {{token}}, keep or delete the
  definition lines as you prefer.
-->

# SKOS Concept-Map Template

A fill-in template for building a concept scheme that renders as the colour-coded,
accordioned hierarchy. Nothing below is sample content — each position states **what
field goes there, what it means in SKOS, and how it applies** when the tree becomes a
page. Replace every `{{token}}`; delete a line only if the field genuinely does not apply.

**Token convention:** `{{like-this}}` = replace with your content · `0..n` = repeatable ·
`1` = exactly one required · `0..1` = optional, at most one.

---

## Node kinds (the legend / colour roles)

| kind | SKOS construct | What it is | Page role it takes |
|---|---|---|---|
| `scheme` | `skos:ConceptScheme` | The whole vocabulary — the root | The course / site index + menu root |
| `family` | `skos:Concept` with **no** `broader` | A top concept | A top-level page / menu group (the spine) |
| `concept` | `skos:Concept` with `broader` | A narrower concept | A lesson / block placed under its family |
| `note` | `skos:scopeNote` | The one-line meaning | The lede / intro paragraph |
| `step` | `skos:definition` → `ProcessSteps` item | One ordered how-to step | One ordered step component in the body |
| `related` | `skos:related` | A sideways link | A "see also" cross-link (never nesting) |

---

## Field dictionary (definition + how it applies)

| Field | SKOS property | Card. | Definition | Applies as |
|---|---|---|---|---|
| id | `@id` | 1 | Stable IRI/slug; the node's identity and jump target | The anchor a `related` link points at |
| prefLabel | `skos:prefLabel` | 1 | The single preferred human-readable name | The `<h>` heading + the menu entry text |
| altLabel | `skos:altLabel` | 0..n | Alternative names / synonyms | Search terms, tags, `aria-label` |
| inScheme | `skos:inScheme` | 1 | The scheme this concept belongs to | Declares which vocabulary/course it is part of |
| broader | `skos:broader` | 1 (concept) / 0 (family) | The one parent concept it sits under | Decides nesting depth + which page/section it lives on |
| scopeNote | `skos:scopeNote` | 0..1 | One sentence fixing the concept's meaning and boundary | The lede / intro paragraph under the heading |
| definition | `skos:definition` → `ProcessSteps` | 0..1 | The ordered how-to for the concept | The body: a numbered list of step components |
| step_title | `grow:stepTitle` | per step | The name of a single step | The step's sub-heading |
| description | `grow:stepDescription` | per step | What the learner does at that step | The step's paragraph |
| related | `skos:related` | 0..n | Symmetric, non-hierarchical links (may leave the scheme) | A "see also" strip of cross-links |

---

## Template 1 — Concept Scheme (`kind: scheme`, one per vocabulary)

```yaml
---
id: {{scheme-slug}}            # @id — stable IRI/slug for the whole vocabulary (the root)
prefLabel: {{Scheme title}}    # skos:prefLabel — the vocabulary's name; the top page/menu title
kind: scheme                   # fixed: this is the ConceptScheme root
# Every concept below carries  skos:inScheme: {{scheme-slug}}  back to this id.
# Top concepts are listed via   skos:hasTopConcept  (the inverse of a concept's topConceptOf).
---
```

> **scopeNote (scheme-level)** — {{one line: what this whole vocabulary covers and who it is for}}
> <!-- Applies as: the intro paragraph on the scheme's landing page / menu root. Optional. -->

---

## Template 2 — Top Concept / family (`kind: family`, one per spine section)

A family is a `skos:Concept` with **no** `broader`. It gathers narrower concepts.

```yaml
---
id: {{family-slug}}            # @id — identity + jump target
prefLabel: {{Family name}}     # skos:prefLabel (1) — the section/page heading
inScheme: {{scheme-slug}}      # skos:inScheme (1) — the scheme id from Template 1
kind: family                   # family = top concept, no broader
# broader: (omit — a top concept has none; that is what makes it top)
---
```

> **scopeNote** — {{one line: what this family groups, and the stance it represents}}
> <!-- Applies as: the lede for this top-level page/section. Optional at family level. -->

**Narrower concepts (`skos:narrower` →):** list the `{{concept-slug}}` of each concept whose
`broader` points here. `0..n`. Each is authored with Template 3 and nested under this family.

---

## Template 3 — Concept / leaf (`kind: concept`, repeat `0..n` per family)

A narrower `skos:Concept`. One markdown file (or block) per concept.

```yaml
---
id: {{concept-slug}}           # @id (1) — identity + the anchor related chips jump to
prefLabel: {{Concept name}}    # skos:prefLabel (1) — the block heading / menu text
altLabel:                      # skos:altLabel (0..n) — synonyms; search terms / aria-label
  - {{synonym}}
broader: {{family-slug}}       # skos:broader (1) — the one family this nests under
inScheme: {{scheme-slug}}      # skos:inScheme (1) — the scheme id
kind: concept
related:                       # skos:related (0..n) — sideways links, NOT nesting
  - {{other-concept-slug}}     #   in-scheme target -> becomes a cross-link that can jump
  - {{EXTERNAL-NAME}}          #   out-of-scheme target (e.g. an external framework) -> plain link, no jump
---
```

> **scopeNote** — {{one sentence defining what this concept covers and where its boundary is}}
> <!-- Applies as: the lede/intro paragraph shown under the heading when the block opens. -->

### Process — `skos:definition` → `ProcessSteps`

<!--
  An ORDERED how-to. 1..n steps, rendered in sequence and numbered.
  Applies as: the body of the block — one step component per item.
  step_title = the step's sub-heading · description = what the learner does there.
-->

1. **{{step_title}}** — {{description — what the learner does at this step}}
2. **{{step_title}}** — {{description}}
3. **{{step_title}}** — {{description}}
<!-- add or remove numbered items: a definition is a sequence, not a fixed count -->

### Related — `skos:related`

<!--
  Mirror the related list from the frontmatter here as readable links.
  Applies as: a "see also" strip. Symmetric (add the reverse link on the target too)
  and non-transitive. In-scheme links jump; out-of-scheme links are plain.
-->

- see also → `{{other-concept-slug}}` {{Concept name}}
- external ⇗ → {{EXTERNAL-NAME}} <!-- a framework/resource outside this scheme; no jump -->

---

## Assembled map skeleton

How the three templates nest to form the whole hierarchy (tokens only — fill per above):

```
scheme: {{scheme-slug}} — "{{Scheme title}}"            [kind: scheme]
│  scopeNote: {{what the vocabulary covers}}
│
├─ family: {{family-slug}} — "{{Family name}}"          [kind: family]  (no broader)
│  │  scopeNote: {{what this family groups}}
│  │
│  ├─ concept: {{concept-slug}} — "{{Concept name}}"    [kind: concept] (broader → {{family-slug}})
│  │     altLabel: {{synonym}}
│  │     scopeNote: {{meaning + boundary}}
│  │     definition → steps:
│  │       1. {{step_title}} — {{description}}
│  │       … ({{n}} ordered steps)
│  │     related → {{other-concept-slug}} · {{EXTERNAL-NAME}} ⇗
│  │
│  └─ concept: {{concept-slug}} …                       (repeat 0..n per family)
│
├─ family: {{family-slug}} …                            (repeat per spine section)
└─ …
```

---

## Authoring rules the SKOS shape enforces

- **Hierarchy is the frame.** `broader`/`narrower` is a tree — it alone decides nesting and menu
  order. Give every concept exactly one `broader`; give a family none. No concept floats free of
  the scheme (`inScheme` is always present).
- **`definition` is ordered.** Its `steps` are a sequence — author and render them in order, numbered.
- **`related` is a link, not a limb.** Never promote a `related` edge to nesting. It is symmetric
  (add the reverse) and may point outside the scheme — render those as plain external links, not pages.
- **One `prefLabel`.** Everything else that names the concept is an `altLabel`.

<!--
  Companion files:
    skos-structure-map.html         — static, colour-coded version of this model
    skos-structure-accordion.html   — interactive template; its DATA node = this template's fields
    academic-processes.skos.jsonld  — a fully filled example of this template
-->
