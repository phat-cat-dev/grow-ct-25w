import React from 'react';
import { compile } from 'core/js/reactHelpers';

/**
 * GROW levels component template (ported from growLevels.hbs).
 *
 * A lead-in + a vertical stack of tiered levels. Each level is a button
 * (badge + title + chevron) with a detail panel (body + an "In practice"
 * advice pop-out). Every class, data-* attribute and the js-grow-levels-card /
 * js-grow-levels-advice hooks are preserved for the View JS and the LESS.
 */
export default function Levels(props) {
  const { displayTitle, body, instruction, _items } = props;
  return (
    <div className="component__inner grow-levels__inner">
      <div className="grow-levels" data-component="grow-levels">

        {displayTitle &&
          <div
            className="grow-levels__title"
            role="heading"
            aria-level="3"
            dangerouslySetInnerHTML={{ __html: compile(displayTitle || '', props) }}
          />
        }

        {body &&
          <div
            className="grow-levels__lead"
            dangerouslySetInnerHTML={{ __html: compile(body || '', props) }}
          />
        }

        {instruction &&
          <div
            className="grow-levels__instruction"
            dangerouslySetInnerHTML={{ __html: compile(instruction || '', props) }}
          />
        }

        <ol className="grow-levels__list">
          {(_items || []).map((item, index) => (
            <li
              key={index}
              className={`grow-levels__item grow-levels__item--${item._tone || 'neutral'}`}
            >
              <button
                type="button"
                className="grow-levels__card js-grow-levels-card"
                aria-expanded="false"
              >
                <span className="grow-levels__badge" aria-hidden="true" />
                <span
                  className="grow-levels__card-title"
                  dangerouslySetInnerHTML={{ __html: compile(item.title || '', props) }}
                />
                <span className="grow-levels__tone-icon" aria-hidden="true" />
                <span className="grow-levels__lock" aria-hidden="true" />
                <span className="grow-levels__chevron" aria-hidden="true" />
              </button>
              <div className="grow-levels__detail" aria-hidden="true">
                {item.body &&
                  <div
                    className="grow-levels__body"
                    dangerouslySetInnerHTML={{ __html: compile(item.body || '', props) }}
                  />
                }
                {item.advice &&
                  <React.Fragment>
                    <button
                      type="button"
                      className="grow-levels__advice-toggle js-grow-levels-advice"
                      aria-expanded="false"
                    >
                      <span className="grow-levels__advice-icon" aria-hidden="true" />In practice
                    </button>
                    <div
                      className="grow-levels__advice"
                      aria-hidden="true"
                      dangerouslySetInnerHTML={{ __html: compile(item.advice || '', props) }}
                    />
                  </React.Fragment>
                }
              </div>
            </li>
          ))}
        </ol>

      </div>
    </div>
  );
}
