import React from 'react';
import { templates, classes } from 'core/js/reactHelpers';

/**
 * Pagefeedback component template.
 *
 * - Two choice buttons (aria-pressed pair) toggle which response is active.
 * - The note + action buttons stay hidden until a response is chosen,
 *   matching the source demo's "choose, then act" flow.
 * - Textarea is uncontrolled (defaultValue from the model) so typing never
 *   fights a re-render — note edits are read by the view directly.
 * - A completion chip (no button — saving a response completes it) shows
 *   only when _isCompletionBearing and already complete.
 * - All learner-facing strings come from schema globals.
 */
export default function Pagefeedback (props) {
  const {
    _id,
    _isEnabled,
    _isComplete,
    _isCompletionBearing,
    _variant,
    _response,
    _globals,
    _choiceLabels,
    _statusKey,
    _initialNote
  } = props;

  const globals = _globals || {};
  const choiceLabels = _choiceLabels || { positive: '', negative: '' };
  const hasResponse = Boolean(_response);
  const statusText = globals[_statusKey] || globals.statusPrompt;

  return (
    <div className="component__inner grow-pagefeedback__inner">

      <templates.header {...props} />

      <div
        className={classes([
          'component__widget grow-pagefeedback__widget',
          !_isEnabled && 'is-disabled',
          _isComplete && 'is-complete',
          hasResponse && 'is-chosen',
          `is-variant-${_variant}`
        ])}
      >

        <div className="grow-pagefeedback__choices" role="group" aria-label={globals.choicesGroupLabel}>
          <button
            type="button"
            className="grow-pagefeedback__choice grow-pagefeedback__choice--positive"
            data-grow-pagefeedback-choice="helpful"
            aria-pressed={_response === 'helpful' ? 'true' : 'false'}
          >
            <span aria-hidden="true">+</span> {choiceLabels.positive}
          </button>
          <button
            type="button"
            className="grow-pagefeedback__choice grow-pagefeedback__choice--negative"
            data-grow-pagefeedback-choice="needs-work"
            aria-pressed={_response === 'needs-work' ? 'true' : 'false'}
          >
            <span aria-hidden="true">&rarr;</span> {choiceLabels.negative}
          </button>
        </div>

        <div
          className={classes([
            'grow-pagefeedback__form',
            !hasResponse && 'u-display-none'
          ])}
        >
          <label className="grow-pagefeedback__note-label" htmlFor={`${_id}-note`}>
            {globals.noteLabel}
          </label>
          <textarea
            id={`${_id}-note`}
            className="grow-pagefeedback__note"
            rows="3"
            maxLength="2000"
            placeholder={globals.notePlaceholder}
            disabled={!_isEnabled}
            defaultValue={_initialNote || ''}
          />
          <div className="grow-pagefeedback__actions">
            <button type="button" className="btn-text grow-pagefeedback__submit">
              {globals.submitButtonLabel}
            </button>
            <button type="button" className="btn-text grow-pagefeedback__clear">
              {globals.clearButtonLabel}
            </button>
          </div>
        </div>

        {_isCompletionBearing && _isComplete &&
          <div className="grow-pagefeedback__completion" tabIndex="-1">
            {globals.completedState}
          </div>
        }

        <p className="grow-pagefeedback__status" role="status">
          {statusText}
        </p>

      </div>

    </div>
  );
}
