import React from 'react';
import { templates, classes } from 'core/js/reactHelpers';

/**
 * Fill-the-blanks (cloze) template.
 *
 * Renders the header (displayTitle, body, instruction), then the sentence with a
 * <select> dropped in at each blank, a Check button, and a polite feedback region.
 *
 * The sentence is built from _segments (computed by the model): literal text runs
 * interleaved with blank descriptors. Correct answers are NOT rendered here; the
 * view compares against the model by blank index.
 *
 * Accessibility:
 * - The sentence is wrapped in role="group" with an accessible name (ariaRegion).
 * - Each blank's <select> has an aria-label ("Blank n of total") and references a
 *   visually-hidden per-blank status (aria-describedby) that the view fills with
 *   "Correct"/"Incorrect" at Check time: state is not conveyed by colour alone.
 * - The glyph mark (tick/cross) is aria-hidden; the status word carries it for SR.
 * - Overall feedback lives in a polite, atomic live region.
 * - All strings come from schema globals (no hard-coded copy).
 */
export default function Cloze(props) {
  const {
    _id,
    _isEnabled,
    _isComplete,
    _globals = {},
    _segments = [],
    _blankCount = 0
  } = props;

  const interpolate = (template, values) =>
    (template || '').replace(/\{\{(\w+)\}\}/g, (match, key) =>
      (values[key] !== undefined ? values[key] : match)
    );

  return (
    <div className="component__inner growcloze__inner">

      <templates.header {...props} />

      <div
        className={classes([
          'component__widget cloze',
          !_isEnabled && 'is-disabled',
          _isComplete && 'is-complete'
        ])}
      >

        <div className="cloze__group" role="group" aria-label={_globals.ariaRegion}>
          <p className="cloze__sentence">
            {_segments.map((segment, i) => {
              if (segment._type === 'text') {
                return <span key={i} className="cloze__text">{segment._value}</span>;
              }

              const statusId = `${_id}-blank-${segment._index}-status`;
              const label = interpolate(_globals.blankLabel, {
                number: segment._number,
                total: _blankCount
              });

              return (
                <span key={i} className="cloze__blank">
                  <select
                    className="cloze__select"
                    data-blank-index={segment._index}
                    defaultValue=""
                    disabled={!_isEnabled}
                    aria-label={label}
                    aria-describedby={statusId}
                  >
                    <option value="">{_globals.blankPlaceholder}</option>
                    {segment._options.map((option, j) => (
                      <option key={j} value={option}>{option}</option>
                    ))}
                  </select>
                  <span className="cloze__mark" aria-hidden="true"></span>
                  <span id={statusId} className="cloze__blank-status"></span>
                </span>
              );
            })}
          </p>
        </div>

        <div className="cloze__actions">
          <button
            type="button"
            className="btn-text cloze__check js-cloze-check"
            disabled={!_isEnabled}
          >
            {_globals.checkButton}
          </button>
          <div
            className="cloze__feedback"
            role="status"
            aria-live="polite"
            aria-atomic="true"
          ></div>
        </div>

      </div>

    </div>
  );
}
