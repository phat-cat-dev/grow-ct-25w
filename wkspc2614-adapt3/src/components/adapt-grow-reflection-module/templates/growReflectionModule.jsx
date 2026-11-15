import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * GROW reflection module template.
 *
 * Two-column composition:
 *  - Sketchbook (left): optional kicker, a lined journal card ("develop your
 *    thought"), optional caption.
 *  - Aside (right): a "change the lens" card of reframing prompts.
 *
 * The journal half mirrors adapt-grow-journal's markup (textarea + counter +
 * over-limit + completion + status + live regions); the view drives it. The
 * lens prompts are static. On narrow screens the grid collapses to one column
 * (see LESS), so the aside falls below the sketchbook.
 *
 * Accessibility:
 *  - Textarea named via aria-labelledby (journal label → instruction → title).
 *  - Counter aria-hidden; thresholds via polite live region; failures via alert.
 *  - The lens is a labelled list region.
 */
export default function ReflectionModule(props) {
  const {
    _id,
    _isEnabled,
    _isComplete,
    _variant,
    _rows,
    _globals,
    _shouldShowCompletionButton,
    displayTitle,
    instruction,
    _kicker,
    _journal = {},
    _caption,
    _lens = {},
    _resolvedPlaceholder,
    _initialText
  } = props;

  const statusNormal = _globals?.statusNormal;
  const completionButtonText = _globals?.completionButton;
  const completedStateText = _globals?.completedState;
  const ariaRegion = _globals?.ariaRegion;

  const variant = _variant || 'reflection';
  const rows = _rows || 4;

  const journalTitle = _journal.title || 'Develop your thought';
  const journalIcon = _journal.icon || 'draw';
  const journalLabel = _journal.label || '';

  const lensTitle = _lens.title || 'Change the lens';
  const lensIcon = _lens.icon || 'lightbulb';
  const lensPrompts = _lens._prompts || [];
  const hasLens = lensPrompts.length > 0;

  const stripTags = (html) => {
    if (!html) return '';
    return html
      .replace(/<\/(p|div|li|h[1-6])>/gi, ' ')
      .replace(/<[^>]*>/g, '')
      .replace(/\s+/g, ' ')
      .trim();
  };

  // Accessible name for the textarea: journal label → instruction → title → region
  const labelId = `${_id}-journal-label`;
  const fallbackLabelText = journalLabel || stripTags(instruction) || stripTags(displayTitle) || ariaRegion || '';

  const headerProps = { ...props, body: null };

  return (
    <div className="component__inner grow-reflection-module__inner">

      <templates.header {...headerProps} />

      <div className={classes([
        'grow-reflection-module__composition',
        hasLens && 'has-aside'
      ])}>

        {/* ── Sketchbook: the lined journal ── */}
        <div className="grow-reflection-module__sketchbook">

          {_kicker &&
            <span className="grow-reflection-module__kicker">{_kicker}</span>
          }

          <div className={classes([
            'grow-reflection-module__card grow-reflection-module__card--journal',
            !_isEnabled && 'is-disabled',
            _isComplete && 'is-complete',
            `is-variant-${variant}`
          ])}>
            <div className="grow-reflection-module__card-title">
              <span className="material-symbol grow-reflection-module__icon" aria-hidden="true">{journalIcon}</span>
              {journalTitle}
            </div>

            <div className="component__widget grow-reflection-module__widget">
              <label id={labelId} className="grow-reflection-module__journal-label">
                {fallbackLabelText}
              </label>

              <div className="grow-reflection-module__textarea-container">
                <textarea
                  id={`${_id}-textarea`}
                  className="grow-reflection-module__textarea"
                  rows={rows}
                  placeholder={_resolvedPlaceholder}
                  disabled={!_isEnabled}
                  defaultValue={_initialText || ''}
                  aria-labelledby={labelId}
                  aria-describedby={`${_id}-status`}
                />
                <button
                  type="button"
                  className="grow-reflection-module__expand-btn"
                  aria-expanded="false"
                  aria-controls={`${_id}-textarea`}
                  aria-label={_globals?.expandButtonLabel}
                >
                  <span className="icon" aria-hidden="true" />
                </button>
              </div>

              <div className="grow-reflection-module__counter u-display-none" aria-hidden="true" />

              <div className="grow-reflection-module__over-limit u-display-none" />

              {_shouldShowCompletionButton &&
                <div className="grow-reflection-module__completion">
                  <button
                    type="button"
                    className={classes([
                      'btn-text grow-reflection-module__complete-btn',
                      _isComplete && 'u-display-none'
                    ])}
                  >
                    {completionButtonText}
                  </button>
                  <div
                    className={classes([
                      'grow-reflection-module__completed-state',
                      !_isComplete && 'u-display-none'
                    ])}
                    tabIndex="-1"
                  >
                    {completedStateText}
                  </div>
                </div>
              }

              <div id={`${_id}-status`} className="grow-reflection-module__status">
                {statusNormal}
              </div>

              <div className="grow-reflection-module__live-region" aria-live="polite" aria-atomic="true" />
              <div className="grow-reflection-module__alert" role="alert" aria-atomic="true" />
            </div>
          </div>

          {_caption &&
            <p
              className="grow-reflection-module__caption"
              dangerouslySetInnerHTML={{ __html: compile(_caption, props) }}
            />
          }
        </div>

        {/* ── Aside: change the lens ── */}
        {hasLens &&
          <aside className="grow-reflection-module__aside">
            <div
              className="grow-reflection-module__card grow-reflection-module__card--lens"
              role="group"
              aria-labelledby={`${_id}-lens-title`}
            >
              <div id={`${_id}-lens-title`} className="grow-reflection-module__card-title">
                <span className="material-symbol grow-reflection-module__icon" aria-hidden="true">{lensIcon}</span>
                {lensTitle}
              </div>
              <ul className="grow-reflection-module__lens-list">
                {lensPrompts.map((prompt, index) => (
                  <li
                    key={index}
                    className="grow-reflection-module__lens-item"
                    dangerouslySetInnerHTML={{ __html: compile(prompt, props) }}
                  />
                ))}
              </ul>
            </div>
          </aside>
        }

      </div>

    </div>
  );
}
