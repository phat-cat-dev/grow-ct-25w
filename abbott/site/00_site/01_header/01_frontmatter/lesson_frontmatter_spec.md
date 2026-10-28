# frontmatter

**Understood: Level 0 is the overall course topic or concept scope, which is then broken down into lessons. It is not the learner’s academic level.**

I recommend separating:

1. **Document metadata:** identity, hierarchy, scope, ownership and review information.
2. **Learning-design metadata:** outcomes, alignment, prerequisites and activities.
3. **Learner-visible front matter:** the concise introduction shown before the lesson begins.

Below is a proposed convention, not an existing enforced schema. Your current `lesson authoring template` already supports a title, subtitle, overview, duration, learner level and objectives; the broader metadata below would extend that model.

## 1. Common document front matter

Use these fields for **both course-scope documents and lessons**.

| Field | Purpose |
|---|---|
| `id` | Stable, unique identifier that does not change when the title changes. |
| `document_type` | What this document represents: `course-scope` or `lesson`. |
| `title` | Clear, human-readable title. |
| `summary` | Brief description for search, listings and orientation. |
| `schema_version` | Version of the metadata structure. |
| `version` | Version of this particular document or learning unit. |
| `status` | Controlled lifecycle value, such as `draft`, `in-review`, `approved` or `archived`. |
| `owner` | Person or team accountable for maintaining the material. |
| `authors` | People who created the material. |
| `reviewers` | People responsible for academic or editorial review. |
| `created`, `updated` | ISO dates, quoted in YAML. |
| `review_due` | Next planned review date. |
| `language` | For example, `en-GB`. |
| `tags` | A small, consistent set of discovery terms. |
| `sources` | Source identifiers and precise locators, not invented references. |
| `rights` | Rights holder and confirmed licence or reuse restrictions. |

**Keep document status separate from review approval.** A draft can have an assigned reviewer without having been approved.

## 2. Level 0: course concept-and-scope front matter

The Level 0 record should establish the **whole topic, its boundaries and what the course is intended to achieve**.

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
created: "2026-10-19"
updated: "2026-10-19"
review_due: null

language: en-GB
tags: []
rights:
  holder: null
  licence: null

audience:
  description: "[Who this course is for.]"
  learner_pitch: introductory
  prior_knowledge: []
  prerequisites: []

scope:
  central_topic: "[The overarching concept or topic.]"
  purpose: "[The need the course addresses.]"
  in_scope: []
  out_of_scope: []

outcomes:
  - id: CO1
    statement: "[Observable course outcome.]"

lesson_map:
  - lesson_id: "lesson-[slug]-01"
    sequence: 1
    title: "[Lesson title]"
    course_outcome_ids: [CO1]

delivery:
  mode: self-paced
  estimated_duration_minutes: null

assessment:
  strategy: "[How achievement of the outcomes will be evidenced.]"

conventions:
  referencing_style: "Harvard (Cite Them Right)"
  voice_specification: "reference/excelling-voice-specification.md"

sources: []

review:
  academic_status: pending
  academic_approved_by: null
  academic_approved_on: null
---
```

### Important distinctions

- **`hierarchy_level: 0`** means the root of your topic breakdown.
- **`learner_pitch: introductory`** describes the teaching pitch. It is independent of hierarchy depth.
- **`scope.in_scope` and `scope.out_of_scope`** prevent the course expanding indefinitely.
- **`outcomes` and `lesson_map`** show how the overall intention breaks down into teachable units.

A lengthy rationale, detailed curriculum map or full assessment specification belongs in the **document body**, not in front matter.

## 3. Lesson front matter

A lesson needs the common document fields plus its **relationship to the course, bounded teaching purpose and outcome alignment**.

```yaml
---
schema_version: "1.0"
id: "lesson-[slug]-01"
document_type: lesson

course_id: "course-[slug]"
parent_id: "course-[slug]"
hierarchy_level: 1
sequence: 1

title: "[Lesson title]"
summary: "[The specific idea or skill this lesson develops.]"

version: "0.1.0"
status: draft
owner: "[Accountable person or team]"
authors: []
reviewers: []
created: "2026-10-19"
updated: "2026-10-19"
review_due: null

language: en-GB
tags: []
sources: []

scope:
  focus: "[The particular part of the course topic taught here.]"
  in_scope: []
  out_of_scope: []

alignment:
  course_outcome_ids: [CO1]

prerequisites:
  knowledge: []
  required_lesson_ids: []

learning_outcomes:
  - id: LO1
    statement: "[Observable lesson outcome.]"
    course_outcome_ids: [CO1]
    evidence: "[What the learner will do to demonstrate this.]"

estimated_duration_minutes: null
materials_required: []

activities:
  - id: ACT1
    purpose: "[What this activity helps the learner understand or practise.]"
    lesson_outcome_ids: [LO1]

assessment:
  purpose: formative
  lesson_outcome_ids: [LO1]

review:
  academic_status: pending
  academic_approved_by: null
  academic_approved_on: null

frontmatter:
  eyebrow: Before you begin
  body: >
    [Explain what you will explore, why it matters and what you will do.]
  meta:
    duration: "[Estimated time]"
    level: "[Learner-facing pitch]"
  objectivesTitle: "By the end of this lesson, you will be able to:"
  objectives:
    - "[Learner-facing outcome.]"
---
```

**Use `hierarchy_level: 1` only when the lesson sits directly below the course.** If you introduce a module or topic layer, the lesson’s parent and depth should reflect that. `sequence` is presentation order, not hierarchy depth.

The `frontmatter` section above follows the shape of the current template. Ideally, its duration, pitch and objective statements should be **derived from the authoritative metadata**, rather than maintained as duplicate values.

## 4. What learners should actually see

The opening should be useful, not an administrative record.

| Learner-visible item | Course opening | Lesson opening |
|---|---|---|
| **Title** | Overall course topic | Specific lesson topic |
| **Position** | Programme/pathway, if relevant | Course/module and lesson position |
| **Purpose and relevance** | Why the course matters | Why this particular lesson matters |
| **Overview** | Broad coverage and boundaries | What you will explore and do |
| **Learning outcomes** | Course outcomes | Lesson outcomes |
| **Estimated time** | Whole-course estimate | Lesson estimate |
| **Starting knowledge** | Entry expectations | Only knowledge genuinely needed here |
| **Materials** | Course-wide requirements | Anything needed for this lesson |
| **Activities and assessment** | Overall approach | What to expect during this lesson |
| **Completion information** | Verified course requirements | Verified lesson requirements |
| **Support/accessibility information** | Main support information | Relevant lesson-specific guidance |

For the **default lesson header**, I would show only:

> **Course / Lesson position**  
> **Lesson title**  
> Short overview explaining the topic and its relevance  
> **Estimated time · Learner pitch**  
> **By the end of this lesson, you will be able to…**  
> **Before you start**, only where prerequisites or materials are necessary

Assessment instructions and support details can sit immediately below, rather than crowding the header.

**Do not promise that an activity is optional, saves answers or affects completion unless that behaviour has been verified.** Documenting an intention does not configure Adapt or SCORM.

## 5. Inheritance rules

To keep this sensible and maintainable:

- **Inherit from the course:** language, learner pitch, voice specification, referencing convention and rights, unless explicitly overridden.
- **Define per lesson:** focus, outcomes, alignment, duration, prerequisites, activities and precise source locators.
- **Derive automatically:** breadcrumbs, lesson position, rendered outcome lists and display labels.
- **Keep internal:** authorship, approval records, versioning, scope exclusions and implementation identifiers.
- **Keep runtime settings separate:** Adapt IDs, tracking IDs, assessment configuration and completion rules.

In your existing pipeline, the course manifest is already the source of truth for design decisions, as described in `the pipeline documentation`. These front-matter records should therefore be **an authoring view or export of those decisions, not a second competing source of truth**.

**Bottom line:** the Level 0 record defines *the whole topic and its boundaries*. Each lesson record defines *its contribution to that topic*. The learner-facing front matter explains *what you will learn, why it matters and how to begin*.