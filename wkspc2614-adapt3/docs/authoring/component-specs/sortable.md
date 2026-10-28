# adapt-abbott-sortable — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec #3)
**Verified against:** `src/components/adapt-abbott-sortable/properties.schema` — **our own schema** (custom component, not an Adapt contrib plugin).
**Grounded in:** `L01-c-20` — the writing-cycle ordering task in Academic Writing / Introductory Stage (`courses/academic-writing-introductory`).
**Note on status:** this component ships no `example.json` and its `schema/` folder is empty (the newer split-schema convention is unused). `properties.schema` is the sole schema authority, and **this doc is the component's primary authoring reference** — there is no upstream Adapt documentation to defer to.
**Relationship to other documents:** references the Voice Specification, the Tier Specification, `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1), and `scoring-and-summative-model.md`; the shared question-feedback pattern lives in `mcq.md §3`. Restates none.

---

## 1. Purpose & when to reach for it

Routing is decided upstream in **Mapping Artefact Part 4** (the resolved-gaps row: "Drag-and-drop sorting → use `adapt-abbott-sortable`"). This is the programme's custom sequencing component — built because no v5-compatible community sorting plugin existed (the only candidate was an unmaintained 2017 plugin that failed the compatibility gate; see `component-candidates-register.md`).

Component-specific "reach for it / don't":

- **Reach for sortable** when the teaching move is *ordering or sequencing* a set of items and the order itself is the learning point — process stages, chronologies, dependency chains, ranked steps. The register anticipates recurring need: research stages, reflective models, revision sequences.
- It **replaced the matching workaround** — before this component existed, ordering was faked with `matching`. Don't fall back to that; sortable is the proper tool and is fully accessible.
- **Don't use sortable** to *pair* items (→ `matching`), to *select* from options (→ `mcq`), or where several orderings are equally defensible and the real demand is *justifying* a choice rather than producing the one correct sequence (see the tier note in §5).

---

## 2. The annotated JSON shape

**[LB]** marks a load-bearing field. This component is deliberately lean — no per-item feedback, no `_selectable`, no scoring toggle. The ordering *is* the answer key.

```jsonc
{
  "_id": "L01-c-20",
  "_parentId": "L01-b-15",
  "_type": "component",
  "_component": "sortable",         // [LB] the component value is "sortable" — NOT "adapt-abbott-sortable" (the plugin dir name). §7 gotcha.
  "_classes": "",
  "_layout": "full",

  "title": "Check your understanding: the five stages",  // internal / tracking
  "displayTitle": "Check your understanding",             // learner-facing heading
  "body": "The stages of the writing cycle follow a particular order… Can you put them in the right sequence, from first to last?", // the ordering question
  "instruction": "Drag items to reorder, or use keyboard (Enter to grab, arrows to move, Enter to drop).", // [LB] MUST state the keyboard method — §3, §6
  "ariaQuestion": "Put the five writing-cycle stages in the correct order from first to last.",            // [LB] the clean question for screen readers — §6

  "_attempts": 2,                    // formative: ≥2 so notFinal feedback works
  "_shouldDisplayAttempts": true,
  "_questionWeight": 1,              // whole-order scoring (§3) — no item scoring
  "_canShowModelAnswer": true,       // reveals the correct order on failure
  "_canShowFeedback": true,          // [LB] must stay true for teaching feedback
  "_canShowMarking": true,
  "_recordInteraction": true,        // SCORM cmi.interactions (sequencing response type)

  "_items": [                        // [LB] AUTHORED IN CORRECT ORDER — the component shuffles for display. Never pre-shuffle. §3
    { "text": "Understand the task" },
    { "text": "Plan" },
    { "text": "Draft" },
    { "text": "Edit" },
    { "text": "Proofread" }
  ],

  "_feedback": {                     // [LB] shared two-tier pattern (mcq.md §3); sortable authors _partlyCorrect too
    "title": "",
    "correct": "That's the right sequence. Each stage has a distinct job…",
    "_incorrect": {
      "notFinal": "That's not quite the right order. Think about what has to happen before each stage can begin…",
      "final": "The correct order is: <em>Understand the task</em> → <em>Plan</em> → … Each stage builds on the one before it."
    },
    "_partlyCorrect": {
      "notFinal": "Some of those are in the right place, but not all. Remember: each stage depends on the one before it.",
      "final": "The correct order is: … Some of your stages were in the right position, but the full sequence matters."
    }
  },

  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }, // see §7 (per-item-indicator fix)

  "_isPartOfAssessment": false       // [LB] assessment-extension field, not in our schema — false = formative (§7)
}
```

The aria globals (`ariaRegion`, `ariaCorrectAnswer`, `ariaUserAnswer`, `ariaItemMoved`, `ariaMoveUp`, `ariaMoveDown`) carry sensible defaults *in our schema*; override in `course.json` only if needed (§6). `_buttons` inherits likewise.

---

## 3. Authoring guardrails (hard rules)

1. **Author `_items` in the correct order.** The schema is explicit: items are listed top-to-bottom as the right sequence, and the component shuffles them at display time. Never pre-shuffle "to make it look mixed" — you'd be defining the wrong answer key. The order in the JSON *is* the answer.
2. **`_component` is `"sortable"`**, not `"adapt-abbott-sortable"`. The plugin directory is `adapt-abbott-sortable`; the component value is the short lowercase `sortable`. Wrong value → doesn't render. (Same family of trap as `textinput`.)
3. **The `instruction` must state the keyboard method.** Unlike core components with a standard submit button, the interaction here is drag-or-keyboard, and the keyboard path is not self-evident. The instruction has to teach it ("Enter to grab, arrows to move, Enter to drop") — this is a hard accessibility requirement, not a stylistic choice (§6).
4. **Scoring is whole-order.** `_questionWeight` is awarded for the fully correct sequence, otherwise zero — there is no item scoring and no `_hasItemScoring` toggle (that's mcq's). The component recognises a *partly-correct* state for **feedback** display; whether partial ever contributes to **score** is defined by the component's marking code, not the schema, and is the subject of the P3 sortable unit-test backlog item. Don't assume partial credit scores unless that's been verified.
5. **Feedback follows the shared two-tier pattern** (`notFinal` = pointer, `final` = teach) — see `mcq.md §3`; don't re-derive it. Sortable-specific additions: author the `_partlyCorrect` branch too (some items correctly placed), and refer to items **by their text**, never by display position ("the top item"), because the display order is shuffled. Good `notFinal` copy teaches the *dependency logic* ("you can't draft until you've planned") rather than just saying "wrong".
6. **Don't reach for behaviours it doesn't implement.** No per-item feedback, no `_selectable`, no `_isRandom` toggle (shuffling is automatic and always on). Keep instances within the lean field set above.

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `body` | The ordering question — a genuine question, not rhetorical | §11.7 |
| `instruction` | Activity instruction (plus the mandatory keyboard method — §6) | §15.4 |
| `_feedback.correct` / `_incorrect.*` / `_partlyCorrect.*` | Formative feedback — confirm/teach with the dependency reasoning; never bare | §15.5 |

Formative feedback contracts (open-decisions #15). The final feedback naming the full correct sequence is good practice — it teaches the *why-this-order*, consistent with why-before-how (§11.8).

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

Sequencing demand is set by **Tier Spec §7**. This doc names how it lands on sortable:

- **Introductory:** a short sequence with clear causal dependencies, where the order is discoverable by reasoning about what must come first (the five writing-cycle stages — you can't draft before you plan).
- **Higher tiers:** longer sequences, less obvious ordering, or items where the dependency is conceptual rather than procedural.
- **Ceiling:** as with mcq, pure ordering weakens at the top of the range. When multiple orderings are defensible and the real demand is *justifying* the chosen order, the sequencing interaction can't capture that — the judgement lives in the reasoning, not the drag. Reach for a reflective/written component to carry the justification, using sortable (if at all) only for the mechanical ordering beat.

Register tracks the pathway's **§16** band. `L01-c-20` is an introductory-tier instance: short, causally transparent, feedback that spells out the dependencies.

---

## 6. Accessibility requirements

Accessibility is the reason this component exists (the rejected community plugin was not accessible), so it carries more weight here than for the core components.

- **Dual interaction, both authored-for.** The component supports drag-and-drop *and* full keyboard operation (grab / move / drop). The visible `instruction` must state the keyboard method explicitly — see guardrail 3. This is the single most important accessibility obligation.
- **Live-region announcements.** Item moves are announced via `ariaItemMoved` (item text + new position + total); the move controls use `ariaMoveUp` / `ariaMoveDown`. These carry defaults in our schema; override in `course.json` only for wording changes.
- **`ariaQuestion`** — populate it with the clean ordering question (as `L01-c-20` does), so the screen reader announces the task without the surrounding body prose.
- **`ariaRegion` / `ariaCorrectAnswer` / `ariaUserAnswer`** default sensibly from the schema; the correct/your-order announcements interpolate the sequence.
- Because this is a custom component, if any aria string appears not to be read, verify the framework is picking up the schema defaults rather than assuming the string is wrong.

---

## 7. Known gotchas & findings

- **`_component: "sortable"`** — short lowercase value, not the plugin directory name `adapt-abbott-sortable`. Commonest failure mode.
- **`_items` are authored in correct order; the component shuffles.** Pre-shuffling breaks the answer key (guardrail 1).
- **`_isPartOfAssessment`** is an assessment-extension field, absent from our schema; `false` on the pilot instance marks it formative.
- **PageLevelProgress needs care with this component.** PLP interacts fussily with custom components; the per-item completion indicator required a fix for sortable (see the register's note). Keep the `_pageLevelProgress` block as in the pilot (`_isCompletionIndicatorEnabled: true`) unless testing shows otherwise.
- **Custom code → upgrade-fragile.** Built and pinned for Adapt 5.56.2. Future base-class changes could break the marking or interaction logic; the P3 backlog item (sortable unit tests) exists to guard exactly this. Treat the field set as fixed — it implements only what's in `properties.schema`.
- **Empty `schema/` folder.** The newer split-schema convention directory exists but is unpopulated; `properties.schema` is the only authority. No `example.json` ships — this spec's worked example (§8) is the reference instance.
- **Feedback refers to items by text, not position** (display is shuffled).

---

## 8. Worked example

`L01-c-20`, the real authored writing-cycle ordering task from Academic Writing / Introductory lesson 1 — the first production use of the component, which replaced the earlier matching workaround.

```json
{
  "_id": "L01-c-20",
  "_parentId": "L01-b-15",
  "_type": "component",
  "_component": "sortable",
  "_classes": "",
  "_layout": "full",
  "title": "Check your understanding: the five stages",
  "displayTitle": "Check your understanding",
  "body": "The stages of the writing cycle follow a particular order, each building on the one before. Can you put them in the right sequence, from first to last?",
  "instruction": "Drag items to reorder, or use keyboard (Enter to grab, arrows to move, Enter to drop).",
  "ariaQuestion": "Put the five writing-cycle stages in the correct order from first to last.",
  "_attempts": 2,
  "_shouldDisplayAttempts": true,
  "_questionWeight": 1,
  "_canShowModelAnswer": true,
  "_canShowFeedback": true,
  "_canShowMarking": true,
  "_recordInteraction": true,
  "_isPartOfAssessment": false,
  "_items": [
    { "text": "Understand the task" },
    { "text": "Plan" },
    { "text": "Draft" },
    { "text": "Edit" },
    { "text": "Proofread" }
  ],
  "_feedback": {
    "title": "",
    "correct": "That's the right sequence. Each stage has a distinct job, and working through them in this order is what makes the process manageable: you're never trying to do everything at once.",
    "_incorrect": {
      "notFinal": "That's not quite the right order. Think about what has to happen before each stage can begin: you can't draft until you've planned, and you can't plan until you've understood the task.",
      "final": "The correct order is: <em>Understand the task</em> → <em>Plan</em> → <em>Draft</em> → <em>Edit</em> → <em>Proofread</em>. Each stage builds on the one before it, and separating them is what keeps the process from becoming overwhelming."
    },
    "_partlyCorrect": {
      "notFinal": "Some of those are in the right place, but not all. Remember: each stage depends on the one that comes before it.",
      "final": "The correct order is: <em>Understand the task</em> → <em>Plan</em> → <em>Draft</em> → <em>Edit</em> → <em>Proofread</em>. Some of your stages were in the right position, but the full sequence matters for the process to work."
    }
  },
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

**How it satisfies the spec:**

- **Guardrail 1** — `_items` are in the correct sequence; the component shuffles them for the learner.
- **Guardrail 2** — `_component: "sortable"`.
- **Guardrail 3 / §6** — the instruction states both the drag and the keyboard method.
- **Guardrail 5** — full two-tier feedback *plus* a `_partlyCorrect` branch; `notFinal` teaches the dependency logic ("you can't draft until you've planned") rather than just flagging wrongness; items named by text, not position.
- **§4 voice** — formative, contracted, confirm-with-reason; the `final` copy names the whole sequence and says *why* the order holds.
- **§5 tier** — introductory: short, causally transparent, dependencies spelled out.
- **§7 findings** — formative (`_isPartOfAssessment: false`); PLP completion indicator on, per the pilot.

*(A second instance, `c-900`, exists in the sandbox as the component's manual test harness — its body walks through both interaction methods for testing. It is not authored lesson content and is not the reference example.)*

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the custom **adapt-abbott-sortable** component, and — since no Adapt upstream exists — serves as its primary authoring reference. Register and content-type voice live in the **Voice Specification**; tier demand lives in the **Tier Specification**; scoring and formative/summative mechanics live in **`scoring-and-summative-model.md`**; the shared question-feedback two-tier pattern lives in **`mcq.md §3`**; teaching-move routing lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1); the build/compatibility and unit-testing story lives in the **project backlog (P3)** and **`component-candidates-register.md`**. This doc points to them; it does not restate them.

---

*End of adapt-abbott-sortable authoring spec — v0.1.*
