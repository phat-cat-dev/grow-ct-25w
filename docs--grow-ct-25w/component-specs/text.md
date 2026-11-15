# text — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec)
**Verified against:** `src/components/adapt-contrib-text/properties.schema` (Adapt 5.56.2)
**Grounded in:** `L01-c-05` (orientation), `L01-c-10` (concept introduction), `L02-c-05` (orientation), and others in Academic Writing / Introductory Stage (`courses/academic-writing-introductory`).
**Relationship to other documents:** references the Voice Specification and the Tier Specification; restates none. This is the programme's prose container; nearly all authoring rules live in the Voice Spec, not here.

---

## 1. Purpose & when to reach for it

Routing is decided upstream in **Mapping Artefact Part 4** (the "Concept explanation" and related prose rows). Text is the **prose container**: the standard component for running explanatory copy that requires no interaction.

Component-specific "reach for it / don't":

- **Reach for text** for any teaching prose that stands alone: orientations, concept explanations, practical guidance, analyses. It is the workhorse.
- **Reach for text** when the material needs no progressive disclosure, no question, no image anchoring — just prose a learner reads straight through.
- **Don't use text for stepped reveals** (→ `accordion`, `hotgraphic`, `narrative`), for reflective input (→ `textInput`), or for any assessed interaction (→ `mcq`, `matching`, `adapt-abbott-sortable`).

Text is the simplest component. Its rules are almost entirely about *voice*, not *schema*.

---

## 2. The annotated JSON shape

The schema is minimal: a text component inherits the base component model and adds only `instruction`.

```jsonc
{
  "_id": "L01-c-05",
  "_parentId": "L01-b-05",
  "_type": "component",
  "_component": "text",
  "_classes": "",                         // custom styling classes if needed (e.g. "scenario-blockquote")
  "_layout": "full",                      // "full" | "left" | "right"

  "title": "Orientation",                 // internal / tracking
  "displayTitle": "",                     // learner-facing heading; often blank
  "body": "<p>Most people picture writing as a single act…</p>", // [LB] the prose; HTML allowed
  "instruction": "",                      // optional; rarely used for pure text

  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": false }
}
```

That is the entire authoring surface. No `_items`, no `_feedback`, no scoring, no special fields. The work is in the `body`.

---

## 3. Authoring guardrails (hard rules)

1. **Author to the Voice Spec.** The component has no mechanics to constrain; the constraints are voice and register. Apply the Voice Spec's running-prose rules (§15.1), the paragraph structure (§10), the sentence rhythm (§8), the rhetorical strategies (§11), and the anti-patterns (§12).
2. **`displayTitle` is often blank.** A text component following directly after a lesson heading rarely needs its own heading. Use `displayTitle` only when the component introduces a distinct section the learner should orient to.
3. **HTML in `body` is standard.** Use `<p>`, `<em>`, `<strong>`, `<ol>`, `<ul>`, `<blockquote>` as needed. Avoid inline styles.
4. **`instruction` is rarely needed.** If the learner is simply reading, no instruction is required. Reserve `instruction` for cases where a read-along or specific action is warranted.

---

## 4. Voice rules (reference — not restated here)

This is the discipline section. Text is a pure prose container; its Voice Spec mapping is almost the entire spec.

| Field | Content type | Voice Spec |
|---|---|---|
| `body` | Running prose | §15.1 (running prose), §10 (paragraph conventions), §8 (sentence-level), §11 (rhetorical strategies), §12 (anti-patterns), §2 (why-before-how), §6 (address and person), §7 (tone and register), §13 (vocabulary) |
| `displayTitle` | Heading (if used) | §5 (formatting — headings) |
| `instruction` | Activity instruction (if used) | §15.4 |

**Do not restate §15.1 here.** The Voice Spec is the authority; this doc points. If you find yourself copying prose rules into this section, that content belongs upstream.

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

Text carries no assessment dimension. Tier affects **register and depth**: sentence length, vocabulary, density of explanation. These are governed by **Voice Spec §16** (tier calibration) and the Tier Spec's register-band anchor. This doc does not restate them.

In practice, introductory text is concrete and plainly worded; higher tiers increase density, nuance, and vocabulary. The specific per-tier sentence-length bands live in Voice Spec §8.1 and the §16 tier calibration (mirrored in the mapping artefact's Part 4 tier column) — author to those; this doc does not restate the numbers.

---

## 6. Accessibility requirements

- **Semantic HTML.** Use `<p>`, `<ul>`, `<ol>`, `<blockquote>` correctly. Screen readers rely on structure.
- **No images in text.** If an image is needed, pair a `graphic` component alongside or use a component that handles images (`hotgraphic`, `narrative`). Text is text.
- **No reliance on formatting for meaning.** Bold and italics are acceptable for emphasis (§5), but do not convey essential information through styling alone.

---

## 7. Known gotchas & findings

- **Text completes on scroll-in.** The component completes as soon as it scrolls into view; there is no "must read" mechanic. `_pageLevelProgress._isCompletionIndicatorEnabled` is typically `false` because there is nothing the learner "does" to complete.
- **Block-quote styling.** For worked-example scenarios (italicised block quotes), add `_classes: "scenario-blockquote"` and use the `<blockquote><em>…</em></blockquote>` pattern in `body`. The class is a project convention, not a schema field.
- **Layout choice.** `"left"` or `"right"` pairs with a sibling component on the other side (commonly `graphic`). `"full"` spans the width alone. Choose based on page design.

---

## 8. Worked example

`L01-c-05`, the real authored orientation from Academic Writing / Introductory lesson 1.

```json
{
  "_id": "L01-c-05",
  "_parentId": "L01-b-05",
  "_type": "component",
  "_component": "text",
  "_classes": "",
  "_layout": "full",
  "title": "Orientation",
  "displayTitle": "",
  "body": "<p>Most people picture writing as a single act: you sit down, you write, and a finished piece appears. It almost never works like that. What actually produces good writing is a series of stages, each doing a different job, and knowing what those stages are takes a surprising amount of pressure off. When you understand that a first draft is only ever meant to be a first draft, the blank screen stops being quite so frightening.</p><p>This lesson introduces that sequence of stages, which we'll call the 'writing cycle'. It's the foundation for everything else in this pathway; each stage gets a closer look of its own later on. For now, the aim is simply to see the shape of the whole process, and to understand why working in stages produces better writing than trying to do everything at once.</p>",
  "instruction": "",
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": false }
}
```

**How it satisfies the spec:**

- **Guardrail 1** — prose follows §15.1: mid-register, varied rhythm, why-before-how, addresses the student as "you".
- **Guardrail 2** — `displayTitle` is blank; the lesson's page heading serves as the section marker.
- **Guardrail 3** — HTML is `<p>` tags only, appropriate for running prose.
- **Guardrail 4** — no `instruction` needed.
- **§5 tier** — introductory: concrete, plainly worded; sentence-length band per §8.1 / §16.
- **§7 findings** — completion indicator off; no learner action required.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape of the **text** component, which is minimal. Register, paragraph structure, sentence rhythm, rhetorical strategies, and anti-patterns live in the **Voice Specification** (§15.1, §8, §10, §11, §12); tier register lives in the **Tier Specification** and **§16**; teaching-move routing lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of text authoring spec — v0.1.*
