# assessmentResults — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec — closes #16 deferral)
**Verified against:** `src/components/adapt-contrib-assessmentResults/properties.schema` (Adapt 5.56.2)
**Grounded in:** `SUMM-c-50` — the results component in the Academic Writing / Introductory Stage summative assessment (`courses/academic-writing-introductory`)
**Relationship to other documents:** references `scoring-and-summative-model.md` (S-1–S-5), open-decisions #15 (contraction scope), open-decisions #16 (this spec closes the deferral). This doc is the single source for how to author an assessmentResults component.

---

## 1. Purpose & when to reach for it

The **summative assessment feedback display** — shows the learner their score, selects banded feedback based on percentage, and offers a retry button when appropriate.

- **Reach for assessmentResults** at the end of a summative assessment page, after all scored question components, to display results and banded feedback.
- **There is exactly one per assessment** (per S-1, scoring-and-summative-model.md). It is wired to its parent assessment article by `_assessmentId`.
- **Don't use assessmentResults** for formative checks (no assessment; use question component feedback directly) or for non-assessment pages.

### Context

This component is **summative wiring** — most fields connect it to the assessment extension, not to authored voice. The only fields carrying substantial authored voice are:

- `_bands[].feedback` / `feedbackNotFinal` — the banded feedback messages
- `_retry.button` / `_retry.feedback` — retry messaging

Everything else (`_assessmentId`, `_isVisibleBeforeCompletion`, `_setCompletionOn`, `_resetType`, `_bands[]._score`, `_bands[]._allowRetry`) is mechanical configuration tied to the assessment extension.

---

## 2. The annotated JSON shape

Skeleton below is the authoring-relevant field set. **[LB]** marks a *load-bearing* field.

```jsonc
{
  "_id": "SUMM-c-50",             // fixed id per tier; see portable-unit-and-shell-format.md
  "_parentId": "SUMM-b-55",       // the block this sits in (after all question blocks)
  "_type": "component",
  "_component": "assessmentResults",
  "_classes": "",
  "_layout": "full",

  "title": "Results",             // internal tracking
  "displayTitle": "Results",      // learner-facing heading (usually blank or "Results")
  "body": "",                     // usually blank; _completionBody takes over
  "instruction": "",              // usually blank

  "_assessmentId": "SUMM-a-01",   // [LB] must match the assessment article's _assessment._id
  "_isVisibleBeforeCompletion": false, // [LB] hide until assessment complete
  "_setCompletionOn": "inview",   // component completes on inview (not on pass)
  "_resetType": "inherit",        // inherit reset behaviour from assessment

  "_retry": {
    "button": "Try again",        // [LB] retry button text — see §4
    "feedback": "",               // optional retry-specific message (rarely used)
    "_routeToAssessment": false   // whether retry navigates back to start
  },

  "_completionBody": "{{{feedback}}}", // [LB] template; {{{feedback}}} inserts the matched band's feedback

  "_bands": [                     // [LB] the feedback bands — see §3
    {
      "_score": 0,                // [LB] threshold: >= this score AND < next band's score
      "feedbackNotFinal": "...",  // shown when attempts remain
      "feedback": "...",          // [LB] shown on final attempt — see §4
      "_allowRetry": true         // [LB] whether retry button appears for this band
    },
    {
      "_score": 50,
      "feedbackNotFinal": "...",
      "feedback": "...",
      "_allowRetry": true
    },
    {
      "_score": 70,               // [LB] the pass mark (S-3)
      "feedback": "...",          // pass feedback — no feedbackNotFinal needed
      "_allowRetry": true
    },
    {
      "_score": 100,              // perfect score
      "feedback": "...",
      "_allowRetry": false        // no retry on perfect
    }
  ],

  "_pageLevelProgress": {
    "_isEnabled": true,
    "_isCompletionIndicatorEnabled": false
  }
}
```

---

## 3. Authoring guardrails (hard rules)

1. **`_assessmentId` must match the assessment article.** The component finds its assessment by matching `_assessmentId` to the article's `_assessment._id`. A mismatch means no results display. If there is only one assessment in the course, both can be blank.

2. **Bands must cover 0–100 with no gaps.** Each band's `_score` is a *lower threshold* (inclusive). The component selects the highest band whose `_score` the learner meets or exceeds. Standard pattern:
   - `_score: 0` — fail (0–49%)
   - `_score: 50` — near-miss (50–69%)
   - `_score: 70` — pass (70–99%)
   - `_score: 100` — perfect (100%)

   The 70% pass mark is per S-3 (scoring-and-summative-model.md). Do not change without revisiting S-3.

3. **`_allowRetry` per band.** When `true` and attempts remain, the retry button appears. Per SRF-1 (open-decisions.md), the retry flow was verified working after the `_isResetOnRevisit` fix. Typically:
   - Fail/near-miss bands: `_allowRetry: true`
   - Pass band: `_allowRetry: true` (allows improvement)
   - Perfect band: `_allowRetry: false` (nothing to improve)

4. **`_isVisibleBeforeCompletion: false`.** The results component should not appear until the assessment is complete. This is the standard setting.

5. **`_completionBody: "{{{feedback}}}"`** is the standard template — it inserts the selected band's feedback as the entire body. The triple-brace `{{{...}}}` is Handlebars unescaped HTML. Variables available: `{{attemptsSpent}}`, `{{attempts}}`, `{{attemptsLeft}}`, `{{score}}`, `{{scoreAsPercent}}`, `{{maxScore}}`, `{{{feedback}}}`.

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `_bands[].feedback` | Summative assessment feedback | §15.5 + #15 |
| `_bands[].feedbackNotFinal` | Summative assessment feedback (attempts remain) | §15.5 + #15 |
| `_retry.button` | Button label | §15.4 (activity instruction register) |

**Critical: no contractions in summative feedback.** Per open-decisions #15, §7's no-contractions restriction applies to **summative/formal assessment feedback**. Formative self-check feedback contracts freely; summative assessment feedback does not. Author `_bands[].feedback` and `feedbackNotFinal` in formal register — "You did not pass" not "You didn't pass".

**Feedback is about the work, not the person.** Per §15.5, feedback is evaluative about the performance, never personal judgement. "You achieved 65%" is factual; avoid "You failed" (labels the person).

**`_retry.button` text.** The verified pattern is `"Try again"` (SRF-1) — imperative, brief, action-oriented.

---

## 5. Tier-dependent guidance

The assessmentResults component is **tier-neutral** in structure. The feedback *content* may reference tier-appropriate material:

- **Introductory**: feedback may point to foundational review ("Have another look through this tier's topics").
- **Intermediate/Advanced**: feedback may point to specific areas or higher-order application.

The bands, thresholds, and retry mechanics do not change by tier (per S-1–S-5, the model is consistent across tiers).

---

## 6. Accessibility requirements

- **Feedback announced on completion.** When the assessment completes and the results component renders, screen readers should announce the feedback. The component handles this via `ariaRegion`.
- **Retry button accessible.** The retry button must be keyboard-focusable and clearly labelled. The schema's `globals.retryText` provides the accessible name; `_retry.button` is the visible label.
- **Score communicated in text.** `{{scoreAsPercent}}%` in feedback ensures the score is in text, not just a visual indicator.

---

## 7. Known gotchas & findings

- **SRF-1: `_isResetOnRevisit` interaction.** The assessment article's `_isResetOnRevisit` was originally `true`, causing the assessment to silently reset on SCORM resume after a fail — no fail message, no retry button. Fixed by setting `_isResetOnRevisit: false` on the assessment article (SRF-1c, open-decisions.md). The assessmentResults component itself was not at fault; the fix is on the assessment article.

- **`feedbackNotFinal` vs `feedback`.** When attempts remain, `feedbackNotFinal` is shown if present; otherwise `feedback`. On the final attempt, only `feedback` is shown. For fail/near-miss bands with unlimited attempts (S-4), `feedbackNotFinal` and `feedback` are typically identical.

- **Variables in feedback.** `{{scoreAsPercent}}` gives the percentage as a number (e.g. `70`); append `%` in the text. `{{score}}` is the raw score; `{{maxScore}}` is the maximum.

- **Perfect score band.** Including a `_score: 100` band allows distinct messaging for a perfect score. Without it, 100% falls into the highest sub-100 band.

- **`_resetType: "inherit"`** is the standard; the component's completion resets when the assessment resets. "soft" would retain completion even if the assessment resets — rarely wanted.

---

## 8. Worked example

`SUMM-c-50`, the real authored results component from Academic Writing / Introductory summative assessment. Reproduced in full.

```json
{
  "_id": "SUMM-c-50",
  "_parentId": "SUMM-b-55",
  "_type": "component",
  "_component": "assessmentResults",
  "_classes": "",
  "_layout": "full",
  "title": "Results",
  "displayTitle": "Results",
  "body": "",
  "instruction": "",
  "_assessmentId": "SUMM-a-01",
  "_isVisibleBeforeCompletion": false,
  "_setCompletionOn": "inview",
  "_resetType": "inherit",
  "_retry": {
    "button": "Try again",
    "feedback": ""
  },
  "_completionBody": "{{{feedback}}}",
  "_bands": [
    {
      "_score": 0,
      "feedbackNotFinal": "You did not pass this time, achieving {{scoreAsPercent}}%. Have another look through this tier's topics, then try again when you are ready.",
      "feedback": "You did not pass this time, achieving {{scoreAsPercent}}%. Have another look through this tier's topics, then try again when you are ready.",
      "_allowRetry": true
    },
    {
      "_score": 50,
      "feedbackNotFinal": "You are close, achieving {{scoreAsPercent}}%, but not quite at the pass mark yet. A little more review of this tier's topics should get you there.",
      "feedback": "You are close, achieving {{scoreAsPercent}}%, but not quite at the pass mark yet. A little more review of this tier's topics should get you there.",
      "_allowRetry": true
    },
    {
      "_score": 70,
      "feedback": "You passed, achieving {{scoreAsPercent}}%. You have brought together the whole writing cycle, not just each stage on its own.",
      "_allowRetry": true
    },
    {
      "_score": 100,
      "feedback": "You passed with a perfect score, achieving {{scoreAsPercent}}%. You have clearly brought the whole cycle together.",
      "_allowRetry": false
    }
  ],
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_isCompletionIndicatorEnabled": false
  }
}
```

**How it satisfies the spec:**

- **Guardrail 1** — `_assessmentId: "SUMM-a-01"` matches the assessment article.
- **Guardrail 2** — bands cover 0–100 with 70% as the pass threshold (S-3).
- **Guardrail 3** — `_allowRetry: true` on fail/near-miss/pass; `false` on perfect.
- **Guardrail 4** — `_isVisibleBeforeCompletion: false`.
- **§4 voice** — no contractions ("did not", "are close", "have brought"); formal register throughout. Feedback is about the performance ("achieving {{scoreAsPercent}}%"), not personal judgement. Retry button is "Try again" per SRF-1.
- **§6 accessibility** — score communicated in text via `{{scoreAsPercent}}%`.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **assessmentResults** component. Scoring mechanics, pass marks, and summative placement live in **`scoring-and-summative-model.md`** (S-1–S-5); contraction scope lives in **open-decisions #15**; the `_id` conventions live in **`portable-unit-and-shell-format.md`**; the `_isResetOnRevisit` fix is documented in **SRF-1** (open-decisions.md). This doc points to them; it does not restate them.

---

*End of assessmentResults authoring spec — v0.1 (closes #16 deferral).*
