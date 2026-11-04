# Lesson page model (v3)

**Superseded 2 November 2026 by
[`lesson-page-model-v4.md`](lesson-page-model-v4.md)**, which merges the
`lesson-formative` and `lesson-reflection` articles below into one
`lesson-practice` article and adds four `activity-1..4` placeholder blocks to
`lesson-concept`. The shared store and schema now generate v4 for every new
course. Kept here as the historical record and because the 36 already-built
courses in the other 12 pathways (every pathway except `criticality`) still
carry this v3 five-article structure on disk until their own migration lands
(deferred; see v4 doc). Do not use this doc to author new content; use v4.

Agreed with Abbott, 9 October 2026 (this sitting). Supersedes the v2 three-section
model (`opening / main / closing`) for lesson pages. The authoritative structure
remains `design-kb/design-kb.skeletons.json` (`articleSections`, lesson
archetype); this doc is the readable spec and the record of the decisions.

Scope: **durable**. The change lands in the shared skeletons store, the shell
generator (`tools/generate-course-shell.js`) and the schema, so every future
course is born with this model; the one already-built pilot
(`understanding-learning-assessment-feedback-introductory`) is then patched to
match by hand (it cannot be re-scaffolded without wiping authored content).

## The five articles

A lesson page is cut into five titled **articles** (an Adapt article's title
renders as a section header above its blocks). Meta-names are the stable section
keys used in the store and generator; the title shown is the student-facing
header.

| meta-name | section key | title shown | blocks it holds |
|---|---|---|---|
| `article-lesson-open` | `lesson-open` | **Lesson overview** | orientation, **orientation-tier** (new), learning-outcomes |
| `article-lesson-concept` | `lesson-concept` | **{per-lesson concept title}** | concept-definition, concept-context, concept-intro (flipcard), worked-example, practical-guidance |
| `article-lesson-formative` | `lesson-formative` | **Check your understanding** | all knowledge-check components |
| `article-lesson-reflection` | `lesson-reflection` | **Your thoughts** | reflective-prompt, reflective-task |
| `article-lesson-close` | `lesson-close` | **Lesson summary** | summary, lesson-references |

Changes from v2:
- `opening` splits: orientation + orientation-tier + learning-outcomes become
  `lesson-open`; the concept blocks move out to `lesson-concept`.
- `main` is absorbed into `lesson-concept` (worked-example + practical-guidance
  now sit under the concept article).
- `closing` splits three ways: knowledge-checks → `lesson-formative`,
  reflective → `lesson-reflection`, summary + references → `lesson-close`.

## New element: orientation-tier

A new block/role `orientation-tier`, a `palette/text` component, placed in
`lesson-open` between orientation and learning-outcomes.

- **Purpose:** situate the lesson's topic at the course's **tier**, speaking to
  the academic level and the student's likely lifecycle stage and its
  challenges. Introductory ≈ Level 3/4 (entering/early undergraduate),
  intermediate ≈ Level 5/6 (mid/later undergraduate), advanced ≈ Level 6/7
  (final-year/postgraduate).
- **Tier source:** the course tier is fixed (`manifest.facetSet.tier`), so the
  passage is tier-aware without a per-lesson tier decision.
- **Authoring venue:** authored per lesson as prose (like orientation), from
  this lesson's `crs-04` topic plus the course tier. The generator creates the
  block and a placeholder component; the prose is written at authoring time.
- **Coupling:** generic (subject-neutral) by default, with the slot markable as
  `token-substitution` or `structured-fields` coupled later if a subject needs
  it; the primary content is tier context, not subject.

## New per-lesson value: concept title

The `lesson-concept` article's title is decided per lesson, **AI-proposed,
human-confirmed**, recorded as `conceptTitle` on each lesson's entry in
`crs-04_lesson-map`. Guidance: usually "Understanding {concept}" or "{concept}
at university". The generator reads it at scaffold time and writes it as the
concept article's `displayTitle`; if absent, it falls back to the lesson title
so a shell still generates.

## Heading hierarchy (ARIA)

Adapt's level model, already live via `_accessibility._ariaLevels` and recorded
in the skeletons store's `headingRules` (A55, 14 September 2026):

- page title — aria level 1
- **article title — aria level 2** (the section headers: "Lesson overview",
  the concept title, "Check your understanding", "Your thoughts", "Lesson
  summary")
- block title — aria level 3
- **component title (`displayTitle`) — aria level 4** (secondary headers within
  a section)

So a component header is already secondary to its article header. We use this
directly:

- **Check questions:** each knowledge-check component's literal question stem
  becomes its `displayTitle` (a level-4 heading), carrying a
  `knowledge-check-question` class, so it reads as that component's header but
  sits visually below the "Check your understanding" article header with correct
  ARIA. The per-component "Check your understanding" displayTitle is dropped (the
  article header carries it once).
- **Learning outcomes:** the "Lesson learning outcomes" component header is
  hidden (it sits under the "Lesson overview" article header).

Theme CSS (`adapt-ab-theme`) defines the visible treatment of this hierarchy
— the level-2 section header and the modest level-4 `knowledge-check-question`
sub-header — so the hierarchy Adapt expresses in ARIA is matched visually.

## Section classes for styling

The generator writes a section class onto each article so the theme can style
sections distinctly: `article--lesson-open`, `article--lesson-concept`,
`article--lesson-formative`, `article--lesson-reflection`,
`article--lesson-close` (alongside any existing `_classes`).

## Build sequence

1. This design doc (record).
2. `design-kb/design-kb.skeletons.json`: new `articleSections` (sectionOrder,
   roleToSection, per-section title + class + meta-name); lesson archetype gains
   the `orientation-tier` block.
3. Schema: allow the new `orientation-tier` role / article section; allow
   `conceptTitle` on a `crs-04` lesson entry; confirm article `displayTitle`/
   `_classes` are permitted.
4. `tools/generate-course-shell.js`: write article `displayTitle` + section
   `_classes` from the section config; create the `orientation-tier` block/
   component; read `conceptTitle` per lesson for the concept article.
   Verified by regenerating a throwaway shell and inspecting the article tree.
5. Reopen `crs-04_lesson-map`: realign the five page titles **and** add each
   lesson's confirmed `conceptTitle` (one reopen).
6. Patch the pilot's `en/articles.json`, `en/blocks.json`, `en/components.json`
   to the five-article structure: re-parent blocks, set article titles/classes,
   add the orientation-tier components (author the five tier passages), move the
   check question stems into headers, hide the learning-outcomes header.
7. Theme CSS: section header hierarchy, the `knowledge-check-question`
   sub-header, section separation.

Each step verified (verify-course, voice-lint, lessc smoke, build) and committed
separately. No push without instruction.

## Open sub-decisions flagged for Abbott

- The other three section titles ("{concept title}", "Your thoughts", "Lesson
  summary") render as level-2 article headers like the two named ones; whether
  the concept / reflection / close sections also need a distinct visual weight
  from "Lesson overview" and "Check your understanding" is left to the CSS step
  (Abbott: "we will return to this").
- orientation-tier prose authoring venue is set here to les-01-style prose
  authoring from crs-04 inputs; if Abbott wants it a structured `crs-04` value
  instead, that is a one-line change to step 5.
