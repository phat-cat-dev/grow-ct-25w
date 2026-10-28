# matching — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec)
**Verified against:** `src/components/adapt-contrib-matching/properties.schema` (Adapt 5.56.2)
**Grounded in:** `c-225` — Adapt demo scaffold instance (`courses/academic-writing-introductory`). **No authored lesson instance exists yet** (no L0x-prefixed matching component in the pilot). The worked example below is therefore illustrative of the schema shape, not an authored voice model; treat it with caution until a real instance is built.
**Relationship to other documents:** references the Voice Specification, the Tier Specification, `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1), and the shared question-feedback pattern in `mcq.md §3`; restates none.

---

## 1. Purpose & when to reach for it

Routing is decided upstream in **Mapping Artefact Part 4** (the question-type rows). Matching presents a set of prompts, each with its own dropdown of options; the learner selects one option per prompt (pairing). It is a **question component** with scoring and feedback.

Component-specific "reach for it / don't":

- **Reach for matching** when the teaching move is *pairing*: matching terms to definitions, examples to categories, causes to effects. Each row has its own option set — they need not be identical across rows, which makes matching more flexible than sortable for tasks where the choices differ by row.
- **Don't use matching for ordering or sequencing** — that's `adapt-abbott-sortable`. Matching is about pairing a prompt to an answer from a set, not arranging items in a sequence.
- **Don't use matching as a workaround for sortable.** Before the custom sortable existed, ordering was faked with matching; don't do this now that the proper tool is available.
- **Don't overload rows.** More than 4–5 rows becomes cognitively heavy; if you have many pairings, consider splitting across multiple components or rethinking the assessment.

---

## 2. The annotated JSON shape

**[LB]** marks a load-bearing field. Matching is a question type; its structure mirrors mcq in many places.

```jsonc
{
  "_id": "c-225",
  "_parentId": "b-215",
  "_type": "component",
  "_component": "matching",
  "_classes": "",
  "_layout": "full",                      // "full" | "left" | "right"

  "title": "Matching",                    // internal / tracking
  "displayTitle": "Check your understanding",  // learner-facing heading
  "body": "<p>Match each stage of the writing cycle to its purpose.</p>", // [LB] the question stem
  "instruction": "Choose an option from each dropdown list and select Submit.", // [LB] §15.4
  "ariaQuestion": "Match each writing-cycle stage to its purpose.", // [LB] clean question for screen readers — §6

  "_attempts": 2,                         // [LB] formative ≥2 so notFinal feedback works
  "_shouldDisplayAttempts": true,
  "_questionWeight": 1,                   // score for fully correct; or sum of item scores if _hasItemScoring
  "_hasItemScoring": false,               // [LB] false = 0 or _questionWeight; true = sum per-option _score
  "_canShowModelAnswer": true,            // [LB] formative bundle
  "_canShowCorrectness": false,           // if true, replaces model-answer button with inline correct-answers display
  "_canShowFeedback": true,               // [LB] must stay true for teaching feedback
  "_canShowMarking": true,
  "_recordInteraction": true,             // SCORM cmi.interactions
  "_shouldResetAllAnswers": true,         // true = reset all on retry; false = reset only incorrect
  "_isRandom": false,                     // shuffle options within each dropdown
  "_isRandomQuestionOrder": false,        // shuffle the order of the rows
  "_allowOnlyUniqueAnswers": false,       // [LB] true = each option can only be selected once across all rows

  "placeholder": "Select an option",      // [LB] default text shown in dropdowns before selection

  "_items": [                             // [LB] the rows (prompts)
    {
      "text": "Understand the task",      // [LB] the prompt label for this row
      "_options": [                       // [LB] the options for this row's dropdown
        { "text": "Works out what you're being asked to do", "_isCorrect": true, "_score": 1 },
        { "text": "Decides what you'll say and in what order", "_isCorrect": false, "_score": 0 },
        { "text": "Gets it down, roughly", "_isCorrect": false, "_score": 0 },
        { "text": "Improves what's there", "_isCorrect": false, "_score": 0 }
      ]
    }
    // …one object per row
  ],

  "_feedback": {                          // [LB] the teaching payload — shared pattern with mcq (mcq.md §3)
    "title": "",
    "correct": "That's right. Each stage has a distinct job…",
    "_incorrect": {
      "notFinal": "Not quite. Think about what each stage's specific job is, and look again.",
      "final": "The correct pairings are: 'Understand the task' → 'Works out what you're being asked to do'; …"
    },
    "_partlyCorrect": {
      "notFinal": "Some of those are right, but not all. Check each row carefully.",
      "final": "The correct pairings are: … Some of your matches were right, but the full set matters."
    }
  },

  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true },

  "_isPartOfAssessment": false            // [LB] assessment-extension field, not in schema — false = formative (§7)
}
```

Global aria strings (`ariaRegion`, `ariaCorrectAnswer`, `ariaUserAnswer`, `correctAnswerPrefix`, `correctAnswersPrefix`) and `_buttons` inherit from `course.json` `_globals`; leave defaults unless overriding.

---

## 3. Authoring guardrails (hard rules)

1. **Each row has its own `_options` array.** Unlike mcq (one option set for the whole question), matching lets you define different options per row. Options do not have to be identical across rows, but they often share a consistent set for true matching tasks.
2. **Exactly one `_isCorrect: true` per row.** Each row must have exactly one correct option. A row with zero or multiple correct options breaks the marking.
3. **Use `_allowOnlyUniqueAnswers` deliberately.** When `true`, an option selected in one row is disabled in others — appropriate when each option should be used once. When `false` (default), the same option can be selected in multiple rows.
4. **Feedback follows the shared two-tier pattern** (`notFinal` = pointer, `final` = teach) — see **`mcq.md §3`**. Matching-specific addition: author the `_partlyCorrect` branch too, since partial credit is common (some rows correct, some not).
5. **Set the formative/summative bundle as a unit.**
   - *Formative* (pilot pattern): `_attempts` ≥ 2, `_canShowModelAnswer: true`, `_canShowFeedback: true`, `_isPartOfAssessment: false`, not inside an assessment article.
   - *Summative*: inside an assessment article, with disclosure controlled by the assessment extension. See `scoring-and-summative-model.md`.
6. **If `_isRandom: true`, never reference option order in feedback** ("the first option", etc.).
7. **If `_isRandomQuestionOrder: true`, never reference row order in feedback** ("in the first row", etc.).

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `body` | The question stem — a genuine question, not rhetorical filler | §11.7 |
| `instruction` | Activity instruction — one line on what to do | §15.4 |
| `_items[].text` | Row prompt labels; clear and concise | §13 (register) |
| `_items[]._options[].text` | Option labels; neutral phrasing | §11.6, §12.3 |
| `_feedback.correct` | Confirm-with-reason; never bare | §15.5 |
| `_feedback._incorrect.*` / `_partlyCorrect.*` | Name what was wrong, explain the issue, teach the correct pairings | §15.5 |

Formative feedback contracts (open-decisions #15). Feedback is evaluative about the work, never about the student.

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

Matching's *demand* is set by **Tier Spec §7** (the assessment dimension). This doc names which fields those rows govern:

- **Question form** row → the `body` stem and complexity of the task.
- **Stimulus** row → how much scene-setting `body` carries.
- **Discrimination** row → plausibility of distractors in `_options`. At introductory, options are clearly distinguishable; at higher tiers, distractors require closer analysis to reject.

Register, vocabulary, and outcome-verb range come from the pathway's anchored **Voice Spec §16** band. Do not restate §16 here.

---

## 6. Accessibility requirements

- **`ariaQuestion`** — populate it with the clean question when `body` carries HTML, block quotes, or scene-setting, so the screen reader announces a clear question when focusing the dropdowns.
- **Dropdown accessibility.** The component uses native `<select>` elements. Screen readers announce the prompt (`_items[].text`) and the dropdown options. Keep prompt text concise.
- **`placeholder`** is announced as the initial dropdown value; make it instructional ("Select an option") not decorative.
- **Never rely on colour alone.** Correctness feedback uses text, not just colour.
- Global aria strings (`ariaCorrectAnswer`, `ariaUserAnswer`) default sensibly; override only for wording changes.

---

## 7. Known gotchas & findings

- **Per-row option sets.** Unlike mcq's single `_items` array of options, matching has `_items` as rows and `_options` nested within each. This is the defining structural difference.
- **`_allowOnlyUniqueAnswers`** is `false` by default. If your task requires each option to be used exactly once (a true 1:1 matching), set it to `true`.
- **`_isPartOfAssessment`** is an assessment-extension field, not in the component schema. Its presence as `false` marks formative; inside an assessment article it is managed automatically.
- **`_canShowCorrectness: true` replaces the model-answer button.** It displays the correct answer inline below each row after submission. Decide which disclosure mode you want.
- **Partial credit.** The `_partlyCorrect` feedback branch fires when some but not all rows are correct. Author it — don't leave it blank, or the learner gets `_incorrect.final` even when partly right.
- **Demo scaffold only in pilot.** `c-225` is Adapt demo content, not authored to programme voice. The first real authored matching component should verify that the accessibility and feedback patterns work as expected before this spec is finalised.

---

## 8. Worked example

**Note:** No authored lesson instance exists yet. The example below is a **hypothetical** matching task in programme voice, illustrating the schema shape and feedback pattern. Treat it as illustrative, not as the reference instance.

```json
{
  "_id": "ILLUSTRATIVE-matching-01",
  "_parentId": "ILLUSTRATIVE-b-01",
  "_type": "component",
  "_component": "matching",
  "_classes": "",
  "_layout": "full",
  "title": "Check your understanding: stage purposes",
  "displayTitle": "Check your understanding",
  "body": "<p>Match each stage of the writing cycle to its purpose.</p>",
  "instruction": "Choose an option from each dropdown list and select Submit.",
  "ariaQuestion": "Match each writing-cycle stage to its purpose.",
  "_attempts": 2,
  "_shouldDisplayAttempts": true,
  "_questionWeight": 1,
  "_hasItemScoring": false,
  "_canShowModelAnswer": true,
  "_canShowCorrectness": false,
  "_canShowFeedback": true,
  "_canShowMarking": true,
  "_recordInteraction": true,
  "_shouldResetAllAnswers": true,
  "_isRandom": false,
  "_isRandomQuestionOrder": false,
  "_allowOnlyUniqueAnswers": true,
  "placeholder": "Select an option",
  "_isPartOfAssessment": false,
  "_items": [
    {
      "text": "Understand the task",
      "_options": [
        { "text": "Works out what you're being asked to do", "_isCorrect": true, "_score": 0 },
        { "text": "Decides what you'll say and in what order", "_isCorrect": false, "_score": 0 },
        { "text": "Gets it down, roughly", "_isCorrect": false, "_score": 0 },
        { "text": "Improves what's there", "_isCorrect": false, "_score": 0 },
        { "text": "Catches the final errors", "_isCorrect": false, "_score": 0 }
      ]
    },
    {
      "text": "Plan",
      "_options": [
        { "text": "Works out what you're being asked to do", "_isCorrect": false, "_score": 0 },
        { "text": "Decides what you'll say and in what order", "_isCorrect": true, "_score": 0 },
        { "text": "Gets it down, roughly", "_isCorrect": false, "_score": 0 },
        { "text": "Improves what's there", "_isCorrect": false, "_score": 0 },
        { "text": "Catches the final errors", "_isCorrect": false, "_score": 0 }
      ]
    },
    {
      "text": "Draft",
      "_options": [
        { "text": "Works out what you're being asked to do", "_isCorrect": false, "_score": 0 },
        { "text": "Decides what you'll say and in what order", "_isCorrect": false, "_score": 0 },
        { "text": "Gets it down, roughly", "_isCorrect": true, "_score": 0 },
        { "text": "Improves what's there", "_isCorrect": false, "_score": 0 },
        { "text": "Catches the final errors", "_isCorrect": false, "_score": 0 }
      ]
    },
    {
      "text": "Edit",
      "_options": [
        { "text": "Works out what you're being asked to do", "_isCorrect": false, "_score": 0 },
        { "text": "Decides what you'll say and in what order", "_isCorrect": false, "_score": 0 },
        { "text": "Gets it down, roughly", "_isCorrect": false, "_score": 0 },
        { "text": "Improves what's there", "_isCorrect": true, "_score": 0 },
        { "text": "Catches the final errors", "_isCorrect": false, "_score": 0 }
      ]
    },
    {
      "text": "Proofread",
      "_options": [
        { "text": "Works out what you're being asked to do", "_isCorrect": false, "_score": 0 },
        { "text": "Decides what you'll say and in what order", "_isCorrect": false, "_score": 0 },
        { "text": "Gets it down, roughly", "_isCorrect": false, "_score": 0 },
        { "text": "Improves what's there", "_isCorrect": false, "_score": 0 },
        { "text": "Catches the final errors", "_isCorrect": true, "_score": 0 }
      ]
    }
  ],
  "_feedback": {
    "title": "",
    "correct": "That's right. Each stage has a distinct job, and knowing what each one does is the foundation for working through them in order.",
    "_incorrect": {
      "notFinal": "Not quite. Think about what each stage's specific purpose is — what single job does it do? — and try again.",
      "final": "The correct pairings are: <em>Understand the task</em> → 'Works out what you're being asked to do'; <em>Plan</em> → 'Decides what you'll say and in what order'; <em>Draft</em> → 'Gets it down, roughly'; <em>Edit</em> → 'Improves what's there'; <em>Proofread</em> → 'Catches the final errors'. Each stage has a distinct job, and separating them is what makes the process manageable."
    },
    "_partlyCorrect": {
      "notFinal": "Some of those are right, but not all. Remember: each stage has one specific job. Look again at the ones you're less sure about.",
      "final": "The correct pairings are: <em>Understand the task</em> → 'Works out what you're being asked to do'; <em>Plan</em> → 'Decides what you'll say and in what order'; <em>Draft</em> → 'Gets it down, roughly'; <em>Edit</em> → 'Improves what's there'; <em>Proofread</em> → 'Catches the final errors'. Some of your matches were right, but the full set matters."
    }
  },
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

**How it would satisfy the spec (if authored):**

- **Guardrail 1 & 2** — each row has its own `_options`, exactly one `_isCorrect: true` per row.
- **Guardrail 3** — `_allowOnlyUniqueAnswers: true` because each purpose should be used once.
- **Guardrail 4** — two-tier feedback with `_partlyCorrect` branch authored.
- **Guardrail 5** — formative bundle intact.
- **§4 voice** — `correct` confirms with reason; `final` names all correct pairings and teaches.
- **§6 accessibility** — `ariaQuestion` populated; `placeholder` instructional.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **matching** component. Register and content-type voice live in the **Voice Specification**; tier demand and assessment parity live in the **Tier Specification**; scoring mechanics live in **`scoring-and-summative-model.md`**; the shared question-feedback two-tier pattern lives in **`mcq.md §3`**; teaching-move routing lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of matching authoring spec — v0.1.*
