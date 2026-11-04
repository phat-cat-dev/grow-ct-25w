# workedExample (adapt-abbott-worked-example) — Authoring Spec

**Version:** 0.1
**Status:** draft — ships with the component (v4 lesson page model work, Nov 2026). No shipped lesson instance yet.
**Verified against:** `src/components/adapt-abbott-worked-example/properties.schema` — **our own schema** (custom component).
**Relationship to other documents:** cloned from `adapt-abbott-checklist`'s toggle+region accordion pattern (`open-decisions.md` #41, CL-1–7/CB-1–5) — that doc's accessibility and build rationale applies here unchanged. The content rule (weaker-then-stronger, `{{learner-a}}`/`{{learner-b}}` tokens, no literal names) lives in `design-kb/design-kb.skeletons.json`'s `worked-example` slot and in `docs/authoring/worked-example-cue-convention.md`; this spec does not restate it.

---

## 1. Purpose & when to reach for it

A **collapsible accordion carrying a single worked-example body**: a weaker attempt contrasted with a stronger one, third person, cast carried by the `{{learner-a}}`/`{{learner-b}}` tokens. Presentational, NOT graded: no marking, no `_recordInteraction`, no response semantics. Completion fires on **first open** — the same gate as checklist — not on any form of self-assessment, because there isn't one here.

Reach for it when:
- The slot is `worked-example` and the content is the standard weaker/stronger contrast (`activity-patterns/evaluate-versions`).
- The example is plain prose with no need for phrase-level annotation, images, or branching.

**Do not reach for it when:**

| If you need... | Use instead | Boundary |
|---|---|---|
| Phrase-level commentary on the weak/strong passages | `annotated` | Annotated highlights specific wording; workedExample is plain prose. |
| An image-based before/after comparison | `narrative` | Narrative is for visual artefacts, not prose contrasts. |
| A tickable self-check | `checklist` | Checklist is a working aid with per-item ticks; workedExample has no items. |

---

## 2. The annotated JSON shape

`_component` is `"workedExample"` (camelCase — the registered name, not the plugin directory name). **[LB]** = load-bearing.

| Field | Required | Notes |
|---|---|---|
| `_component: "workedExample"` | ✓ | **[LB]** camelCase |
| `title` | ✓ | Internal title |
| `displayTitle` | ✓ | Learner-facing toggle label (e.g., "Worked example: paraphrasing") |
| `body` | ✓ | **[LB]** The worked-example prose. Carries the `we-weaker`/`we-stronger` paragraph classes, applied by `merge-context.js`'s `wrapProse()` before this component ever sees it — the component itself does no token or cast logic. |

### Minimal valid instance

```json
{
  "_component": "workedExample",
  "title": "Worked example: paraphrasing",
  "displayTitle": "Worked example: paraphrasing",
  "body": "<p class=\"we-weaker\">{{learner-a}} copies the sentence and swaps a few words for synonyms...</p><p class=\"we-stronger\">{{learner-b}} reads the passage, closes the book, and writes the idea in {{learner-b-possessive-pronoun}} own words...</p>"
}
```

---

## 3. Authoring guardrails (hard rules)

The cast/token rule, the weaker-then-stronger order, and the `we-weaker`/`we-stronger` class convention are governed by `design-kb/design-kb.skeletons.json`'s `worked-example` slot and `docs/authoring/worked-example-cue-convention.md` — not restated here. The component-level rules are:

### 1. One body, no items

Unlike checklist, this component has no `_items[]`. The entire contrast lives in one `body` field as continuous prose (the merge renders it as a block quote).

### 2. Completion fires on first open (not on any self-assessment)

The learner does not tick or answer anything. Opening the accordion is the whole gate — mirrors checklist's CL-3 pattern exactly, with no CL-4 (one-way visitation) or CL-2 (tick reset) to speak of, because there is no tick state at all.

### 3. No summary, no scoring, no closing feedback

Same as checklist's CL-6: this is presentational, not an assessment. Nothing resembling a verdict belongs in the body.

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `displayTitle` | Heading | §14.2 |
| `body` | Worked-example prose | §15.1; cast via `{{learner-a}}`/`{{learner-b}}` tokens per the cue convention doc |

---

## 5. Accessibility requirements

Identical model to checklist (`docs/authoring/component-specs/checklist.md` §6), minus the checkbox-specific points:

- **Real `<button>` toggle** with `aria-expanded`/`aria-controls`; region labelled via `aria-labelledby` and `aria-label` (from the `ariaRegion` global).
- **Unique IDs per instance**, derived from `_id`, to prevent collisions when multiple instances appear on one page.
- **Reduced motion**: `prefers-reduced-motion` → icon rotation is instant.

---

## 6. Known gotchas & findings

- **`_component` is `"workedExample"`** (camelCase), not the plugin directory name (`adapt-abbott-worked-example`).
- **Static template assignment is mandatory** — `WorkedExampleView.template = 'worked-example.jsx';` after the class definition, same lesson learned building checklist.
- **No `_checkedMap`, no transient tick state at all.** If a future variant needs per-item ticks, that is a different component (checklist already exists for that); do not bolt ticking onto this one.
- **The `we-weaker`/`we-stronger` classes are not this component's concern.** They arrive already baked into `body` from the merge step; this component only renders `body` as-is.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **workedExample** component. Its accessibility/build rationale is inherited from checklist's `open-decisions.md` #41 (CL-1–7, CB-1–5); the cast-token and cue-class content rule lives in `design-kb/design-kb.skeletons.json` and `docs/authoring/worked-example-cue-convention.md`; the routing decision (workedExample vs annotated vs narrative vs text) is recorded in **`design-kb/design-kb.activity-patterns.json`** (`evaluate-versions`) and **`design-kb/design-kb.palette.json`**. This doc points to them; it does not restate them.

---

*End of workedExample authoring spec — v0.1.*
