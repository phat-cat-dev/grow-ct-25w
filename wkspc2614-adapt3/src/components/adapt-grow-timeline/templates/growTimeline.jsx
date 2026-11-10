import React from 'react';
import { compile } from 'core/js/reactHelpers';

/**
 * GROW timeline component template (ported from growTimeline.hbs).
 *
 * Iterates _displayItems (computed by TimelineView to apply the
 * ascending/descending direction) rather than _items directly. Base classes
 * carried over from congen11's grow-timeline renderer; every class, data-*
 * attribute and the js-grow-timeline-toggle hook are preserved for the View JS
 * and the LESS.
 */
export default function Timeline(props) {
  const { title, _displayItems, _reveal } = props;
  return (
    <div className="component__inner grow-timeline__inner">
      <div className="grow-timeline" data-component="grow-timeline">
        {title &&
          <h2 className="grow-timeline__title">{title}</h2>
        }
        <div className="grow-timeline__track">
          {(_displayItems || []).map((item, index) => (
            <div
              key={index}
              className={`grow-timeline__event${item._highlight ? ' grow-timeline__event--highlight' : ''}${_reveal ? ' grow-timeline__event--revealable' : ''}`}
            >
              <div className="grow-timeline__marker" />
              <div className="grow-timeline__content">
                <div className="grow-timeline__date">{item.dateLabel}</div>
                {_reveal ? (
                  item.body ? (
                    <React.Fragment>
                      <button
                        type="button"
                        className="grow-timeline__event-toggle js-grow-timeline-toggle"
                        aria-expanded="false"
                      >
                        <span className="grow-timeline__event-title">{item.title}</span>
                        <span className="grow-timeline__toggle-icon" aria-hidden="true" />
                      </button>
                      <div
                        className="grow-timeline__description"
                        aria-hidden="true"
                        dangerouslySetInnerHTML={{ __html: compile(item.body || '', props) }}
                      />
                    </React.Fragment>
                  ) : (
                    <h4 className="grow-timeline__event-title">{item.title}</h4>
                  )
                ) : (
                  <React.Fragment>
                    <h4 className="grow-timeline__event-title">{item.title}</h4>
                    {item.body &&
                      <div
                        className="grow-timeline__description"
                        dangerouslySetInnerHTML={{ __html: compile(item.body || '', props) }}
                      />
                    }
                  </React.Fragment>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
