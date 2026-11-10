import React from 'react';
import { templates, compile } from 'core/js/reactHelpers';

/**
 * GROW "show your working" template.
 *
 * Renders an ordered list of working lines. Each line carries its stagger delay
 * (--d) as an inline custom property; the LESS plays them off .is-playing. A
 * line can carry an annotation (the move explained) and, on a check line, a tick
 * SVG that draws on.
 *
 * Authoring note: wrap a substituted value in <mark> inside `eq` to give it the
 * highlight band (e.g. "2(<mark>4</mark>) + 6 = 14").
 *
 * Accessibility: the list reads in order at rest regardless of animation; the
 * tick is aria-hidden and a visually-hidden phrase conveys "this checks out".
 */
export default function ShowWorking(props) {
  const {
    _id,
    _globals,
    _kicker,
    _working = {}
  } = props;

  const steps = _working._steps || [];
  const stagger = Number(_working._stagger) > 0 ? Number(_working._stagger) : 0.3;

  const replayLabel = _globals?.replayButton || 'Replay';
  const checkedLabel = _globals?.checkedAnnouncement || 'this checks out';

  return (
    <div className="component__inner grow-show-working__inner">

      {_kicker &&
        <div className="grow-show-working__tag">{_kicker}</div>
      }

      <templates.header {...props} />

      <div className="component__widget grow-show-working__widget">

        <div className="grow-show-working__stage">
          <ol className="grow-show-working__work">
            {steps.map((step, index) => {
              const delay = `${(index * stagger).toFixed(3)}s`;
              const tickDelay = `${((index * stagger) + stagger).toFixed(3)}s`;
              return (
                <li
                  key={index}
                  className="grow-show-working__wline"
                  style={{ '--d': delay }}
                >
                  <span
                    className="grow-show-working__eq"
                    dangerouslySetInnerHTML={{ __html: compile(step.eq || '', props) }}
                  />
                  {step.ann &&
                    <span
                      className="grow-show-working__ann"
                      dangerouslySetInnerHTML={{ __html: compile(step.ann, props) }}
                    />
                  }
                  {step._isCheck &&
                    <>
                      <svg
                        className="grow-show-working__tick"
                        viewBox="0 0 48 48"
                        style={{ '--d': tickDelay }}
                        aria-hidden="true"
                        focusable="false"
                      >
                        <path
                          className="grow-show-working__edge"
                          pathLength="1"
                          d="M9 26 L21 38 L40 11"
                        />
                      </svg>
                      <span className="grow-show-working__sr-only">{checkedLabel}</span>
                    </>
                  }
                </li>
              );
            })}
          </ol>
        </div>

        <button type="button" className="grow-show-working__replay">
          {replayLabel}
        </button>

      </div>

    </div>
  );
}
