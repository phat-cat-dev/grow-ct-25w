import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * OpenText component template.
 *
 * Stage 3: auto-grow, counter, status line.
 * Stage 4: completion button and state.
 * - Textarea defaultValue set from model (restored at adapt:start)
 * - Counter visible when approaching/over limit (view controls visibility)
 * - Over-limit message shown when exceeded (view controls visibility)
 * - Status line updated by view on save success/failure
 * - Completion button shown for reflection variant when _isCompletionBearing
 * - All learner-facing strings from schema globals (spec §10)
 *
 * Accessibility (spec §9):
 * - Body rendered with ID, referenced by aria-labelledby on textarea
 * - Counter is aria-hidden (not announced on keystrokes)
 * - Status line referenced by aria-describedby
 * - Live regions: polite for thresholds, alert for failures
 * - Completion announced via live region
 */
export default function OpenText(props) {
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

  // Get strings from globals (single source of truth, no fallback)
  const statusNormal = _globals?.statusNormal;
  const completionButtonText = _globals?.completionButton;
  const completedStateText = _globals?.completedState;
  const ariaRegion = _globals?.ariaRegion;

  // Variant and rows come from model defaults (spec §2)
  const variant = _variant || 'reflection';
  const rows = _rows || 4;

  // Label configuration (spec §9.1): fallback chain for accessible name
  // body → instruction → displayTitle → ariaRegion
  // All use aria-labelledby pointing to a rendered element with ID
  const hasBody = Boolean(body);
  const labelId = hasBody ? `${_id}-body` : `${_id}-label`;

  // Strip HTML tags from fallback content — instruction/displayTitle may contain
  // block-level HTML which could cause screen readers to run text together
  const stripTags = (html) => {
    if (!html) return '';
    return html
      .replace(/<\/(p|div|li|h[1-6])>/gi, ' ')  // Space after block closers
      .replace(/<[^>]*>/g, '')                   // Strip all tags
      .replace(/\s+/g, ' ')                      // Normalize whitespace
      .trim();
  };
  const fallbackLabelText = stripTags(instruction) || stripTags(displayTitle) || ariaRegion || '';

  // Render header without body — body renders separately for aria-labelledby
  const headerProps = { ...props, body: null };

  return (
    <div className="component__inner grow-opentext__inner">

      {/* Header renders displayTitle and instruction; body excluded */}
      <templates.header {...headerProps} />

      {/* Body rendered separately with ID for aria-labelledby (spec §9.1) */}
      {body &&
        <div className="grow-opentext__body">
          <div
            id={`${_id}-body`}
            className="grow-opentext__body-inner"
            dangerouslySetInnerHTML={{ __html: compile(body, props) }}
          />
        </div>
      }

      {/* Fallback label when no body — visually hidden, provides accessible name (spec §9.1) */}
      {/* Chain: instruction → displayTitle → ariaRegion (tags stripped for clean SR output) */}
      {!body &&
        <div
          id={`${_id}-label`}
          className="grow-opentext__label--hidden"
        >
          {fallbackLabelText}
        </div>
      }

      <div
        className={classes([
          'component__widget grow-opentext__widget',
          !_isEnabled && 'is-disabled',
          _isComplete && 'is-complete',
          `is-variant-${variant}`
        ])}
      >

        {/* Textarea with auto-grow (view handles resizing) */}
        <div className="grow-opentext__textarea-container">
          <textarea
            id={`${_id}-textarea`}
            className="grow-opentext__textarea"
            rows={rows}
            placeholder={_resolvedPlaceholder}
            disabled={!_isEnabled}
            defaultValue={_initialText || ''}
            aria-labelledby={labelId}
            aria-describedby={`${_id}-status`}
          />
          {/* Manual expand/collapse — auto-grow already handles typing/pasting;
              this lets the learner pre-expand before writing anything (view
              toggles height + label directly, no re-render needed) */}
          <button
            type="button"
            className="grow-opentext__expand-btn"
            aria-expanded="false"
            aria-controls={`${_id}-textarea`}
            aria-label={_globals?.expandButtonLabel}
          >
            <span className="icon" aria-hidden="true" />
          </button>
        </div>

        {/* Character counter — hidden until approaching limit (spec §8) */}
        {/* aria-hidden: must not be announced on every keystroke (spec §9.1) */}
        <div
          className="grow-opentext__counter u-display-none"
          aria-hidden="true"
        >
          {/* Content and visibility controlled by view */}
        </div>

        {/* Over-limit warning — hidden until limit exceeded (spec §8, §10) */}
        <div className="grow-opentext__over-limit u-display-none">
          {/* Content and visibility controlled by view */}
        </div>

        {/* Completion UI — only for reflection variant with _isCompletionBearing (spec §7) */}
        {_shouldShowCompletionButton &&
          <div className="grow-opentext__completion">
            {/* Button — hidden when complete, shown otherwise */}
            <button
              type="button"
              className={classes([
                'btn-text grow-opentext__complete-btn',
                _isComplete && 'u-display-none'
              ])}
            >
              {completionButtonText}
            </button>
            {/* Completed state — hidden until complete, receives focus (spec §9.5) */}
            <div
              className={classes([
                'grow-opentext__completed-state',
                !_isComplete && 'u-display-none'
              ])}
              tabIndex="-1"
            >
              {completedStateText}
            </div>
          </div>
        }

        {/* Status line — updated by view on save success/failure (spec §9.3) */}
        {/* Default text from schema globals (spec §10) */}
        <div
          id={`${_id}-status`}
          className="grow-opentext__status"
        >
          {statusNormal}
        </div>

        {/* Live region for routine announcements: thresholds, completion (spec §9.2) */}
        <div
          className="grow-opentext__live-region"
          aria-live="polite"
          aria-atomic="true"
        >
          {/* Announcements injected by view */}
        </div>

        {/* Alert region for write failures — assertive (spec §9.3) */}
        <div
          className="grow-opentext__alert"
          role="alert"
          aria-atomic="true"
        >
          {/* Failure message injected by view when write fails */}
        </div>

      </div>

    </div>
  );
}
