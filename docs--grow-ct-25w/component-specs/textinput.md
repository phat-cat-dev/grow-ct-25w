# textInput — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec #2)
**Verified against:** `src/components/adapt-contrib-textInput/properties.schema` (Adapt 5.56.2)
**Grounded in:** `L02-c-40` — the reflective "steer" prompt in Academic Writing / Introductory Stage (`courses/academic-writing-introductory`). The *assessed* mode below is documented from the schema; it is not yet exercised in authored pilot content (see §7).
**Relationship to other documents:** references the Voice Specification, the Tier Specification, `design-kb/design-kb.activity-patterns.json`, and `scoring-and-summative-model.md`; restates none. This doc is the single source for how to author a textInput (component-mapping-artefact.md is SUPERSEDED, MA-1; its textInput Schema Reference block is retired, D-F4-4).

---

## 1. Purpose & when to reach for it

Routing is decided upstream in **Mapping Artefact Part 4** — textInput appears in two different rows there ("Application / self-check task" and "Reflective task"), which is the single most important fact about this component:

> **textInput is one component running in two entirely different modes.** *Assessed* short-answer (marked, with answer-matching) and *reflective* journaling (unmarked, optional). The JSON that distinguishes them is a bundle of flags — get the bundle right and the mode is right; half-set it and you get a broken hybrid. §2 and §3 are mostly about that bundle.

Component-specific "reach for it / don't":

- **Reach for assessed textInput** when the answer is a short, *enumerable* string — a keyword, a term, a cloze blank — where you can list every acceptable spelling. It is exact-match (with tolerance), not comprehension: it cannot judge a paraphrase or the quality of reasoning.
- **Reach for reflective textInput** for self-regulated-learning prompts where the learner needs a space to jot a private response that is never marked and never blocks progress. Note this is the programme's current stopgap for reflective interaction; a richer reflective-prompt component is on the backlog (P1) and "Open Text Input" is the strongest register candidate — until one is built, reflective textInput is the pattern.
- **Don't use textInput** to assess reasoning or accept free-form answers (no component does this well; textInput least of all), to pick from options (→ `mcq`), or to order items (→ `adapt-abbott-sortable`).

---

## 2. The annotated JSON shape

**[LB]** marks a load-bearing field. The right-hand columns give the value each *mode* takes — this pairing is the core of the doc.

| Field | Assessed (marked) | Reflective (journaling) | Notes |
|---|---|---|---|
| `_component` | `"textinput"` | `"textinput"` | **[LB]** lowercase, always — the plugin dir is `adapt-contrib-textInput` but the component value is `textinput` (§7 gotcha). |
| `_isOptional` | absent / `false` | **`true`** | **[LB]** the completion lever. `true` = never blocks page/SCORM completion (open-decisions #2). Not in `properties.schema` — it's a core field (§7). |
| `_items[]._answers` | `["…","…"]` | *omitted* | **[LB]** acceptable answer strings. Reflective has none — there is nothing to match. |
| `_items[].placeholder` | e.g. `"e.g. a keyword"` | `"Your reflection (optional)"` | Hint text; disappears on typing — never put essential instruction here (§6). |
| `_allowsAnyCase` | set deliberately | `true` (inert) | **[LB]** in assessed mode. Case-insensitive matching. |
| `_allowsPunctuation` | set deliberately | `true` (inert) | **[LB]** in assessed mode. Ignore punctuation differences. |
| `_canShowFeedback` | `true` | **`false`** | **[LB]** reflective shows no feedback. |
| `_canShowMarking` | `true` | **`false`** | **[LB]** reflective is unmarked (no tick/cross). |
| `_canShowModelAnswer` | `true` | **`false`** | **[LB]** no "model answer" for a reflection. |
| `_canShowCorrectness` | optional | `false` | If true (assessed), replaces the model-answer button with a correct-answers list. |
| `_questionWeight` | `1` (or higher) | `0` | **[LB]** reflective contributes nothing to score. |
| `_attempts` | `1`+ | `1` | Reflective attempts are irrelevant (nothing is checked). |
| `_recordInteraction` | `true` | `true` in pilot | **[LB-ish]** even reflective text is sent to SCORM `cmi.interactions` — a real decision (§7). |
| `_isRandom` | `false` (default) | `false` | Shuffles multi-item order on each attempt. Rarely needed; leave false unless item independence is deliberate. |
| `_feedback.*` | authored | *omitted / empty* | Assessed feedback follows the shared two-tier pattern (§3). |
| `body` | the question | the reflective prompt | HTML allowed. Voice differs sharply by mode (§4). |
| `instruction` | "Input your answer…" | "…jot down your thoughts… won't be marked." | §4. |
| `displayTitle` | optional heading | `""` (blank) | Reflective uses the body as the visible prompt, no heading. |
| `ariaQuestion` | populate if `body` has framing | `""` acceptable | §6. |
| `_pageLevelProgress._isCompletionIndicatorEnabled` | `true` | **`false`** | Optional reflective shows no required-completion tick (contrast mcq). |

Global aria strings and `_buttons` inherit from `course.json` `_globals`; omit unless overriding.

---

## 3. Authoring guardrails (hard rules)

1. **Set the whole mode bundle, never half of it.** The two valid configurations are the two full columns in §2. The dangerous states are hybrids: a reflective prompt with `_canShowMarking: true` (marks an unmarkable jotting), or an assessed input with no `_items[]._answers` (unanswerable). Copy the whole column.
2. **Reflective mode's completion guarantee is `_isOptional: true`, not `_questionWeight: 0`.** Weight-zero still leaves a required interaction that can gate completion; optionality is what makes it never block (open-decisions #2, resolved). Always pair reflective `_isOptional: true` with `_pageLevelProgress._isCompletionIndicatorEnabled: false`.
3. **Assessed mode is exact-match — enumerate every acceptable string.** `_answers` is literal matching softened only by `_allowsAnyCase` / `_allowsPunctuation`. If you can't list the acceptable answers, textInput is the wrong tool. For multi-blank cloze, use multiple `_items`, each with its own `_answers` (and `prefix`/`suffix`).
4. **`_component` is `"textinput"`, lowercase.** The commonest textInput authoring error; the wrong case silently fails to render.
5. **Assessed feedback uses the shared two-tier pattern** (`notFinal` = pointer that sends the learner back; `final` = the teach) — this mechanic is common to the question components, documented in `mcq.md §3`; author to that rather than re-deriving it here. The textInput-specific wrinkle: feedback fires on *match failure*, so a learner who phrased the right idea in unlisted words gets the incorrect branch — write `final` to account for near-misses, or reconsider whether the item should be assessed at all.
6. **Reflective mode carries no `_feedback`.** Leave it omitted or empty; there is nothing to respond to and a feedback popup breaks the private-jotting intent.

---

## 4. Voice rules (reference — not restated here)

Voice diverges more by mode here than in any other component.

| Field | Mode | Content type | Voice Spec |
|---|---|---|---|
| `body` | reflective | Reflective prompt — 1–3 sentences, genuine question, connects to the preceding section, "no right or wrong answers" | §15.3 |
| `body` | assessed | A real question, not rhetorical filler | §11.7 |
| `instruction` | both | Activity instruction | §15.4 |
| `instruction` | reflective | The "optional / won't be marked" reassurance is part of the SRL register | §15.3 |
| `_feedback.*` | assessed | Confirm-with-reason; never bare; partial acknowledged | §15.5 |
| `placeholder` | both | Short, non-essential hint (see §6 — not a label) | §15.4 |

Note the register split: reflective prompts use warm, contracted direct address (§7). Formative feedback also contracts; §7's no-contractions restriction is scoped to *summative/formal* assessment feedback and learning outcomes, not formative self-check feedback (open-decisions #15).

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

- **Assessed** demand is set by **Tier Spec §7** (question form and discrimination), exactly as for mcq — the `body` stem and the tightness of the acceptable-answer set climb with tier.
- **Reflective** is where the **learner-autonomy dimension** does its work. The directive → Socratic progression that the Tier Spec folds into autonomy (open-decisions #12) shows up directly in prompt phrasing: introductory prompts are concrete and guided, naming the thing to notice ("Did you move through stages, or try to do everything in one go?"); advanced prompts are open and self-directed, handing the framing to the learner. Register tracks the pathway's **§16** band.

`L02-c-40` is an introductory-tier reflective prompt: concrete, tied to the just-taught "steer" concept, with the reassurance built in. The same beat at a higher tier would drop the scaffolding and pose a more open, self-evaluative question.

---

## 6. Accessibility requirements

- **`ariaQuestion`** — populate it when `body` carries HTML framing or several sentences before the actual question, so the screen reader announces a clean question. For a diffuse reflective prompt with no single extractable question (as in `L02-c-40`), blank is acceptable — the whole body is read.
- **Placeholder is not a label.** It vanishes as soon as the learner types, so never put essential instruction in `placeholder`; the real guidance lives in the visible `instruction`. Keep placeholders short and genuinely hint-like.
- **State optionality visibly.** For reflective mode, the "won't be marked / optional" reassurance must be in the visible `instruction`, not implied by the absence of a marking button.
- Global aria strings come from `course.json` `_globals`; leave defaults unless a lesson needs an override.

---

## 7. Known gotchas & findings

- **`_component: "textinput"` is lowercase** despite the plugin directory being `adapt-contrib-textInput`. Wrong case → the component doesn't render.
- **`_isOptional` is not in `properties.schema`.** It's a core component-model field, and it is the completion lever for reflective mode — the resolved answer to open-decisions #2 ("reflective input never blocks completion"). Verified `true` on both pilot reflective instances (`L01-c-40`, `L02-c-40`).
- **Reflective text is still recorded to the LMS.** `_recordInteraction: true` (the pilot's setting) sends the learner's reflection to SCORM `cmi.interactions`, so Moodle stores it. That may be desirable (retrievable by learner/tutor) or not (if the reflection should stay private) — a deliberate per-prompt call, not a default to leave unexamined.
- **Optional pairs with completion-indicator off.** Reflective instances set `_pageLevelProgress._isCompletionIndicatorEnabled: false`, so an optional element doesn't display a required-completion tick (mcq sets it `true`).
- **Exact-match only.** `_answers` is literal string matching with case/punctuation tolerance — no paraphrase, no reasoning. Enumerate acceptable strings or don't assess.
- **Assessed mode is not yet exercised in authored content.** The only assessed textInput in the workspace (`c-215`) is Adapt demo scaffold, not authored to voice; its `_answers` array is even left unpopulated. The first authored assessed textInput will validate the tolerance-flag and feedback choices documented here.
- **HTML is allowed** in `body`; `displayTitle` blank is fine for reflective.

---

## 8. Worked example

`L02-c-40`, the real authored **reflective** prompt from Academic Writing / Introductory lesson 2 — the dominant textInput pattern in the pilot. (An assessed worked example is deferred until one is authored; see §7.)

```json
{
  "_id": "L02-c-40",
  "_parentId": "L02-b-35",
  "_type": "component",
  "_component": "textinput",
  "_classes": "",
  "_layout": "full",
  "title": "Reflective prompt",
  "displayTitle": "",
  "body": "<p>Think about an assignment you've got coming up, or one you've recently handed in. What's its steer, and did you work out what it was really asking you to do before you started writing? There's no right or wrong answer here; the point is just to notice whether you read the task, or only the topic.</p>",
  "instruction": "If you'd like, jot down your thoughts below. This is for your own reflection and won't be marked.",
  "ariaQuestion": "",
  "_isOptional": true,
  "_attempts": 1,
  "_shouldDisplayAttempts": false,
  "_questionWeight": 0,
  "_canShowModelAnswer": false,
  "_canShowCorrectness": false,
  "_canShowFeedback": false,
  "_canShowMarking": false,
  "_recordInteraction": true,
  "_allowsAnyCase": true,
  "_allowsPunctuation": true,
  "_items": [
    { "prefix": "", "suffix": "", "placeholder": "Your reflection (optional)" }
  ],
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": false }
}
```

**How it satisfies the spec:**

- **Guardrail 1 & 2** — the full reflective bundle: `_isOptional: true`, feedback/marking/model-answer/correctness all `false`, `_questionWeight: 0`, no `_answers`, completion indicator off. Never blocks completion.
- **Guardrail 6** — no `_feedback` object at all.
- **§4 voice** — `body` is a §15.3 reflective prompt: two sentences, a genuine question, tied to the just-taught "steer" concept, with "no right or wrong answer" stated; `instruction` carries the optional/unmarked reassurance in the SRL register.
- **§5 tier** — introductory: concrete, guided, names the thing to notice. Autonomy dimension at its lower end.
- **§6 accessibility** — diffuse prompt, so `ariaQuestion` blank is acceptable; the optional nature is in the visible instruction, not just the missing marking button.
- **§7 findings** — `_component` lowercase; `_isOptional` present though not in the schema; reflection recorded to the LMS (`_recordInteraction: true`); completion indicator off.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **textInput** component in both its assessed and reflective modes. Register and content-type voice live in the **Voice Specification** (reflective §15.3, feedback §15.5); tier demand and the autonomy progression live in the **Tier Specification**; scoring and formative/summative mechanics live in **`scoring-and-summative-model.md`**; the shared question-feedback two-tier pattern lives in **`mcq.md §3`**; teaching-move routing lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of textInput authoring spec — v0.1.*
