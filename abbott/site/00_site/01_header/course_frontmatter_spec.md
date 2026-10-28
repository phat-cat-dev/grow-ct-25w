# course frontmatter

**Understood: the course is the Level 0 node. It is one coherent concept, broken down into lessons. It is also a node in its own right, so the record has to work as a document and as a concept node that other nodes can point at.**

This is the plan for the course record. It extends the Level 0 section of `frontmatter_spec.md` and keeps its field names where they exist. Nothing here is an enforced schema. It is a proposed convention.

## 1. What changes between a lesson and a course

A lesson record says what one lesson teaches. A course record has four extra jobs:

| Job | What the record must do |
|---|---|
| **Name the concept** | State the one idea the course is about, define it and say what binds the lessons together. |
| **Place the concept** | Say where the concept sits among other concepts: what it belongs to, what it needs first, what it is easily confused with. |
| **Decompose it** | Map every lesson to the concept: its role, the terms it introduces and the outcomes it serves. |
| **Open the course** | Give the learner a front page and a lesson menu without anyone retyping the data. |

Because the course is a node, every field that describes it should be readable on its own, without the document body. A viewer, a graph or a search index should be able to read the front matter and draw the node.

## 2. Four layers

Keep these apart, as the lesson spec does:

1. **Document metadata:** identity, hierarchy, ownership, version, review and rights.
2. **Concept node:** the concept, its definition, terms, relations and coherence claim.
3. **Learning design:** audience, scope, outcomes, lesson map, delivery and assessment.
4. **Learner-visible front matter:** the course opening and the lesson menu.

Layers 1 to 3 are the authoritative record. Layer 4 is a display view of them. The course manifest stays the source of truth for design decisions, so this record is an authoring view of the manifest, not a competing copy.

## 3. Common document fields

Use the common fields from `frontmatter_spec.md` section 1 unchanged: `id`, `document_type`, `title`, `summary`, `schema_version`, `version`, `status`, `owner`, `authors`, `reviewers`, `created`, `updated`, `review_due`, `language`, `tags`, `sources` and `rights`.

For a course, `document_type` is `course-scope` and `hierarchy_level` is `0`.

**Keep document status separate from review approval.** A draft can have an assigned reviewer without having been approved.

## 4. The full course record

This is a copyable starting point. Bracketed values are placeholders.

```yaml
---
schema_version: "1.0"
id: "course-[slug]"
document_type: course-scope
hierarchy_level: 0

title: "[Course title]"
summary: "[What the course covers and why it matters.]"

version: "0.1.0"
status: draft
owner: "[Accountable person or team]"
authors: []
reviewers: []
created: "2026-10-20"
updated: "2026-10-20"
review_due: null

language: en-GB
tags: []
rights:
  holder: null
  licence: null

# ---- Layer 2: the concept node -------------------------------------------
concept:
  node_id: "concept-[slug]"
  label: "[Preferred label]"
  alt_labels: []
  definition: "[One or two sentences saying what the concept is.]"
  coherence_claim: "[Why these lessons belong together. What binds them.]"
  through_line: "[The question or idea that runs through every lesson.]"
  key_terms:
    - id: T1
      term: "[Term]"
      definition: "[Plain definition.]"
      introduced_in: "lesson-[slug]-01"
  threshold_concepts: []
  misconceptions:
    - id: M1
      statement: "[A common wrong idea learners arrive with.]"
      addressed_in: ["lesson-[slug]-01"]
  relations:
    - predicate: broader
      target: "concept-[other-slug]"
      note: null
    - predicate: requires
      target: "concept-[other-slug]"
      note: null
    - predicate: contrasts_with
      target: "concept-[other-slug]"
      note: null
  external_refs: []

# ---- Layer 3: learning design --------------------------------------------
audience:
  description: "[Who this course is for.]"
  learner_pitch: introductory
  prior_knowledge: []
  prerequisites:
    knowledge: []
    required_course_ids: []

scope:
  central_topic: "[The overarching concept or topic.]"
  purpose: "[The need the course addresses.]"
  in_scope: []
  out_of_scope: []
  assumptions: []

outcomes:
  - id: CO1
    statement: "[Observable course outcome.]"
    evidence: "[What the learner will do to demonstrate this.]"
    concept_term_ids: [T1]

lesson_map:
  - lesson_id: "lesson-[slug]-01"
    sequence: 1
    title: "[Lesson title]"
    role: introduces
    course_outcome_ids: [CO1]
    concept_term_ids: [T1]
    requires_lesson_ids: []
    estimated_duration_minutes: null
    status: draft

delivery:
  mode: self-paced
  estimated_duration_minutes: null
  lesson_order: guided
  materials_required: []

assessment:
  strategy: "[How achievement of the outcomes will be evidenced.]"
  purpose: formative
  course_outcome_ids: [CO1]

support:
  accessibility_statement: null
  help_contact: null

conventions:
  referencing_style: "Harvard (Cite Them Right)"
  voice_specification: "reference/excelling-voice-specification.md"

inherits_to_lessons:
  - language
  - learner_pitch
  - referencing_style
  - voice_specification
  - rights

sources: []

review:
  academic_status: pending
  academic_approved_by: null
  academic_approved_on: null

# ---- Layer 4: learner-visible front matter -------------------------------
frontmatter:
  eyebrow: "Welcome"
  body: >
    [Explain what the course covers, why it matters and how you will work through it.]
  meta:
    duration: "[Estimated time]"
    level: "[Learner-facing pitch]"
  objectivesTitle: "By the end of this course, you will be able to:"
  objectives:
    - "[Learner-facing outcome.]"
  menu:
    title: "Lessons"
    show: [position, title, duration, outcomes]
---
```

## 5. The concept node block

This is the part a lesson record does not need.

| Field | Purpose |
|---|---|
| `concept.node_id` | Stable identifier for the concept. It does not change when the label changes. It is separate from the document `id`, so one concept can outlive a rewrite of the course. |
| `concept.label`, `alt_labels` | Preferred name and the other names people use for it. |
| `concept.definition` | A short definition that stands without the body. |
| `concept.coherence_claim` | The reason the lessons form one course. If you cannot write it, the course may be two courses. |
| `concept.through_line` | The question that every lesson helps answer. Each lesson summary should connect to it. |
| `concept.key_terms` | Terms the course defines, each with the lesson that introduces it. Learners meet a term first in one place. |
| `concept.threshold_concepts` | Ideas that change how learners see the whole topic. Leave empty if there are none. Do not invent them. |
| `concept.misconceptions` | Common wrong ideas, each tied to the lesson that addresses it. |
| `concept.relations` | Typed links to other concept nodes (see below). |
| `concept.external_refs` | Identifiers or links in outside vocabularies. Use only confirmed ones. |

### Relation predicates

Use a small controlled set so the links can be drawn and queried:

| Predicate | Meaning |
|---|---|
| `broader` | This concept sits inside the target concept. |
| `narrower` | The target concept sits inside this one. |
| `requires` | Learners need the target concept first. |
| `related` | Linked, with no ordering or containment. |
| `contrasts_with` | Easily confused with the target. Say how in `note`. |
| `applies` | This concept puts the target concept to use. |

State each link once, from the node that owns it. Do not record both directions by hand. A viewer can derive the reverse.

### Distinctions

- **`concept.definition`** says what the idea is. **`scope`** says how much of it this course teaches.
- **`coherence_claim`** explains why the lessons belong together. **`lesson_map`** lists them.
- **`concept.relations`** link concepts. **`audience.prerequisites`** link courses and knowledge. A course can require a concept without requiring another course.

## 6. The lesson map as the edges

Each entry joins the course node to a lesson node, so give it enough to draw the join.

| Field | Purpose |
|---|---|
| `lesson_id`, `sequence`, `title` | Which lesson, in what presentation order. Sequence is order, not depth. |
| `role` | How the lesson serves the concept: `introduces`, `develops`, `applies`, `synthesises` or `assesses`. |
| `course_outcome_ids` | Course outcomes the lesson serves. |
| `concept_term_ids` | Key terms the lesson teaches. |
| `requires_lesson_ids` | Lessons that must come first. This is dependency, which can differ from sequence. |
| `estimated_duration_minutes` | Lesson estimate, used to derive the course estimate. |
| `status` | Lesson lifecycle value, so the course view can show what is ready. |

Keep the lesson's own record authoritative for its content. The map holds only what the course needs to draw and check the whole.

## 7. What learners should actually see

| Learner-visible item | Course front page | Lesson menu entry |
|---|---|---|
| **Title** | Course title | Lesson title |
| **Position** | Pathway or programme, if relevant | Lesson number in the course |
| **Purpose and relevance** | Why the concept matters | One line from the lesson summary |
| **Overview** | Broad coverage and boundaries | Not shown |
| **Learning outcomes** | Course outcomes | Not shown |
| **Estimated time** | Whole-course estimate | Lesson estimate |
| **Starting knowledge** | Entry expectations | Only where a lesson has its own prerequisite |
| **Materials** | Course-wide requirements | Not shown |
| **Concept map** | How the lessons relate to the central concept | Which terms this lesson introduces |
| **Completion information** | Verified course requirements | Verified lesson state |
| **Support and accessibility** | Main support information | Not shown |

For the **default course header**, show only:

> **Pathway or course position**
> **Course title**
> Short overview explaining the concept and why it matters
> **Estimated time · Learner pitch**
> **By the end of this course, you will be able to…**
> **Lessons**, as a menu

Assessment detail and support information sit immediately below the menu, not in the header.

**Do not promise that a lesson is optional, saves answers, unlocks the next lesson or affects completion unless that behaviour has been verified.** Recording an intention in `lesson_order` or `status` does not configure Adapt or SCORM.

## 8. Inheritance rules

- **Inherit from the course:** the fields listed in `inherits_to_lessons`. A lesson may override one, and the override is visible in its own record.
- **Define per course:** concept, scope, outcomes, lesson map, assessment strategy and support information.
- **Derive automatically:** course duration from the lesson estimates, lesson position, the outcome-coverage table, breadcrumbs and the menu itself.
- **Keep internal:** authorship, approval records, versioning, scope exclusions, assumptions, misconceptions that are not shown to learners and implementation identifiers.
- **Keep runtime separate:** Adapt IDs, tracking IDs, assessment configuration and completion rules.

## 9. Coherence checks

Because the course is one concept, the record can be checked mechanically. A check that fails is a defect in the plan, not a style note.

1. Every course outcome is served by at least one lesson.
2. Every lesson serves at least one course outcome.
3. Every key term is introduced in exactly one lesson, and that lesson exists in the map.
4. Every misconception is addressed in at least one existing lesson.
5. `requires_lesson_ids` form no cycle, and no lesson requires a later lesson unless `lesson_order` allows free order.
6. `sequence` values are unique and run without gaps.
7. Nothing appears in both `in_scope` and `out_of_scope`.
8. Every `concept.relations` target resolves to a known node, or is flagged as external.
9. The course duration equals the sum of its lesson estimates, or the record says why not.
10. Learner-facing duration, level and outcomes match the authoritative fields, or are derived from them.

## 10. Decisions to settle before building the menu page

1. **Concept id.** One `concept.node_id` per course, or can a course carry more than one concept node? This plan assumes one.
2. **Relation vocabulary.** The six predicates above are a starting set. Keep them, or align them to a vocabulary you already use.
3. **Lesson roles.** Five roles are proposed. Add or drop to match how you plan courses.
4. **Free or guided order.** `delivery.lesson_order` decides whether the menu can offer any lesson at any time. Confirm what Adapt can enforce before the page implies either.

**Bottom line:** the course record defines *the concept, its place among other concepts and how the lessons break it down*. Each lesson record defines *its contribution to that concept*. The learner-facing front matter and the menu are *views of that record*, derived from it and never retyped.
