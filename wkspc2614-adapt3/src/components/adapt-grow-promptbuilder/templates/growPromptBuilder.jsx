import React from 'react';
import { compile } from 'core/js/reactHelpers';

/**
 * adapt-grow-promptbuilder template (React / 5.x pipeline).
 *
 * Lead-in + one block per prompt part (label, help, quick example chips, an
 * editable field, and an optional dropdown of starters grouped by level), then
 * the live-assembled prompt with copy/clear and a "why" note.
 *
 * The View (adapt-grow-promptbuilder.js) binds events and caches nodes by the
 * classes and data-* attributes emitted here, so every one is preserved exactly:
 *   .grow-promptbuilder (is-ready toggle), .js-pb-input[data-key],
 *   .js-pb-chip[data-key][data-text], .js-pb-starter[data-key],
 *   .js-pb-output, .js-pb-copy, .js-pb-clear.
 */
export default function PromptBuilder(props) {
  const {
    _id,
    displayTitle,
    body,
    instruction,
    _parts,
    _assembledLabel,
    _copyText,
    _clearText,
    _whyText
  } = props;

  return (
    <div className="component__inner grow-promptbuilder__inner">
      <div className="grow-promptbuilder" data-component="grow-promptbuilder">

        {displayTitle &&
          <div
            className="grow-promptbuilder__title"
            role="heading"
            aria-level="3"
            dangerouslySetInnerHTML={{ __html: compile(displayTitle, props) }}
          />
        }
        {body &&
          <div
            className="grow-promptbuilder__lead"
            dangerouslySetInnerHTML={{ __html: compile(body, props) }}
          />
        }
        {instruction &&
          <div
            className="grow-promptbuilder__instruction"
            dangerouslySetInnerHTML={{ __html: compile(instruction, props) }}
          />
        }

        <div className="grow-promptbuilder__parts">
          {(_parts || []).map((part, index) => (
            <div className="grow-promptbuilder__part" key={index}>
              <label
                className="grow-promptbuilder__part-label"
                htmlFor={`${_id}-pb-${part._key}`}
                dangerouslySetInnerHTML={{ __html: compile(part.label || '', props) }}
              />
              {part.help &&
                <div
                  className="grow-promptbuilder__part-help"
                  dangerouslySetInnerHTML={{ __html: compile(part.help, props) }}
                />
              }

              {(part._options && part._options.length)
                ? (
                  // a standalone dropdown whose chosen option IS the value
                  <select
                    id={`${_id}-pb-${part._key}`}
                    className="grow-promptbuilder__input grow-promptbuilder__select js-pb-input"
                    data-key={part._key}
                    defaultValue=""
                  >
                    <option value="">{part.placeholder || 'Choose...'}</option>
                    {part._options.map((opt, oi) => (
                      <option value={opt} key={oi}>{opt}</option>
                    ))}
                  </select>
                )
                : (
                  <React.Fragment>
                    {part._chips && part._chips.length > 0 &&
                      <div className="grow-promptbuilder__chips" role="group" aria-label="Quick examples">
                        {part._chips.map((chip, ci) => (
                          <button
                            type="button"
                            className="grow-promptbuilder__chip js-pb-chip"
                            data-key={part._key}
                            data-text={chip}
                            key={ci}
                          >
                            {chip}
                          </button>
                        ))}
                      </div>
                    }
                    <textarea
                      id={`${_id}-pb-${part._key}`}
                      className="grow-promptbuilder__input js-pb-input"
                      data-key={part._key}
                      rows={2}
                      placeholder={part.placeholder || ''}
                      defaultValue=""
                    />
                    {/* starters dropdown — inserts a full starter into the field above */}
                    {(part._starterGroups && part._starterGroups.length)
                      ? (
                        <select
                          className="grow-promptbuilder__starters js-pb-starter"
                          data-key={part._key}
                          aria-label="Insert a prompt starter"
                          defaultValue=""
                        >
                          <option value="">{part._startersPlaceholder || 'Insert a starter by level…'}</option>
                          {part._starterGroups.map((group, gi) => (
                            <optgroup label={group.label} key={gi}>
                              {(group.items || []).map((item, ii) => (
                                <option value={item} key={ii}>{item}</option>
                              ))}
                            </optgroup>
                          ))}
                        </select>
                      )
                      : (part._starters && part._starters.length)
                        ? (
                          <select
                            className="grow-promptbuilder__starters js-pb-starter"
                            data-key={part._key}
                            aria-label="Insert a prompt starter"
                            defaultValue=""
                          >
                            <option value="">{part._startersPlaceholder || 'Insert a starter…'}</option>
                            {part._starters.map((item, si) => (
                              <option value={item} key={si}>{item}</option>
                            ))}
                          </select>
                        )
                        : null
                    }
                  </React.Fragment>
                )
              }
            </div>
          ))}
        </div>

        <div className="grow-promptbuilder__result">
          <div className="grow-promptbuilder__result-label">{_assembledLabel || 'Your prompt'}</div>
          <output className="grow-promptbuilder__output js-pb-output" aria-live="polite"></output>
          <div className="grow-promptbuilder__actions">
            <button type="button" className="grow-promptbuilder__copy js-pb-copy" disabled>
              <span className="grow-promptbuilder__copy-icon" aria-hidden="true"></span>{_copyText || 'Copy prompt'}
            </button>
            <button type="button" className="grow-promptbuilder__clear js-pb-clear">{_clearText || 'Clear'}</button>
          </div>
        </div>

        {_whyText &&
          <div
            className="grow-promptbuilder__why"
            dangerouslySetInnerHTML={{ __html: compile(_whyText, props) }}
          />
        }

      </div>
    </div>
  );
}
