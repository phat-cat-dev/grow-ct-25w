import React, { useEffect } from 'react';
import a11y from 'core/js/a11y';
import { compile } from 'core/js/reactHelpers';

/**
 * grow-hotgraphic popup body.
 *
 * Shows only the single item that was just activated - this component's
 * `_defaultAction: "popup"` opens one hotspot's content, not a paginated
 * gallery of every hotspot - so there is no back/next control here and no
 * dependency on the stock hotgraphic's pagination-label globals.
 *
 * `id="notify-heading"` on the title is load-bearing: notifyPopup.hbs sets
 * `aria-labelledby="notify-heading"` on the dialog itself, and this popup is
 * rendered with `_showCloseButton: false` (because the close button below
 * replaces it), so nothing else supplies that id.
 */
export default function GrowHotgraphicPopup({ item, onCloseClick }) {

  useEffect(() => {
    a11y.focusFirst($('.grow-hotgraphic-popup'));
  });

  if (!item) return null;

  return (
    <div className="grow-hotgraphic-popup__inner">

      <button
        type="button"
        className="grow-hotgraphic-popup__close btn-icon js-grow-hotgraphic-popup-close"
        onClick={onCloseClick}
      >
        <span className="icon" aria-hidden="true" />
      </button>

      {item.title && (
        <div
          id="notify-heading"
          className="grow-hotgraphic-popup__title"
          role="heading"
          aria-level={a11y.ariaLevel({ level: 'notify' })}
        >
          <div
            className="grow-hotgraphic-popup__title-inner"
            dangerouslySetInnerHTML={{ __html: compile(item.title) }}
          />
        </div>
      )}

      {item.body && (
        <div className="grow-hotgraphic-popup__body">
          <div
            className="grow-hotgraphic-popup__body-inner"
            dangerouslySetInnerHTML={{ __html: compile(item.body) }}
          />
        </div>
      )}

    </div>
  );
}
