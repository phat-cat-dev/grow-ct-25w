# Lesson page model (v4)

Agreed with Abbott, 2 November 2026. Supersedes
[`lesson-page-model-v3.md`](lesson-page-model-v3.md)'s five-article model. The
authoritative structure remains `design-kb/design-kb.skeletons.json`
(`articleSections`, lesson archetype); this doc is the readable spec and the
record of the decisions.

Scope: **durable**. The change lands in the shared skeletons store, its schema,
and (separately, see `docs/authoring/component-specs/worked-example.md` and
the activity-1..4 slots below) the lesson archetype's `blockSequence`. Every
future course is born with this model. The three already-built criticality-tier
courses are migrated in place by hand (a shell cannot be re-scaffolded without
wiping authored content); the other 36 courses stay on v3 until their own
migration, tracked separately.

## Why: two directives, one page model

1. **Fewer, more purposeful articles.** v3's `lesson-formative` and
   `lesson-reflection` articles each held a thin sliver of content (just the
   knowledge-check, or just the reflective prompt). Merging them into one
   `lesson-practice` article — "put what you've learned into practice" —
   gives the check and the reflection a shared home without changing what
   either one does.
2. **More in-lesson activity.** v3's lesson-concept article carried exactly one
   variable "intro" slot (`concept-intro`, usually a flipcard or accordion)
   between the concept definition and the worked example. Four distinct
   activity slots (`activity-1..4`) replace it, each independently decidable
   and independently lintable, so a lesson can carry four small, varied tasks
   instead of one.

## The four articles

| meta-name | section key | title shown | blocks it holds |
|---|---|---|---|
| `article-lesson-open` | `lesson-open` | **Lesson overview** | orientation, orientation-tier, learning-outcomes |
| `article-lesson-concept` | `lesson-concept` | **{per-lesson concept title}** | concept-definition, concept-context, **activity-1, activity-2, activity-3, activity-4** (new), worked-example, practical-guidance |
| `article-lesson-practice` | `lesson-practice` | **Lesson practice** | all knowledge-check components, reflective-prompt, reflective-task |
| `article-lesson-close` | `lesson-close` | **Lesson summary** | summary, lesson-references |

Changes from v3:
- `lesson-formative` (knowledge-check) and `lesson-reflection` (reflective,
  reflective-task) merge into one `lesson-practice` article, retitled "Lesson
  practice". `roleToSection` stays monotonic (`generate-course-shell.js`
  depends on this): `knowledge-check`, `reflective`, and `reflective-task` all
  now map to `lesson-practice` instead of two separate sections.
- `concept-intro` (one variable slot, role `concept`) is renamed `activity-1`
  and joined by three new siblings `activity-2`, `activity-3`, `activity-4`,
  all role `concept`, all landing in `lesson-concept` — no new roles, no new
  schema enums beyond the four-section ones above.
- `lesson-open` and `lesson-close` are unchanged from v3.

## Why four distinct keys, not a repeated band

`generate-course-shell.js` writes exactly one block per `blockSequence` entry;
it does not expand a cardinality band into multiple blocks. A banded
`concept-intro` slot would scaffold one block and leave three to be hand-added
in every future lesson, forever. Four distinct keys sharing the single
existing role `concept` cost nothing new in the schema (`roleToSection` keys on
`role`, not `key`) and stay independently checkable: `conformance-lint.js`
matches a required block by `skeletonKey`, so four blocks sharing one key would
make only the first ever get checked, silently hiding activity mis-ordering.
Each activity must teach a distinct facet of the concept; the worked example
and the practical-guidance checklist are not counted among the four.

## Build sequence (this change)

1. This design doc (record); superseding header added to
   `lesson-page-model-v3.md`.
2. `schemas/design-kb.skeletons.schema.json`: `sectionOrder.items.enum` and all
   eleven `roleToSection` property enums collapse from the five v3 section
   names to `["lesson-open", "lesson-concept", "lesson-practice",
   "lesson-close"]`; `sectionOrder.minItems`/`maxItems` 5 -> 4.
3. `design-kb/design-kb.skeletons.json`'s `articleSections`: `sectionOrder`,
   `roleToSection` (knowledge-check/reflective/reflective-task ->
   `lesson-practice`), `sectionMeta` (drop `lesson-formative` +
   `lesson-reflection`, add `lesson-practice`), `sourcePointer.doc` -> this
   file.
4. Lesson archetype (`archetypes[id="skeletons/lesson"]`, separate edit,
   `design-kb/design-kb.skeletons.json`): rename `concept-intro` ->
   `activity-1`, clone to `activity-2/3/4`. `tools/manifest-completeness.js`'s
   three hardcoded `'concept-intro'` references and
   `tools/conformance-lint.js`'s `TITLE_CHECK_EXEMPT_KEYS` updated to match.
5. Theme CSS (`adapt-ab-theme`): add `article--lesson-practice` alongside the
   existing `article--lesson-*` rules.
6. Migrate the three criticality-tier courses in place (map by `_skeletonKey`,
   never by id, since the id numbering already diverges between lessons):

   | v3 block(s) | v3 article | v4 article | action |
   |---|---|---|---|
   | orientation, orientation-tier, learning-outcomes | a-01 (`lesson-open`) | `lesson-open` | unchanged |
   | concept-definition, concept-context | a-02 (`lesson-concept`) | `lesson-concept` | unchanged |
   | concept-intro | a-02 | `lesson-concept` | restamp `_skeletonKey` to `activity-1`; keeps its authored content |
   | *(new)* | — | `lesson-concept` | add `activity-2`, `activity-3`, `activity-4` placeholders; ids appended at the tail |
   | worked-example | a-02 | `lesson-concept` | convert component `text` -> `workedExample` (see `docs/authoring/component-specs/worked-example.md`) |
   | practical-guidance | a-02 | `lesson-concept` | unchanged |
   | check (3 blocks) | a-03 (`lesson-formative`) | `lesson-practice` | reparent; article retitled "Lesson practice" |
   | reflective-prompt | a-04 (`lesson-reflection`) | `lesson-practice` | reparent |
   | summary, lesson-references | a-05 (`lesson-close`) | `lesson-close` | reparent |
   | — | a-05 | — | delete (now empty) |

   Greenfield ids a future shell generator now emits for a lesson (15 blocks,
   `blockIdRule.step: 5`):

   ```
   a-01 lesson-open      05 orientation  10 orientation-tier  15 learning-outcomes
   a-02 lesson-concept   20 concept-definition  25 concept-context
                         30 activity-1  35 activity-2  40 activity-3  45 activity-4
                         50 worked-example  55 practical-guidance
   a-03 lesson-practice  60 check  [62] [64]  65 reflective-prompt
   a-04 lesson-close     70 summary  75 lesson-references
   ```

Each step verified (`validate-design-schemas.py`, `verify-course.js`, `lessc`
smoke, `grunt build`) and committed separately.

## Open sub-decisions flagged for Abbott

- Whether `lesson-practice`'s two activity types (knowledge-check,
  reflective/reflective-task) need distinct sub-headers within the one
  article (mirroring v3's separate "Check your understanding" / "Your
  thoughts" article titles) is left to the CSS step, as the equivalent v3
  decision was.
- The four activities' own titles are free text per lesson; no house
  convention yet exists for naming them distinctly from the worked example or
  the checklist title. Flag at first authoring pass.
