# slider — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec)
**Verified against:** `src/components/adapt-contrib-slider/properties.schema` (Adapt 5.56.2)
**Grounded in:** `c-230` — Adapt demo scaffold instance (`courses/academic-writing-introductory`). **No authored lesson instance exists yet** (no L0x-prefixed slider component in the pilot). The worked example below is therefore illustrative of the schema shape, not an authored voice model; treat it with caution until a real instance is built.
**Relationship to other documents:** references the Voice Specification, the Tier Specification, and the shared question-feedback pattern in `mcq.md §3`; restates none.

---

## 1. Purpose & when to reach for it

Routing is decided upstream in **Mapping Artefact Part 4** (the question-type rows). Slider is a **numeric scale question**: the learner drags a slider to select a value, then submits.

Component-specific "reach for it / don't":

- **Reach for slider** when the answer is a **number on a scale** — estimating a quantity, placing a value on a continuum, selecting a rating.
- **Reach for slider** when the correct answer is a single value or a range (e.g., "any value between 5 and 9").
- **Don't use slider for discrete multiple-choice** — that's `mcq` or `gmcq`.
- **Don't use slider for ranking/ordering** — that's `adapt-abbott-sortable`.
- **Don't use slider for open-ended reflection** — that's `textInput`.

Slider is a niche component. Most question needs are met by mcq. Slider is appropriate when the numeric-scale mechanic genuinely fits the teaching move (e.g., estimation tasks, Likert-style self-assessment where there's a correct answer).

---

## 2. The annotated JSON shape

**[LB]** marks a load-bearing field. Slider is a question type; it shares the feedback structure with mcq.

```jsonc
{
  "_id": "c-230",
  "_parentId": "b-220",
  "_type": "component",
  "_component": "slider",
  "_classes": "",
  "_layout": "full",                      // "full" | "left" | "right"

  "title": "Slider",                      // internal / tracking
  "displayTitle": "Check your understanding", // learner-facing heading
  "body": "<p>How many items can working memory hold at once, according to Miller?</p>", // [LB] the question stem
  "instruction": "Drag the slider to make your choice and select Submit.", // [LB] §15.4
  "ariaQuestion": "How many items can working memory hold?", // [LB] clean question for screen readers
  "ariaScaleName": "number of items",     // describes the scale for screen readers

  "_attempts": 2,                         // [LB] formative >= 2 so notFinal feedback works
  "_shouldDisplayAttempts": true,
  "_questionWeight": 1,
  "_canShowModelAnswer": true,            // [LB] formative bundle
  "_canShowCorrectness": false,           // if true, replaces model-answer button
  "_canShowFeedback": true,               // [LB] must stay true for teaching feedback
  "_canShowMarking": true,
  "_recordInteraction": true,             // SCORM cmi.interactions

  "_scaleStart": 1,                       // [LB] lowest value on the scale
  "_scaleEnd": 10,                        // [LB] highest value on the scale
  "_scaleStep": 1,                        // increment between values
  "scaleStepPrefix": "",                  // prefix before each value (e.g., "$")
  "scaleStepSuffix": "",                  // suffix after each value (e.g., "%")
  "labelStart": "",                       // label at left end of scale
  "labelEnd": "",                         // label at right end of scale

  "_correctAnswer": "7",                  // [LB] exact correct value (as string); leave blank if using range
  "_correctRange": {                      // [LB] correct range (ignored if _correctAnswer is set)
    "_bottom": 5,
    "_top": 9
  },

  "_showScaleIndicator": true,            // show position marker
  "_showNumber": true,                    // show number on indicator
  "_showScale": true,                     // show scale lines and numbers
  "_showScaleNumbers": true,              // show numbers on the scale

  "_feedback": {                          // [LB] the teaching payload — shared pattern (mcq.md §3)
    "title": "",
    "correct": "That's right. Miller's 'magic number' is 7 plus or minus 2, so any value from 5 to 9 is correct.",
    "_incorrect": {
      "notFinal": "Not quite. Think about the 'magic number' — it's a famous result in cognitive psychology.",
      "final": "The correct answer is 7 (plus or minus 2). Miller's research showed that working memory can hold about 7 items, give or take 2, which is why we set the correct range as 5–9."
    }
  },

  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true },

  "_isPartOfAssessment": false            // [LB] assessment-extension field — false = formative
}
```

Global aria strings (`ariaRegion`, `ariaCorrectAnswer`, `ariaCorrectAnswerRange`, `ariaUserAnswer`, `labelStart`, `labelEnd`) and `_buttons` inherit from `course.json` `_globals`; leave defaults unless overriding.

---

## 3. Authoring guardrails (hard rules)

Slider shares mcq's feedback mechanics. The guardrails below extend those in **`mcq.md §3`**; read that first.

1. **Set either `_correctAnswer` or `_correctRange`, not both.** If `_correctAnswer` is populated (as a string), the range is ignored. Use `_correctAnswer` for an exact value; use `_correctRange` when a range is acceptable.
2. **`notFinal` is a pointer; `final` is the teach.** Same two-tier pattern as mcq — see **`mcq.md §3`** for the discipline.
3. **Set the formative/summative bundle as a unit.** Same as mcq (`mcq.md §3`, guardrail 4).
4. **`_scaleStart` and `_scaleEnd` must include the correct answer.** If `_correctAnswer` is 7, the scale must include 7.
5. **`ariaScaleName` is required for accessibility.** It tells screen-reader users what the scale measures (e.g., "number of items", "percentage", "rating").
6. **Scale labels (`labelStart`, `labelEnd`) are optional but helpful.** Use them when the scale ends have meaningful names (e.g., "Strongly disagree" to "Strongly agree").

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `body` | The question stem — a genuine question | §11.7 |
| `instruction` | Activity instruction — one line on what to do | §15.4 |
| `labelStart` / `labelEnd` | Scale labels; concise | §13 (register) |
| `_feedback.correct` | Confirm-with-reason; never bare | §15.5 |
| `_feedback._incorrect.*` | Explain the issue, teach the correct answer | §15.5 |

Formative feedback contracts (open-decisions #15). Feedback is evaluative about the work, never about the student.

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

Slider's *demand* is set by **Tier Spec §7** (the assessment dimension). This doc names which fields those rows govern:

- **Question form** row → the `body` stem and type of estimation task.
- **Stimulus** row → how much context `body` provides.
- **Discrimination** row → how precise the learner must be. Introductory may accept a wide range; advanced may require exact answers.

Register follows **Voice Spec §16**. Do not restate §16 here.

---

## 6. Accessibility requirements

- **`ariaQuestion`** — populate it with the clean question when `body` carries HTML or scene-setting.
- **`ariaScaleName`** — required; describes what the scale measures for screen-reader users.
- **Keyboard accessible.** The slider can be operated with arrow keys.
- **`labelStart` / `labelEnd`** — if the scale ends have meaningful labels, include them for clarity.
- Global aria strings (`ariaCorrectAnswer`, `ariaCorrectAnswerRange`) default sensibly; override if needed.

---

## 7. Known gotchas & findings

- **Slider is niche.** Most question needs are better served by mcq. Use slider only when the numeric-scale mechanic genuinely fits.
- **`_correctAnswer` is a string, not a number.** The schema defines it as a string; populate it as `"7"`, not `7`.
- **`_canShowCorrectness: true` replaces the model-answer button.** Decide which disclosure mode you want.
- **`_isPartOfAssessment`** is an assessment-extension field, not in the component schema. Its presence as `false` marks formative.
- **No `_partlyCorrect` branch.** Unlike mcq, slider has no partial-credit feedback — you're either in the range or out.
- **Demo scaffold only in pilot.** `c-230` is Adapt demo content. The first real authored slider must follow Voice Spec.

---

## 8. Worked example

**Note:** No authored lesson instance exists yet. The example below is from the Adapt demo scaffold (`c-230`), reproduced to show schema shape. It is **ILLUSTRATIVE**, not a voice model.

```json
{
  "_id": "c-230",
  "_parentId": "b-220",
  "_type": "component",
  "_component": "slider",
  "_classes": "",
  "_layout": "full",
  "title": "Slider",
  "displayTitle": "Slider",
  "body": "Working memory is thought to be responsible for our ability to temporarily hold and manipulate information, but according to a paper by Miller (1956) what 'magic number' describes its capacity?",
  "instruction": "Drag the slider to make your choice and select Submit.",
  "ariaQuestion": "",
  "ariaScaleName": "",
  "_attempts": 1,
  "_shouldDisplayAttempts": false,
  "_questionWeight": 1,
  "_canShowModelAnswer": true,
  "_canShowCorrectness": false,
  "_canShowFeedback": true,
  "_canShowMarking": true,
  "_recordInteraction": true,
  "_showNumber": true,
  "_showScaleIndicator": true,
  "labelStart": "",
  "labelEnd": "",
  "_scaleStart": 1,
  "_scaleEnd": 10,
  "_scaleStep": 1,
  "scaleStepPrefix": "",
  "scaleStepSuffix": "",
  "_correctAnswer": "",
  "_correctRange": {
    "_bottom": 5,
    "_top": 9
  },
  "_feedback": {
    "title": "Feedback",
    "altTitle": "",
    "correct": "Correct answer feedback.<br><br>Yes, that's right. According to Miller's paper 7 +/- 2 chunks of information was the limited capacity of working memory. Various theories from the field of cognitive psychology such as Miller's magical number, chunking, the forgetting curve and spaced repetition have all influenced learning theory over the last 50 years or so.",
    "_incorrect": {
      "notFinal": "",
      "final": "Incorrect answer feedback.<br><br>Sorry, that's not right. According to Miller's paper 7 +/- 2 chunks of information was the limited capacity of working memory. Various theories from the field of cognitive psychology such as Miller's magical number, chunking, the forgetting curve and spaced repetition have all influenced learning theory over the last 50 years or so."
    }
  },
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

**Gaps vs programme spec (demo scaffold, not authored):**

- `ariaQuestion` is blank — should be populated.
- `ariaScaleName` is blank — violates §6 accessibility.
- `_attempts: 1` means no `notFinal` feedback is needed, but the field is blank anyway — if this were multi-attempt, it would fail.
- Feedback starts with "Correct answer feedback" / "Incorrect answer feedback" — not programme voice.
- The first authored slider must address all these.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **slider** component. Register and content-type voice live in the **Voice Specification**; tier demand and assessment parity live in the **Tier Specification**; scoring mechanics live in **`scoring-and-summative-model.md`**; the shared question-feedback two-tier pattern lives in **`mcq.md §3`**; teaching-move routing lives in **`design-kb/design-kb.activity-patterns.json`** (`activity-patterns/place-on-a-scale`; component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of slider authoring spec — v0.1 (illustrative example — no authored instance yet).*
