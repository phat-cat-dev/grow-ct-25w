import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';
import { resolvePresentation } from '../js/scrollScenesLogic';

/**
 * Scroll-scenes template.
 *
 * Renders only the component's own header plus the scroll engine's markup —
 * the demo workshop chrome (effect/snap pickers, download links) from the
 * original study is deliberately gone. The design dials are resolved from the
 * author's preset + overrides and applied as data-* attributes the CSS reads;
 * the learner just scrolls.
 *
 * Required engine hooks: [data-scroll-viewport], one [data-scroll-scene] per
 * scene, each wrapping a [data-scene-content]. Nav buttons, progress and status
 * are optional and authorable.
 */
export default function ScrollScenes(props) {
  const {
    _id,
    _items,
    _showNav,
    _showProgress,
    _showStatus,
    displayTitle
  } = props;

  const items = _items || [];
  const presentation = resolvePresentation(props);

  const hostAttrs = {};
  if (presentation.scheme && presentation.scheme !== 'default') hostAttrs['data-scheme'] = presentation.scheme;
  if (presentation.background) hostAttrs['data-scene-bg'] = presentation.background;
  if (presentation.transition && presentation.transition !== 'none') hostAttrs['data-scene-transition'] = presentation.transition;

  const showNav = _showNav !== false;
  const showProgress = _showProgress !== false;
  const showStatus = _showStatus !== false;
  const showNavBar = showNav || showProgress || showStatus;

  const pad = index => String(index + 1).padStart(2, '0');
  const viewportLabel = displayTitle ? compile(displayTitle).replace(/<[^>]+>/g, '').trim() : 'Scrollable scenes';

  return (
    <div className="component__inner grow-scroll-scenes__inner">

      <templates.header {...props} />

      <div className="component__widget grow-scroll-scenes__widget">
        <div className="scroll-scenes" {...hostAttrs}>

          {showNavBar && (
            <nav className="scene-nav" aria-label="Choose a scene">
              {showNav && items.map((item, index) => (
                <button type="button" key={index} data-scroll-to={index}>
                  {pad(index)} {item.stageLabel || ''}
                </button>
              ))}
              {showProgress && (
                <progress data-scroll-progress max="1" value="0" aria-label="Scroll progress" />
              )}
              {showStatus && (
                <span className="scene-status" data-scroll-status aria-live="polite" />
              )}
            </nav>
          )}

          <div
            data-scroll-viewport
            tabIndex={0}
            role="region"
            aria-label={viewportLabel}
          >
            {items.map((item, index) => {
              const sceneAttrs = {};
              if (item._background) sceneAttrs['data-scene-bg'] = item._background;
              if (item._colourSlot) sceneAttrs['data-scene-colour'] = item._colourSlot;
              const label = item.stageLabel || `Scene ${index + 1}`;

              return (
                <section
                  data-scroll-scene
                  key={index}
                  aria-label={label}
                  {...sceneAttrs}
                >
                  <div data-scene-content>
                    {item.stageLabel && (
                      <p className="scene-number">{pad(index)} / {String(item.stageLabel).toUpperCase()}</p>
                    )}
                    {item.heading && (
                      <h2 dangerouslySetInnerHTML={{ __html: compile(item.heading) }} />
                    )}
                    {item.body && (
                      <p className="scene-copy" dangerouslySetInnerHTML={{ __html: compile(item.body) }} />
                    )}
                    <SceneExtras extras={item._extras} />
                  </div>
                </section>
              );
            })}
          </div>

        </div>
      </div>

    </div>
  );
}

/**
 * Optional per-scene teaching extras. Mirrors the lead-ins the retired
 * scenes.py renderer produced, so content authored for the old pipeline reads
 * the same here.
 */
function SceneExtras({ extras }) {
  if (!extras) return null;

  const parts = [];
  const push = (key, lead, html, extraClass) => {
    parts.push(
      <p className={classes(['scene-extra', extraClass])} key={key}>
        {lead && <strong>{lead} </strong>}
        <span dangerouslySetInnerHTML={{ __html: compile(html) }} />
      </p>
    );
  };

  if (extras.questionPrompt) push('q', 'Ask yourself:', extras.questionPrompt);
  if (extras.microTask && extras.microTask.instruction) {
    const minutes = extras.microTask.minutes;
    const lead = minutes ? `Try this (${minutes} min):` : 'Try this:';
    push('t', lead, extras.microTask.instruction);
  }
  if (extras.evidenceCue) push('e', 'You will know it worked when:', extras.evidenceCue);
  if (extras.reflectionNote) push('r', 'In your notes:', extras.reflectionNote);
  if (extras.transitionCue) push('c', null, extras.transitionCue, 'scene-cue');

  if (!parts.length) return null;
  // Return the keyed array directly (valid in React) rather than a fragment,
  // so the template does not depend on JSX fragment-shorthand support.
  return parts;
}
