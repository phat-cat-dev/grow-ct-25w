import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * Step wizard template.
 *
 * Renders a static shell; the view drives the step changes imperatively (so the
 * marked-up panels are not discarded by a React re-render):
 * - progress bar (role="progressbar") with a fill whose width is --p
 * - a row of step labels, the current one carrying aria-current="step"
 * - all step panels, only the current visible (hidden removes the rest from the
 *   a11y tree and tab order)
 * - Back and Next, disabled at the ends
 * - a polite live region the view writes step-change announcements into
 *
 * All learner-facing chrome strings come from schema globals. Per-step labels and
 * bodies are authored content, compiled with the Adapt react helper.
 */
export default function Wizard(props) {
  const {
    _id,
    _isEnabled,
    _globals,
    _startIndex = 0,
    _stepCount = 0,
    _startPercent = 0,
    _valueText,
    _steps = []
  } = props;

  const regionLabel = _globals?.regionLabel;
  const progressLabel = _globals?.progressLabel;
  const backLabel = _globals?.backButton;
  const nextLabel = _globals?.nextButton;

  const start = _startIndex;
  const count = _stepCount || _steps.length;

  return (
    <div className="component__inner grow-wizard__inner">

      <templates.header {...props} />

      <div
        className={classes([
          'component__widget grow-wizard__widget grow-wizard',
          !_isEnabled && 'is-disabled'
        ])}
        role="group"
        aria-label={regionLabel}
      >

        {/* Progress bar — width tracked by the view via --p */}
        <div
          className="grow-wizard__bar js-grow-wizard-bar"
          role="progressbar"
          aria-label={progressLabel}
          aria-valuemin={1}
          aria-valuemax={count}
          aria-valuenow={start + 1}
          aria-valuetext={_valueText}
        >
          <i
            className="grow-wizard__bar-fill js-grow-wizard-fill"
            style={{ '--p': `${_startPercent}%` }}
            aria-hidden="true"
          />
        </div>

        {/* Step labels — the current one is highlighted and marked */}
        <ol className="grow-wizard__steps">
          {_steps.map((step, index) => (
            <li
              key={index}
              className={classes([
                'grow-wizard__step js-grow-wizard-step',
                index === start && 'is-current'
              ])}
              aria-current={index === start ? 'step' : undefined}
            >
              <span className="grow-wizard__step-label">{step.label}</span>
            </li>
          ))}
        </ol>

        {/* Panels — only the current one is visible; it fades in */}
        <div className="grow-wizard__panels">
          {_steps.map((step, index) => (
            <div
              key={index}
              id={`${_id}-panel-${index}`}
              className={classes([
                'grow-wizard__panel js-grow-wizard-panel',
                index === start && 'is-current'
              ])}
              hidden={index !== start}
              aria-hidden={index !== start}
              dangerouslySetInnerHTML={{ __html: compile(step.body || '', props) }}
            />
          ))}
        </div>

        {/* Controls — Back and Next, clamped at the ends by the view */}
        <div className="grow-wizard__controls">
          <button
            type="button"
            className="grow-wizard__btn grow-wizard__btn--back js-grow-wizard-back"
            disabled={start <= 0}
            aria-disabled={start <= 0}
          >
            {backLabel}
          </button>
          <button
            type="button"
            className="grow-wizard__btn grow-wizard__btn--next js-grow-wizard-next"
            disabled={start >= count - 1}
            aria-disabled={start >= count - 1}
          >
            {nextLabel}
          </button>
        </div>

        {/* Polite live region for step-change announcements */}
        <div
          className="grow-wizard__live js-grow-wizard-live"
          aria-live="polite"
          aria-atomic="true"
        />

      </div>
    </div>
  );
}
