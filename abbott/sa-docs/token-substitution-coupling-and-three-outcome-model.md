# Token-substitution coupling (`tokenMode`) and the three-outcome lesson model

Status: agreed with Abbott, 9 October 2026. Design of record for execution; read
this from disk before each write rather than relying on conversation memory
(durability rule, CLAUDE.md "Decisions agreed in conversation are not durable").

This spec captures two linked, programme-wide model changes agreed in one
sitting. It governs the shell layer (generator, skeletons, the shared rules) and
every pathway-tier built after it, not one pilot course.

## A. Three learning outcomes per lesson (was two)

Every lesson carries **three** learning outcomes, and a **three-item** formative
check, one item testing each outcome. Rationale (Abbott): two outcomes
under-specify a lesson; the third is authored alongside the first two during
design, with its own consequential check item.

- Each lesson outcome still serves exactly one course outcome (AL-1) and states
  one verb + one object (AL-2).
- The three check items each name via `tests` the one lesson outcome they test;
  the three `tests` values are distinct and together cover all three of the
  lesson's outcome ids (AL-3a, tightened from "two different" to "all three,
  one per outcome").
- Check-item coupling pattern (AL-3 / CK-1), using the real `coupling` values
  (confirmed against existing les-01 records): item 1 `shell-coupled` (general,
  tests o1); item 2 `whole-prose` or `structured-fields` (context-specific body,
  tests o2, per-pack authoring as now); item 3 `token-substitution` (tests o3,
  shell body carrying `{{context}}` — see B). One per-pack body item only, to
  keep per-pack authoring light. (positionRules: position 1 = `shell-coupled`;
  "rest" = `{token-substitution, structured-fields, whole-prose}` already covers
  items 2 and 3, so no positionRules change — only the block band widens 2/3→3/3.)

## B. `token-substitution` coupling + the `tokenMode` qualifier

`token-substitution` is already a first-class coupling `variationType`
(`schemas/course-design.schema.json` contextCoupling `variationType` enum:
`token-substitution | structured-fields | whole-prose`; same set enforced by
`validate-design-schemas.py` CPL-1 coupled-variationType). This change adds a
per-case qualifier to it, available to ANY token-substitution coupling (not just
the third outcome — decided case by case at whatever gate sets that slot's
coupling).

### The token

- Token: `{{context}}`. Value source: a new top-level `context: { "label": ... }`
  in each pack's `context.json` (free text, beside the existing `character.*` and
  `subject.*` blocks). `merge-context.js` registers `{{context}}` as one of its
  own tokens (so it hard-errors only if genuinely unresolved) and substitutes it
  globally, like `character.name`.
- The surround wording stays grammar-neutral so any fill reads correctly:
  "in {{context}}", "an assessment in {{context}}", "how you study {{context}}".
  Free-text labels are the author's responsibility for grammatical fit
  (e.g. "psychology", "your subject", "subjects within the School of Health
  Sciences"); voice-lint still runs over the merged output.

### `tokenMode` (per token-substitution coupling)

- `generic` — `{{context}}` always resolves to the fixed fallback **"your
  subject"**. The pack cannot fill it; nothing is authored in the CXP. For slots
  that read better staying generic, or broad audiences.
- `cxp-fillable` (default when unset) — the token is exposed for the pack to
  fill. The pack's `context.label` is used if set; if the pack leaves it unset,
  it still falls back to "your subject".

Fill ladder for a `cxp-fillable` token-substitution slot:
1. pack sets `context.label` -> that exact phrase (subject / discipline /
   faculty grouping / anything that fits the surround);
2. pack leaves `context.label` unset -> "your subject";
3. slot set to `generic` at its gate -> always "your subject", pack cannot touch
   it.

"your subject" is the guaranteed floor, so a base/standalone build (no merge)
and an unfilled pack both render sensibly; the base course is a template and is
never shipped un-merged.

### Where `tokenMode` is recorded

- On the `contextCoupling` object (instantiations slotChoices) for a
  token-substitution slot: add optional `tokenMode` beside `coupled`,
  `variationType`, `facetOverrides`.
- On a les-01 `check.items[]` item that uses token-substitution: add optional
  `tokenMode` beside `coupling`, `tests`.
- Decided at the gate that sets that slot's coupling (for the lesson third
  outcome and its check item: les-01).

## C. The five third outcomes (this pilot course)

Course `understanding-learning-assessment-feedback-introductory`. Each serves
the same course outcome as that lesson's other two outcomes; one verb + one
object; token-bearing; default `tokenMode: cxp-fillable`.

| Lesson | Serves | o3 |
|---|---|---|
| L01 | co1 | Distinguish surface learning from deep learning in {{context}}. |
| L02 | co1 | Describe how teaching in {{context}} is organised to build your learning. |
| L03 | co2 | Explain the purpose an assessment in {{context}} serves. |
| L04 | co3 | Turn one piece of feedback in {{context}} into a specific next action. |
| L05 | co4 | Plan one change to how you study {{context}} using the learning, assessment and feedback cycle. |

Each lesson gains a third check item testing its o3 (shell body +
`{{context}}`), new MCQ content for SME academic-accuracy approval.

## D. Implementation touch-points (references by file + rule, not line number)

Mechanical / shell-layer (no gate ceremony):
- `design-kb/design-kb.gates.json` — les-01 `check` decidedValueShape:
  `items` minItems/maxItems 2 -> 3; add optional `tokenMode` enum
  `[generic, cxp-fillable]` to the check-item properties.
- `schemas/course-design.schema.json` — add optional `tokenMode` enum
  `[generic, cxp-fillable]` to the `contextCoupling` object (meaningful only when
  `variationType` = `token-substitution`).
- `tools/manifest-completeness.js` — CK-1: `check item count !== 2` -> `!== 3`.
  AL-3a: `!== 2` -> `!== 3`; replace the pairwise `tests[0] === tests[1]`
  distinctness with an all-three-distinct test that also covers all three lesson
  outcome ids; fix the detail string ("2 items, tests X and Y" -> three).
- `design-kb/design-kb.skeletons.json` — lesson `check` slot band
  `{min:2,max:3}` -> `{min:3,max:3}`; update bandRationale; positionRules keep
  position 1 shell-coupled general and `"rest"` covering positions 2-3 (item 2
  context-coupled, item 3 token-substitution).
- `.claude/commands/gate.md` — AL-3 rule statement: "exactly two check items"
  -> "exactly three ... one per outcome, all three `tests` distinct".
- `merge-context.js` (repo root, not tools/) — resolves `{{context}}` PER LESSON.
  Every token-substitution item (o3 outcome + o3 check) carries `{{context}}`
  (so it satisfies the skeleton positionRules, which admit only
  token-substitution/structured-fields/whole-prose at "rest" positions, not
  shell-coupled). `merge-context` reads each lesson's `tokenMode` from the
  generated manifest's les-01 check item that tests `-o3`
  (`readLessonTokenModes`), then substitutes `{{context}}` in each component by
  its `_id` L## prefix: `generic` -> "your subject" regardless of the pack;
  `cxp-fillable` -> `context.label`, or "your subject" when the pack sets none.
  One pack can thus fill some lessons disciplinarily and leave others generic.
  `character.*` tokens stay global. Because the token is always present,
  `tokenMode` is a pure data flag: flipping a lesson is a one-field les-01
  reopen, no text re-authoring.
- `validate-design-schemas.py` CPL-1 `valid_variation` already includes
  `token-substitution`; no count hardcoded for outcomes (OC-1 accepts >=1).

OC-1 (manifest-completeness.js) already accepts three outcomes (fails only on
zero) — no count change there.

Content (governed reopen cascade; manifest is append-only, so direct edits are
prohibited — reopen.md):
- `/reopen crs-04_lesson-map` (changeKind `amended`) — add each lesson's o3
  (serves + token-bearing text from C). This sweep marks every per-lesson
  `les-01` **invalidate** (constitutive dependency), confirmed per lesson.
- `/reopen` each `<slug>-L0x-les-01` — set the third check item (coupling
  `token-substitution`, `tokenMode`, `tests` = o3 id), its MCQ content, and the
  per-lesson `tokenMode` choice.

Shell presentation items (separate, after the model change):
- Page title: generator writes `displayTitle: ''`; populate from the lesson
  title so the page header renders.
- "By the end of this topic" -> "By the end of this lesson" (authored content;
  fix the authoring convention so future lessons use "lesson").
- New committed custom theme (child of adapt-contrib-vanilla) as the CSS home
  for: worked-example +/- cues, the Check-your-understanding section grouping +
  heading levels + background, flipcard 2x2 responsive stacking, and feedback
  overlay width + correct/wrong styling. (Flipcard can also be styled in its own
  committed `adapt-abbott-flipcard/less`.)

### Transient-red note
The rule edits (D mechanical) and the content reopens are interdependent: the
course validates green only when both are complete. There is an unavoidable
transient red window between them. Do not push a red intermediate state; verify
green end-to-end, then push for Abbott to pull and build.
