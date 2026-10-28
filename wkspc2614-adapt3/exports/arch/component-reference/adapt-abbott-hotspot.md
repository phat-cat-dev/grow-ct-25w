# Hotspot  (`hotspot`)

- plugin: `adapt-abbott-hotspot` (component)
- targetAttribute: `_hotspot`
- framework: `>=5.19.1`
- used in this course: no

## Authorable properties

| field | type | req | default | title / help |
|---|---|---|---|---|
| `ariaRegion` | string | yes | "Hotspot question" |   |
| `ariaCorrectAnswer` | string | yes | "The correct answer is {{{correctAnswer} |  Text that will be announced by the screen reader when the learner selects the 'correct answer' button (and there is only one correct region) |
| `ariaCorrectAnswers` | string | yes | "The correct answers are {{{correctAnswe |  Text that will be announced by the screen reader when the learner selects the 'correct answer' button (and there is more than one correct region) |
| `ariaUserAnswer` | string | yes | "The answer you chose was {{{userAnswer} |  Text that will be announced by the screen reader when the learner selects the 'hide correct answer' button (and the learner only chose one region) |
| `ariaUserAnswers` | string | yes | "The answers you chose were {{{userAnswe |  Text that will be announced by the screen reader when the learner selects the 'hide correct answer' button (and the learner chose more than one region) |
| `areaLabel` | string | yes | "Area {{index}} of {{total}}: {{text}}" |  Template for each region's accessible name. {{index}} is the region's 1-based position, {{total}} is the region count, {{text}} is the region's own authored label. |
| `listModeInstruction` | string | yes | "This question is shown as a list becaus |  Shown above the items when the component falls back to list mode (see hotspotLogic.js listModeThreshold) |
| `_supportedLayout` | string enum: full-width, half-width, both | yes | "full-width" |   |
| `instruction` | string |  | "Choose {{#if _isRadio}}one area{{else}} |  This is the instruction text |
| `ariaQuestion` | string |  | "" |  This will be read out by screen readers instead of reading the 'Display title', 'Body' & 'Instruction' fields when focusing on the regions. To be clear and concise, ensure the text encompasses only the question associated. |
| `_graphic` | object | yes |  | Image  |
| `large` | string | yes | "" |  The large sized image for desktop devices. Regions are positioned by percentage, so this and the small image should share the same aspect ratio and region layout. |
| `small` | string | yes | "" |  The small sized image for mobile devices. Regions are positioned by percentage, so this and the large image should share the same aspect ratio and region layout. |
| `alt` | string | yes | "" | Alternative text A short description of the image itself, read before the question's regions. Required (see the component spec's accessibility contract). |
| `longdescription` | string | yes | "" | Long image description A long description of the image's layout, sufficient for a screen reader user to understand what is depicted before choosing between the regions. Required (see the component spec's accessibility contract). |
| `attribution` | string |  | "" |  Text to be displayed as an attribution |
| `_items` | array | yes |  | Regions 2 to 8 rectangular regions on the image (see hotspotLogic.js validateRegions). Author the correct region or regions plus 2 to 5 decoys. |
| `text` | string | yes | "" | Region label This region's own accessible-name text, e.g. '2006'. Read as part of 'Area N of M: <this text>'. |
| `shape` | string enum: rect | yes | "rect" | Shape Only rectangular regions are supported. |
| `left` | number | yes | 0 | Left (%) Distance from the image's left edge, as a percentage of image width (0 to 100). |
| `top` | number | yes | 0 | Top (%) Distance from the image's top edge, as a percentage of image height (0 to 100). |
| `width` | number | yes | 0 | Width (%) Region width as a percentage of image width. Regions under 12% width trigger a geometry warning (see hotspotLogic.js geometryWarnings). |
| `height` | number | yes | 0 | Height (%) Region height as a percentage of image height. Regions under 8% height trigger a geometry warning (see hotspotLogic.js geometryWarnings). |
| `_shouldBeSelected` | boolean | yes | false | Correct region?  |
| `_isPartlyCorrect` | boolean | yes | false | Is only partly correct?  |
| `feedback` | string |  | "" | Region-specific feedback When 'Selectable Items' is set to 1, this can be used to give the user feedback specific to the region they selected - if incorrect. |
| `_score` | number |  | 0 | Score If item scoring is enabled, selected region scores are summed to give the question score. |
| `_attempts` | number | yes | 2 | Attempts How many attempts the learner is allowed |
| `_canShowModelAnswer` | boolean | yes | true | Display Model Answer Allow the user to view the 'model answer' (the correct region or regions outlined and labelled) if they answer the question incorrectly? |
| `_canShowCorrectness` | boolean |  | false | Display region correctness If enabled, this replaces the associated 'model answer' toggle button and displays correctness directly on the regions. |
| `_canShowFeedback` | boolean | yes | true | Display Feedback  |
| `_canShowMarking` | boolean |  | true | Display Marking  |
| `_shouldDisplayAttempts` | boolean |  | false | Display Attempts Display the number of attempts remaining? |
| `_isRandom` | boolean |  | false | Randomise region order Randomises the DOM/tab order of regions. Does not affect where each region is positioned on the image. |
| `_recordInteraction` | boolean |  | true | Record interaction If disabled, recording the user's answer(s) to this question to cmi.interactions on the LMS will be disabled for this component only. |
| `_hasItemScoring` | boolean |  | false | Enable item scoring When disabled, this question scores 0 for incorrect and 'Question Weight' for correct. When enabled, this question scores by summing the scores of the selected regions. |
| `_questionWeight` | number |  | 1 | Question Weight When item scoring is disabled, this is the question score for a correct response. |
| `_selectable` | number | yes | 1 | Selectable Regions How many regions are selectable |
| `_feedback` | object |  |  | Feedback  |
| `title` | string |  | "" | Feedback Title Leave blank to have the component's title shown instead. |
| `correct` | string |  | "" | Correct Correct answer feedback for this question |
| `_incorrect` | object |  |  | Incorrect Feedback  |
| `final` | string |  | "" | Incorrect Final Incorrect answer feedback for the final attempt |
| `notFinal` | string |  | "" | Incorrect Not Final Incorrect answer feedback for any attempt apart from the last attempt. If you leave this blank, the 'Incorrect Final' feedback will be used instead. |
| `_partlyCorrect` | object |  |  |   |
| `final` | string |  | "" | Partly Correct Final Partly correct answer feedback for the final attempt. If you leave this blank, the 'Incorrect Final' feedback will be used instead. |
| `notFinal` | string |  | "" | Partly Correct Not Final Partly correct answer feedback for any attempt apart from the last attempt. If you leave this blank, the 'Partly Correct Final' feedback will be used instead. |
| `_buttons` | object |  |  | Buttons  |
| `_submit` | object |  |  | Submit  |
| `buttonText` | string |  | "" |  Button label text for the submit button |
| `ariaLabel` | string |  | "" |  Aria label for the submit button |
| `_reset` | object |  |  | Reset  |
| `buttonText` | string |  | "" |  Button label text for the reset button |
| `ariaLabel` | string |  | "" |  Aria label for the reset button |
| `_showCorrectAnswer` | object |  |  | Show Correct Answer  |
| `buttonText` | string |  | "" |  Button label text to show the model answer |
| `ariaLabel` | string |  | "" |  Aria label for the show model answer button |
| `_hideCorrectAnswer` | object |  |  | Hide Correct Answer  |
| `buttonText` | string |  | "" |  Button label text to hide the model answer |
| `ariaLabel` | string |  | "" |  Aria label for the hide model answer button |
| `_showFeedback` | object |  |  | Show Feedback  |
| `buttonText` | string |  | "" |  Button label text to show feedback |
| `ariaLabel` | string |  | "" |  Aria label for the show feedback button |
| `remainingAttemptsText` | string |  | "" | Attempts Remaining Text Shown when there are multiple attempts left |
| `remainingAttemptText` | string |  | "" | Final Attempt Text Shown when there is one attempt left |

## JSX template(s)

**hotspot.jsx**

```jsx
import Adapt from 'core/js/adapt';
import a11y from 'core/js/a11y';
import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * Hotspot Template
 *
 * Two render modes, both native-input based (the accessibility
 * contract):
 *
 * - Positioned mode (default): each region is a real radio/checkbox input,
 *   absolutely positioned over the authored image by percentage geometry,
 *   invisible until hover/focus/after-submit (see less/hotspot.less), with
 *   its own accessible name built from the areaLabel global template
 *   ("Area N of M: <region text>").
 * - List mode (props._isListMode, set by HotspotView/HotspotModel once the
 *   rendered image size is known — see hotspotLogic.js listModeThreshold):
 *   the same inputs, laid out as a plain stacked list instead of positioned
 *   over the image, for when regions would render under 44x44 CSS px.
 *
 * Fieldset/legend (not a role=radiogroup div) is used for the region group,
 * per the accessibility requirement's explicit instruction — this is the
 * one point where this template does NOT copy mcq.jsx's div+role approach
 * verbatim.
 */
export default function Hotspot(props) {
  const ariaLabels = Adapt.course.get('_globals')._accessibility._ariaLabels;
  const hotspotGlobals = props._globals?._components?._hotspot || {};

  const {
    _id,
    _isEnabled,
    _isInteractionComplete,
    _isCorrect,
    _isCorrectAnswerShown,
    _shouldShowMarking,
    _canShowModelAnswer,
    _canShowCorrectness,
    _isRadio,
    _isListMode,
    _graphic,
    displayTitle,
    body,
    instruction,
    ariaQuestion,
    onKeyDown,
    onItemSelect,
    onItemFocus,
    onItemBlur
  } = props;

  const items = props._items || [];
  const total = items.length;

  const legendText = ariaQuestion || displayTitle || body || instruction || hotspotGlobals.ariaRegion || '';

  const buildAreaLabel = (index, text) => {
    const template = hotspotGlobals.areaLabel || 'Area {{index}} of {{total}}: {{text}}';
    return Handlebars.compile(template)({ index: index + 1, total, text });
  };

  const buildInputAriaLabel = (item, index) => {
    const areaLabel = buildAreaLabel(index, a11y.normalize(item.text));
    if (!_shouldShowMarking) return areaLabel;
    return `${item._shouldBeSelected ? ariaLabels.correct : ariaLabels.incorrect}, ${item._isActive ? ariaLabels.selectedAnswer : ariaLabels.unselectedAnswer}. ${areaLabel}`;
  };

  return (
    <div className='component__inner hotspot__inner'>

      <templates.header {...props} />

      <div
        className={classes([
          'component__widget',
          'hotspot__widget',
          !_isEnabled && 'is-disabled',
          _isInteractionComplete && 'is-complete is-submitted',
          _isInteractionComplete && !_canShowCorrectness && !_isCorrectAnswerShown && 'show-user-answer',
          _isInteractionComplete && _canShowModelAnswer && _isCorrectAnswerShown && 'show-correct-answer',
          _isInteractionComplete && _canShowCorrectness && 'show-correctness',
          _isCorrect && 'is-correct',
          _isListMode && 'is-list-mode'
        ])}
      >

        <div className='hotspot__image-container'>
          <templates.image {..._graphic}
            id={`hotspot__image__${_id}`}
            longDescriptionId={`hotspot__longdescription__${_id}`}
            classNamePrefixes={['hotspot']}
          />
        </div>

        {_graphic?.longdescription &&
        <div
          id={`hotspot__longdescription__${_id}`}
          className='hotspot__longdescription'
        >
          <div className='hotspot__longdescription-inner'>
            {_graphic.longdescription}
          </div>
        </div>
        }

        {_isListMode &&
        <p className='hotspot__list-mode-instruction'>
          {hotspotGlobals.listModeInstruction}
        </p>
        }

        <fieldset className='hotspot__fieldset'>

          <legend className='aria-label'>
            {legendText}
          </legend>

          <div
            className={classes([
              'hotspot__regions',
              _isListMode && 'hotspot__regions--list'
            ])}
            role={_isRadio ? 'radiogroup' : 'group'}
          >

            {items.map((item, index) => {
              const { text, _index, _isActive, _shouldBeSelected, _isHighlighted, left, top, width, height } = item;

              const positionStyle = _isListMode ? null : {
                left: `${left}%`,
                top: `${top}%`,
                width: `${width}%`,
                height: `${height}%`
              };

              return (
                <div
                  className={classes([
                    `hotspot-region item-${index}`,
                    _isHighlighted && 'is-highlighted',
                    _shouldShowMarking && _shouldBeSelected && 'is-correct',
                    _shouldShowMarking && !_shouldBeSelected && 'is-incorrect'
                  ])}
                  style={positionStyle}
                  key={_index}
                >

                  <input
                    className='hotspot-region__input'
                    id={`${_id}-${index}-input`}
                    name={_isRadio ? `${_id}-item` : null}
                    type={_isRadio ? 'radio' : 'checkbox'}
                    aria-disabled={!_isEnabled}
                    checked={_isActive}
                    aria-label={buildInputAriaLabel(item, index)}
                    data-adapt-index={_index}
                    onKeyDown={onKeyDown}
                    onChange={onItemSelect}
                    onFocus={onItemFocus}
                    onBlur={onItemBlur}
                  />

                  <label
                    className={classes([
                      'hotspot-region__label',
                      'u-no-select',
                      !_isEnabled && 'is-disabled',
                      (_isCorrectAnswerShown ? _shouldBeSelected : _isActive) && 'is-selected'
                    ])}
                    aria-hidden={true}
                    htmlFor={`${_id}-${index}-input`}
                    data-adapt-index={_index}
                  >

                    <span className='hotspot-region__state'>
                      <span
                        className={classes([
                          'hotspot-region__icon',
                          'hotspot-region__answer-icon',
                          _isRadio ? 'is-radio' : 'is-checkbox'
                        ])}
                      >
                        <span className='icon'></span>
                      </span>
                    </span>

                    {_isListMode &&
                    <span className='hotspot-region__text'>
                      <span className='hotspot-region__text-inner' dangerouslySetInnerHTML={{ __html: compile(text) }}>
                      </span>
                    </span>
                    }

                    <span className='hotspot-region__state hotspot-region__state-correctness'>
                      <span className='hotspot-region__icon hotspot-region__correct-icon'>
                        <span className='icon'></span>
                      </span>

                      <span className='hotspot-region__icon hotspot-region__incorrect-icon'>
                        <span className='icon'></span>
                      </span>
                    </span>

                  </label>

                </div>
              );
            })}

          </div>

        </fieldset>

      </div>

      <div className='btn__container'></div>

    </div>
  );
}
```

## Live example (from this course)

_No instance of this component in the sampled course._

## Files a component like this needs

- `bower.json` — name, `component` (the type string used in JSON), `targetAttribute` (the `_config` key), `displayName`, `main` (the JS entry).
- `properties.schema` — JSON Schema (draft-04) of authorable fields; drives the authoring UI and validation.
- `js/<Name>Model.js` + `js/<Name>View.js` + `js/<name>.js` (registers the component with Adapt).
- `templates/<name>.jsx` — the React template (modern Adapt renders components with JSX, not Handlebars).
- `less/<name>.less` — styles (compiled globally; see adapt-abbott-theme for the committed-CSS pattern).
