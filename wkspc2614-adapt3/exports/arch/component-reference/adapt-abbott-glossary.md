# Glossary Passage  (`glossary`)

- plugin: `adapt-abbott-glossary` (component)
- targetAttribute: `_glossary`
- framework: `>=5.19.1`
- used in this course: no

## Authorable properties

| field | type | req | default | title / help |
|---|---|---|---|---|
| `ariaRegion` | string | yes | "Glossary passage. Select marked terms t |   |
| `_supportedLayout` | string enum: full-width, half-width, both | yes | "full-width" |   |
| `instruction` | string |  | "" |  Instruction text for the glossary passage. |
| `_passage` | array | yes |  | Passage segments The passage as an ordered array of segments. Plain segments have only 'text'; term segments add '_term' with 'term' (headword) and 'definition'. IMPORTANT: Mark exactly 2–8 terms per passage. The schema cannot enforce this constraint on the marked subset; a console warning will appear if violated. |
| `text` | string | yes | "" | Segment text The text of this segment (word, phrase, or sentence). |
| `_term` | object |  |  | Term definition Optional term definition for this segment. Mark only the first use of each term. |
| `term` | string | yes | "" | Headword The glossary headword (may differ from segment text, e.g. 'reference' for 'referencing'). |
| `definition` | string | yes | "" | Definition The definition. First sentence must be self-contained. No contractions. HTML allowed. |

## JSX template(s)

**glossary.jsx**

```jsx
import React from 'react';
import { templates, classes, html, compile } from 'core/js/reactHelpers';

/**
 * Glossary Passage Template
 *
 * Renders a passage of teaching prose with inline marker buttons for
 * term segments. A single definition region beneath shows the expanded term.
 *
 * Design refs: GL-A (accessibility model), GB-4 (view/template)
 */
export default function Glossary(props) {
  const {
    _id,
    body,
    instruction,
    _passage,
    _terms,
    _expandedIndex,
    _globals
  } = props;

  const ariaRegion = _globals?._components?._glossary?.ariaRegion ||
    'Glossary passage. Select marked terms to see their definitions.';

  // Build a map of sourceIndex -> termIndex for quick lookup
  const termMap = new Map();
  (_terms || []).forEach(term => {
    termMap.set(term.sourceIndex, term.termIndex);
  });

  // Get the expanded term if any
  const expandedTerm = _expandedIndex !== null && _terms
    ? _terms[_expandedIndex]
    : null;

  // Definition region ID (shared across all term markers)
  const defRegionId = `${_id}-definition-region`;

  return (
    <div className="component__inner glossary__inner">

      <templates.header {...props} />

      <div
        className={classes([
          'component__widget',
          'glossary__widget'
        ])}
        role="region"
        aria-label={ariaRegion}
      >

        {/* Passage rendered as continuous prose */}
        <div className="glossary__passage">
          {(_passage || []).map((segment, sourceIndex) => {
            const termIndex = termMap.get(sourceIndex);
            const hasTerm = termIndex !== undefined;
            const isExpanded = termIndex === _expandedIndex;
            const markerId = `${_id}-marker-${termIndex}`;
            const term = hasTerm ? _terms[termIndex] : null;

            if (hasTerm && term) {
              // Term segment with marker button
              return (
                <span
                  key={sourceIndex}
                  className={classes([
                    'glossary__segment',
                    'glossary__segment--term',
                    isExpanded && 'is-expanded'
                  ])}
                >
                  <button
                    id={markerId}
                    className={classes([
                      'glossary__marker',
                      'js-glossary-marker'
                    ])}
                    data-index={termIndex}
                    aria-expanded={isExpanded ? 'true' : 'false'}
                    aria-controls={defRegionId}
                  >
                    <span className="glossary__marker-label">
                      Definition of: {term.term}
                    </span>
                    <span className="glossary__marker-text" aria-hidden="true">
                      {segment.text}
                    </span>
                  </button>
                </span>
              );
            } else {
              // Plain segment
              return (
                <span
                  key={sourceIndex}
                  className="glossary__segment"
                >
                  {segment.text}
                </span>
              );
            }
          })}
        </div>

        {/* Definition region (single, beneath passage) */}
        <div
          id={defRegionId}
          className={classes([
            'glossary__definition-region',
            'js-glossary-definition-region',
            _expandedIndex === null && 'u-display-none'
          ])}
          role="region"
          aria-live="polite"
          aria-hidden={_expandedIndex === null ? 'true' : 'false'}
          tabIndex="-1"
        >
          {expandedTerm && (
            <>
              <div className="glossary__definition-header">
                <h4 className="glossary__term-heading js-glossary-term-heading">
                  {expandedTerm.term}
                </h4>
              </div>
              <div
                className="glossary__definition-body js-glossary-definition-body"
                dangerouslySetInnerHTML={{ __html: expandedTerm.definition }}
              />
              <button
                className="glossary__back js-glossary-back"
                aria-label={`Back to passage, after the term ${expandedTerm.term}`}
              >
                <span className="glossary__back-icon" aria-hidden="true">↩</span>
                <span className="glossary__back-text">Back to passage</span>
              </button>
            </>
          )}
        </div>

      </div>

    </div>
  );
}
```

## Live example (from this course)

_No instance of this component in the sampled course._

## Files a component like this needs

- `bower.json` — name, `component` (the type string used in JSON), `targetAttribute` (the `_config` key), `displayName`, `main` (the JS entry).
- `properties.schema` — JSON Schema (draft-04) of authorable fields; drives the authoring UI and validation.
- `js/<Name>Model.js` + `js/<Name>View.js` + `js/<name>.js` (registers the component with Adapt).
- `templates/<name>.jsx` — the React template (modern Adapt renders components with JSX, not Handlebars).
- `less/<name>.less` — styles (compiled globally; see adapt-ab-theme for the committed-CSS pattern).
