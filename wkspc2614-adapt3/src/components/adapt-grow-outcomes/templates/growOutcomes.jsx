import React from 'react';
import { compile } from 'core/js/reactHelpers';

/**
 * GROW learning-outcomes component template (ported from growOutcomes.hbs).
 *
 * Lead-in + an ordered list of outcomes. Every outcome is rendered, but the
 * View reveals them one at a time (is-revealed / aria-hidden). The reveal
 * button carries a live counter. Every class, data-* attribute and the
 * js-grow-outcomes-reveal / js-grow-outcomes-counter hooks are preserved for
 * the View JS and the LESS.
 */
export default function Outcomes(props) {
  const { body, instruction, _items, _revealButtonText } = props;
  return (
    <div className="component__inner grow-outcomes__inner">
      <div className="grow-outcomes" data-component="grow-outcomes">

        {body &&
          <div
            className="grow-outcomes__lead"
            dangerouslySetInnerHTML={{ __html: compile(body || '', props) }}
          />
        }

        {instruction &&
          <div
            className="grow-outcomes__instruction"
            dangerouslySetInnerHTML={{ __html: compile(instruction || '', props) }}
          />
        }

        <ol className="grow-outcomes__list" aria-live="polite">
          {(_items || []).map((item, index) => (
            <li key={index} className="grow-outcomes__item" aria-hidden="true">
              <span className="grow-outcomes__item-marker" aria-hidden="true" />
              <span
                className="grow-outcomes__item-text"
                dangerouslySetInnerHTML={{ __html: compile(item.text || '', props) }}
              />
            </li>
          ))}
        </ol>

        <div className="grow-outcomes__controls">
          <button
            type="button"
            className="btn-text grow-outcomes__reveal js-grow-outcomes-reveal"
          >
            <span className="grow-outcomes__reveal-label">{_revealButtonText}</span>
            <span className="grow-outcomes__counter js-grow-outcomes-counter" aria-hidden="true" />
          </button>
        </div>

      </div>
    </div>
  );
}
