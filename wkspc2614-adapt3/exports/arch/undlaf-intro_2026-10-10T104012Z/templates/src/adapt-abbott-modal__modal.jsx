import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * Modal launcher template.
 * Header + optional teaser body + a .cm.btn trigger. The trigger opens the
 * authored _popup content in the Adapt notify popup (themed by cm-notify.less).
 */
export default function Modal(props) {
  const {
    _id,
    _isEnabled,
    _isComplete,
    body,
    _trigger
  } = props;

  const triggerText = _trigger?.text || 'Open';
  const triggerAria = _trigger?.ariaLabel || triggerText;
  const triggerIcon = _trigger?._icon || '';   // optional cm icon name, e.g. "learning"

  return (
    <div className="component__inner modal__inner">

      <templates.header {...props} />

      {body && (
        <div
          className="component__body modal__body"
          dangerouslySetInnerHTML={{ __html: compile(body) }}
        />
      )}

      <div className="btn__container modal__btn-container">
        <button
          type="button"
          className={classes([
            'cm btn primary js-modal-trigger',
            _isComplete && 'is-complete'
          ])}
          disabled={_isEnabled === false}
          aria-label={triggerAria}
        >
          {triggerIcon && (
            <span className={`cm icon-${triggerIcon}-svg modal__trigger-icon`} aria-hidden="true" />
          )}
          <span className="modal__trigger-label">{triggerText}</span>
        </button>
      </div>

    </div>
  );
}
