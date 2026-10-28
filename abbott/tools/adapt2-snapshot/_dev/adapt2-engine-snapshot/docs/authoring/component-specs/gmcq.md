# gmcq — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec)
**Verified against:** `src/components/adapt-contrib-gmcq/properties.schema` (Adapt 5.56.2)
**Grounded in:** `c-210` — Adapt demo scaffold instance (`courses/academic-writing-introductory`). **No authored lesson instance exists yet** (no L0x-prefixed gmcq component in the pilot). The worked example below is therefore illustrative of the schema shape, not an authored voice model; treat it with caution until a real instance is built.
**Relationship to other documents:** references the Voice Specification, the Tier Specification, and the shared question-feedback pattern in `mcq.md §3`; restates none.

---

## 1. Purpose & when to reach for it

Routing is decided upstream in **Mapping Artefact Part 4** (the question-type rows). GMCQ (Graphical Multiple Choice Question) is a variant of mcq where each option is represented by an image with an optional caption.

Component-specific "reach for it / don't":

- **Reach for gmcq** when the discrimination task is *visual*: matching a diagram, identifying a correct chart, recognising a visual pattern, or any mcq where the options cannot be adequately distinguished by text alone.
- **Don't use gmcq for text-based questions** — that's `mcq`. If the options can be expressed adequately in words, prefer mcq for simplicity and accessibility.
- **Don't use gmcq for ordering/sequencing** — that's `adapt-abbott-sortable`.
- **Don't use gmcq for pairing** — that's `matching`.

GMCQ shares mcq's question mechanics (feedback, attempts, scoring, `_selectable`); the structural difference is that `_items` carry `_graphic` objects.

---

## 2. The annotated JSON shape

**[LB]** marks a load-bearing field. GMCQ is a question type; its structure mirrors mcq closely.

```jsonc
{
  "_id": "c-210",
  "_parentId": "b-205",
  "_type": "component",
  "_component": "gmcq",
  "_classes": "",
  "_layout": "full",                      // gmcq is typically full-width

  "title": "Graphical Multiple Choice Question",  // internal / tracking
  "displayTitle": "Check your understanding",      // learner-facing heading
  "body": "<p>Which diagram correctly shows the relationship?</p>", // [LB] the question stem
  "instruction": "Choose one option and select Submit.", // [LB] §15.4
  "ariaQuestion": "Which diagram correctly shows the relationship?", // [LB] clean question for screen readers

  "_attempts": 2,                         // [LB] formative >= 2 so notFinal feedback works
  "_shouldDisplayAttempts": true,
  "_questionWeight": 1,
  "_hasItemScoring": false,               // [LB] false = 0 or _questionWeight; true = sum of _score
  "_canShowModelAnswer": true,            // [LB] formative bundle
  "_canShowCorrectness": false,           // if true, replaces model-answer button
  "_canShowFeedback": true,               // [LB] must stay true for teaching feedback
  "_canShowMarking": true,
  "_recordInteraction": true,             // SCORM cmi.interactions
  "_isRandom": false,                     // [LB] shuffle options — if true, don't reference option order
  "_selectable": 1,                       // [LB] how many options learner may pick

  "_columns": 3,                          // number of columns for layout (0 = default)
  "_isRound": false,                      // if true, images get 50% border radius

  "_items": [                             // [LB] the options with graphics
    {
      "text": "Diagram A",                // [LB] optional caption below image
      "altText": "",                      // screen-reader override for pronunciation
      "_shouldBeSelected": true,          // [LB] marks a correct option
      "_isPartlyCorrect": false,
      "feedback": "",                     // per-item feedback — single-select only (see mcq.md §3)
      "_score": 0,
      "_graphic": {                       // [LB] the image for this option
        "large": "course/en/images/option-a.png",   // desktop image
        "small": "course/en/images/option-a.png",   // mobile image
        "alt": "A flow diagram showing…",           // [LB] meaningful alt text
        "attribution": ""
      }
    }
    // …remaining options
  ],

  "_feedback": {                          // [LB] the teaching payload — shared pattern (mcq.md §3)
    "title": "",
    "correct": "That's right. Diagram A shows the relationship because…",
    "_incorrect": {
      "notFinal": "Not quite. Look at how the arrows connect the elements and try again.",
      "final": "The correct answer is Diagram A. It shows the relationship because…"
    },
    "_partlyCorrect": { "notFinal": "", "final": "" }
  },

  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true },

  "_isPartOfAssessment": false            // [LB] assessment-extension field — false = formative
}
```

Global aria strings (`ariaRegion`, `ariaCorrectAnswer`, `ariaUserAnswer`) and `_buttons` inherit from `course.json` `_globals`; leave defaults unless overriding.

---

## 3. Authoring guardrails (hard rules)

GMCQ shares mcq's question mechanics. The guardrails below extend those in **`mcq.md §3`**; read that first.

1. **`_shouldBeSelected` count must match intent.** Single-select: exactly one `true`. Multi-select: set `_selectable` to the number of correct options and mark that many `true`.
2. **Every distractor must be defensibly wrong, and the learner must be told why.** The feedback pattern is shared with mcq (see `mcq.md §3`).
3. **`notFinal` is a pointer; `final` is the teach.** Same two-tier pattern as mcq — see **`mcq.md §3`** for the discipline.
4. **Set the formative/summative bundle as a unit.** Same as mcq (`mcq.md §3`, guardrail 4).
5. **Per-item `feedback` is single-select only.** Same as mcq — ignored on multi-select.
6. **If `_isRandom: true`, never reference option order** in `body`, `instruction`, `_items[].text`, or feedback.
7. **Each image must have meaningful `alt` text.** Because the discrimination is visual, the `alt` text must describe what the image shows, not just "Option A". Screen-reader users must be able to distinguish the options.
8. **Image dimensions should be consistent.** All option images should be the same aspect ratio for clean layout; `_columns` controls the grid.

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `body` | The question stem — a genuine question | §11.7 |
| `instruction` | Activity instruction — one line on what to do | §15.4 |
| `_items[].text` | Option caption; neutral phrasing | §11.6, §12.3 |
| `_items[]._graphic.alt` | Alt text; describe what the image shows | §14 |
| `_feedback.correct` | Confirm-with-reason; never bare | §15.5 |
| `_feedback._incorrect.*` | Name what was chosen, explain the issue, teach | §15.5 |

Formative feedback contracts (open-decisions #15). Feedback is evaluative about the work, never about the student.

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

GMCQ's *demand* is set by **Tier Spec §7** (the assessment dimension). This doc names which fields those rows govern:

- **Question form** row → the `body` stem and type of visual discrimination.
- **Stimulus** row → complexity of the images.
- **Discrimination** row → visual plausibility of distractors. At introductory, differences are clear; at higher tiers, distractors require closer analysis.

Register, vocabulary, and outcome-verb range come from the pathway's anchored **Voice Spec §16** band. Do not restate §16 here.

---

## 6. Accessibility requirements

- **`alt` text on every option image is mandatory.** Each `_items[]._graphic.alt` must describe the image meaningfully so screen-reader users can discriminate between options. Generic alt like "Option 1" defeats the component's purpose.
- **`ariaQuestion`** — populate it with the clean question when `body` carries HTML or scene-setting.
- **Never rely on colour alone.** If the visual discrimination involves colour, ensure shape or label differences also distinguish the options.
- **`_isRound`** — use only when circular cropping does not obscure essential visual information.
- Global aria strings default sensibly; override only if needed.

---

## 7. Known gotchas & findings

- **GMCQ is always full-width.** The schema sets `_supportedLayout: "both"`, but in practice the image grid needs width; avoid half-width layouts.
- **`_columns`** defaults to 0 (component decides). Set explicitly (2, 3, or 4) for consistent layout.
- **`_canShowCorrectness: true` replaces the model-answer button.** Decide which disclosure mode you want.
- **`_isPartOfAssessment`** is an assessment-extension field, not in the component schema. Its presence as `false` marks formative.
- **Demo scaffold only in pilot.** `c-210` is Adapt demo content, not authored to programme voice. The first real authored gmcq should verify accessibility and feedback patterns work as expected.

---

## 8. Worked example

**Note:** No authored lesson instance exists yet. The example below is from the Adapt demo scaffold (`c-210`), reproduced to show schema shape. It is **ILLUSTRATIVE**, not a voice model.

```json
{
  "_id": "c-210",
  "_parentId": "b-205",
  "_type": "component",
  "_component": "gmcq",
  "_classes": "",
  "_layout": "full",
  "title": "Graphical Multiple Choice Question",
  "displayTitle": "Graphical Multiple Choice Question",
  "body": "The <b>Graphical Multiple Choice Question</b> is an alternative to the standard MCQ, and allows you to ask a question and present the options as graphics (with accompanying captions). This component is always spanned.",
  "instruction": "Choose option 2 and select Submit.",
  "ariaQuestion": "",
  "_attempts": 1,
  "_shouldDisplayAttempts": false,
  "_hasItemScoring": false,
  "_questionWeight": 1,
  "_isRandom": false,
  "_selectable": 1,
  "_canShowModelAnswer": true,
  "_canShowCorrectness": false,
  "_canShowFeedback": true,
  "_canShowMarking": true,
  "_recordInteraction": true,
  "_columns": 3,
  "_isRound": false,
  "_items": [
    {
      "text": "Option 1",
      "altText": "",
      "_shouldBeSelected": false,
      "_isPartlyCorrect": false,
      "_graphic": {
        "alt": "",
        "attribution": "",
        "large": "course/en/images/gmcq.png",
        "small": "course/en/images/gmcq.png"
      }
    },
    {
      "text": "Option 2",
      "altText": "",
      "_shouldBeSelected": true,
      "_isPartlyCorrect": false,
      "_graphic": {
        "alt": "",
        "attribution": "",
        "large": "course/en/images/gmcq.png",
        "small": "course/en/images/gmcq.png"
      }
    },
    {
      "text": "Option 3",
      "altText": "",
      "_shouldBeSelected": false,
      "_isPartlyCorrect": false,
      "_graphic": {
        "alt": "",
        "attribution": "",
        "large": "course/en/images/gmcq.png",
        "small": "course/en/images/gmcq.png"
      }
    }
  ],
  "_feedback": {
    "title": "Feedback",
    "altTitle": "",
    "correct": "Correct feedback text.<br><br>That's correct. <strong>Option 2</strong> is what we were looking for!",
    "_incorrect": {
      "final": "Incorrect feedback text.<br><br>Sorry, that's not right. In fact <strong>Option 2</strong> is what we were looking for (the clue was in the instruction text!)."
    },
    "_partlyCorrect": {
      "notFinal": "",
      "final": "This is the partly correct feedback."
    }
  },
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

**Gaps vs programme spec (demo scaffold, not authored):**

- `alt` text is blank on all images — violates §6 accessibility.
- `ariaQuestion` is blank — should be populated.
- `notFinal` feedback is missing — would fail on multi-attempt formative.
- Feedback does not explain *why* Option 2 is correct — violates §15.5.
- The first authored gmcq must address all these.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **gmcq** component. Register and content-type voice live in the **Voice Specification**; tier demand and assessment parity live in the **Tier Specification**; scoring mechanics live in **`scoring-and-summative-model.md`**; the shared question-feedback two-tier pattern lives in **`mcq.md §3`**; teaching-move routing lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of gmcq authoring spec — v0.1 (illustrative example — no authored instance yet).*
