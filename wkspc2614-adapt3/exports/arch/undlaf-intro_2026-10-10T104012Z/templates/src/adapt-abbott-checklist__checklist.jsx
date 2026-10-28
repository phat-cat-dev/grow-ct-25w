import React from 'react';
import { templates, classes } from 'core/js/reactHelpers';

/**
 * Checklist Template
 *
 * Renders a set of native checkboxes with properly associated labels.
 * Uses fieldset/legend for programmatic grouping.
 *
 * Accessibility: native <input type="checkbox"> with <label> via for/id.
 * IDs derived from component _id for multi-instance safety.
 *
 * Design refs: CL-A (accessibility model), CB-4 (view/template)
 */
export default function Checklist(props) {
  const {
    _id,
    _items,
    instruction,
    _globals
  } = props;

  const ariaRegion = _globals?._components?._checklist?.ariaRegion ||
    'Checklist. Work through each item and tick it when done.';

  const itemCount = (_items || []).length;

  return (
    <div className="component__inner checklist__inner">

      <templates.header {...props} />

      <div
        className={classes([
          'component__widget',
          'checklist__widget'
        ])}
        role="region"
        aria-label={ariaRegion}
      >

        {/* Fieldset groups the checkboxes with a programmatic label */}
        <fieldset className="checklist__fieldset">
          {instruction && (
            <legend className="checklist__legend aria-label">
              {instruction}
            </legend>
          )}

          <div className="checklist__items">
            {(_items || []).map((item, index) => {
              // Derive unique IDs from component _id for multi-instance safety
              const inputId = `${_id}-item-${index}`;

              return (
                <div
                  key={index}
                  className={classes([
                    'checklist__item'
                  ])}
                >
                  <input
                    type="checkbox"
                    id={inputId}
                    className="checklist__input js-checklist-input"
                    data-index={index}
                  />
                  <label
                    htmlFor={inputId}
                    className="checklist__label"
                  >
                    <span className="checklist__indicator" aria-hidden="true"></span>
                    <span className="checklist__text">{item.text}</span>
                  </label>
                </div>
              );
            })}
          </div>

        </fieldset>

        {/* Neutral progress count (CL-6: no evaluative copy) */}
        <div
          className="checklist__progress"
          aria-live="polite"
          aria-atomic="true"
        >
          <span className="checklist__progress-text js-checklist-progress">
            0 of {itemCount} checked
          </span>
        </div>

      </div>

    </div>
  );
}
