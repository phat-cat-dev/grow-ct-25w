import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * GROW journal component template.
 *
 * - Textarea defaultValue set from model (restored at adapt:start)
 * - Counter visible when approaching/over limit (view controls visibility)
 * - Over-limit message shown when exceeded (view controls visibility)
 * - Status line updated by view on save success/failure
 * - Completion button shown for reflection variant when _isCompletionBearing
 * - All learner-facing strings from schema globals
 *
 * Accessibility:
 * - Body rendered with ID, referenced by aria-labelledby on textarea
 * - Counter is aria-hidden (not announced on keystrokes)
 * - Status line referenced by aria-describedby
 * - Live regions: polite for thresholds, alert for failures
 */
export default function Journal(props) {
  const {
    _id,
    _isEnabled,
    _isComplete,
    _variant,
    _rows,
    _globals,
    _shouldShowCompletionButton,
    displayTitle,
    body,
    instruction,
    _resolvedPlaceholder,
    _initialText
  } = props;

  const statusNormal = _globals?.statusNormal;
  const completionButtonText = _globals?.completionButton;
  const completedStateText = _globals?.completedState;
  const ariaRegion = _globals?.ariaRegion;

  const variant = _variant || 'reflection';
  const rows = _rows || 4;

  const hasBody = Boolean(body);
  const labelId = hasBody ? `${_id}-body` : `${_id}-label`;

  const stripTags = (html) => {
    if (!html) return '';
    return html
      .replace(/<\/(p|div|li|h[1-6])>/gi, ' ')
      .replace(/<[^>]*>/g, '')
      .replace(/\s+/g, ' ')
      .trim();
  };
  const fallbackLabelText = stripTags(instruction) || stripTags(displayTitle) || ariaRegion || '';

  const headerProps = { ...props, body: null };

  return (
    <div className="component__inner grow-journal__inner">

      <templates.header {...headerProps} />

      {body &&
        <div className="grow-journal__body">
          <div
            id={`${_id}-body`}
            className="grow-journal__body-inner"
            dangerouslySetInnerHTML={{ __html: compile(body, props) }}
          />
        </div>
      }

      {!body &&
        <div
          id={`${_id}-label`}
          className="grow-journal__label--hidden"
        >
          {fallbackLabelText}
        </div>
      }

      <div
        className={classes([
          'component__widget grow-journal__widget',
          !_isEnabled && 'is-disabled',
          _isComplete && 'is-complete',
          `is-variant-${variant}`
        ])}
      >

        <div className="grow-journal__textarea-container">
          <textarea
            id={`${_id}-textarea`}
            className="grow-journal__textarea"
            rows={rows}
            placeholder={_resolvedPlaceholder}
            disabled={!_isEnabled}
            defaultValue={_initialText || ''}
            aria-labelledby={labelId}
            aria-describedby={`${_id}-status`}
          />
          <button
            type="button"
            className="grow-journal__expand-btn"
            aria-expanded="false"
            aria-controls={`${_id}-textarea`}
            aria-label={_globals?.expandButtonLabel}
          >
            <span className="icon" aria-hidden="true" />
          </button>
        </div>

        <div
          className="grow-journal__counter u-display-none"
          aria-hidden="true"
        />

        <div className="grow-journal__over-limit u-display-none" />

        {_shouldShowCompletionButton &&
          <div className="grow-journal__completion">
            <button
              type="button"
              className={classes([
                'btn-text grow-journal__complete-btn',
                _isComplete && 'u-display-none'
              ])}
            >
              {completionButtonText}
            </button>
            <div
              className={classes([
                'grow-journal__completed-state',
                !_isComplete && 'u-display-none'
              ])}
              tabIndex="-1"
            >
              {completedStateText}
            </div>
          </div>
        }

        <div
          id={`${_id}-status`}
          className="grow-journal__status"
        >
          {statusNormal}
        </div>

        <div
          className="grow-journal__live-region"
          aria-live="polite"
          aria-atomic="true"
        />

        <div
          className="grow-journal__alert"
          role="alert"
          aria-atomic="true"
        />

      </div>

    </div>
  );
}
