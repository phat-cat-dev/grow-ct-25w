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
