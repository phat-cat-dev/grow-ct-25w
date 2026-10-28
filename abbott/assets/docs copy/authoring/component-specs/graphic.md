# graphic — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec)
**Verified against:** `src/components/adapt-contrib-graphic/properties.schema` (Adapt 5.56.2)
**Grounded in:** `c-105`, `c-120`, `c-205` — Adapt demo scaffold instances (`courses/academic-writing-introductory`). **No authored lesson instance exists yet** (no L0x-prefixed graphic component in the pilot). The worked example below is therefore illustrative of the schema shape, not an authored voice model; treat it with caution until a real instance is built.
**Relationship to other documents:** references the Voice Specification and the Tier Specification; restates none. This is the static-image container; the authoring rules are almost entirely about accessibility, not mechanics.

---

## 1. Purpose & when to reach for it

Routing is decided upstream in **Mapping Artefact Part 4**. Graphic is the **static image container**: the standard component for displaying an image without interaction.

Component-specific "reach for it / don't":

- **Reach for graphic** for any image that stands alone or pairs with a text component: diagrams, charts, photographs, illustrations that the learner views but does not interact with.
- **Reach for graphic** when no stepped reveal, hotspot interaction, or slideshow behaviour is needed.
- **Don't use graphic for interactive image exploration** (hotspots, multiple items) — that's `hotgraphic` or `narrative`.
- **Don't use graphic for video or audio** — that's `media`.

Graphic is a thin component. Its rules are almost entirely about *alt text and accessibility*, not schema mechanics.

---

## 2. The annotated JSON shape

The schema is minimal.

```jsonc
{
  "_id": "c-120",
  "_parentId": "b-110",
  "_type": "component",
  "_component": "graphic",
  "_classes": "",
  "_layout": "full",                      // "full" | "left" | "right"

  "title": "Graphic",                     // internal / tracking
  "displayTitle": "",                     // learner-facing heading; often blank
  "body": "",                             // optional body text above the image
  "instruction": "",                      // rarely used for pure graphic

  "_graphic": {                           // [LB] the image
    "large": "course/en/images/diagram.png",   // desktop image
    "small": "course/en/images/diagram.png",   // mobile image
    "alt": "A diagram showing the five stages of the writing cycle arranged in a circle.", // [LB] meaningful alt text
    "longdescription": "",                // optional extended description displayed below image
    "attribution": "",                    // copyright/attribution line
    "_url": "",                           // optional click-through URL
    "_target": "_blank"                   // link target if _url is set
  },

  "_isScrollable": false,                 // enables horizontal panning for wide images
  "_defaultScrollPercent": 0,             // starting scroll position (0=left, 50=centre, 100=right)

  "_isOptional": false,                   // base component-model field (not in graphic's own schema); if true, doesn't count toward completion — §7

  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": false }
}
```

That is the entire authoring surface. No `_items`, no `_feedback`, no interaction. The work is in the `_graphic` object and the `alt` text.

---

## 3. Authoring guardrails (hard rules)

1. **Every meaningful image must have `alt` text.** If the image conveys information the learner needs, describe that information. For purely decorative images, leave `alt` blank — but in educational content, most images are meaningful.
2. **`alt` text describes what the image shows, not what it is.** "A diagram showing the five stages of the writing cycle" is better than "Writing cycle diagram".
3. **Use `longdescription` for complex images.** Charts, diagrams, and infographics that cannot be adequately described in a short `alt` should have a `longdescription` with full detail; it displays below the image.
4. **Provide `small` and `large` versions.** Both are required by the schema. Use appropriately sized images for mobile and desktop.
5. **`attribution` for licensed images.** If the image requires copyright or source acknowledgement, put it in `attribution`.
6. **`_isOptional: true` for decorative pairings.** When a graphic is purely decorative (e.g., a visual paired with a text component where the text carries all the meaning), set `_isOptional: true` so it doesn't block completion.

---

## 4. Voice rules (reference — not restated here)

Graphic has minimal learner-facing copy.

| Field | Content type | Voice Spec |
|---|---|---|
| `body` | Running prose (if used) | §15.1 |
| `displayTitle` | Heading (if used) | §5 |
| `instruction` | Activity instruction (if used) | §15.4 |
| `_graphic.alt` | Alt text; describe what the image shows | §14 (inclusivity) |
| `_graphic.longdescription` | Extended description | §14 |
| `_graphic.attribution` | Attribution line | §17 (referencing conventions) |

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

Graphic carries no assessment dimension. Tier affects **image complexity and the depth of description**:

- **Introductory:** Images are concrete and clearly labelled; alt text is straightforward.
- **Advanced:** Images may be more complex (e.g., multi-variable charts); `longdescription` may be needed.

Register for any `body` or `displayTitle` follows **Voice Spec §16**. This doc does not restate those numbers.

---

## 6. Accessibility requirements

- **`alt` text is the primary accessibility feature.** Screen readers announce it. Ensure it conveys the same information a sighted learner would gain.
- **`longdescription`** renders below the image and is visible to all users; use for complex diagrams.
- **`_isScrollable`** — when enabled, the component gets a scrollbar aria label. Ensure `alt` still describes the full image; don't rely solely on scrolling.
- **Never rely on colour alone.** If an image uses colour to distinguish elements, ensure shapes, labels, or patterns also distinguish them.
- **Global `scrollAriaLabel`** inherits from `course.json` `_globals`; leave default unless overriding.

---

## 7. Known gotchas & findings

- **Completes on scroll-in.** The component completes as soon as it scrolls into view; there is no "must view" mechanic. `_isCompletionIndicatorEnabled` is typically `false`.
- **`_isOptional`** — decorative graphics paired with text should be marked optional so they don't block progress. Note it's a base component-model field (inherited via the schema's `$ref`), not defined in graphic's own `properties.schema` — the same inherited field textInput uses for reflective prompts.
- **`_url` and `_target`** — if set, the image becomes a clickable link. Use sparingly; unexpected click behaviour can confuse learners.
- **Demo scaffold only in pilot.** All instances (`c-105`, `c-120`, etc.) are Adapt demo content with blank `alt` text. The first real authored graphic must populate `alt` properly.

---

## 8. Worked example

**Note:** No authored lesson instance exists yet. The example below is from the Adapt demo scaffold (`c-120`), reproduced to show schema shape. It is **ILLUSTRATIVE**, not a voice model.

```json
{
  "_id": "c-120",
  "_parentId": "b-110",
  "_type": "component",
  "_component": "graphic",
  "_classes": "",
  "_layout": "full",
  "title": "Graphic",
  "displayTitle": "Graphic",
  "body": "This is the <b>Graphic</b> component body. You can introduce your graphic or you may just want to let the graphics do the talking.<br><br>Component can either be single or spanned.",
  "instruction": "",
  "_graphic": {
    "alt": "",
    "longdescription": "",
    "large": "course/en/images/full-width.png",
    "small": "course/en/images/full-width.png",
    "attribution": "",
    "_url": "",
    "_target": ""
  },
  "_isScrollable": false,
  "_defaultScrollPercent": 0,
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": false }
}
```

**Gaps vs programme spec (demo scaffold, not authored):**

- `alt` text is blank — violates §6 accessibility.
- `body` text is generic demo content, not programme voice.
- The first authored graphic must populate `alt` and follow Voice Spec for any `body` text.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **graphic** component, which is minimal. Accessibility and alt-text conventions are grounded in **Voice Spec §14**; tier register lives in the **Tier Specification** and **§16**; teaching-move routing lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of graphic authoring spec — v0.1 (illustrative example — no authored instance yet).*
