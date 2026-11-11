# hotspot (adapt-abbott-hotspot) — Authoring Spec

**Version:** 0.1
**Status:** draft — ships with the component (built 20 September 2026). No shipped lesson instance yet; the worked examples are **build-verified** (ESLint clean, schema-valid JSON, unit-tested logic module) but there is no authored placement yet.
**Verified against:** `src/components/adapt-abbott-hotspot/properties.schema` — **our own schema** (custom component; extensionless, matching this repo's actual convention for custom components, not the `.schema.json` naming used in some upstream/contrib references).
**Relationship to other documents:** this component's design and build rationale was set out directly to the builder as a six-point ruling set on 20 September 2026 (region/interaction model, correctness, feedback, accessibility, small-region/mobile behaviour, build scope). No prior `open-decisions.md` entry exists for this component — this spec is the first design record for it, and the design points below are named descriptively rather than by a numeric id, since none has been assigned upstream. This spec references the Voice Specification, the Tier Specification, and `design-kb/design-kb.activity-patterns.json` / `design-kb/design-kb.palette.json` (component-mapping-artefact.md is SUPERSEDED, MA-1); it restates none of them.

---

## 1. Purpose & when to reach for it

A **question component where the learner selects one or more labelled rectangular regions on an authored image** — "click the part of the diagram that is X." Built on the same base as `mcq` (`ItemsQuestionModel`): attempts, marking, feedback selection, model-answer display and "choice" SCORM interaction recording all come from that base with no override.

Reach for it when:
- The teaching point is genuinely **spatial or structural** — identifying a part of a labelled diagram, image, screenshot, or document layout — and text-only options (an mcq) would lose that spatial reasoning.
- A single authored image can be marked out into 2 to 8 non-overlapping rectangular regions: the correct one or ones, plus two to five decoys.

**Do not reach for it when:**

| If you need... | Use instead | Boundary |
|---|---|---|
| A closed set of text options with no spatial component | `mcq` | Hotspot's only reason to exist over mcq is the image geometry; if the options are equally well expressed as text, mcq is simpler to author and has no image-authoring burden |
| Regions on more than one image, or a sequence of images | Not supported | Hotspot is single-image only; see §7 known limits |
| A shape other than a rectangle (a circle, a polygon, a diagonal) | Not supported | `shape` accepts only `"rect"`; see §7 |
| Free-text identification ("what is this part called?") | `textInput` | Hotspot is selection, not recall/construction |

**First home:** not yet placed in an authored pathway. The activity-pattern routing (`activity-patterns/label-a-structure`, `activity-patterns/spot-the-error`) is recorded in `design-kb/design-kb.activity-patterns.json`; see that store for which teaching moves route here.

---

## 2. The annotated JSON shape

`_component` is `"hotspot"` (lowercase). **[LB]** = load-bearing.

```jsonc
{
  "_id": "c-20",
  "_parentId": "b-20",
  "_type": "component",
  "_component": "hotspot",
  "_layout": "full",

  "title": "Hotspot",                       // internal
  "displayTitle": "Hotspot",                 // learner-facing heading
  "body": "Select the region of the diagram that shows the topic sentence.", // [LB] the question stem
  "instruction": "Choose {{#if _isRadio}}one area{{else}}one or more areas{{/if}} on the image then select Submit.", // default; _isRadio is set automatically from _selectable, not authored
  "ariaQuestion": "",                        // as mcq: populate whenever body carries HTML/framing; read in place of displayTitle/body/instruction when focus lands on a region

  "_graphic": {                              // [LB] required — a single top-level image (unlike gmcq's per-item _graphic)
    "large": "course/en/images/hotspot-example-large.jpg",   // [LB]
    "small": "course/en/images/hotspot-example-small.jpg",   // [LB]
    "alt": "A single paragraph of academic writing, annotated with four labelled regions.", // [LB] REQUIRED — read before the regions
    "longdescription": "The paragraph runs across four lines. The first line...", // [LB] REQUIRED (stricter than adapt-contrib-graphic, where this is optional) — see §6
    "attribution": ""
  },

  "_items": [                                // [LB] 2 to 8 regions — see hotspotLogic.js validateRegions
    {
      "text": "the first line",              // [LB] this region's OWN accessible-name text, e.g. "the first line" — becomes "Area 1 of 3: the first line"
      "shape": "rect",                       // [LB] only permitted value
      "left": 5, "top": 8, "width": 40, "height": 15, // [LB] percentages of the image; left+width and top+height each ≤ 100; regions never overlap
      "_shouldBeSelected": true,              // [LB] marks a correct region
      "_isPartlyCorrect": false,
      "feedback": "",                         // per-region feedback — SINGLE-ANSWER QUESTIONS ONLY, same convention as mcq (see §7 gotcha)
      "_score": 0
    }
    // …remaining regions (2 to 8 total)
  ],

  "_selectable": 1,                          // [LB] 1 = radio inputs (single answer); >1 = checkbox inputs
  "_attempts": 2,                            // [LB] defaults to 2 (mcq's schema default is 1) — this component's design fixes attempts at two
  "_shouldDisplayAttempts": false,
  "_isRandom": false,                        // randomises DOM/tab order only, never region position on the image
  "_hasItemScoring": false,
  "_questionWeight": 1,

  "_canShowModelAnswer": true,               // [LB] the model answer outlines and labels the correct region(s)
  "_canShowCorrectness": false,               // [LB] replaces the model-answer toggle when true, same mcq interaction — see mcq.md §7
  "_canShowFeedback": true,
  "_canShowMarking": true,
  "_recordInteraction": true,                // reports a "choice" interaction to cmi.interactions — inherited from ItemsQuestionModel, zero override

  "_feedback": {                             // [LB] question-level feedback for all three outcomes
    "title": "Feedback",
    "correct": "Congratulations, this is the correct feedback.",
    "_incorrect": { "notFinal": "", "final": "This feedback will appear if you answered the question incorrectly." },
    "_partlyCorrect": { "notFinal": "", "final": "This feedback will appear if you answered the question partly correctly." } // only reachable when more than one region is correct
  }

  // "_buttons": {…}  // omit unless overriding course.json global button labels
}
```

Everything in `_buttons` and the global aria strings (`ariaRegion`, `ariaCorrectAnswer(s)`, `ariaUserAnswer(s)`, `areaLabel`, `listModeInstruction`) is inherited from `course.json` `_globals`; leave them out of the component unless a specific override is needed. `_isRadio` and `_isListMode` are both set automatically at runtime (`_isRadio` from `_selectable` by `ItemsQuestionModel.init`; `_isListMode` from the rendered image size by `HotspotModel.setListModeFromImageSize`, called from `HotspotView.onQuestionRendered`) — neither is authored.

---

## 3. Authoring guardrails (hard rules)

1. **2 to 8 regions; the correct one or ones, plus two to five decoys.** Enforced by `hotspotLogic.js`'s `validateRegions` at the unit-test level (see its own test suite); **not currently wired into any build-time or runtime validation** — see §7 gotcha.
2. **Only `shape: "rect"` is supported.** No circles, polygons, or freeform shapes.
3. **Regions never overlap, and each sits wholly within the image (0 to 100 on both axes, `left + width` and `top + height` each ≤ 100).** `validateRegions` checks this; again, not currently wired into any automated build-time gate — check it by eye or with a manual `node` invocation of the module until it is.
4. **Every region needs its own accessible-name text** in `_items[].text` — this is what fills the `{{text}}` slot of the "Area N of M: {{text}}" label, so it must stand alone (e.g. "the first line", not "this one" or "correct").
5. **`_shouldBeSelected` count matches intent**, exactly as mcq: single-answer questions mark exactly one region `true`; several-correct questions mark as many as are actually correct, and `_selectable` should be set so the learner can select at least that many.
6. **Per-region `feedback` is single-answer only**, same convention as mcq (mcq.md §7): only meaningful when `_selectable: 1`. On a several-correct question, put the teaching in `_feedback._incorrect` / `_partlyCorrect` instead.
7. **Regions under 12% width or 8% height produce a geometry warning** (`hotspotLogic.js geometryWarnings`, naming the region) — again unit-tested but not yet wired into any authoring-time check; a small region is still valid, just flagged.
8. **List mode is automatic, not authored.** Do not set `_isListMode` by hand — it is computed from the rendered image's actual pixel size against the authored region percentages (`listModeThreshold`, 44×44 CSS px floor) every time the question renders.
9. **Both `alt` and the long description are required, not optional**, unlike `adapt-contrib-graphic`'s own schema where both are optional. See §6.

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `body` | The question stem | §11.7 (real questions) |
| `instruction` | Activity instruction | §15.4 |
| `_items[].text` | Region label — the region's own accessible-name text, plain and self-contained | §11.6, §12.3 (same distractor-neutrality rule as mcq's `_items[].text`) |
| `_graphic.alt` | Short image description | image alt-text conventions, not a Voice Spec content type |
| `_graphic.longdescription` | Long, structural description of the image's layout | image long-description conventions; written so a screen-reader user can picture the layout before choosing between regions |
| `_feedback.correct` / `_incorrect.*` / `_partlyCorrect.*` | Question-level feedback — confirm-with-reason, never a bare verdict | §15.5 |
| `_items[].feedback` | Per-region feedback (single-answer only) | §15.5 |

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

The component's mechanics do not change by tier. What shifts:

- **Region count and decoy plausibility** — Tier Spec §7's discrimination row governs how close the decoys sit to the correct region(s); introductory decoys are clearly distinguishable, advanced decoys require closer reading of the image.
- **Long description density** — at lower tiers, spell out the image's layout in full; at higher tiers, a learner can be assumed to extract more from the alt text alone, so the long description can be leaner (but never removed — it stays required at every tier, per §6).

---

## 6. Accessibility requirements

This is a contract, not a suggestion — built directly against the accessibility design points ruled for this component.

- **Native inputs, not simulated controls.** Each region is a real `<input type="radio">` (single-answer) or `<input type="checkbox">` (several-answer), inside a `<fieldset>` with a `<legend>` — explicitly not the `div role="radiogroup"` pattern `mcq.jsx` uses (see `adapt-abbott-checklist`'s `checklist.jsx` for the same fieldset/legend precedent this component follows).
- **Accessible name per region** in the form "Area 3 of 6: (2006)" — built at render time from the `areaLabel` global template (default `"Area {{index}} of {{total}}: {{text}}"`) against the region's own `text`.
- **Reading order: question, then alt text, then long description, then the regions.** `templates.header` (title/displayTitle/body/instruction/ariaQuestion) renders before the image; the image (with `alt`) renders before the long-description block; the long-description block renders before the `fieldset`/`legend`/regions. All four are in that DOM order.
- **Both the short alt text and the long description are required**, not optional — `properties.schema` marks `_graphic.alt` and `_graphic.longdescription` both `required: true` with a `"required"` validator, stricter than `adapt-contrib-graphic`'s own (optional) schema for both fields, per Abbott's accessibility ruling that both are required.
- **Arrow-key navigation between regions** comes free from the native radio-group behaviour when `_selectable: 1` (checkbox groups do not have this browser behaviour; several-answer questions navigate by Tab, as native checkbox groups do).
- **Focus outline** — `hotspot-region__input:focus-visible + hotspot-region__label` gets a 3px solid outline in `@hotspot-region-focus` (traced to `@item-color-focus`, the same variable `adapt-abbott-checklist`'s own focus-outline rule traces to), offset 2px.
- **Selection signalled by a thicker outline plus a visible marker, never colour alone (SEL-1).** A selected region's label carries a 4px solid outline (`@hotspot-region-selected`, traced to `@item-color-selected`) — thicker than the 3px focus outline, so "selected" and "focused" read as visibly distinct — AND its answer-icon switches from the unchecked to the checked native radio/checkbox glyph (the same `is-radio`/`is-checkbox` icon-swap `mcq-item` uses). Per SEL-1, this marker is always drawn while answering and never hidden behind the image; the general hover/focus/is-complete reveal rule below does not apply to a selected region's own label. After submission, correctness carries its own, separate tick/cross marks (`hotspot-region__correct-icon`/`incorrect-icon`) — selection and correctness never share one symbol. Both states carry screen-reader text via the region's own accessible name and the global aria strings, so neither depends on seeing a shape or a colour alone.
- **Regions invisible until hover, focus, selection, or after submission** — `hotspot-region__label` sits at `opacity: 0` by default outside list mode, and is set to `opacity: 1` on `:hover`, `:focus`/`:focus-visible` of its input, when the widget carries `is-complete`, or — per SEL-1 — whenever the region's own label carries `is-selected`, regardless of hover/focus/is-complete state.
- **Zoom is never blocked.** No `maximum-scale`/`user-scalable` restriction is introduced anywhere in this component; regions are positioned by percentage (relative units), not fixed pixels, so they scale with the image at any zoom level.
- **List-mode fallback** — see §7 known limits. In list mode the hover/focus-reveal rule above does not apply; region labels are always visible, laid out as a plain stacked list, each with a minimum 44px tap target.

---

## 7. Known gotchas & findings

- **`validateRegions` and `geometryWarnings` are now wired at runtime.** `HotspotModel.checkRegions()` runs both against the authored `_items` once, when the question initialises, logging any finding via `core/js/logging` (errors for `validateRegions`' rule violations, warnings for `geometryWarnings`' small-region findings), naming the component's own id and the offending region; neither blocks. This is a runtime-only check, not a build-time one — an author only sees the finding in the browser console when the course is previewed or played, not at build or package time. See the project backlog's build-time region-check entry for the remaining gap and why runtime-only checking is not enough on its own.
- **`hotspotLogic.js` carries no `mark()` of its own.** Marking at runtime comes entirely from the inherited, unmodified `ItemsQuestionModel.isCorrect`/`isPartlyCorrect`. A separate `mark()` mirroring that same rule existed briefly as a pure, independently-tested function, but was removed: with `HotspotModel` overriding neither `isCorrect` nor `isPartlyCorrect`, marking already had exactly one live code path, and a second, independently-tested mirror of the same rule would have tested code the browser never runs. See `HotspotModel.js`'s own header note and `hotspotLogic.js`'s module header for the reasoning in full.
- **`properties.schema` is extensionless**, not `properties.schema.json` — matching every other custom component in this repo (`adapt-abbott-checklist`, `adapt-abbott-branching`, etc.), despite that filename appearing with a `.json` suffix in some upstream/external references.
- **`_isRadio` and `_isListMode` are both computed, never authored** — see §2.
- **Single top-level `_graphic`, not per-item.** Unlike `gmcq`, which gives each option its own image, hotspot has exactly one image with all regions positioned on it by percentage.
- **List mode is a full layout switch, not a CSS media query.** It is driven by the actual rendered pixel size of the authored image (measured via `imageready()`, the same jQuery plugin `GmcqView`/`GraphicView` use) against the regions' authored percentages — a region can trigger list mode on a narrow viewport that would not trigger it on a wide one, and vice versa depending on how large the source image itself is.

---

## 8. Known limits (design points, not defects)

- **Images must be author-supplied.** There is no in-tool region-drawing UI; region `left`/`top`/`width`/`height` are authored as raw percentages against a specific image, so the author needs the image's real dimensions (or a way to measure percentage placement against it) before authoring regions.
- **Small regions fall back to list mode**, which drops the spatial-reasoning element of the question entirely (the learner picks from a plain list of the same region labels, not the image). A hotspot question authored with several regions under the 44×44px floor at common viewport sizes effectively degrades to an mcq-shaped list on those viewports; if that is unacceptable for a given question, the regions need to be drawn larger, or the image cropped/enlarged, not left to the automatic fallback.
- **Single image, single shape.** No multi-image sequences, no non-rectangular regions.
- **Region-rule violations are only caught at runtime, not at build time.** `checkRegions()` (see §7) only runs when the question initialises in a rendered course — an author who violates the region-count, overlap, geometry, or shape rules gets no warning until the course is previewed or played, and nothing stops a course with invalid regions from being built and packaged. A build-time equivalent is recorded in the project backlog, not built in this sitting.

---

## 9. Worked example

From `example.json` (single-answer, build-verified — schema-valid JSON, no shipped lesson instance yet).

```json
{
  "_id": "c-20",
  "_parentId": "b-20",
  "_type": "component",
  "_component": "hotspot",
  "_layout": "full",
  "title": "Hotspot",
  "displayTitle": "Hotspot",
  "body": "Select the region of the diagram that shows the topic sentence.",
  "instruction": "Choose {{#if _isRadio}}one area{{else}}one or more areas{{/if}} on the image then select Submit.",
  "ariaQuestion": "",
  "_attempts": 2,
  "_shouldDisplayAttempts": false,
  "_isRandom": false,
  "_hasItemScoring": false,
  "_questionWeight": 1,
  "_selectable": 1,
  "_canShowModelAnswer": true,
  "_canShowCorrectness": false,
  "_canShowFeedback": true,
  "_canShowMarking": true,
  "_recordInteraction": true,
  "_graphic": {
    "large": "course/en/images/hotspot-example-large.jpg",
    "small": "course/en/images/hotspot-example-small.jpg",
    "alt": "A single paragraph of academic writing, annotated with four labelled regions.",
    "longdescription": "The paragraph runs across four lines. The first line, in the top-left quarter of the image, is the topic sentence. The following two lines, filling the middle of the image, are supporting detail. The final line, in the bottom-right quarter, is the concluding sentence.",
    "attribution": ""
  },
  "_items": [
    { "text": "the first line", "shape": "rect", "left": 5, "top": 8, "width": 40, "height": 15, "_shouldBeSelected": true, "_isPartlyCorrect": false },
    { "text": "the middle two lines", "shape": "rect", "left": 5, "top": 30, "width": 90, "height": 30, "_shouldBeSelected": false, "feedback": "This is the supporting detail, not the topic sentence.", "_isPartlyCorrect": false },
    { "text": "the final line", "shape": "rect", "left": 55, "top": 70, "width": 40, "height": 15, "_shouldBeSelected": false, "feedback": "This is the concluding sentence, not the topic sentence.", "_isPartlyCorrect": false }
  ],
  "_feedback": {
    "title": "Feedback",
    "correct": "Congratulations, this is the correct feedback.",
    "_incorrect": { "notFinal": "", "final": "This feedback will appear if you answered the question incorrectly." },
    "_partlyCorrect": { "notFinal": "", "final": "This feedback will appear if you answered the question partly correctly." }
  }
}
```

**How it satisfies the spec:**

- **Guardrail 1** — 3 regions (within the 2–8 bound), one correct plus two decoys.
- **Guardrail 4/5** — each region carries its own `text`; exactly one `_shouldBeSelected: true` for this single-answer question.
- **Guardrail 6** — per-region `feedback` is authored on the two decoys, valid because `_selectable: 1`.
- **§6 accessibility / Guardrail 9** — both `_graphic.alt` and `_graphic.longdescription` are populated, satisfying the required-field rule for both; `longdescription` describes the layout structurally (four lines, their screen positions), sufficient to picture the image before choosing a region, and `alt` gives the short description read first.
- **§2** — `_attempts: 2`, matching the ruling.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **hotspot** component. Register and content-type voice live in the **Voice Specification**; tier demand and assessment parity live in the **Tier Specification**; scoring mechanics live in **`scoring-and-summative-model.md`**; teaching-move routing lives in **`design-kb/design-kb.activity-patterns.json`** and **`design-kb/design-kb.palette.json`**; the `_id`/context-slot conventions live in **`portable-unit-and-shell-format.md`**. This doc points to them; it does not restate them.

---

*End of hotspot authoring spec — v0.1.*
