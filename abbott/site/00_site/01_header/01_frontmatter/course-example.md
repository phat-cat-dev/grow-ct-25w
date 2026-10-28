---
schema_version: "1.0"
id: "course-design-tokens"
document_type: course-scope
hierarchy_level: 0

title: "Design tokens for coherent courses"
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

concept:
  node_id: "concept-design-tokens"
  label: "Design tokens"
  alt_labels: []
  definition: "Named design decisions, such as a colour, a size or a space, that every part of a course reads from one place."
  coherence_claim: "[Why these lessons belong together. What binds them.]"
  through_line: "How can a course stay consistent as it grows without anyone matching things by hand?"
  key_terms:
    - id: T1
      term: "Token"
      definition: "A named design decision. Components read it by name and never hold the raw value."
      introduced_in: "lesson-tokens-01"
    - id: T2
      term: "Cascade"
      definition: "The way a token set at a high level reaches everything below it unless something overrides it."
      introduced_in: "lesson-tokens-02"
    - id: T3
      term: "Theme"
      definition: "A complete set of token values that changes how the whole course looks."
      introduced_in: "lesson-tokens-04"
    - id: T4
      term: "Block metadata"
      definition: "Data a block carries about itself so the system can place, label and check it."
      introduced_in: "lesson-tokens-03"
  threshold_concepts: []
  misconceptions:
    - id: M1
      statement: "[A common wrong idea learners arrive with.]"
      addressed_in: ["lesson-[slug]-01"]
  relations:
    - predicate: broader
      target: "concept-design-systems"
      note: null
    - predicate: requires
      target: "concept-css-custom-properties"
      note: null
    - predicate: applies
      target: "concept-accessibility"
      note: "contrast and spacing rules"
    - predicate: contrasts_with
      target: "concept-style-guide"
      note: "a guide describes, a token system enforces"
  external_refs: []

audience:
  description: "[Who this course is for.]"
  learner_pitch: intermediate
  prior_knowledge: []
  prerequisites:
    knowledge: ["You can read basic CSS, for example a custom property such as var(--accent).", "You have built or edited a course page before."]
    required_course_ids: []

scope:
  central_topic: "[The overarching concept or topic.]"
  purpose: "[The need the course addresses.]"
  in_scope: []
  out_of_scope: []
  assumptions: []

outcomes:
  - id: CO1
    statement: "Explain how a token system keeps a course visually consistent."
    evidence: null
    concept_term_ids: null
  - id: CO2
    statement: "Build course blocks that carry their own metadata."
    evidence: null
    concept_term_ids: null
  - id: CO3
    statement: "Evaluate a theme against accessibility guidance."
    evidence: null
    concept_term_ids: null

lesson_map:
  - lesson_id: "lesson-tokens-01"
    sequence: 1
    title: "What a token is"
    summary: "Meet the smallest unit of a design system and see why a name beats a raw value."
    role: introduces
    course_outcome_ids: ["CO1"]
    concept_term_ids: ["T1"]
    requires_lesson_ids: []
    estimated_duration_minutes: 10
    status: null
  - lesson_id: "lesson-tokens-02"
    sequence: 2
    title: "The token cascade"
    summary: "Follow a value from the page down to a single button and see what overrides it."
    role: develops
    course_outcome_ids: ["CO1"]
    concept_term_ids: ["T2"]
    requires_lesson_ids: ["lesson-tokens-01"]
    estimated_duration_minutes: 12
    status: null
  - lesson_id: "lesson-tokens-03"
    sequence: 3
    title: "Designing for depth"
    summary: "Build a block that carries its own metadata and watch it stay coherent."
    role: develops
    course_outcome_ids: ["CO1", "CO2"]
    concept_term_ids: ["T4"]
    requires_lesson_ids: ["lesson-tokens-02"]
    estimated_duration_minutes: 12
    status: null
  - lesson_id: "lesson-tokens-04"
    sequence: 4
    title: "Themes and modes"
    summary: "Swap a whole set of values and keep the course readable in light and dark."
    role: applies
    course_outcome_ids: ["CO2", "CO3"]
    concept_term_ids: ["T3"]
    requires_lesson_ids: ["lesson-tokens-02"]
    estimated_duration_minutes: 15
    status: null
  - lesson_id: "lesson-tokens-05"
    sequence: 5
    title: "Checking accessibility"
    summary: "Test contrast, spacing and focus against the tokens you chose."
    role: applies
    course_outcome_ids: ["CO3"]
    concept_term_ids: []
    requires_lesson_ids: ["lesson-tokens-04"]
    estimated_duration_minutes: 14
    status: null
  - lesson_id: "lesson-tokens-06"
    sequence: 6
    title: "Pulling it together"
    summary: "Review a small course end to end and say what keeps it coherent."
    role: synthesises
    course_outcome_ids: ["CO1", "CO2", "CO3"]
    concept_term_ids: []
    requires_lesson_ids: ["lesson-tokens-03", "lesson-tokens-05"]
    estimated_duration_minutes: 10
    status: null

delivery:
  mode: self-paced
  estimated_duration_minutes: null
  lesson_order: guided
  materials_required: ["A small course page of your own to experiment on", "About an hour in total, in any number of sittings"]

assessment:
  strategy: "[How achievement of the outcomes will be evidenced.]"
  purpose: formative
  course_outcome_ids: ["CO1"]

support:
  accessibility_statement: "Every example is keyboard-navigable and described in text. Need an adjustment? Contact your tutor or the course help link."
  help_contact: null

conventions:
  referencing_style: "Harvard (Cite Them Right)"
  voice_specification: "reference/excelling-voice-specification.md"

inherits_to_lessons: ["language", "learner_pitch", "referencing_style", "voice_specification", "rights"]

sources: []

review:
  academic_status: pending
  academic_approved_by: null
  academic_approved_on: null

frontmatter:
  eyebrow: "Welcome"
  body: >
    Consistent courses do not come from matching colours by hand. They come
    from a system. You will meet the idea of a design token, follow it through
    a real course, and learn to check that what you build stays coherent and
    accessible.
  meta:
    duration: "1 h 13 min"
    level: "Intermediate"
  objectivesTitle: "By the end of this course, you will be able to:"
  objectives: ["Explain how a token system keeps a course visually consistent.", "Build course blocks that carry their own metadata.", "Evaluate a theme against accessibility guidance."]
  menu:
    title: "Lessons"
    show: ["position", "title", "duration", "outcomes"]
---

# Design tokens for coherent courses

[What the course covers and why it matters.]

## The concept

**Design tokens.** Named design decisions, such as a colour, a size or a space, that every part of a course reads from one place.

**Why these lessons belong together.** [Why these lessons belong together. What binds them.]

**The question running through the course.** How can a course stay consistent as it grows without anyone matching things by hand?

## Scope

**In scope**

- None yet.

**Out of scope**

- None yet.

## Outcomes

- **CO1** Explain how a token system keeps a course visually consistent.
- **CO2** Build course blocks that carry their own metadata.
- **CO3** Evaluate a theme against accessibility guidance.

## Lessons

| # | Lesson | Role | Time |
|---|---|---|---|
| 1 | What a token is | introduces | 10 min |
| 2 | The token cascade | develops | 12 min |
| 3 | Designing for depth | develops | 12 min |
| 4 | Themes and modes | applies | 15 min |
| 5 | Checking accessibility | applies | 14 min |
| 6 | Pulling it together | synthesises | 10 min |

## Rationale

<!-- Longer rationale, the detailed curriculum map and the full assessment
     specification belong here in the body, not in the front matter. -->

## Assessment

<!-- How achievement of the outcomes will be evidenced. -->

## Sources

<!-- Source identifiers and precise locators. Do not invent references. -->
