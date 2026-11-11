# checklist (adapt-abbott-checklist) — Authoring Spec

**Version:** 0.1
**Status:** draft — ships with the component (built 2 August 2026). No shipped lesson instance yet; the worked examples are **build-verified** in sandbox.
**Verified against:** `src/components/adapt-abbott-checklist/properties.schema` — **our own schema** (custom component).
**Relationship to other documents:** this component's full rationale lives in `open-decisions.md` #41 (CL-1–7 design, CB-1–5 build spec). This spec references the Voice Specification and the Tier Specification; it restates none of them.

---

## 1. Purpose & when to reach for it

A **set of concrete, tickable actions** the learner works through before or after a task — "before you submit, check these." It is a **working aid, not an assessment**. Presentational, NOT graded: no marking, no `_recordInteraction`, no response semantics.

Reach for it when:
- The learner benefits from a concrete checklist to work through (pre-submission, pre-presentation, revision readiness)
- The items are **actions answerable yes/no without judgement**
- The intent is a working aid that can be reused for multiple tasks

**Do not reach for it when:**

| If you need... | Use instead | Boundary |
|---|---|---|
| A self-efficacy measure (how confident you feel) | `adapt-abbott-confidence` | Confidence measures *belief*; checklist confirms *action*. Both look like "a list of statements the learner responds to" — the distinction is evaluative vs concrete. A confidence item asks "how confident are you about X?"; a checklist item asks "have you done X?" |
| A graded knowledge check | `mcq` | MCQ marks answers correct/incorrect; checklist has no correct answers — ticking is completion, not correctness |
| A static list of actions (no interaction) | `text` (with bulleted list) | Use text when the list is informational and read-through suffices; use checklist when the learner should tick through actively |
| An ordering task | `adapt-abbott-sortable` | Sortable assesses sequence; checklist assesses completeness without order |

> **First homes:** Presenting (7) rehearsal/delivery checks; Revising & Exams (8) revision-readiness; Academic Writing (6) pre-submission; Work-Based (11) placement preparation.

---

## 2. The annotated JSON shape

`_component` is `"checklist"` (lowercase). **[LB]** = load-bearing.

| Field | Required | Notes |
|---|---|---|
| `_component: "checklist"` | ✓ | **[LB]** lowercase |
| `title` | ✓ | Internal title |
| `displayTitle` | ✓ | Learner-facing heading (e.g., "Before you submit") |
| `body` | ✓ | What the checklist is for and when to use it |
| `instruction` | ✓ | How to use it (e.g., "Tick each item when you have checked it.") — also becomes the legend for the fieldset grouping |
| `_items[]` | ✓ | **[LB]** Array of 4–8 items. Each item has a `text` field (required). |
| `_items[].text` | ✓ | **[LB]** A concrete action phrased as a yes/no check. See §3 guardrail 1. |

### Minimal valid instance

```json
{
  "_component": "checklist",
  "title": "Pre-submission checklist",
  "displayTitle": "Before you submit",
  "body": "Work through each item before submitting your essay.",
  "instruction": "Tick each item when you have checked it.",
  "_items": [
    { "text": "Have I answered the question that was actually asked?" },
    { "text": "Have I checked every in-text citation appears in my reference list?" },
    { "text": "Have I run a spell-check and read through for errors it might miss?" },
    { "text": "Have I saved the file in the required format?" }
  ]
}
```

---

## 3. Authoring guardrails (hard rules)

### 1. Voice guardrail — concrete actions only (CL-7)

**This is the component's hard guardrail.** Every item must be a concrete action answerable yes or no without judgement. The checklist collapses if items are vague or evaluative.

| Good | Bad | Why |
|---|---|---|
| "Have I checked every in-text citation appears in my reference list?" | "Is my referencing good?" | "Good" is evaluative; the learner cannot tick yes/no without judging quality |
| "Have I read my conclusion aloud to check it flows?" | "Does my conclusion work?" | "Work" is vague; reading aloud is a concrete check |
| "Have I checked the word count is within the limit?" | "Is my essay the right length?" | "Right length" requires judgement; checking the count does not |
| "Have I asked someone else to read it?" | "Have I got feedback?" | "Feedback" is abstract; "asked someone" is a concrete action |

If you find yourself writing an evaluative item, either:
- Make it concrete by specifying *what to do* rather than *what to assess*
- Move it to a `adapt-abbott-confidence` component (self-efficacy, not action)

### 2. Ticks do not persist (CL-2)

Tick state resets on every visit. Completion persists.

**Why:** A pre-submission checklist ticked for essay one showing all-green when opened for essay two is actively harmful. Checklists are meant to be reused across tasks, so ticks must clear. The learner's *having worked through the checklist* persists (completion) — the individual ticks do not.

**Authoring implication:** Do not write copy implying a saved record of what was ticked. The progress count ("3 of 6 checked") resets to "0 of 6 checked" on revisit.

### 3. 4–8 items

The schema enforces `minItems: 4` and `maxItems: 8`. Fewer than 4 is too sparse for the component to be worthwhile (use text or a simpler prompt). More than 8 is cognitively overwhelming for a working-aid checklist.

### 4. Two states only — unticked / ticked (CL-5)

No "not applicable" third state. If an item doesn't apply to some learners, the authoring answer is a better-worded item, not a third state. Phrase items to be universally applicable to the target audience.

### 5. No summary, no scoring, no closing feedback (CL-6)

A neutral progress count ("3 of 6 checked") is permitted. Evaluative copy is not. Anything resembling a verdict drifts into the confidence component's territory and implies assessment.

**Do not add:**
- "Well done! You've checked everything." (evaluative)
- "You scored 4/6" (implies grading)
- "You might want to revisit the unchecked items." (summative guidance)

The progress count exists for the learner's awareness, not for evaluating their performance.

### 6. Completion fires when all items ticked (CL-3)

The learner must tick every item once to complete the component. Unticking after completion does not un-complete it (CL-4 — one-way visitation).

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `displayTitle` | Heading | §14.2 |
| `body` | Orientation prose | §15.1 |
| `instruction` | Activity instruction | §15.4 |
| `_items[].text` | Checklist item (concrete action) | §15.4 (instructional) — second-person, present tense, question form |

Items are phrased as first-person questions ("Have I...") or second-person instructions ("Check that..."). The first-person question form is preferred for reflective checklists; the imperative form works for procedural checklists.

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

Tier calibration is **content only**, expressed in the specificity of actions:

| Tier | How items are phrased |
|---|---|
| Introductory | Spell out what to look for. Example: "Have I checked that every sentence ends with a full stop, question mark, or exclamation mark?" |
| Intermediate | Name the practice. Example: "Have I checked my punctuation?" |
| Advanced | Assume the learner knows what the practice entails. Example: "Punctuation check completed?" |

The component mechanics do not change by tier — only the granularity of instruction in the items.

---

## 6. Accessibility requirements

### Native checkbox controls (CL-A)

The component uses **native `<input type="checkbox">`** elements with properly associated `<label>` elements. This is one of the rare cases where the native control is exactly right — keyboard operation (Space to toggle, Tab to move) and state announcement ("checked"/"unchecked") come free.

**Do not style checkboxes as custom divs.** The native checkbox is visually hidden but accessible; a custom indicator renders the visible state.

### Unique IDs per instance

Each checkbox's `id` and its label's `for` attribute are derived from the component's `_id`. This prevents collisions when multiple checklist instances appear on the same page.

**Silent-failure risk:** If two instances had colliding IDs, clicking a label in instance B would toggle instance A's checkbox — incorrect behaviour that fails silently (no error). The component derives IDs as `{_id}-item-{index}` to prevent this.

### Group label

The checkboxes are grouped inside a `<fieldset>` with a `<legend>` containing the instruction text. This provides a programmatic group label for screen readers.

### Focus behaviour

Focus stays on the checkbox after ticking — no focus movement. This follows the flipcard/timeline/tabs pattern, not the confidence/branching move-focus pattern.

### Not colour alone

Ticked state is signalled by the native checkmark plus font-weight or strikethrough on the label — never colour alone.

### Progress announcement

The progress count uses `aria-live="polite"` to announce updates without interrupting. It is never the only signal of state (the checkboxes themselves convey state).

### Reduced motion

`prefers-reduced-motion` → transitions are instant.

---

## 7. Known gotchas & findings

- **`_component` is `"checklist"`** (lowercase), not the plugin directory name.
- **Ticks reset on revisit.** This is intentional (CL-2). Do not author copy implying persistence.
- **Completion persists but ticks do not.** After completion, revisiting shows all checkboxes unchecked but the component marked complete. This is correct behaviour — the CL-2/CL-4 contract.
- **Static template assignment is mandatory.** The View uses `ChecklistView.template = 'checklist.jsx';` after the class definition — inline `export default class` leaves the template unassigned (learned from the annotated build).
- **`_checkedMap` is a plain instance property, not a Backbone attribute.** It cannot serialise to SCORM. This is the CB-2 amendment — component-level map instead of per-item `_isChecked`.
- **Label uniqueness across instances.** IDs derive from `_id` to prevent collision. If you ever see clicking one checklist toggle another's checkbox, check for duplicate component `_id` values.

---

## 8. Worked examples (BUILD-VERIFIED — no shipped instance yet)

From Stage 2 sandbox verification (2 August 2026). Both examples passed all Playwright checks including cross-instance label association and revisit-check (ticks cleared, completion restored).

### 4-item checklist (minimum bound) — pre-submission

```json
{
  "_id": "TEST-c-05",
  "_component": "checklist",
  "title": "Pre-submission checklist (4 items)",
  "displayTitle": "Before you submit",
  "body": "Work through each item before submitting your essay.",
  "instruction": "Tick each item when you have checked it.",
  "_items": [
    { "text": "Have I answered the question that was actually asked?" },
    { "text": "Have I checked every in-text citation appears in my reference list?" },
    { "text": "Have I run a spell-check and read through for errors it might miss?" },
    { "text": "Have I saved the file in the required format?" }
  ]
}
```

**How it satisfies the spec:** 4 items (minimum bound); every item is a concrete action answerable yes/no (guardrail 1); items phrased as first-person questions; no evaluative copy; `_id` used for unique checkbox IDs.

### 8-item checklist (maximum bound) — editing

```json
{
  "_id": "TEST-c-10",
  "_component": "checklist",
  "title": "Comprehensive editing checklist (8 items)",
  "displayTitle": "Editing checklist",
  "body": "Use this checklist when editing your draft.",
  "instruction": "Work through each item before moving to proofreading.",
  "_items": [
    { "text": "Does my introduction state what I will argue?" },
    { "text": "Does each paragraph have a clear topic sentence?" },
    { "text": "Have I shown the relationship between ideas, not just listed them?" },
    { "text": "Have I used signpost words to guide the reader?" },
    { "text": "Does my conclusion follow from the argument I made?" },
    { "text": "Have I removed any repetition that does not add emphasis?" },
    { "text": "Have I checked that every claim is supported by evidence?" },
    { "text": "Is each paragraph roughly the same length as the others?" }
  ]
}
```

**How it satisfies the spec:** 8 items (maximum bound); all items are concrete checks; mix of first-person ("Have I...") and structure-focused ("Does my...") phrasing; no evaluative summary.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **checklist** component. Its design rationale lives in `open-decisions.md` #41 (CL-1–7, CB-1–5); register and voice live in the **Voice Specification**; tier register and demand calibration live in the **Tier Specification**; the routing decision (checklist vs confidence vs mcq vs text) is summarised in this doc's §1 table and recorded in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of checklist authoring spec — v0.1.*
