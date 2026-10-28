# accordion — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec)
**Verified against:** `src/components/adapt-contrib-accordion/properties.schema` (Adapt 5.56.2)
**Grounded in:** `L02-c-20` — the "Rhian reads her question" worked example in Academic Writing / Introductory Stage (`courses/academic-writing-introductory`).
**Relationship to other documents:** references the Voice Specification, the Tier Specification, and `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1); restates none.

---

## 1. Purpose & when to reach for it

Routing is decided upstream in **Mapping Artefact Part 4**. Accordion presents a series of headings which expand to reveal associated text; it is the programme's tool for **text-only stepped reveals**.

Component-specific "reach for it / don't":

- **Reach for accordion** when you have a sequence of discrete points the learner explores at their own pace, and those points are text (with optional supporting images) rather than anchored to a base diagram. Typical uses: process steps that need explanation, stepped worked examples (as in `L02-c-20`), recaps, lists that need unpacking.
- **Don't use accordion for image-anchored stepped reveals** — that's `hotgraphic` (pins over a base image) or `narrative` (image-text slideshow). Accordion is the text-first option; if the teaching move centres on an image, use the image-based component.
- **Don't overload it.** Long item bodies defeat the purpose of progressive disclosure; if an item needs several paragraphs, reconsider whether the information belongs in running `text` instead.

---

## 2. The annotated JSON shape

**[LB]** marks a load-bearing field. Accordion is lean — no scoring, no feedback, no answer key.

```jsonc
{
  "_id": "L02-c-20",
  "_parentId": "L02-b-15",
  "_type": "component",
  "_component": "accordion",
  "_classes": "",                         // custom styling classes if needed
  "_layout": "full",                      // "full" | "left" | "right"

  "title": "Worked example: Rhian reads her question",   // internal / tracking
  "displayTitle": "",                     // learner-facing heading; often blank for accordion
  "body": "Let's see how this works on a real question…", // optional lead-in text
  "instruction": "Select the headings to follow Rhian's reasoning.", // [LB] §15.4 — tells the learner what to do

  "_setCompletionOn": "allItems",         // [LB] "allItems" = must open every item; "inview" = scrolled past. §7 gotcha
  "_shouldCollapseItems": true,           // [LB] true = opening one closes others (default). False = multiple open.
  "_shouldExpandFirstItem": false,        // true = first item expanded on load
  "_isCenterAligned": false,              // rarely used; vertical button layout

  "_items": [                             // [LB] the expandable items
    {
      "title": "She reads the question, not the topic",  // [LB] item heading — should be meaningful on its own
      "body": "<p><em>Rhian reads her essay question…</em></p>", // item content; HTML allowed
      "_classes": "",                     // per-item styling
      // "_titleIcon": "",                // optional decorative icon class (not used in pilot)
      "_imageAlignment": "full",          // "full" | "left" | "right" — if image provided
      "_graphic": {                       // optional image inside item
        "src": "",
        "alt": "",
        "attribution": ""
      }
    }
    // …one object per item
  ],

  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

Global aria strings (`ariaRegion`) inherit from `course.json` `_globals`; leave the component defaults unless a lesson needs an override.

---

## 3. Authoring guardrails (hard rules)

1. **Item titles must be meaningful in isolation.** The learner scans the closed headings before deciding which to open; a title like "Step 1" says nothing. Prefer titles that name the step's content (as in `L02-c-20`: "She reads the question, not the topic").
2. **Keep item bodies concise.** Accordion is for progressive disclosure, not hiding long prose. One or two short paragraphs per item; if you need more, reconsider the component choice.
3. **Decide completion deliberately.** `_setCompletionOn: "allItems"` means the learner must open every item before the component completes; this interacts with trickle/PLP gating. Use it when you want guaranteed engagement with each point; switch to `"inview"` only if opening every item shouldn't be mandatory.
4. **Set collapse behaviour for the teaching move.** `_shouldCollapseItems: true` (the default) keeps only one item open at a time — good for sequential steps where context builds. `false` lets multiple stay open — useful for reference lists the learner may want to compare.

---

## 4. Voice rules (reference — not restated here)

Accordion is presentation, not assessment — there is no feedback to author.

| Field | Content type | Voice Spec |
|---|---|---|
| `body` (component) | Optional lead-in prose | §15.1 |
| `instruction` | Activity instruction | §15.4 |
| `_items[].title` | Concise meaningful heading | §5 (headings), §13 (register) |
| `_items[].body` | Short expository teaching text (or worked-example steps, as in `L02-c-20`) | §15.1 (§15.2 for worked examples) |
| `_items[]._graphic.alt` | Accessible image description | §14 |

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

Accordion carries no assessment dimension, so the tier does not change its mechanics — it changes the **depth and register of the item content**. Item bodies follow the cognitive-demand and register expectations of the tier (introductory: concrete and plain; higher tiers: more analytical or nuanced). Register tracks the pathway's **§16** band. The Tier Spec's §7 (assessment) does not apply here.

---

## 6. Accessibility requirements

- **Item titles are the primary navigation.** Screen-reader users hear the titles first; make them descriptive.
- **`ariaRegion`** defaults to "List of expandable sections. Select each button to expand the content." Override in `course.json` only if needed.
- **Per-item `_graphic.alt`** where an image conveys meaning; leave blank for decorative images.
- **Keep `_shouldExpandFirstItem: false`** unless there is a strong design reason to expand on load — starting collapsed lets the learner orient before committing.

---

## 7. Known gotchas & findings

- **`_setCompletionOn: "allItems"` gates on opening, not reading.** The component completes once every item has been opened, regardless of scroll depth within the item. Treat as "must visit", not "must read in full".
- **Collapse behaviour is visual, not tracked.** Whether items are allowed to stay open (`_shouldCollapseItems: false`) does not affect completion or tracking — it's a UX choice only.
- **Images inside items follow the standard `_graphic` shape** but are optional. For text-only items, omit `_graphic` or leave `src` blank.
- **HTML is allowed** in `body` (both component-level and item-level).

---

## 8. Worked example

`L02-c-20`, the real authored "Rhian reads her question" worked example from Academic Writing / Introductory lesson 2 — five items stepping through her reading of an essay question.

**LK-1 note (22 September 2026):** `_classes` below shows the marker form this real, already-built
example actually carries, quoted as authored. The current form, written by the generator (not by
hand), is `slot__<page>__<slotType>` — see `open-decisions.md` LK-1.

```json
{
  "_id": "L02-c-20",
  "_parentId": "L02-b-15",
  "_type": "component",
  "_component": "accordion",
  "_classes": "context-slot slot-understandingTheTask-workedExample",
  "_layout": "full",
  "title": "Worked example: Rhian reads her question",
  "displayTitle": "",
  "body": "<p>Let's see how this works on a real question. Rhian, a second-year criminology student, has been set the following task. Select each heading to follow how she reads it, one part at a time.</p>",
  "instruction": "Select the headings to follow Rhian's reasoning.",
  "_setCompletionOn": "allItems",
  "_shouldCollapseItems": true,
  "_shouldExpandFirstItem": false,
  "_items": [
    {
      "title": "She reads the question, not the topic",
      "body": "<p><em>Rhian reads her essay question: 'To what extent does poverty explain rising youth knife crime in England and Wales?' Her first instinct is to open a blank document and start writing everything she knows about knife crime. Instead, she stops and looks at the question itself.</em></p>"
    },
    {
      "title": "The steer: 'To what extent'",
      "body": "<p><em>She starts with the opening phrase. 'To what extent', she decides, is asking her to reach a judgement, to weigh how far poverty explains the problem rather than just describing the problem itself.</em></p>"
    },
    {
      "title": "The obvious keywords",
      "body": "<p><em>Then she looks at the rest. 'Poverty', 'youth knife crime' and 'England and Wales' are the obvious keywords; they tell her what the essay is about and where its boundaries sit.</em></p>"
    },
    {
      "title": "The hidden word: 'explain'",
      "body": "<p><em>But two smaller words catch her eye. The question doesn't ask what poverty is linked to; it asks what poverty 'explains', which pushes her towards causes, and towards weighing poverty against other possible explanations.</em></p>"
    },
    {
      "title": "The hidden word: 'rising'",
      "body": "<p><em>And it doesn't ask about knife crime in general; it asks about 'rising' knife crime, which means she'll need to account for a change over time, not just a snapshot.</em></p>"
    }
  ],
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

**How it satisfies the spec:**

- **Guardrail 1** — item titles are meaningful: "She reads the question, not the topic", "The steer: 'To what extent'", etc.
- **Guardrail 2** — item bodies are one paragraph each, italicised scenario prose.
- **Guardrail 3 & 4** — `allItems` completion (open every step) and `_shouldCollapseItems: true` (one open at a time, sequential reading).
- **§4 voice** — component body is §15.1 lead-in prose; instruction is §15.4; item bodies are §15.2 worked-example narrative (italicised third-person).
- **§5 tier** — introductory: concrete, scenario-driven.
- **Context slot** — `_classes` marks it as a context slot for portability.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **accordion** component. Register and content-type voice live in the **Voice Specification**; tier register and content depth live in the **Tier Specification**; teaching-move routing (text-only stepped reveal vs image-anchored) lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of accordion authoring spec — v0.1.*
