# narrative — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec)
**Verified against:** `src/components/adapt-contrib-narrative/properties.schema` (Adapt 5.56.2)
**Grounded in:** `c-125` — Adapt demo scaffold instance (`courses/academic-writing-introductory`). **No authored lesson instance exists yet** (no L0x-prefixed narrative component in the pilot). The worked example below is therefore illustrative of the schema shape, not an authored voice model; treat it with caution until a real instance is built.
**Relationship to other documents:** references the Voice Specification, the Tier Specification, and `design-kb/design-kb.activity-patterns.json` (which points accordion/hotgraphic away from narrative; component-mapping-artefact.md is SUPERSEDED, MA-1); restates none.

---

## 1. Purpose & when to reach for it

Routing is decided upstream in **Mapping Artefact Part 4**. Narrative is an **image-per-item slideshow**: each step pairs an image with text, and the learner clicks through.

Component-specific "reach for it / don't":

- **Reach for narrative** for **sequential visual content** where each step pairs a distinct image with explanatory text: dialogue between characters (with images showing each speaker), case-study timelines, step-by-step processes where each step has its own visual.
- **Reach for narrative** when the teaching move is "walk through a sequence visually".
- **Don't use narrative for definitions or glossary-style content** — that's `accordion` (progressive disclosure without the image-per-item requirement).
- **Don't use narrative for hotspot exploration over a single base image** — that's `hotgraphic`.
- **Don't use narrative for non-sequential, explore-in-any-order content** — `hotgraphic` or `accordion` may fit better.

The mapping artefact (Part 2) notes that accordion and hotgraphic are the primary progressive-disclosure components for this programme; narrative is available when the image-per-item slideshow pattern is genuinely needed.

---

## 2. The annotated JSON shape

**[LB]** marks a load-bearing field.

```jsonc
{
  "_id": "c-125",
  "_parentId": "b-115",
  "_type": "component",
  "_component": "narrative",
  "_classes": "",
  "_layout": "full",                      // narrative is full-width only

  "title": "Narrative",                   // internal / tracking
  "displayTitle": "",                     // learner-facing heading
  "body": "<p>Walk through the stages of the process.</p>", // [LB] introductory prose
  "instruction": "Select the next and back arrows to find out more.", // [LB] §15.4
  "mobileInstruction": "Select the plus icon followed by the next arrow to find out more.", // mobile-specific

  "_setCompletionOn": "allItems",         // [LB] "inview" | "allItems" — allItems = must view each slide
  "_hasNavigationInTextArea": false,      // move nav buttons to text area
  "_isTextBelowImage": false,             // place text below image instead of beside
  "_isMobileTextBelowImage": false,       // mobile-specific layout
  "_isStackedOnMobile": false,            // stack items vertically on mobile (no interaction)

  "_items": [                             // [LB] the slides
    {
      "title": "Step 1: Understand the task",           // [LB] heading for this slide
      "body": "<p>Before you write a word, work out what the question is asking.</p>", // [LB] text for this slide
      "strapline": "Understand the task",               // short label for mobile strapline button
      "_graphic": {
        "src": "course/en/images/step1.png",            // [LB] the image for this slide
        "alt": "A student reading an essay question carefully.", // [LB] meaningful alt text
        "attribution": ""
      }
    }
    // …one object per slide
  ],

  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

Global aria strings (`ariaRegion`, `previous`, `next`, `titleDialog`, `titleStrapline`) inherit from `course.json` `_globals`; leave defaults unless overriding.

---

## 3. Authoring guardrails (hard rules)

1. **Use narrative only when each step needs its own image.** If the images are incidental or repeated, accordion or hotgraphic is probably a better fit.
2. **Order matters.** Items are presented sequentially; author them in the order the learner should view them. Don't assume learners will jump around.
3. **Each `_items[].body` is self-contained.** The learner may not have the previous slide's text visible; don't rely on "as we saw above".
4. **Each image must have meaningful `alt` text.** Same accessibility rule as graphic — describe what the image shows.
5. **`_setCompletionOn: "allItems"`** is the teaching default. Use `"inview"` only if viewing all slides is genuinely optional.
6. **Keep slide count manageable.** 3–6 items is typical; more than 8 becomes tedious. If you have more, consider splitting across components or rethinking the structure.

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `body` (component-level) | Introductory prose | §15.1 |
| `instruction` / `mobileInstruction` | Activity instruction | §15.4 |
| `_items[].title` | Heading | §5 |
| `_items[].body` | Running prose | §15.1, §8, §10 |
| `_items[]._graphic.alt` | Alt text; describe what the image shows | §14 |
| `strapline` | Short label for mobile | concise, same register |

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

Narrative carries no assessment dimension. Tier affects **text density and image complexity**:

- **Introductory:** Text per slide is concrete and plainly worded; images are straightforward.
- **Advanced:** Text may be denser; images may be more complex.

Register for all text follows **Voice Spec §16**. This doc does not restate those bands.

---

## 6. Accessibility requirements

- **`alt` text on every slide image is mandatory.** Each `_items[]._graphic.alt` must describe the image meaningfully.
- **`strapline`** is announced on mobile; keep it concise and informative.
- **Keyboard navigation.** The component uses arrow buttons; ensure screen-reader announcements (from `_globals`) are clear.
- **`_isStackedOnMobile: true`** — if enabled, items stack vertically with no interaction; ensure this is intentional and that the experience still makes sense.

---

## 7. Known gotchas & findings

- **Narrative is always full-width.** The schema sets `_supportedLayout: "full-width"`.
- **Falls back to narrative on mobile.** On mobile, the display changes to a strapline-button pattern unless `_isStackedOnMobile: true`.
- **`_isTextBelowImage`** — can improve layout on narrow screens but changes the desktop experience too.
- **Demo scaffold only in pilot.** `c-125` is Adapt demo content with generic placeholder text. The first real authored narrative must follow Voice Spec.

---

## 8. Worked example

**Note:** No authored lesson instance exists yet. The example below is from the Adapt demo scaffold (`c-125`), reproduced to show schema shape. It is **ILLUSTRATIVE**, not a voice model.

```json
{
  "_id": "c-125",
  "_parentId": "b-115",
  "_type": "component",
  "_component": "narrative",
  "_classes": "",
  "_layout": "full",
  "title": "Narrative",
  "displayTitle": "Narrative",
  "body": "The <b>Narrative</b> component lets you scroll through a series of images each with some accompanying text.<br><br>This component is always spanned.",
  "instruction": "Select the next and back arrows to find out more.",
  "mobileInstruction": "Select the plus icon followed by the next arrow to find out more.",
  "_setCompletionOn": "allItems",
  "_hasNavigationInTextArea": false,
  "_isTextBelowImage": false,
  "_isMobileTextBelowImage": false,
  "_isStackedOnMobile": false,
  "_items": [
    {
      "title": "Narrative item 1",
      "body": "Narratives are particularly good for showing dialogue between two or more characters, with each step of the conversation being accompanied by an image. This photo story approach can be used to provide context for the learning to follow, to illustrate real-world application of the learning or to show the impact on people when the learning hasn't been applied correctly.",
      "_graphic": {
        "src": "course/en/images/narrative.png",
        "alt": "",
        "attribution": "Copyright (C) 2024"
      },
      "strapline": "Narrative item 1"
    },
    {
      "title": "Narrative item 2",
      "body": "It can also be used to present case studies, where the different displays are used to set the scene, show the key events and then the outcome.",
      "_graphic": {
        "src": "course/en/images/narrative.png",
        "alt": "",
        "attribution": ""
      },
      "strapline": "Narrative item 2"
    },
    {
      "title": "Narrative item 3",
      "body": "This component can also be useful when you want to illustrate the constituent steps that make up a larger process.",
      "_graphic": {
        "src": "course/en/images/narrative.png",
        "alt": "",
        "attribution": ""
      },
      "strapline": "Narrative item 3"
    }
  ],
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

**Gaps vs programme spec (demo scaffold, not authored):**

- `alt` text is blank on all images — violates §6 accessibility.
- Item titles are generic ("Narrative item 1") — not voice-compliant.
- Body text is generic demo content, not programme voice.
- The first authored narrative must address all these.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **narrative** component. Register and content-type voice live in the **Voice Specification** (§15.1, §8, §10); accessibility lives in **§14**; tier register lives in the **Tier Specification** and **§16**; teaching-move routing lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of narrative authoring spec — v0.1 (illustrative example — no authored instance yet).*
