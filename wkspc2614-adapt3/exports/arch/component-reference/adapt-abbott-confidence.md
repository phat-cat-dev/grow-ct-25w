# Confidence Check  (`confidence`)

- plugin: `adapt-abbott-confidence` (component)
- targetAttribute: `_confidence`
- framework: `>=5.19.1`
- used in this course: yes

## Authorable properties

| field | type | req | default | title / help |
|---|---|---|---|---|
| `ariaRegion` | string | yes | "Confidence check. Rate how confident yo |   |
| `ariaScaleName` | string | yes | "confidence" |  Name announced for the rating scale. |
| `ariaItemRated` | string | yes | "{{{item}}}: rated {{{label}}}, {{{value |  Announced when a rating is selected. Placeholders: item, label, value, max. |
| `_supportedLayout` | string enum: full-width, half-width, both | yes | "full-width" |   |
| `_mode` | string enum: pre, post | yes | "pre" | Mode "pre" (before the lesson) or "post" (after). The PRE carries _items and _scale; the POST carries _feedback and _hasSummativeFollowing and inherits the pre's items/scale by group id. |
| `_selfAssessmentGroupId` | string | yes | "" | Self-assessment group id Identical on the pre and post of a pair (lesson-derived). The post finds its pre by matching this; state, items and scale key off it. |
| `instruction` | string |  | "Rate how confident you feel about each  |   |
| `ariaQuestion` | string |  | "" |  Screen-reader text; if blank, uses title + body + instruction. |
| `_items` | array |  |  | Items (authored on the PRE) Each item is a lesson learning outcome phrased as a can-do confidence statement (SA-2). Authored on the PRE only; the post leaves this empty and inherits by group id. |
| `_id` | string | yes | "" |  Stable unique id within the group. Keys the stored rating and any per-item feedback override. Stable across pre/post. |
| `text` | string | yes | "" |  The confidence statement, e.g. "...identify the steer in an essay question." |
| `_scale` | object |  |  | Confidence scale (authored on the PRE) Shared by every item. Authored on the PRE; inherited by the post so pre and post are identical. |
| `_labels` | array |  | ["Not at all confident","Slightly confid | Scale labels (low to high) One label per point, low to high. Five per SA-3. Stored value is the 1-based index. |
| `_hasSummativeFollowing` | boolean |  | false | Has summative following (POST) POST only. Set at assembly from the lesson shell. true -> hand-off points to the assessment ahead; false -> points to application/practice. Default false. |
| `_preConfirmation` | string |  | "Thank you. You will revisit these state | Pre confirmation message PRE only. Shown after the learner submits the pre-ratings. |
| `_feedback` | object |  |  | Feedback (POST) POST only. Five movement-pattern templates, three summary variants, and the standalone (no-pre) text. Templates use {{item}} for the statement text. |
| `_patterns` | object |  |  | Movement pattern templates  |
| `rose` | string |  | "" | Rose Pre low/mid -> higher. Affirm, hand forward. {{item}} available. |
| `stayedHigh` | string |  | "" | Stayed high High -> stayed high. Neutral. {{item}} available. |
| `stayedLow` | string |  | "" | Stayed low Low -> stayed low. Honest flag, suggest revisiting. {{item}} available. |
| `noMovement` | string |  | "" | No movement (mid) Mid, no shift. Gentle, points forward. {{item}} available. |
| `dropped` | string |  | "" | Dropped Fell. Reframe as a more accurate view; suggest revisiting. {{item}} available. |
| `_summary` | object |  |  | Summary variants  |
| `_predominantlyUp` | string |  | "" | Predominantly up Most rose/stayed-high. Affirming close, hand forward. |
| `_mixed` | string |  | "" | Mixed Spread of movement. Normalise downward/unsure items, then hand forward. |
| `_flatOrLow` | string |  | "" | Flat or low Little movement, mostly low/mid or dropped. Honest, non-defeatist, revisit then forward. |
| `_standalone` | string |  | "" | Standalone (no pre - SA-8) POST shown when no pre ratings exist: a single-reading framing, no delta, pointed forward. {{item}} available. |
| `_forward` | object |  |  | Forward hand-off (POST) SA-7. Appended to the summary (and standalone) on every path. One is selected by _hasSummativeFollowing. |
| `_summative` | string |  | "" | If a summative follows Used when _hasSummativeFollowing is true — points to the assessment ahead. |
| `_application` | string |  | "" | If no summative follows Used when _hasSummativeFollowing is false — points to applying it next. |
| `_itemFeedbackOverrides` | array |  |  | Per-item feedback overrides (POST, optional) OPTIONAL. Bespoke pattern wording for specific items, keyed by item _id. Empty -> the component-level _patterns are used. |
| `_itemId` | string | yes | "" |  The item _id this override applies to. |
| `rose` | string |  | "" |   |
| `stayedHigh` | string |  | "" |   |
| `stayedLow` | string |  | "" |   |
| `noMovement` | string |  | "" |   |
| `dropped` | string |  | "" |   |
| `_recordInteraction` | boolean |  | true | Record interaction Record each rating to cmi.interactions (likert type) as a self-report. Enables cohort delta extraction from Moodle. |
| `_buttons` | object |  |  | Buttons  |
| `_submit` | object |  |  | Submit  |
| `buttonText` | string |  | "Submit" |   |
| `ariaLabel` | string |  | "" |   |

## JSX template(s)

**confidence.jsx**

```jsx
import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

export default function Confidence(props) {
  const {
    _id,
    _isEnabled,
    _isComplete,
    _mode,
    _items,
    _scale,
    _globals,
    _isSubmitted,
    displayTitle,
    body,
    instruction,
    ariaQuestion,
    _buttons,
    // View methods exposed via props spread
    model
  } = props;

  const globalsComponent = _globals?._components?._confidence || {};
  const ariaScaleName = globalsComponent.ariaScaleName || 'confidence';
  const ariaItemRated = globalsComponent.ariaItemRated || '{{{item}}}: rated {{{label}}}, {{{value}}} of {{{max}}}';

  const items = _items || [];
  const scale = _scale || {};
  const scaleLabels = scale._labels || ['Not at all confident', 'Slightly confident', 'Fairly confident', 'Very confident', 'Completely confident'];
  const ratings = model?.getRatings?.() || [];
  const canSubmit = model?.canSubmit?.() || false;
  const isSubmitted = _isSubmitted || false;
  const mode = _mode || 'pre';
  const isPre = mode === 'pre';
  const isPost = mode === 'post';

  // Feedback data for POST
  const feedbackItems = isPost && isSubmitted ? (model?.getFeedbackItems?.() || []) : [];
  const summaryText = isPost && isSubmitted ? (model?.getSummaryText?.() || '') : '';
  const isStandalone = model?.isStandalone?.() || false;

  // Submit button text
  const submitText = _buttons?._submit?.buttonText || 'Submit';
  const submitAriaLabel = _buttons?._submit?.ariaLabel || submitText;

  // FIX 5: PRE confirmation message from props (authorable), with schema default fallback
  const preConfirmation = props._preConfirmation || "Thank you. You will revisit these statements at the end of the lesson to see how your confidence has changed.";

  return (
    <div className="component__inner confidence__inner">

      <templates.header {...props} />

      <div
        className={classes([
          'component__widget confidence__widget',
          !_isEnabled && 'is-disabled',
          isSubmitted && 'is-submitted',
          _isComplete && 'is-complete',
          `is-${mode}`
        ])}
        role="group"
        aria-labelledby={ariaQuestion ? null : (displayTitle || body || instruction) && `${_id}-header`}
        aria-label={ariaQuestion || null}
      >

        {/* Rating form - shown when not yet submitted */}
        {!isSubmitted && (
          <div className="confidence__form">
            <fieldset className="confidence__items">
              <legend className="u-display-none">
                {instruction || 'Rate how confident you feel about each statement.'}
              </legend>

              {items.map((item, itemIndex) => {
                const itemId = item._id || `item-${itemIndex}`;
                const currentRating = ratings[itemIndex];
                const groupName = `${_id}-${itemId}`;

                return (
                  <div
                    key={itemId}
                    className="confidence__item"
                    data-item-index={itemIndex}
                  >
                    <div
                      className="confidence__item-text"
                      id={`${_id}-${itemId}-label`}
                      dangerouslySetInnerHTML={{ __html: compile(item.text) }}
                    />

                    <div
                      className="confidence__scale"
                      role="radiogroup"
                      aria-labelledby={`${_id}-${itemId}-label`}
                    >
                      {scaleLabels.map((label, scaleIndex) => {
                        const value = scaleIndex + 1; // 1-based
                        const isSelected = currentRating === value;
                        const radioId = `${_id}-${itemId}-${value}`;

                        return (
                          <label
                            key={value}
                            className={classes([
                              'confidence__option',
                              isSelected && 'is-selected'
                            ])}
                            htmlFor={radioId}
                          >
                            <input
                              type="radio"
                              id={radioId}
                              name={groupName}
                              value={value}
                              checked={isSelected}
                              disabled={!_isEnabled}
                              className="confidence__radio js-confidence-radio"
                              data-item-index={itemIndex}
                              aria-label={`${item.text}: ${label}, ${value} of ${scaleLabels.length}`}
                              onChange={() => model.setRating(itemIndex, value)}
                            />
                            <span className="confidence__option-indicator" aria-hidden="true" />
                            <span className="confidence__option-label">{label}</span>
                          </label>
                        );
                      })}
                    </div>
                  </div>
                );
              })}
            </fieldset>

            <div className="btn__container">
              <button
                type="button"
                className={classes([
                  'btn-text btn__action js-confidence-submit',
                  !canSubmit && 'is-disabled'
                ])}
                disabled={!canSubmit || !_isEnabled}
                aria-label={submitAriaLabel}
              >
                {submitText}
              </button>
            </div>
          </div>
        )}

        {/* PRE: confirmation message after submit */}
        {isPre && isSubmitted && (
          <div className="confidence__confirmation" role="status" aria-live="polite">
            <p className="confidence__confirmation-text">{preConfirmation}</p>
          </div>
        )}

        {/* POST: feedback after submit */}
        {isPost && isSubmitted && (
          <div className="confidence__feedback" role="region" aria-live="polite" tabIndex="-1">

            {/* Per-item feedback */}
            {feedbackItems.length > 0 && (
              <ul className="confidence__feedback-items">
                {feedbackItems.map((fi, index) => (
                  <li
                    key={fi.itemId || index}
                    className={classes([
                      'confidence__feedback-item',
                      fi.pattern && `is-${fi.pattern}`
                    ])}
                  >
                    <span
                      className="confidence__feedback-item-text"
                      dangerouslySetInnerHTML={{ __html: compile(fi.itemText) }}
                    />
                    {!isStandalone && fi.preRating !== undefined && fi.postRating !== undefined && (
                      <span
                        className={classes([
                          'confidence__movement',
                          fi.direction && `is-${fi.direction}`
                        ])}
                        aria-label={
                          fi.direction === 'up' ? `Confidence rose by ${fi.delta} (from ${fi.preRating} to ${fi.postRating})`
                          : fi.direction === 'down' ? `Confidence fell by ${Math.abs(fi.delta)} (from ${fi.preRating} to ${fi.postRating})`
                          : `Confidence unchanged at ${fi.postRating}`
                        }
                      >
                        <span className="confidence__movement-ratings" aria-hidden="true">
                          {fi.preRating} → {fi.postRating}
                        </span>
                        <span className="confidence__movement-badge" aria-hidden="true">
                          {fi.direction === 'up' ? '▲' : fi.direction === 'down' ? '▼' : '—'}
                          {fi.delta > 0 ? ` +${fi.delta}` : fi.delta < 0 ? ` ${fi.delta}` : ''}
                        </span>
                      </span>
                    )}
                    {fi.feedbackText && (
                      <span
                        className="confidence__feedback-text"
                        dangerouslySetInnerHTML={{ __html: compile(fi.feedbackText) }}
                      />
                    )}
                  </li>
                ))}
              </ul>
            )}

            {/* Summary */}
            {summaryText && (
              <div
                className="confidence__summary"
                dangerouslySetInnerHTML={{ __html: compile(summaryText) }}
              />
            )}

          </div>
        )}

      </div>

    </div>
  );
}
```

## Live example (from this course)

```json
{
  "_id": "understanding-learning-assessment-feedback-introductory-C-PRE-c-05",
  "_parentId": "understanding-learning-assessment-feedback-introductory-C-PRE-b-05",
  "_type": "component",
  "_component": "confidence",
  "_classes": "",
  "_layout": "full",
  "title": "Confidence check",
  "displayTitle": "",
  "body": "",
  "instruction": "Before you start, rate how confident you feel about each statement. There are no right or wrong answers.",
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_isCompletionIndicatorEnabled": false
  },
  "_mode": "pre",
  "_selfAssessmentGroupId": "understanding-learning-assessment-feedback-introductory",
  "_scale": {
    "_labels": [
      "Not at all confident",
      "Slightly confident",
      "Fairly confident",
      "Confident",
      "Very confident"
    ]
  },
  "_preConfirmation": "Thank you. You will see these statements again at the end of the course, so you can see how your confidence has changed.",
  "_items": [
    {
      "_id": "co1",
      "text": "I can apply what I know about how university learning works to my own study."
    },
    {
      "_id": "co2",
      "text": "I can interpret my own assessment tasks and marking criteria."
    },
    {
      "_id": "co3",
      "text": "I can act on feedback to improve my own work."
    },
    {
      "_id": "co4",
      "text": "I can align my own academic practice with the learning, assessment and feedback cycle."
    }
  ]
}
```

## Files a component like this needs

- `bower.json` — name, `component` (the type string used in JSON), `targetAttribute` (the `_config` key), `displayName`, `main` (the JS entry).
- `properties.schema` — JSON Schema (draft-04) of authorable fields; drives the authoring UI and validation.
- `js/<Name>Model.js` + `js/<Name>View.js` + `js/<name>.js` (registers the component with Adapt).
- `templates/<name>.jsx` — the React template (modern Adapt renders components with JSX, not Handlebars).
- `less/<name>.less` — styles (compiled globally; see adapt-ab-theme for the committed-CSS pattern).
