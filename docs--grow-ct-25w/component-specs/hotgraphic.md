# hotgraphic — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec #4)
**Verified against:** `src/components/adapt-contrib-hotgraphic/properties.schema` (Adapt 5.56.2)
**Grounded in:** `L01-c-15` — the writing-cycle diagram in Academic Writing / Introductory Stage (`courses/academic-writing-introductory`).
**Relationship to other documents:** references the Voice Specification, the Tier Specification, and `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1, and its former "Hotgraphic notes" block is retired, D-F4-4); restates none.

---

## 1. Purpose & when to reach for it

Routing is decided upstream in **Mapping Artefact Part 4** (the "Interactive labelled diagram" row). hotgraphic presents a base image with selectable pins, each revealing a titled popup of teaching text — good for labelled diagrams, process maps, cycles, and annotated exemplars where the learner explores each part.

Component-specific "reach for it / don't":

- **Reach for hotgraphic** when there is a genuine *base image* and discrete points on it to reveal — the image carries meaning and the pins annotate it (the writing-cycle diagram: five stages positioned around a circle).
- **Don't use hotgraphic for text-only stepped reveals** — that's `accordion`. hotgraphic is image-anchored; using it without a real base image means fighting the required-image machinery (see the tax in §3). Equally, don't reach for `narrative` for text-only stepped content — it has the same per-item-image requirement.
- **Don't overload it.** Dense, overlapping pins are an accessibility and usability problem (§6); if you have many points, reconsider whether a diagram is the right vehicle.

---

## 2. The annotated JSON shape

**[LB]** marks a load-bearing field. The pin array is where the work is.

```jsonc
{
  "_component": "hotgraphic",        // standard component value
  "_layout": "full",

  "title": "The writing cycle",       // internal / tracking
  "displayTitle": "",                 // often blank — the diagram carries the heading
  "instruction": "Select each stage to find out what it does.", // §15.4

  "_setCompletionOn": "allItems",     // [LB] "allItems" = learner must open every pin to complete (default). Alternative "inview" = just scrolled into view. §7
  "_useNumberedPins": true,           // [LB] numbered pins when order matters (a process/sequence). Pilot: the five ordered stages.
  "_isNarrativeOnMobile": true,       // [LB] converts to a narrative slideshow on mobile — keep true for accessibility. §6
  "_pinOffsetOrigin": true,           // [LB] center origin so pins stay put when the image scales responsively. §7

  "_graphic": {                       // [LB] the base image behind the pins
    "src": "course/en/images/L01-writing-cycle.png",
    "alt": "The writing cycle: a circular diagram showing five stages…" // [LB] meaningful alt — the diagram conveys content. §6
  },

  "_items": [                         // [LB] the pins
    {
      "title": "1. Understand the task",   // [LB] popup title (carries the step number too)
      "body": "<p>The first stage works out what you're being asked to do…</p>", // the teaching text; HTML allowed. §4
      "strapline": "Understand the task",  // [LB] REQUIRED; the label shown in the mobile narrative. §3
      "_left": 50, "_top": 10,             // [LB] pin position as PERCENTAGES of the base image. §7
      "_classes": "hide-popup-image",      // [LB] text-only pins: hides the (still-required) popup image. §3 — the hotgraphic tax
      "_graphic": {                        // [LB] REQUIRED even for text-only pins (schema-required)
        "src": "course/en/images/single-width.png"  // placeholder image, suppressed by hide-popup-image
      }
      // "_tooltip": {                     // optional — hover/focus tooltip on the pin itself
      //   "_isEnabled": true,             // must be true for the tooltip to render (false if omitted)
      //   "text": "",                     // tooltip text (keep short)
      //   "_position": "top",             // "top" | "bottom" | "left" | "right"
      //   "_classes": ""                  // optional styling hook
      // },
      // "_pin": {                         // optional — custom pin image
      //   "src": "",
      //   "alt": ""                       // populate if the custom pin conveys meaning; leave blank if decorative
      // }
    }
    // …one object per pin
  ]
}
```

Further optional fields exist beyond the annotated example above (the
pilot uses none of them), organised by the level they apply at. Values
and defaults are from the live schema, not guessed.

**Component-level:**
- `mobileBody` (string, default `""`): body text shown on mobile when
  the component converts to a Narrative.
- `_isMobileTextBelowImage` (boolean, default `false`): on mobile, drops
  the text area below the image instead of behind the strapline button.
  Only applies when rendering as a Narrative on mobile.
- `_hidePagination` (boolean, default `false`): hides the popup's
  progress indicator and previous/next links.
- `_canCycleThroughPagination` (boolean, default `false`): lets the
  popup navigation wrap around (next on the last item shows the first).
- `_useGraphicsAsPins` (boolean, default `false`): hides the main
  graphic and shows pins as positioned images instead.
- `_hasStaticTooltips` (boolean, default `false`): tooltips (if enabled)
  always show rather than only on hover.
- `_isRound` (boolean, default `false`): applies a 50% border radius to
  the items' popup images. Component-level, not item-level, despite
  living conceptually close to per-item pin styling.

**Item-level** (`_items[]`):
- `_graphic.attribution` (string, default `""`): attribution text shown
  for the popup image.
- `_graphic._classes` (string, default `""`): custom CSS classes on the
  pin, or on the hotspot tile if `_useGraphicsAsPins` is true.
- `_classes` (string, default `""`): custom CSS classes on the popup
  item itself. Two documented values: `hide-desktop-image` (hides the
  popup image on desktop only) and `hide-popup-image` (hides it on all
  screen sizes, the pilot's own pattern for text-only pins).

**Pin-level** (`_items[]._pin`):
- `_pin.srcHover` (string, default `""`): pin image hover state.
- `_pin.srcVisited` (string, default `""`): pin image visited state.

Global aria strings and the mobile `mobileBody`/`mobileInstruction`
default sensibly; set the mobile texts only if the narrative fallback
needs its own framing.

---

## 3. Authoring guardrails (hard rules)

1. **The hotgraphic tax: every pin requires `_graphic.src`, even text-only ones.** The schema makes the per-pin popup image *required*. For a text-only pin you still supply an image (a shared placeholder like `single-width.png`) **and** add `_classes: "hide-popup-image"` to suppress it at all screen sizes. This is the single most re-explained hotgraphic rule; the pilot applies it to all five pins. (`hide-desktop-image` hides only on desktop — use `hide-popup-image` for genuinely text-only content.)
2. **`strapline` is required on every pin.** It's the label the mobile narrative uses; a missing or vague strapline breaks the mobile experience. Keep it a short, meaningful name for the pin.
3. **Pin positions are percentages tied to the specific base image.** `_left` / `_top` are percent coordinates over the current artwork. If the base image changes, the positions must be re-tuned — and the pilot's base is a provisional placeholder (see the backlog asset note), so its positions are provisional too.
4. **Use `_pinOffsetOrigin: true` for stable responsive placement.** Without it, pins anchor at top-left and drift as the image scales. The pilot sets it true.
5. **Choose completion deliberately.** `_setCompletionOn: "allItems"` (the pilot's setting) means the learner must open every pin before the component completes — which interacts with trickle/PageLevelProgress gating. Use it when you want guaranteed engagement with each point; switch to `"inview"` only if opening every pin shouldn't be mandatory.
6. **Numbered pins when order matters.** Set `_useNumberedPins: true` for a process or sequence so pins read as steps; the pilot also carries the number in each pin `title` ("1. Understand the task").

---

## 4. Voice rules (reference — not restated here)

hotgraphic is presentation, not assessment — there is no feedback to author.

| Field | Content type | Voice Spec |
|---|---|---|
| `_items[].body` | Short expository teaching text per pin | §15.1 |
| `instruction` | Activity instruction | §15.4 |
| `_items[].title` / `strapline` | Concise labels | §13 (register) |
| `_graphic.alt`, pin `_graphic.alt` | Accessible image descriptions | §14 |

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

hotgraphic carries no assessment dimension, so the tier does not change its mechanics — it changes the *depth of the pin content*. The `body` text per pin follows the cognitive-demand and register expectations of the tier: introductory pins are concise and concrete (as in `L01-c-15` — a plain sentence or two per stage); higher tiers carry denser, more analytical annotation. Register tracks the pathway's **§16** band. The Tier Spec's §7 (assessment) does not apply here.

---

## 6. Accessibility requirements

- **Meaningful base `alt`.** The base image conveys content (a diagram), so `_graphic.alt` is required and must describe what the diagram shows — not "decorative". The pilot describes the circular five-stage layout.
- **Keep `_isNarrativeOnMobile: true`.** On mobile the component becomes a narrative slideshow, which makes every pin reachable by simple next/previous rather than precise pointer targeting on a small image. Disabling it (a scaled-down desktop render) is hard for touch and assistive tech — keep the narrative fallback.
- **`strapline` feeds the mobile narrative** and must be meaningful (guardrail 2).
- **Pin `_graphic.alt`** where a popup image conveys meaning; for hidden (`hide-popup-image`) or decorative images, leave blank.
- **Pin density and overlap.** The artefact flags dense pins as an accessibility concern; keep pins few enough and positioned so they don't overlap or crowd, and numbered pins (guardrail 6) aid orientation.
- **`_tooltip` and `_pin.alt`.** If using `_tooltip`, keep the text short — it appears on hover/focus and should orient, not teach. If using a custom `_pin` image, populate `alt` only when the pin graphic itself conveys meaning (e.g. a distinctive icon); leave blank for decorative custom pins.
- Global aria strings (`ariaRegion`, item count, previous/next, `popupPagination`) default sensibly; override only for wording.

---

## 7. Known gotchas & findings

- **The required-image tax** (guardrail 1) is the defining hotgraphic gotcha: text-only pins still need a `_graphic.src`, hidden via `hide-popup-image`. All five pilot pins do exactly this.
- **`_pinOffsetOrigin: true`** is needed for pins to stay put under responsive scaling (center vs top-left origin). The pilot sets it.
- **Percentage pin positions are artwork-specific and provisional in the pilot.** The base image is currently a placeholder (backlog: "real hotgraphic base image… pin positions to be tuned when it lands"), so `_left`/`_top` will need re-tuning against final artwork.
- **`_setCompletionOn: "allItems"`** gates completion on opening every pin — deliberate, and it interacts with trickle/PLP.
- **Mobile is a different render.** The narrative fallback uses `strapline` and, if set, `mobileBody` / `mobileInstruction`; test the mobile path separately from desktop.
- **`hide-desktop-image` ≠ `hide-popup-image`.** The former hides the popup image on desktop only; use the latter for all-size suppression of text-only pins.

---

## 8. Worked example

`L01-c-15`, the real authored writing-cycle diagram from Academic Writing / Introductory lesson 1 — five numbered pins around a cycle, all text-only. Component config and the first pin shown in full; the remaining four pins follow the identical shape (numbered `title`, `strapline`, `_left`/`_top`, `hide-popup-image`, placeholder `_graphic.src`), differing only in position and body. Pin bodies truncated for length.

```json
{
  "_id": "L01-c-15",
  "_parentId": "L01-b-10",
  "_type": "component",
  "_component": "hotgraphic",
  "_classes": "",
  "_layout": "full",
  "title": "The writing cycle",
  "displayTitle": "",
  "instruction": "Select each stage to find out what it does.",
  "_setCompletionOn": "allItems",
  "_useNumberedPins": true,
  "_isNarrativeOnMobile": true,
  "_pinOffsetOrigin": true,
  "_isStackedOnMobile": false,
  "_graphic": {
    "src": "course/en/images/L01-writing-cycle.png",
    "alt": "The writing cycle: a circular diagram showing five stages in sequence."
  },
  "_items": [
    {
      "title": "1. Understand the task",
      "body": "<p>The first stage works out what you're being asked to do. Before you write a word, you need to…</p>",
      "strapline": "Understand the task",
      "_left": 50, "_top": 10,
      "_classes": "hide-popup-image",
      "_graphic": { "src": "course/en/images/single-width.png" }
    },
    { "title": "2. Plan",       "strapline": "Plan",       "_left": 85, "_top": 35, "_classes": "hide-popup-image", "_graphic": { "src": "course/en/images/single-width.png" }, "body": "<p>Planning decides what you'll say and in what order…</p>" },
    { "title": "3. Draft",      "strapline": "Draft",      "_left": 70, "_top": 75, "_classes": "hide-popup-image", "_graphic": { "src": "course/en/images/single-width.png" }, "body": "<p>The first draft gets it down, roughly…</p>" },
    { "title": "4. Edit",       "strapline": "Edit",       "_left": 30, "_top": 75, "_classes": "hide-popup-image", "_graphic": { "src": "course/en/images/single-width.png" }, "body": "<p>Editing improves what's there…</p>" },
    { "title": "5. Proofread",  "strapline": "Proofread",  "_left": 15, "_top": 35, "_classes": "hide-popup-image", "_graphic": { "src": "course/en/images/single-width.png" }, "body": "<p>Proofreading catches the final errors…</p>" }
  ],
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

**How it satisfies the spec:**

- **Guardrail 1** — every pin is text-only: `hide-popup-image` plus a placeholder `_graphic.src`. The required-image tax, paid five times.
- **Guardrail 2** — each pin has a meaningful `strapline` for the mobile narrative.
- **Guardrail 3 & 4** — percentage positions arranged around the cycle, with `_pinOffsetOrigin: true` for responsive stability (positions provisional pending final artwork).
- **Guardrail 5 & 6** — `allItems` completion (open every stage) and numbered pins for the sequence, with the number echoed in each `title`.
- **§4 voice** — pin bodies are §15.1 expository prose, one or two plain sentences per stage.
- **§5 tier** — introductory: concise, concrete explanations.
- **§6 accessibility** — meaningful base `alt`; narrative-on-mobile kept on; straplines present.

*(A second instance, `c-130`, exists in the sandbox as Adapt demo scaffold — placeholder pins, not authored content, and not the reference example.)*

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **hotgraphic** component. Register and content-type voice live in the **Voice Specification**; tier register and pin-content depth live in the **Tier Specification**; teaching-move routing (diagram vs text-only stepped reveal) lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1); the base-image artwork task lives in the **project backlog**. This doc points to them; it does not restate them.

---

*End of hotgraphic authoring spec — v0.1.*
