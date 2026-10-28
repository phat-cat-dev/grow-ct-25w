# Sortable Question  (`sortable`)

- plugin: `adapt-abbott-sortable` (component)
- targetAttribute: `_sortable`
- framework: `>=5.19.1`
- used in this course: yes

## Authorable properties

| field | type | req | default | title / help |
|---|---|---|---|---|
| `ariaRegion` | string | yes | "Sorting. Put the items in the correct o |   |
| `ariaCorrectAnswer` | string | yes | "The correct order is: {{{correctAnswer} |  Text announced by screen reader when learner selects 'show correct answer' |
| `ariaUserAnswer` | string | yes | "Your order was: {{{userAnswer}}}" |  Text announced by screen reader when learner selects 'hide correct answer' |
| `ariaItemMoved` | string | yes | "{{{itemText}}} moved to position {{{pos |  Text announced by screen reader when an item is moved |
| `ariaMoveUp` | string | yes | "Move up" |  Aria label for move up button |
| `ariaMoveDown` | string | yes | "Move down" |  Aria label for move down button |
| `_supportedLayout` | string enum: full-width, half-width, both | yes | "half-width" |   |
| `instruction` | string |  | "Put the items in the correct order, the |  Instruction text |
| `ariaQuestion` | string |  | "" |  Screen reader text for the question. If blank, uses title + body + instruction. |
| `_attempts` | number | yes | 1 | Attempts How many attempts the learner is allowed |
| `_canShowModelAnswer` | boolean | yes | true | Display Model Answer Allow the user to view the correct order if they answer incorrectly? |
| `_canShowFeedback` | boolean | yes | true | Display Feedback  |
| `_canShowMarking` | boolean |  | true | Display Marking  |
| `_shouldDisplayAttempts` | boolean |  | false | Display Attempts Display the number of attempts remaining? |
| `_questionWeight` | number |  | 1 | Question Weight How much this question is worth |
| `_recordInteraction` | boolean |  | true | Record interaction If disabled, recording to cmi.interactions on the LMS will be disabled for this component. |
| `_items` | array | yes |  | Items (in correct order) Items are authored in the CORRECT order. The component shuffles them for display. |
| `text` | string | yes | "" |  The text displayed for this item |
| `_feedback` | object |  |  | Feedback  |
| `title` | string |  | "" | Feedback Title Leave blank to use the component's title. |
| `correct` | string |  | "" | Correct Feedback for correct answer |
| `_incorrect` | object |  |  | Incorrect Feedback  |
| `final` | string |  | "" | Incorrect Final Feedback for incorrect answer on final attempt |
| `notFinal` | string |  | "" | Incorrect Not Final Feedback for incorrect answer when attempts remain. If blank, uses 'Incorrect Final'. |
| `_partlyCorrect` | object |  |  | Partly Correct Feedback  |
| `final` | string |  | "" | Partly Correct Final Feedback for partly correct answer on final attempt. If blank, uses 'Incorrect Final'. |
| `notFinal` | string |  | "" | Partly Correct Not Final Feedback for partly correct answer when attempts remain. If blank, uses 'Partly Correct Final'. |
| `_buttons` | object |  |  | Buttons  |
| `_submit` | object |  |  | Submit  |
| `buttonText` | string |  | "" |   |
| `ariaLabel` | string |  | "" |   |
| `_reset` | object |  |  | Reset  |
| `buttonText` | string |  | "" |   |
| `ariaLabel` | string |  | "" |   |
| `_showCorrectAnswer` | object |  |  | Show Correct Answer  |
| `buttonText` | string |  | "" |   |
| `ariaLabel` | string |  | "" |   |
| `_hideCorrectAnswer` | object |  |  | Hide Correct Answer  |
| `buttonText` | string |  | "" |   |
| `ariaLabel` | string |  | "" |   |
| `_showFeedback` | object |  |  | Show Feedback  |
| `buttonText` | string |  | "" |   |
| `ariaLabel` | string |  | "" |   |
| `remainingAttemptsText` | string |  | "" |   |
| `remainingAttemptText` | string |  | "" |   |

## JSX template(s)

**sortable.jsx**

```jsx
import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

export default function Sortable(props) {
  const {
    _id,
    _isEnabled,
    _isInteractionComplete,
    _isCorrect,
    _shouldShowMarking,
    _isCorrectAnswerShown,
    _displayItems,
    _globals,
    displayTitle,
    body,
    instruction,
    ariaQuestion
  } = props;

  const globalsComponent = _globals?._components?._sortable || {};
  const ariaMoveUp = globalsComponent.ariaMoveUp || 'Move up';
  const ariaMoveDown = globalsComponent.ariaMoveDown || 'Move down';

  const displayAsCorrect = _isInteractionComplete && (_isCorrectAnswerShown || _isCorrect);
  const items = _displayItems || [];
  const totalItems = items.length;

  return (
    <div className="component__inner sortable__inner">

      <templates.header {...props} />

      {/* ARIA live region for announcing moves */}
      <div
        id={`${_id}-sortable-live`}
        className="sortable__live-region aria-label"
        aria-live="polite"
        aria-atomic="true"
      />

      <div
        className={classes([
          'component__widget sortable__widget',
          !_isEnabled && 'is-disabled',
          _isInteractionComplete && 'is-complete is-submitted',
          displayAsCorrect && 'is-correct'
        ])}
        aria-labelledby={ariaQuestion ? null : (displayTitle || body || instruction) && `${_id}-header`}
        aria-label={ariaQuestion || null}
      >

        {/* Screen reader instructions - placed outside ol for valid HTML */}
        <div id={`${_id}-sortable-instructions`} className="aria-label">
          Use the up and down arrow keys or the move buttons to reorder items. Press Enter or Space to pick up an item, then arrow keys to move it, then Enter or Space to drop it.
        </div>

        <ol
          className="sortable__items-list"
          role="group"
          aria-label={displayTitle || instruction || 'Reorderable items'}
          aria-describedby={`${_id}-sortable-instructions`}
        >
          {items.map((item, displayIndex) => {
            const isFirst = displayIndex === 0;
            const isLast = displayIndex === totalItems - 1;
            const itemId = `${_id}-sortable-item-${item._index}`;

            // Determine correctness for this position
            const isInCorrectPosition = item._correctPosition === displayIndex;
            const showItemCorrect = _shouldShowMarking && isInCorrectPosition;
            const showItemIncorrect = _shouldShowMarking && !isInCorrectPosition;

            return (
              <li
                key={item._index}
                id={itemId}
                className={classes([
                  'sortable__item',
                  'js-sortable-item',
                  _isEnabled && 'is-draggable',
                  showItemCorrect && 'is-correct',
                  showItemIncorrect && 'is-incorrect'
                ])}
                aria-label={`Position ${displayIndex + 1} of ${totalItems}: ${item.text}`}
                data-index={item._index}
                data-display-index={displayIndex}
                tabIndex={_isEnabled ? 0 : -1}
                draggable={_isEnabled ? 'true' : 'false'}
              >
                <span className="sortable__item-position" aria-hidden="true">
                  {displayIndex + 1}
                </span>

                <span
                  className="sortable__item-text"
                  dangerouslySetInnerHTML={{ __html: compile(item.text) }}
                />

                {_isEnabled && (
                  <span className="sortable__item-controls" aria-hidden="true">
                    <button
                      type="button"
                      className={classes([
                        'sortable__move-btn sortable__move-up-btn js-sortable-move-up',
                        isFirst && 'is-disabled'
                      ])}
                      aria-label={`${ariaMoveUp}: ${item.text}`}
                      disabled={isFirst}
                      data-direction="up"
                      data-display-index={displayIndex}
                      tabIndex={-1}
                    >
                      <span className="icon" aria-hidden="true" />
                    </button>
                    <button
                      type="button"
                      className={classes([
                        'sortable__move-btn sortable__move-down-btn js-sortable-move-down',
                        isLast && 'is-disabled'
                      ])}
                      aria-label={`${ariaMoveDown}: ${item.text}`}
                      disabled={isLast}
                      data-direction="down"
                      data-display-index={displayIndex}
                      tabIndex={-1}
                    >
                      <span className="icon" aria-hidden="true" />
                    </button>
                  </span>
                )}

                {_shouldShowMarking && (
                  <span className="sortable__item-state">
                    <span className="sortable__item-icon sortable__item-correct-icon" aria-label={_globals?._accessibility?._ariaLabels?.correct || 'Correct'}>
                      <span className="icon" aria-hidden="true" />
                    </span>
                    <span className="sortable__item-icon sortable__item-incorrect-icon" aria-label={_globals?._accessibility?._ariaLabels?.incorrect || 'Incorrect'}>
                      <span className="icon" aria-hidden="true" />
                    </span>
                  </span>
                )}
              </li>
            );
          })}
        </ol>

      </div>

      <div className="btn__container" />

    </div>
  );
}
```

## Live example (from this course)

```json
{
  "_id": "L05-c-25",
  "_parentId": "L05-b-25",
  "_type": "component",
  "_component": "sortable",
  "_classes": "",
  "_layout": "full",
  "title": "Put the cycle in order",
  "displayTitle": "Put the cycle in order",
  "body": "These four stages make up the learning, assessment and feedback cycle, but they only work in one order, each depending on the one before. Can you put them in sequence, from first to last?",
  "instruction": "Drag items to reorder, or use the keyboard (Enter to grab, arrows to move, Enter to drop). You can try as many times as you like.",
  "ariaQuestion": "Put the four stages of the learning, assessment and feedback cycle in order from first to last.",
  "_attempts": -1,
  "_shouldDisplayAttempts": false,
  "_questionWeight": 1,
  "_canShowModelAnswer": true,
  "_canShowFeedback": true,
  "_canShowMarking": true,
  "_recordInteraction": true,
  "_isPartOfAssessment": false,
  "_items": [
    {
      "text": "You learn something new, in lectures, reading and seminars."
    },
    {
      "text": "You are assessed on it, through an essay, exam, presentation or another task."
    },
    {
      "text": "You receive feedback on how you did."
    },
    {
      "text": "You act on that feedback, which feeds your next round of learning."
    }
  ],
  "_feedback": {
    "title": "",
    "correct": "That's the cycle. Learning leads into assessment, assessment produces feedback, and feedback, once you act on it, feeds your next round of learning. They form one connected loop rather than four separate steps, which is why feedback is worth having and assessment is worth preparing for.",
    "_incorrect": {
      "notFinal": "Not in order yet. Think about what has to happen before each stage can: you cannot be assessed on what you have not learned, and feedback comes after the assessment, not before it. Try again.",
      "final": ""
    },
    "_partlyCorrect": {
      "notFinal": "Some of those are in the right place, but not all. Each stage depends on the one before it, so work out what has to come first and try again.",
      "final": ""
    }
  },
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_isCompletionIndicatorEnabled": true
  }
}
```

## Files a component like this needs

- `bower.json` — name, `component` (the type string used in JSON), `targetAttribute` (the `_config` key), `displayName`, `main` (the JS entry).
- `properties.schema` — JSON Schema (draft-04) of authorable fields; drives the authoring UI and validation.
- `js/<Name>Model.js` + `js/<Name>View.js` + `js/<name>.js` (registers the component with Adapt).
- `templates/<name>.jsx` — the React template (modern Adapt renders components with JSX, not Handlebars).
- `less/<name>.less` — styles (compiled globally; see adapt-ab-theme for the committed-CSS pattern).
