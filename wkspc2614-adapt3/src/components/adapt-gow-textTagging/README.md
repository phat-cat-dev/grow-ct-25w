# adapt-gow-textTagging

An interactive text-tagging / annotation question: learners select a category
from a palette, then click spans of a passage to tag them with it. Scored
against a per-span correct category. Supports multiple passages, including
read-only "contrast" passages with no taggable spans.

Behaviour ported from pw02's `src/shared/js/activities/text-tagging.js`
(a bespoke `ActivityEngine`-based prototype, not an Adapt component). Data
model ported from congen11's `schemas/activities/text-tagging.schema.json`.
No `.njk` renderer existed for text-tagging in congen11 to cross-check against.

This is a **question component**, extending Adapt's `QuestionView`/
`QuestionModel`, so it participates in standard completion, scoring,
assessment and SCORM interaction tracking - the source's `scoring` fields
(`pass_threshold`, `max_attempts`, `feedback_timing`, `show_score`,
`score_label`), which the prototype JS never actually read, map onto that
native API instead.

## Source mapping

| This plugin | Source |
|---|---|
| Interaction behaviour (palette/span click, toggle, counter) | pw02 `src/shared/js/activities/text-tagging.js` |
| Interaction markup/CSS | pw02 `src/shared/css/activities/text-tagging.css` |
| Data model (`_tagCategories`, `_passages`, `_taggableSpans`, scoring) | congen11 `schemas/activities/text-tagging.schema.json` |

## Properties

| Property | Type | Required | Notes |
|---|---|---|---|
| `body` | HTML string | No | |
| `instruction` | HTML string | Yes | ~60 words or fewer. |
| `_tagMode` | enum: `single\|multi` | No (default `multi`) | `multi` requires every scorable span tagged to submit; `single` requires at least one. |
| `_tagCategories` | array, 2-6 items | Yes | Each: `_id` (pattern `^[a-z][a-z0-9_-]*$`, required), `label` (required), `description` (optional, rendered as a palette button tooltip). |
| `_passages` | array, 1-3 items | Yes | Each: `_passageId` (required), `label` (required), `text` (plain, required, ~200 words or fewer), `_taggableSpans` (optional array). |
| `_passages[]._taggableSpans` | array | No | Each: `text` (required, must appear verbatim once in the passage), `_tagId` (required, must match a `_tagCategories[]._id`), `feedback` (optional, shown on marking). |
| `_attempts`, `_canShowFeedback`, `_canShowMarking`, `_shouldDisplayAttempts`, `_recordInteraction` | standard question props | No | Standard Adapt question-component properties. |
| `_scoreLabel` | plain string | No (default `"Tags identified"`) | Ported from congen11's default (`"Your score"`); the real fixture overrode it, kept as the new default here. |
| `_showScore` | boolean | No (default `true`) | |
| `_feedback.correct` / `_feedback._incorrect` / `_feedback._partlyCorrect` | plain strings | No | Default messages provided. |

A passage with **no** `_taggableSpans` renders as a plain, non-interactive
"contrast passage" - the pattern congen11's schema documented but pw02 never
implemented (pw02 only ever rendered a single tagged passage).

## Model (`TextTaggingModel.js`)

- `_buildSegments()` resolves each passage's `text` + `_taggableSpans` into an
  ordered segment array (`_segments`): locate every span's position with
  `text.indexOf`, sort by document order, then scan with a cursor, splitting
  into `{ text, _isSpan: false }` (plain) and `{ text, _isSpan: true, _spanId,
  _tagId, feedback }` (taggable) segments. Spans not found in the text, or
  that overlap an earlier match, are **skipped with a console warning**
  rather than corrupting the render.
- `_buildAllSpans()` flattens every taggable span across every passage, in
  document order, into `_allSpans` - the scoring unit - and initialises
  `_userAnswer` to an array of `-1` (untagged) the same length, unless one
  already exists at the right length (revisit case).
- `_userAnswer` is a **compact array of category indices** (`-1` = untagged),
  not a DOM-attribute/object map - this matters given pw02's documented 48KB
  SCORM `cmi.suspend_data` ceiling.
- `setSpanTag(spanId, categoryIndex)` / `getSpanTag(spanId)` are the view's
  only touchpoints into the model during interaction.
- `isCorrect()` requires every scorable span to match its `_tagId`
  (`_isCorrect` is all-or-nothing); `_isPartlyCorrect` is exposed separately
  (some but not all correct) and `setScore()` uses the raw correct-span count.
- `canSubmit()` branches on `_tagMode` (see Properties table above).
- `getResponse()` / `getResponseType()` / `getInteractionObject()` implement
  the standard SCORM interaction contract (`type: 'matching'`, spans as
  `source`, categories as `target`).

## View (`TextTaggingView.js`)

Ported interaction model (see pw02's `TextTagging.init` /
`handlePaletteClick` / `handleSpanClick` / `applyTag` / `removeTag` /
`updateCounter`), adapted onto Adapt's `QuestionView` lifecycle instead of
pw02's bespoke `ActivityEngine` + `ActivityStateManager`:

- Two-step interaction: click a palette button to select a category
  (radio-like - clicking the already-active button deselects it), then click
  an untagged span to apply it.
- Clicking an **already-tagged** span always clears its tag, regardless of
  whether a category is currently selected.
- Clicking an untagged span with **no** category selected is a no-op.
- Keyboard equivalent: spans are `tabindex="0"`/`role="button"`, Enter/Space
  trigger the same handler as a click.
- Live `N / M tagged` counter with 3-state styling (none/partial/all).
- `resetQuestion()`, `restoreUserAnswer()` (re-applies tags from
  `_userAnswer` on revisit, and shows marking + disables the question if
  already submitted), `disableQuestion()`/`enableQuestion()`,
  `showMarking()`/`hideMarking()` wired to Adapt's standard question
  lifecycle - replacing pw02's manual `getState()`/`restoreState()` +
  `ActivityStateManager`.

### Adapt API fidelity note

No live Adapt framework install was available in this environment to verify
against. The `QuestionView`/`QuestionModel` method names used here
(`resetQuestion`, `restoreUserAnswer`, `disableQuestion`, `enableQuestion`,
`showMarking`, `hideMarking`, `canSubmit`, `storeUserAnswer`,
`resetUserAnswer`, `getResponseType`, `getResponse`, `getInteractionObject`)
follow the common pattern used by official question components such as
`adapt-contrib-matching`. **Verify these against the exact Adapt framework
version installed** before shipping, since method signatures have shifted
slightly between major versions.

## Bugs fixed, not ported

All ported from pw02's `text-tagging.js`/`.css`, fixed here rather than
carried forward:

1. **Category id vocabulary mismatch.** pw02's content data used underscore
   ids (`signal_phrase`, `formal_vocabulary`) while its palette buttons used
   hyphenated `data-tag` attributes (`signal-phrase`, `formal-vocabulary`) -
   breaking scoring for half the categories as shipped. This port uses a
   single `_id` (pattern-validated) everywhere: schema, palette, scoring.
2. **`activeCategory` was module-level singleton state** - two text-tagging
   activities on one page would interfere with each other's selection. Now
   `this._activeCategoryIndex`, a per-instance property.
3. **Hardcoded category label map** inside pw02's `showFeedback`. This port
   always derives labels from `_tagCategories`.
4. **Hardcoded per-category CSS colours for 4 specific ids.** This port uses
   an index-based 6-slot palette (`--tag-0` .. `--tag-5`, matching the
   schema's `_tagCategories` max of 6), applied to both palette buttons and
   tagged spans, so any author-chosen `_id` gets a working colour. The
   semantic `--{_id}` class is still added alongside it for authors who want
   to target one category specifically in custom CSS.
5. **Unescaped, first-occurrence-only `String.replace`** for locating span
   text in the passage (`buildTaggedPassage`) - fragile, order-dependent, and
   silently wrong when one span's text is a substring of another's. Replaced
   with the ordered, non-overlapping cursor-based scan in
   `TextTaggingModel._resolvePassageSegments()`, rendered via Handlebars
   `{{#each}}` (also removing the `innerHTML` XSS surface pw02's DOM-string
   approach had).
6. **Applied-tag label appended as a child `<span>`**, which contaminated
   `span.textContent` - read elsewhere by pw02's feedback-truncation logic.
   This port renders the label via a `data-applied-label` attribute + CSS
   `::after { content: attr(data-applied-label) }` (see
   `less/textTagging.less`), so it never touches the span's text content.
7. **Correct/incorrect marking classes scoped only to `.lap`** (pw02's own
   page-body wrapper), never to `.modal`/`.popup` - marking never rendered
   when the activity was shown inside a modal. This port scopes marking
   rules under both the page body and `.modal`/`.popup`.
8. **`.activity__summary-feedback` not initially `hidden`**, causing a
   spuriously-true `feedbackShown` flag on load. Not applicable here - Adapt's
   `QuestionView` owns feedback visibility state natively.

## Adapt v5 (AMD) equivalent

```javascript
define([
  'core/js/adapt',
  'core/js/models/questionModel',
  'core/js/views/questionView'
], function(Adapt, QuestionModel, QuestionView) {

  var TextTaggingModel = QuestionModel.extend({

    init: function() {
      QuestionModel.prototype.init.apply(this, arguments);
      this._buildSegments();
      this._buildAllSpans();
      this.setupRandomisation();
    },

    setupRandomisation: function() {},

    // ... _buildSegments / _resolvePassageSegments / _buildAllSpans /
    // setSpanTag / getSpanTag / isCorrect / setScore / canSubmit /
    // storeUserAnswer / resetUserAnswer / getResponseType / getResponse /
    // getInteractionObject: same bodies as TextTaggingModel.js, written as
    // object-literal methods instead of class methods.

  });

  var TextTaggingView = QuestionView.extend({

    events: function() {
      return {
        'click .js-text-tagging-tag-btn': 'onPaletteClick',
        'click .js-text-tagging-tag-target': 'onSpanClick',
        'keydown .js-text-tagging-tag-target': 'onSpanKeydown'
      };
    },

    initialize: function() {
      QuestionView.prototype.initialize.apply(this, arguments);
      this._activeCategoryIndex = -1;
    }

    // ... remaining methods: same bodies as TextTaggingView.js, written as
    // object-literal methods instead of class methods.

  });

  Adapt.register('textTagging', {
    model: TextTaggingModel,
    view: TextTaggingView
  });

  return TextTaggingView;

});
```
