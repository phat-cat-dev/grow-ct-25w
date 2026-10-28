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
