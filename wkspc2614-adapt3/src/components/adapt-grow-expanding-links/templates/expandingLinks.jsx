import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * Expanding Links (GROW) template.
 *
 * A learning-sequence stepper whose step buttons are expanding icon-links.
 * - Header renders displayTitle, body (lead-in) and instruction.
 * - Nav holds one button per step: an icon at rest plus a label that expands
 *   on hover, keyboard focus and for the current step (aria-current="step",
 *   set by the view). data-labels="always" keeps labels expanded on desktop.
 * - A polite role="status" live region reports progress (written by the view).
 * - Every step panel is rendered (so all activities are visible without JS);
 *   the view hides all but the current one after mount and uses each panel as
 *   the focus target for Back/Next.
 * - Actions: Back, Mark step complete, Next. Labels come from schema globals.
 *
 * All fixed learner-facing strings come from _globals (single source of truth).
 * Authored per-step label and activity HTML come from the model.
 */
export default function ExpandingLinks(props) {
  const {
    _id,
    _globals = {},
    _elGlobals = {},
    _stepsResolved = [],
    _labelDisplay
  } = props;

  // Minimal {{number}}/{{label}} interpolation for the initial accessible name;
  // the view rewrites aria-label on render to add the completed state.
  const stepName = (number, label) =>
    (_elGlobals.stepLabel || 'Step {{number}}: {{label}}')
      .replace('{{number}}', number)
      .replace('{{label}}', label || '');

  return (
    <div className="component__inner grow-expanding-links__inner">

      <templates.header {...props} />

      <div className="component__widget grow-expanding-links__widget">

        <nav
          className="grow-expanding-links__nav js-grow-el-nav"
          aria-label={_elGlobals.navAriaLabel}
          data-labels={_labelDisplay === 'always' ? 'always' : undefined}
        >
          {_stepsResolved.map((step) => (
            <button
              key={step._index}
              type="button"
              className="grow-expanding-links__step-btn js-grow-el-step"
              data-complete="false"
              aria-label={stepName(step._number, step.label)}
            >
              {step._iconIsSvg
                ? (
                  <span
                    className="grow-expanding-links__icon"
                    aria-hidden="true"
                    dangerouslySetInnerHTML={{ __html: step._icon }}
                  />
                )
                : (
                  <span
                    className="grow-expanding-links__icon material-symbols-outlined"
                    aria-hidden="true"
                  >
                    {step._icon}
                  </span>
                )}
              <span className="grow-expanding-links__label" aria-hidden="true">
                <span>
                  <span className="grow-expanding-links__label-text">{step.label}</span>
                </span>
              </span>
              <span className="grow-expanding-links__check" aria-hidden="true">{'✓'}</span>
            </button>
          ))}
        </nav>

        <p
          id={`${_id}-status`}
          className="grow-expanding-links__status js-grow-el-status"
          role="status"
          aria-live="polite"
          aria-atomic="true"
        >
          {/* Progress text written by the view */}
        </p>

        <div className="grow-expanding-links__panels">
          {_stepsResolved.map((step) => (
            <section
              key={step._index}
              className="grow-expanding-links__panel js-grow-el-panel"
              tabIndex="-1"
              role="group"
              aria-label={step.label}
            >
              <div
                className="grow-expanding-links__panel-inner"
                dangerouslySetInnerHTML={{ __html: compile(step.body || '', props) }}
              />
            </section>
          ))}
        </div>

        <div className="grow-expanding-links__actions">
          <button
            type="button"
            className={classes(['grow-expanding-links__btn grow-expanding-links__back js-grow-el-back'])}
          >
            {_elGlobals.backButton}
          </button>
          <button
            type="button"
            className={classes(['grow-expanding-links__btn grow-expanding-links__complete js-grow-el-complete'])}
          >
            {_elGlobals.markStepButton}
          </button>
          <button
            type="button"
            className={classes(['grow-expanding-links__btn grow-expanding-links__next js-grow-el-next'])}
          >
            {_elGlobals.nextButton}
          </button>
        </div>

      </div>

    </div>
  );
}
