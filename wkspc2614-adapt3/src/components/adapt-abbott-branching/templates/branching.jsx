import React from 'react';
import { templates, compile } from 'core/js/reactHelpers';

/**
 * Branching scenario template. Renders the model's CURRENT node in one of three
 * states and nothing else:
 *   - decision   : the node body + its choices as buttons
 *   - consequence: after a choice, "You chose X" + the consequence + Continue
 *   - outcome    : an ending's body (styled good/poor/neutral) + Start over
 * The view re-renders this whenever navigation state changes.
 */
export default function Branching(props) {
  const {
    _scenario = {},
    _currentNode,
    _pendingChoice,
    _path = []
  } = props;

  const nodes = _scenario._nodes || {};
  const node = nodes[_currentNode] || {};
  const isOutcome = !!node._outcome;
  const pending = (_pendingChoice != null && Array.isArray(node._choices))
    ? node._choices[_pendingChoice]
    : null;
  const step = (_path ? _path.length : 0) + 1;

  return (
    <div className="component__inner branching__inner">

      <templates.header {...props} />

      <div className="component__widget branching__widget">

        {!isOutcome && (
          <p className="branching__step-count" aria-hidden="true">Step {step}</p>
        )}

        {isOutcome ? (
          <div
            className={'branching__outcome branching__outcome--' + node._outcome}
            tabIndex="-1"
            role="status"
          >
            <div
              className="branching__node-body"
              dangerouslySetInnerHTML={{ __html: compile(node.body || '') }}
            />
            <button type="button" className="branching__restart js-branching-restart">
              Start over
            </button>
          </div>
        ) : pending ? (
          <div className="branching__step">
            <div
              className="branching__node-body"
              dangerouslySetInnerHTML={{ __html: compile(node.body || '') }}
            />
            <div className="branching__consequence" tabIndex="-1" role="status">
              <p className="branching__chosen">You chose: {pending.text}</p>
              <div
                className="branching__consequence-body"
                dangerouslySetInnerHTML={{ __html: compile(pending.consequence || '') }}
              />
            </div>
            <button type="button" className="branching__continue js-branching-continue">
              Continue
            </button>
          </div>
        ) : (
          <div className="branching__step">
            <div
              className="branching__node-body"
              dangerouslySetInnerHTML={{ __html: compile(node.body || '') }}
            />
            <div className="branching__choices" role="group" aria-label="Choices">
              {(node._choices || []).map((choice, index) => (
                <button
                  key={index}
                  type="button"
                  className="branching__choice js-branching-choice"
                  data-index={index}
                >
                  <span className="branching__choice-text">{choice.text}</span>
                </button>
              ))}
            </div>
          </div>
        )}

      </div>

    </div>
  );
}
