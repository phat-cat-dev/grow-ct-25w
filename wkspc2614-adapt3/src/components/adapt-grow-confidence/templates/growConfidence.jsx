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

  const globalsComponent = _globals?._components?._growConfidence || {};
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
    <div className="component__inner grow-confidence__inner">

      <templates.header {...props} />

      <div
        className={classes([
          'component__widget grow-confidence__widget',
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
          <div className="grow-confidence__form">
            <fieldset className="grow-confidence__items">
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
                    className="grow-confidence__item"
                    data-item-index={itemIndex}
                  >
                    <div
                      className="grow-confidence__item-text"
                      id={`${_id}-${itemId}-label`}
                      dangerouslySetInnerHTML={{ __html: compile(item.text) }}
                    />

                    <div
                      className="grow-confidence__scale"
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
                              'grow-confidence__option',
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
                              className="grow-confidence__radio js-grow-confidence-radio"
                              data-item-index={itemIndex}
                              aria-label={`${item.text}: ${label}, ${value} of ${scaleLabels.length}`}
                              onChange={() => model.setRating(itemIndex, value)}
                            />
                            <span className="grow-confidence__option-indicator" aria-hidden="true" />
                            <span className="grow-confidence__option-label">{label}</span>
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
                  'btn-text btn__action js-grow-confidence-submit',
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
          <div className="grow-confidence__confirmation" role="status" aria-live="polite">
            <p className="grow-confidence__confirmation-text">{preConfirmation}</p>
          </div>
        )}

        {/* POST: feedback after submit */}
        {isPost && isSubmitted && (
          <div className="grow-confidence__feedback" role="region" aria-live="polite" tabIndex="-1">

            {/* Before/After comparison chart (visual echo of the list below;
                the exact numbers live in the per-item movement, so the chart is
                never the only carrier of meaning). Only when we have a real
                pre/post pairing to show. */}
            {!isStandalone && feedbackItems.length > 0 && (
              <div className="grow-confidence__chart">
                <canvas
                  className="grow-confidence__chart-canvas js-grow-confidence-chart"
                  role="img"
                  aria-label="Bar chart comparing your before and after confidence for each statement. The exact ratings and change are listed below."
                />
              </div>
            )}

            {/* Per-item feedback */}
            {feedbackItems.length > 0 && (
              <ul className="grow-confidence__feedback-items">
                {feedbackItems.map((fi, index) => (
                  <li
                    key={fi.itemId || index}
                    className={classes([
                      'grow-confidence__feedback-item',
                      fi.pattern && `is-${fi.pattern}`
                    ])}
                  >
                    <span
                      className="grow-confidence__feedback-item-text"
                      dangerouslySetInnerHTML={{ __html: compile(fi.itemText) }}
                    />
                    {!isStandalone && fi.preRating !== undefined && fi.postRating !== undefined && (
                      <span
                        className={classes([
                          'grow-confidence__movement',
                          fi.direction && `is-${fi.direction}`
                        ])}
                        aria-label={
                          fi.direction === 'up' ? `Confidence rose by ${fi.delta} (from ${fi.preRating} to ${fi.postRating})`
                          : fi.direction === 'down' ? `Confidence fell by ${Math.abs(fi.delta)} (from ${fi.preRating} to ${fi.postRating})`
                          : `Confidence unchanged at ${fi.postRating}`
                        }
                      >
                        <span className="grow-confidence__movement-ratings" aria-hidden="true">
                          {fi.preRating} → {fi.postRating}
                        </span>
                        <span className="grow-confidence__movement-badge" aria-hidden="true">
                          {fi.direction === 'up' ? '▲' : fi.direction === 'down' ? '▼' : '—'}
                          {fi.delta > 0 ? ` +${fi.delta}` : fi.delta < 0 ? ` ${fi.delta}` : ''}
                        </span>
                      </span>
                    )}
                    {fi.feedbackText && (
                      <span
                        className="grow-confidence__feedback-text"
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
                className="grow-confidence__summary"
                dangerouslySetInnerHTML={{ __html: compile(summaryText) }}
              />
            )}

          </div>
        )}

      </div>

    </div>
  );
}
