# mcq — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 exemplar — the template the remaining component specs follow)
**Verified against:** `src/components/adapt-contrib-mcq/properties.schema` (Adapt 5.56.2)
**Grounded in:** `L02-c-30` — the "identifying the steer" formative check in Academic Writing / Introductory Stage (`courses/academic-writing-introductory`)
**Relationship to other documents:** references the Voice Specification, the Tier Specification, and `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1); restates none. This doc is the single source for how to author an mcq; the mapping artefact's former MCQ Schema Reference block points here (open-decisions D-F4-4).

---

## 1. Purpose & when to reach for it

Routing — *whether* an mcq is the right component for a teaching move — is decided upstream in **Mapping Artefact Part 4** (the "Application / self-check task" row) and **Part 2** (the component audit). This doc does not re-derive that; it assumes the decision to use an mcq has been made and covers how to author it well.

Component-specific "reach for it / don't", which the artefact does not spell out:

- **Reach for mcq** when the answer set is *closed and known* and the learner's job is to recognise, discriminate, or apply a rule to pick from it — single-select (`_selectable: 1`) for one right answer, multi-select for "which of these apply".
- **Don't use mcq** to assess the *quality of reasoning* or free recall (→ `textInput`), to order or sequence items (→ `adapt-abbott-sortable`), or for visual discrimination between images (→ `gmcq`). If the real demand is construction or justification rather than selection, mcq is the wrong tool — see the tier note in §5, where mcq weakens at the top of the range.

---

## 2. The annotated JSON shape

**LK-1 note (22 September 2026):** the `_classes` values below (`context-slot slot-…`) are quoted
as authored in this real, already-built example. The current marker form, written by the
generator (not by hand), is `slot__<page>__<slotType>` — see `open-decisions.md` LK-1.

Skeleton below is the authoring-relevant field set, grouped. **[LB]** marks a *load-bearing* field — one this programme's contract actually pins, where a wrong value breaks voice, tier, scoring, or completion. Fields left at Adapt defaults are noted as such.

```jsonc
{
  "_id": "L02-c-30",              // lesson-key convention; see portable-unit-and-shell-format.md
  "_parentId": "L02-b-25",        // the block this sits in; chain must terminate at course
  "_type": "component",
  "_component": "mcq",
  "_classes": "context-slot slot-understandingTheTask-steerCheck", // [LB] if this is a context slot — structure stays context-neutral, content is filled by the pack
  "_layout": "full",              // full | left | right — presentation only

  "title": "Formative check: identifying the steer",   // [LB] INTERNAL — used for tracking/menus, not shown as the heading
  "displayTitle": "Check your understanding",           // learner-facing heading
  "body": "<p>In Rhian's essay question, '…', which word or phrase is the steer?</p>", // [LB] the question stem; HTML allowed
  "instruction": "Choose one option and select Submit.", // one line; see §4
  "ariaQuestion": "Which word or phrase is the steer in this essay question?", // [LB] see §6 — populate whenever body carries HTML/framing

  "_selectable": 1,               // [LB] how many the learner may pick. 1 = single-select. Multi = set to the number of correct items
  "_items": [                     // [LB] the options
    {
      "text": "To what extent",   // [LB] option label; HTML allowed
      "altText": "",              // screen-reader override for pronunciation/clarity; usually blank
      "_shouldBeSelected": true,  // [LB] marks a correct option. Count of true must match the intended answer
      "_isPartlyCorrect": false,  // multi-select partial credit only
      "feedback": "",             // per-item feedback — SINGLE-SELECT ONLY (see §7 gotcha)
      "_score": 0                 // only read when _hasItemScoring is true
    }
    // …remaining options
  ],

  "_attempts": 2,                 // [LB] formative ≥ 2 so notFinal feedback can do its work; see §3
  "_shouldDisplayAttempts": true, // show "attempts remaining"
  "_isRandom": true,              // [LB] shuffles _items — body/feedback must not reference option order (§7)
  "_hasItemScoring": false,       // [LB] false = 0 or _questionWeight; true = sum of selected _score values
  "_questionWeight": 1,           // score for a correct response when item scoring is off

  "_canShowModelAnswer": true,    // [LB] formative bundle; but see the _canShowCorrectness interaction (§7)
  "_canShowCorrectness": true,    // [LB] shows correctness inline on items; REPLACES the model-answer toggle (§7)
  "_canShowFeedback": true,       // [LB] must stay true for teaching feedback to appear
  "_canShowMarking": true,        // show tick/cross marking
  "_recordInteraction": true,     // report answer to SCORM cmi.interactions (Moodle)

  "_feedback": {                  // [LB] the teaching payload — see §3 and §4
    "title": "",                  // blank → component title is used
    "correct": "That's right. 'To what extent' is the steer because…",
    "_incorrect": {
      "notFinal": "Not quite. The steer is the opening word or phrase that tells you how to approach the question. Look again at where the question begins.",
      "final": "The steer is 'To what extent'. It sits at the very start… The other options … are keywords, not the opening steer."
    },
    "_partlyCorrect": { "notFinal": "", "final": "" } // used only in multi-select with partial credit
  },

  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true },

  "_isPartOfAssessment": false    // [LB] injected/managed by the assessment extension, NOT in properties.schema — false = formative (§7)
  // "_buttons": {…}  // omit unless overriding course.json global button labels
}
```

Everything in `_buttons` and the global aria strings (`ariaRegion`, `ariaCorrectAnswer`, `ariaUserAnswer`, and their plurals) is inherited from `course.json` `_globals`; leave them out of the component unless a specific override is needed.

---

## 3. Authoring guardrails (hard rules)

These are mcq-specific mechanics. Voice obligations live in §4; tier obligations in §5.

1. **`_shouldBeSelected` count must match intent.** Single-select: exactly one `true`. Multi-select: set `_selectable` to the number of correct options, and mark exactly that many `true`. A mismatch produces a question that can't be answered correctly.
2. **Every distractor must be defensibly wrong, and the learner must be told why.** Do not ship a distractor whose wrongness you can't explain in the feedback. This is the "teach not bark" rule in mechanical form.
3. **`notFinal` is a pointer; `final` is the teach.** On any non-final attempt Adapt shows `_incorrect.notFinal` — author it to send the learner *back to reconsider* without giving the answer ("Look again at where the question begins"). On the last attempt it shows `_incorrect.final` — author it to name the answer, say *why*, and say why the plausible distractors fail. `L02-c-30` is the reference for this two-tier pattern. (If `notFinal` is blank, Adapt falls back to `final` — so a blank `notFinal` hands the answer over early; don't leave it blank on a multi-attempt question.)
4. **Set the formative/summative bundle as a unit.**
   - *Formative self-check* (the pilot pattern): `_attempts` ≥ 2, `_canShowModelAnswer: true` (or `_canShowCorrectness: true`), `_canShowFeedback: true`, `_isPartOfAssessment: false`, not inside an assessment article.
   - *Summative*: the component sits inside an assessment article (which sets `_isPartOfAssessment: true`), attempts are limited, and marking/feedback are governed by the assessment, not the component. See `scoring-and-summative-model.md`; do not hand-tune a summative mcq's disclosure fields in isolation.
5. **Per-item `feedback` is single-select only.** The schema only surfaces it when `_selectable: 1`. For multi-select, put the teaching in `_feedback._incorrect` / `_partlyCorrect`; per-item `feedback` on a multi-select item is silently ignored.
6. **If `_isRandom: true`, never reference option order** anywhere in `body`, `instruction`, `_items[].text`, or feedback ("the first option", "options 1 and 3"). Randomisation reshuffles per learner.

---

## 4. Voice rules (reference — not restated here)

Each field that carries learner-facing copy maps to a Voice Spec section. Author to the section; do not treat the tags below as the rule.

| Field | Content type | Voice Spec |
|---|---|---|
| `body` | The question stem — a genuine question, not rhetorical filler | §11.7 (real questions) |
| `instruction` | Activity instruction — one line on what to do | §15.4 |
| `_items[].text` | Option labels; distractors neutral, never mocking the "wrong" thinking | §11.6, §12.3 |
| `_feedback.correct` | Confirm-with-reason; never a bare "Correct!" | §15.5 |
| `_feedback._incorrect.notFinal` / `.final` | Name what was chosen, explain the issue, point the way; never "Wrong." | §15.5 |
| `_feedback._partlyCorrect.*` | Acknowledge what was right before the gap | §15.5 |

Formative feedback contracts, as in running prose (§7 permits contractions in direct student address); §7's no-contractions restriction is scoped to summative/formal assessment feedback and learning outcomes, not formative self-check feedback (open-decisions #15). Feedback is evaluative about the work, never about the student.

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

An mcq's *demand* is set by **Tier Spec §7** (the parity-bearing assessment dimension). Author the stem and distractors to your tier's row there; this doc only names which fields those rows govern:

- **Question form** row → the `body` stem and `instruction` verb.
- **Stimulus** row → how much scene-setting `body` carries (clean single concept → rich/ambiguous scenario).
- **Discrimination** row → distractor plausibility in `_items` (clearly distinguishable at introductory; plausible-and-analysis-requiring at intermediate).

Register, vocabulary, and outcome-verb range come from the pathway's anchored **Voice Spec §16** band (via the Tier Spec's voice-band anchor). Do not restate §16 here.

Two mcq-specific tier points:

- **mcq weakens toward the top of the range.** Tier Spec §7 puts advanced demand in *construction and justification*, "not in trap-spotting". A pure mcq can't ask a learner to construct or justify, so at advanced it's mostly a lower-order check inside a larger task; reach for `textInput`/open-response or `adapt-abbott-sortable` for the real advanced demand.
- **Feedback voice is constant across tiers; only vocabulary shifts** (open-decisions, resolved #2 / mapping-artefact resolved Q2). Do not add extra scaffolding to feedback at lower tiers.

`L02-c-30` is the Tier Spec's own worked illustration (**§9**): an introductory check that asks the learner only to *identify* the steer (recognition, D2-introductory) while the surrounding lesson *models* the analytical move (high scaffold, D4). Read §9 alongside this instance to see the "whole column" principle in practice — and how the same item would climb to analyse/evaluate at higher tiers.

---

## 6. Accessibility requirements

- **`ariaQuestion` — populate it whenever `body` carries HTML, a block quote, or scene-setting.** Screen readers announce `ariaQuestion` in place of the display title, body, and instruction when focusing the options, so it must be the bare question, self-contained. `L02-c-30` is the model: `body` holds the quoted essay question with markup; `ariaQuestion` is the clean "Which word or phrase is the steer in this essay question?". If `body` is already a plain single sentence, `ariaQuestion` may be left blank.
- **`altText` per item** only where the option text needs pronunciation or disambiguation help; otherwise blank.
- **Never rely on colour alone** to convey correctness. `_canShowCorrectness` uses text and iconography, which is fine; if custom `_classes` are added, preserve a non-colour cue.
- **Global aria strings** (`ariaRegion` and the correct/user-answer announcements) come from `course.json` `_globals`; leave the component defaults unless a lesson genuinely needs an override.

---

## 7. Known gotchas & findings

- **`_canShowCorrectness: true` replaces the model-answer button.** Per the schema, inline correctness "replaces the associated 'model answer' toggle button". `L02-c-30` sets *both* `_canShowModelAnswer: true` and `_canShowCorrectness: true` — the inline display wins, and no separate model-answer button appears. Decide which you want; don't assume both render.
- **`_isPartOfAssessment` is not in `properties.schema`.** It's added by the assessment extension. Its presence as `false` on the real instance marks it formative. It's managed by whether the component sits in an assessment article, not by loose hand-editing — see guardrail 4.
- **Two valid places to name distractors, don't blur them.** You can give per-item `feedback` (single-select only) *or* name every distractor in one `_incorrect.final` block. `L02-c-30` uses the latter — a single final block that walks through why "poverty", "explain", and "rising" are keywords rather than the opening steer. Both are fine; pick one approach per question.
- **HTML is allowed** in `body` and feedback (`<p>`, `<br>`, `<em>` all appear in the pilot). Use it for emphasis and structure, within the Voice Spec's formatting rules (§5).
- **`title` vs `displayTitle`.** `title` is internal (tracking, menus) — keep it descriptive ("Formative check: identifying the steer"). `displayTitle` is the learner-facing heading ("Check your understanding"). They are not interchangeable.
- **The question stem goes in `displayTitle`, with `body` left empty — never both.** The header template only renders a `.component__title` heading when `displayTitle` is non-empty, and `grow-headings.less` scopes a dedicated, smaller font size to `.mcq .component__title` so the stem reads at body size rather than oversized h3 size. If the same stem text is also put in `body`, the question renders twice — once as the correctly-sized heading, once again as a duplicate paragraph below it — and any mcq that does this reads as inconsistent against every other mcq in the course (found and fixed across all three criticality tiers, 2 Nov 2026: `L04-c-40/42/44` and `SUMM-c-50/55` each had the stem duplicated in both fields; `body` was cleared on all 15). `ariaQuestion` still carries the clean screen-reader-only version regardless of which field holds the visible stem (see §6).
- **Context slot.** An mcq can be a context slot (`_classes: "slot__<page>__<slotType>"`, written
  by the generator, never by hand — LK-1, `open-decisions.md`), in which case its stem, items, and
  feedback are supplied per context by a pack; the JSON *structure* stays context-neutral. See
  `portable-unit-and-shell-format.md`.

---

## 8. Worked example

`L02-c-30`, the real authored formative check from Academic Writing / Introductory lesson 2 — single-select, two attempts, formative, context-slot. Reproduced in full, then read against the guardrails. Its `_classes` value is quoted as authored, predating LK-1 (22 September 2026) — see the note in §2.

```json
{
  "_id": "L02-c-30",
  "_parentId": "L02-b-25",
  "_type": "component",
  "_component": "mcq",
  "_classes": "context-slot slot-understandingTheTask-steerCheck",
  "_layout": "full",
  "_attempts": 2,
  "_questionWeight": 1,
  "_shouldDisplayAttempts": true,
  "_isRandom": true,
  "_selectable": 1,
  "title": "Formative check: identifying the steer",
  "displayTitle": "Check your understanding",
  "body": "<p>In Rhian's essay question, 'To what extent does poverty explain rising youth knife crime in England and Wales?', which word or phrase is the steer?</p>",
  "instruction": "Choose one option and select Submit.",
  "ariaQuestion": "Which word or phrase is the steer in this essay question?",
  "_hasItemScoring": false,
  "_canShowModelAnswer": true,
  "_canShowCorrectness": true,
  "_canShowFeedback": true,
  "_canShowMarking": true,
  "_recordInteraction": true,
  "_isPartOfAssessment": false,
  "_items": [
    { "text": "To what extent", "altText": "", "_shouldBeSelected": true,  "_isPartlyCorrect": false },
    { "text": "poverty",        "altText": "", "_shouldBeSelected": false, "_isPartlyCorrect": false },
    { "text": "explain",        "altText": "", "_shouldBeSelected": false, "_isPartlyCorrect": false },
    { "text": "rising",         "altText": "", "_shouldBeSelected": false, "_isPartlyCorrect": false }
  ],
  "_feedback": {
    "title": "",
    "correct": "That's right. 'To what extent' is the steer because it appears at the opening and tells you how to answer: reach a judgement about how far poverty explains the rise, rather than simply describing the problem.",
    "_incorrect": {
      "notFinal": "Not quite. The steer is the opening word or phrase that tells you how to approach the question. Look again at where the question begins.",
      "final": "The steer is 'To what extent'. It sits at the very start of the question and tells Rhian she needs to reach a judgement, not just describe. The other options, 'poverty', 'explain' and 'rising', are all important, but they're keywords or hidden steers within the content, not the opening steer that sets the whole approach."
    },
    "_partlyCorrect": { "notFinal": "", "final": "" }
  },
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

**How it satisfies the spec:**

- **Guardrail 1** — single-select (`_selectable: 1`), exactly one `_shouldBeSelected: true`.
- **Guardrail 3** — `notFinal` points back ("Look again at where the question begins") without giving the answer; `final` names the answer, says why it's the steer, and walks through why each distractor is a keyword rather than the opening steer. Textbook two-tier feedback.
- **Guardrail 4** — formative bundle intact: two attempts, feedback on, `_isPartOfAssessment: false`, not in an assessment article.
- **§4 voice** — `correct` confirms with a reason; the incorrect feedback is evaluative about the work, never the learner (§15.5).
- **§5 tier** — introductory demand: the task is to *identify* (recognition), even though the lesson around it models an analytical move. This is the Tier Spec §9 illustration.
- **§6 accessibility** — `body` carries the quoted essay question with markup; `ariaQuestion` is the clean, self-contained question.
- **§7 gotchas** — distractors named in one `final` block (not per-item); both `_canShowModelAnswer` and `_canShowCorrectness` set, with inline correctness taking precedence; it's a context slot.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **mcq** component. Register and content-type voice live in the **Voice Specification**; tier demand and assessment parity live in the **Tier Specification**; scoring mechanics live in **`scoring-and-summative-model.md`**; teaching-move routing lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1); the `_id`/context-slot conventions live in **`portable-unit-and-shell-format.md`**. This doc points to them; it does not restate them.

---

*End of mcq authoring spec — v0.1 (F4 exemplar).*
