import React from 'react';
import { classes, compile } from 'core/js/reactHelpers';

/**
 * Checklist Template
 *
 * A collapsible accordion: the title is a toggle button that opens a region of
 * native checkboxes. Collapsed by default; the view completes the component on
 * first open (passing the trickle), so opening - not ticking - is the gate.
 * Ticking stays a self-assessment aid.
 *
 * Accessibility: the toggle is a real <button> with aria-expanded / aria-controls;
 * the region is labelled by the heading. Items are native checkboxes with labels.
 *
 * Design refs: CL-A (accessibility model), CB-4 (view/template)
 */
export default function Checklist(props) {
  const {
    _id,
    _items,
    instruction,
    displayTitle,
    body,
    _globals
  } = props;

  const ariaRegion = _globals?._components?._growChecklist?.ariaRegion ||
    'Checklist. Work through each item and tick it when done.';

  const itemCount = (_items || []).length;
  const regionId = `${_id}-checklist-region`;
  const headingId = `${_id}-checklist-heading`;

  return (
    <div className="component__inner grow-checklist__inner">

      {/* Accordion toggle: the title opens the checklist. Collapsed by default;
          the view calls setCompletionStatus() on first open (passes trickle). */}
      <h3 className="grow-checklist__heading" id={headingId}>
        <button
          type="button"
          className="grow-checklist__toggle js-grow-checklist-toggle"
          aria-expanded="false"
          aria-controls={regionId}
        >
          <span
            className="grow-checklist__toggle-title"
            dangerouslySetInnerHTML={{ __html: compile(displayTitle || 'Checklist') }}
          />
          <span className="grow-checklist__toggle-icon" aria-hidden="true"></span>
        </button>
      </h3>

      <div
        id={regionId}
        className={classes([
          'component__widget',
          'grow-checklist__widget',
          'grow-checklist__region'
        ])}
        role="region"
        aria-labelledby={headingId}
      >

        {body && (
          <div
            className="grow-checklist__intro"
            dangerouslySetInnerHTML={{ __html: compile(body) }}
          />
        )}

        {/* Fieldset groups the checkboxes with a programmatic label */}
        <fieldset className="grow-checklist__fieldset">
          {instruction && (
            <legend className="grow-checklist__legend aria-label">
              {instruction}
            </legend>
          )}

          <div className="grow-checklist__items">
            {(_items || []).map((item, index) => {
              const inputId = `${_id}-item-${index}`;
              return (
                <div
                  key={index}
                  className={classes(['grow-checklist__item'])}
                >
                  <input
                    type="checkbox"
                    id={inputId}
                    className="grow-checklist__input js-grow-checklist-input"
                    data-index={index}
                  />
                  <label
                    htmlFor={inputId}
                    className="grow-checklist__label"
                  >
                    <span className="grow-checklist__indicator" aria-hidden="true"></span>
                    <span className="grow-checklist__text">{item.text}</span>
                  </label>
                </div>
              );
            })}
          </div>

        </fieldset>

        {/* Neutral progress count (CL-6: no evaluative copy) */}
        <div
          className="grow-checklist__progress"
          aria-live="polite"
          aria-atomic="true"
        >
          <span className="grow-checklist__progress-text js-grow-checklist-progress">
            0 of {itemCount} checked
          </span>
        </div>

      </div>

    </div>
  );
}
