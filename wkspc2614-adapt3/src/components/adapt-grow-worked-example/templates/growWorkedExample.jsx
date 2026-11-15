import React from 'react';
import { classes, compile } from 'core/js/reactHelpers';

/**
 * Worked Example Template
 *
 * A collapsible accordion: the title is a toggle button that opens a region
 * holding the worked-example prose. Collapsed by default; the view
 * completes the component on first open (passing the trickle) - there is
 * nothing to tick, so opening is the whole gate. The we-weaker/we-stronger
 * cue classes on the body's paragraphs are already baked in by
 * merge-context.js's wrapProse() before this template ever renders.
 *
 * Accessibility: the toggle is a real <button> with aria-expanded /
 * aria-controls; the region is labelled by the heading.
 *
 * Cloned from adapt-grow-checklist's template, stripped of the
 * fieldset/checkbox/progress machinery this component doesn't need.
 *
 * BEM prefix note: the root element's auto-generated class is `growworkedexample`
 * (Adapt's ComponentView lowercases `_component` - "growWorkedExample" has no
 * hyphen to preserve), so the BEM block name here is `growworkedexample`, not
 * `worked-example`, to stay nested under that root in the LESS.
 */
export default function WorkedExample(props) {
  const {
    _id,
    displayTitle,
    body,
    _globals
  } = props;

  const ariaRegion = _globals?._components?._growWorkedExample?.ariaRegion ||
    'Worked example. Expand to read it.';

  const regionId = `${_id}-growworkedexample-region`;
  const headingId = `${_id}-growworkedexample-heading`;

  return (
    <div className="component__inner growworkedexample__inner">

      {/* Accordion toggle: the title opens the worked example. Collapsed by
          default; the view calls setCompletionStatus() on first open. */}
      <h3 className="growworkedexample__heading" id={headingId}>
        <button
          type="button"
          className="growworkedexample__toggle js-growworkedexample-toggle"
          aria-expanded="false"
          aria-controls={regionId}
        >
          <span
            className="growworkedexample__toggle-title"
            dangerouslySetInnerHTML={{ __html: compile(displayTitle || 'Worked example') }}
          />
          <span className="growworkedexample__toggle-icon" aria-hidden="true"></span>
        </button>
      </h3>

      <div
        id={regionId}
        className={classes([
          'component__widget',
          'growworkedexample__widget',
          'growworkedexample__region'
        ])}
        role="region"
        aria-labelledby={headingId}
        aria-label={ariaRegion}
      >

        {body && (
          <div
            className="growworkedexample__body"
            dangerouslySetInnerHTML={{ __html: compile(body) }}
          />
        )}

      </div>

    </div>
  );
}
