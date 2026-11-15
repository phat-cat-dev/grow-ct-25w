# ab-hotgraphic — Authoring Spec

**Version:** 0.1
**Status:** draft
**Verified against:** `src/components/adapt-ab-hotgraphic/properties.schema`, `js/HotgraphicView.js`, `js/HotgraphicModel.js`, `js/hotgraphicLogic.js`.
**Grounded in:** `understanding-learning-assessment-feedback-introductory-W-OPEN-c-20` — the learning/assessment/feedback cycle diagram in the ULAF introductory course (`courses/understanding-learning-assessment-feedback-introductory`), the component's first consumer.
**Relationship to other documents:** registered as `palette/ab-hotgraphic` in `design-kb/design-kb.palette.json` and as a realisation of `activity-patterns/explore-model` in `design-kb/design-kb.activity-patterns.json`; references the Voice Specification and the Tier Specification; restates none. See also `docs/authoring/component-specs/hotgraphic.md` for the stock component this one does not replace outright (§1).

---

## 1. Purpose & when to reach for it

ab-hotgraphic inlines a real, authored SVG diagram into the page (fetched as text, parsed, and mounted live — never an `<img>`) and resolves each item's `_hotspot` config to a node inside it. Because the SVG is in the document, its own shapes get real CSS: hover, focus-visible, the page's `--ab-*` custom properties, transitions. The stock `hotgraphic` component renders its base image through an `<img>`, which is an opaque replaced element — nothing inside an SVG `src` is reachable by CSS or by a nested interactive element.

Component-specific "reach for it / don't":

- **Reach for ab-hotgraphic** when the diagram's own shapes need to respond to interaction (hover/focus paint, a themed accent on the active region) or when a new diagram should cost a *theme-level token block*, not new component code — see §2's `_diagram`/`_hotspot` shape and the paired `--ab-hotgraphic-wedge-*` tokens in `src/extensions/adapt-ab-theme/less/ab-hotgraphic.less`.
- **Reach for stock `hotgraphic` instead** when the base artwork is a flat raster image (a photo, a scan, a screenshot) with pins positioned over it — there is no SVG to inline, and hotgraphic's pin/popup machinery is the better fit. ab-hotgraphic has no pin-position (`_left`/`_top`) concept at all; hotspot position comes entirely from where the shape already is in the SVG.
- **Don't author a diagram with no `data-ab-hotspot`/`id` on its shapes.** Resolution (§2, §7) depends on the SVG carrying stable hooks; a diagram authored without them cannot be bound to `_items` at all.
- **Don't overload a single diagram with many small regions.** The container-query swap to the accessible list (§6) is the escape hatch for narrow viewports, but a diagram crowded with hotspots is still a usability problem at any width — reconsider whether one diagram should carry that many points.

---

## 2. The annotated JSON shape

**[LB]** marks a load-bearing field.

```jsonc
{
  "_component": "ab-hotgraphic",      // standard component value
  "_layout": "full",

  "title": "Signpost",                 // internal / tracking
  "displayTitle": "What's ahead",
  "instruction": "Select each part of the cycle to find out what the course covers.", // §15.4

  "_setCompletionOn": "allItems",      // [LB] "allItems" (default) = every non-decorative hotspot must be visited. "inview" = just scrolled into view. §7

  "_diagram": {                        // [LB] the inlined SVG
    "src": "course/en/images/ulaf-cycle.svg",   // [LB] relative path under "course/" — enforced at load time, not just schema-level
    "title": "Learning, assessment and feedback cycle", // [LB] accessible label for the narrow-band fallback list (aria-label on the <ol>)
    "_slug": ""                        // advanced; overrides the generated ab-hotgraphic--<slug> / ab-hotgraphic__svg--<slug> class hooks. Defaults to the filename without ".svg"
  },

  "_items": [                          // [LB] one object per hotspot, in the SVG's own document order (§3)
    {
      "_id": "learning",               // stable id, e.g. for analytics — distinct from _hotspot._id below
      "title": "Learning",             // [LB] popup/inlineReveal heading AND the accessible name composed for the control
      "body": "<p>Learning at university is not the same as at school…</p>", // teaching text; HTML allowed. Not read for _action: "none"
      "_hotspot": {                    // [LB] the binding into the SVG
        "_id": "learning",             // [LB] matches a data-ab-hotspot attribute or element id in the SVG
        "_selector": "",               // advanced; an explicit CSS selector, tried BEFORE the _id-based fallbacks — must match exactly one node
        "_action": "popup"             // [LB] "popup" | "inlineReveal" | "none". §3
      }
    }
    // …one object per hotspot
  ]
}
```

No per-item position, image, or strapline field exists — ab-hotgraphic has none of hotgraphic's required-popup-image tax (`hotgraphic.md` §3 guardrail 1). An item's only required fields are `title` and `_hotspot._action`; `body` is optional (and unused for `_action: "none"`).

---

## 3. Authoring guardrails (hard rules)

1. **Every `_hotspot` must resolve to exactly one node.** Resolution tries, in order: `_selector` (if authored) → `[data-ab-hotspot="<_id>"]` → `#<_id>`. The first candidate to match exactly one node wins; zero or multiple matches on a given selector moves to the next candidate, but zero or multiple matches across *all* candidates is a hard authoring error — logged via `logging.error` naming the component id, the hotspot id, and every selector tried (`hotgraphicLogic.resolveHotspotSelector`). This is silent to the learner (that hotspot is simply never decorated), so check the console during authoring.
2. **`_diagram.src` must be a relative path under `"course/"`.** `HotgraphicView.loadDiagram()` throws before fetching if it isn't — this is checked at load time, not only documented in the schema's `help` text.
3. **SVG document order should match `_items` order.** The view checks this on every render (`checkDocumentOrder`) and `logging.warn`s on mismatch — a warning only, since fixing it means re-authoring the SVG, not the JSON. A mismatch means the tab order will not match the reading order a sighted user infers from the diagram's layout.
4. **`_action: "none"` hotspots are painted but never focusable.** They get the full class vocabulary (`is-hotspot-<id>`, `is-visited`, etc.) but no `role="button"`, `tabindex`, or click/keydown binding, and `body` is never read for them. Use this for a decorative region of the diagram that still needs to visually track visited state (e.g. a context shape) without being an interactive stop. Decorative hotspots are also excluded from the completion denominator (§5).
5. **Choose completion deliberately.** `_setCompletionOn: "allItems"` (the default and the pilot's setting) requires every non-`"none"` hotspot visited; the denominator is `isAllRequiredVisited`, which excludes decorative hotspots so they can never block completion. Switch to `"inview"` only if visiting every hotspot shouldn't be mandatory.
6. **A diagram's `<title>`/`<desc>` need their own `id` attributes, authored in the SVG.** `decorateRoot()` reads `titleEl.id`/`descEl.id` directly to set `aria-labelledby`/`aria-describedby` on the root — it does not assign ids itself. Any plain id works (e.g. `id="title"`); it gets namespaced like every other id (§7).

---

## 4. Voice rules (reference — not restated here)

ab-hotgraphic is presentation, not assessment — there is no feedback to author.

| Field | Content type | Voice Spec |
|---|---|---|
| `_items[].body` | Short expository teaching text per hotspot | §15.1 |
| `instruction` | Activity instruction | §15.4 |
| `_items[].title` | Concise label, doubles as popup/reveal heading | §13 (register) |
| `_diagram.title` | Accessible label for the diagram as a whole | §14 |

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

ab-hotgraphic carries no assessment dimension, so the tier does not change its mechanics — it changes the depth of each hotspot's `body`. Introductory hotspots are concise and concrete (the ULAF pilot: one short paragraph per part of the cycle); higher tiers carry denser, more analytical annotation. Register tracks the pathway's **§16** band. The Tier Spec's §7 (assessment) does not apply here.

---

## 6. Accessibility requirements

- **The SVG root is `role="group"`, never `role="img"`.** `role="img"` would prune every descendant — including the hotspot controls — from the accessibility tree. `decorateRoot()` sets `role="group"`, `focusable="false"`, and `aria-labelledby`/`aria-describedby` from the SVG's own `<title>`/`<desc>` (guardrail 6), and strips any authored `aria-label` on the root.
- **Per-hotspot accessible names are composed fresh on every state change**, never prepended — `composeHotspotLabel` builds `"<visited-word>. <title>"` from scratch each call, specifically to avoid the stacking-announcement bug in `adapt-contrib-hotgraphic`'s `hotgraphicView.js` (which prepends into `el.innerHTML` on every change, producing "Visited. Visited. Visited." on repeat fires).
- **Keyboard: hotspot controls are `role="button"` + `tabindex="0"`, with Enter/Space bound explicitly.** An `<a>` without `href`, or a bare `<g>`/`<path>`, is not natively focusable or activatable — the view removes any authored `href`/`xlink:href`, adds `tabindex="0"`, and binds both `click` and `keydown` (Space is `preventDefault`-ed to stop it scrolling the page).
- **Focus is drawn as both `outline` and `stroke`.** The component's own `:focus-visible` rule (`ab-hotgraphic.less`) draws a geometric dashed stroke on the wedge alongside the themed outline, because `outline` alone can vanish in Windows high-contrast/forced-colors modes. Never remove the stroke fallback in a theme override.
- **Visited state must not rely on colour alone.** The paint change on `.is-visited`/hover is not itself sufficient for 1.4.1 (Use of Colour) — a diagram's theme-level styling should add a non-colour cue (e.g. an icon or glyph toggled by `.is-visited`) if the asset doesn't already carry one in its geometry.
- **Narrow-width fallback is a real `<ol>` of native buttons, not a visually-hidden duplicate.** Below `@ab-cq-wide` the SVG is hidden and the list shown instead (§7) — it is the *only* rendering at that width, not an always-present parallel list, so there is exactly one tab stop per hotspot at any given width.
- **Reduced motion is gated on both signals.** The `.wedge` fill transition is disabled under both `html.is-prefers-reduced-motion` (the core-detected class) and the raw `@media (prefers-reduced-motion: reduce)` query, so it's correct whether or not core's detector has run yet.

---

## 7. Known gotchas & findings

- **Two instances of the same diagram on one page do not collide.** Every `[id]` in the inlined SVG — including `<marker>` ids and the `<title>`/`<desc>` ids from guardrail 6 — is prefixed with the component's own `_id` at mount time, and every reference to it (`fill`, `stroke`, `marker-end`, `clip-path`, `mask`, `filter`, `href`, `aria-labelledby`, `aria-describedby`, `for`) is rewritten to match. Author plain, readable ids in the source SVG (`arrowhead-learning`, `title`, `desc`); there is no need to hand-prefix anything — the runtime namespacing already solves the collision problem regardless of what the asset's own ids are.
- **The mount point is deliberately childless in the JSX.** `.ab-hotgraphic__canvas` renders with no children; the view moves the fetched, decorated SVG into it imperatively and only touches the DOM when it isn't already mounted (`mount.firstElementChild === this._svgEl`). This is what lets the live SVG, its generated classes, and any focus currently inside it survive a React re-render triggered by an unrelated model change or `device:changed` — `dangerouslySetInnerHTML` would blow the subtree away on every change.
- **`setReadyStatus()` runs in a `finally`, deliberately.** If the SVG fails to load or parse, the catch block adds `.is-diagram-error` (which the LESS forces the accessible list to show at every width, overriding the responsive swap) and logs the error — but `setReadyStatus()` still has to run, or page-ready hangs forever. Never move it out of the `finally`.
- **`wedge`/`label`/`label-sub` are the only classes wired to theme tokens.** The asset-authoring contract (`ab-hotgraphic.less`) paints `.wedge` fill and `.label`/`.label-sub` ink from paired `--ab-hotgraphic-wedge-fill`/`-fill-hover`/`-ink` custom properties, overridden per diagram in `src/extensions/adapt-ab-theme/less/ab-hotgraphic.less` under `.ab-hotgraphic--<slug> .is-hotspot-<id>`. A diagram's `rule` (boundary/radii) and `flow` (directional arrow + its own `<marker>`) elements deliberately keep whatever stroke/fill they were authored with — `<marker>` content cannot reliably inherit colour from the element that references it without the poorly-supported `context-stroke`, so each hotspot's marker just hardcodes its own arrowhead colour, same as the original un-merged assets did.
- **`_hotspot._action: "none"` hotspots are excluded from completion, not just from focus** (guardrail 4/5) — a diagram can carry purely decorative, context-only shapes without ever blocking `areAllItemsCompleted()`.
- **The SVG is project-authored build input, not a security boundary**, but it does get a DOM-level hygiene pass on load (`sanitiseSvg`): `<script>`/`<foreignObject>` removed, every `on*` attribute stripped, and any `href`/`xlink:href` that isn't a bare `#fragment` removed. This catches design-tool accidents (an artist leaving a placeholder `https://example.com/...` href on a shape, as the original ULAF wedges did) — it is not a substitute for reviewing what's committed.

---

## 8. Worked example

`understanding-learning-assessment-feedback-introductory-W-OPEN-c-20`, the real authored learning/assessment/feedback cycle — three hotspots, all popups, replacing the course's previous stock `hotgraphic` instance at the same position.

```json
{
  "_id": "understanding-learning-assessment-feedback-introductory-W-OPEN-c-20",
  "_parentId": "understanding-learning-assessment-feedback-introductory-W-OPEN-b-20",
  "_type": "component",
  "_component": "ab-hotgraphic",
  "_classes": "",
  "_layout": "full",
  "title": "Signpost",
  "displayTitle": "What's ahead",
  "body": "<p>Learning, assessment and feedback are not three separate things. They form a cycle…</p>",
  "instruction": "Select each part of the cycle to find out what the course covers.",
  "_setCompletionOn": "allItems",
  "_diagram": {
    "src": "course/en/images/ulaf-cycle.svg",
    "title": "Learning, assessment and feedback cycle"
  },
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true },
  "_items": [
    {
      "_id": "learning",
      "title": "Learning",
      "body": "<p>Learning at university is not the same as at school…</p>",
      "_hotspot": { "_id": "learning", "_action": "popup" }
    },
    {
      "_id": "assessment",
      "title": "Assessment",
      "body": "<p>Assessment is how your learning is tested…</p>",
      "_hotspot": { "_id": "assessment", "_action": "popup" }
    },
    {
      "_id": "feedback",
      "title": "Feedback",
      "body": "<p>Feedback is what you get back on your work…</p>",
      "_hotspot": { "_id": "feedback", "_action": "popup" }
    }
  ]
}
```

The diagram itself (`course/en/images/ulaf-cycle.svg`) authors three `<g data-ab-hotspot="learning|assessment|feedback">` groups, in that document order, each containing a `.wedge` path, its boundary `rule` lines, a directional `flow` arrow with its own `<marker>`, and `.label`/`.label-sub` text — merged from three originally-separate wedge SVGs sharing one coordinate space, so no path geometry needed transforming, only the `viewBox`.

**How it satisfies the spec:**

- **Guardrail 1** — all three `_hotspot._id` values (`learning`, `assessment`, `feedback`) match a `data-ab-hotspot` attribute in the SVG exactly once each.
- **Guardrail 3** — the SVG's `<g>` order is learning, assessment, feedback, matching `_items` order.
- **Guardrail 5** — `allItems` completion; all three hotspots are `_action: "popup"`, so all three count toward the denominator.
- **Guardrail 6** — the SVG authors `<title id="title">`/`<desc id="desc">` at its root.
- **§4 voice** — hotspot bodies are §15.1 expository prose, one short paragraph per part.
- **§5 tier** — introductory: concise, concrete explanations, directly adapted from the prior stock-hotgraphic copy at this position.
- **§6 accessibility** — `role="group"` root with `<title>`/`<desc>`-derived labelling; keyboard-operable controls; narrow-width list fallback.
- **§7 theming** — `.ab-hotgraphic--ulaf-cycle` picks up its three hotspots' fill/ink from `src/extensions/adapt-ab-theme/less/ab-hotgraphic.less`, not from anything authored in the JSON above.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **ab-hotgraphic** component, and the authoring contract a new diagram's SVG must follow to bind into it. Register and content-type voice live in the **Voice Specification**; tier register and hotspot-content depth live in the **Tier Specification**; teaching-move routing (when a diagram is the right vehicle at all) lives in **`design-kb/design-kb.activity-patterns.json`** (`activity-patterns/explore-model`); the component-vs-component choice against stock `hotgraphic` is in §1 above and in `docs/authoring/component-specs/hotgraphic.md`, not restated here; per-diagram colour tokens live in `src/extensions/adapt-ab-theme/less/ab-hotgraphic.less`, not in this doc.

---

*End of ab-hotgraphic authoring spec — v0.1.*
