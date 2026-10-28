# Annotated Exemplar  (`annotated`)

- plugin: `adapt-abbott-annotated` (component)
- targetAttribute: `_annotated`
- framework: `>=5.19.1`
- used in this course: no

## Authorable properties

| field | type | req | default | title / help |
|---|---|---|---|---|
| `ariaRegion` | string | yes | "Annotated text passage. Select marked p |   |
| `_supportedLayout` | string enum: full-width, half-width, both | yes | "full-width" |   |
| `instruction` | string |  | "" |  Instruction text for the annotated exemplar. |
| `_passage` | array | yes |  | Passage segments The passage as an ordered array of segments. Plain segments have only 'text'; annotated segments add '_note' with 'title' and 'body'. |
| `text` | string | yes | "" | Segment text The text of this segment (sentence or phrase). |
| `_note` | object |  |  | Note Optional explanatory note for this segment. |
| `title` | string |  | "" | Note title Short heading for the note (e.g. 'Clear thesis statement'). |
| `body` | string | yes | "" | Note body The explanatory commentary. HTML allowed. |

## JSX template(s)

**annotated.jsx**

```jsx
import React from 'react';
import { templates, classes, html, compile } from 'core/js/reactHelpers';

/**
 * Annotated Exemplar Template
 *
 * Renders a passage of sample text with inline marker buttons for
 * annotated segments. A single note region beneath shows the expanded note.
 *
 * Design refs: AE-A (accessibility model), AB-4 (view/template)
 */
export default function Annotated(props) {
  const {
    _id,
    body,
    instruction,
    _passage,
    _notes,
    _expandedIndex,
    _globals
  } = props;

  const ariaRegion = _globals?._components?._annotated?.ariaRegion ||
    'Annotated text passage. Select marked phrases to see explanatory notes.';

  // Build a map of sourceIndex -> noteIndex for quick lookup
  const noteMap = new Map();
  (_notes || []).forEach(note => {
    noteMap.set(note.sourceIndex, note.noteIndex);
  });

  // Get the expanded note if any
  const expandedNote = _expandedIndex !== null && _notes
    ? _notes[_expandedIndex]
    : null;

  return (
    <div className="component__inner annotated__inner">

      <templates.header {...props} />

      <div
        className={classes([
          'component__widget',
          'annotated__widget'
        ])}
        role="region"
        aria-label={ariaRegion}
      >

        {/* Passage rendered as continuous prose */}
        <div className="annotated__passage">
          {(_passage || []).map((segment, sourceIndex) => {
            const noteIndex = noteMap.get(sourceIndex);
            const hasNote = noteIndex !== undefined;
            const isExpanded = noteIndex === _expandedIndex;
            const markerId = `${_id}-marker-${noteIndex}`;
            const noteRegionId = `${_id}-note-region`;

            if (hasNote) {
              // Annotated segment with marker button
              return (
                <span
                  key={sourceIndex}
                  className={classes([
                    'annotated__segment',
                    'annotated__segment--annotated',
                    isExpanded && 'is-expanded'
                  ])}
                >
                  <span className="annotated__segment-text">
                    {segment.text}
                  </span>
                  <button
                    id={markerId}
                    className={classes([
                      'annotated__marker',
                      'js-annotated-marker'
                    ])}
                    data-index={noteIndex}
                    aria-expanded={isExpanded ? 'true' : 'false'}
                    aria-controls={noteRegionId}
                  >
                    <span className="annotated__marker-label">
                      Note {noteIndex + 1}
                    </span>
                    <span className="annotated__marker-number" aria-hidden="true">
                      {noteIndex + 1}
                    </span>
                  </button>
                </span>
              );
            } else {
              // Plain segment
              return (
                <span
                  key={sourceIndex}
                  className="annotated__segment"
                >
                  {segment.text}
                </span>
              );
            }
          })}
        </div>

        {/* Note region (single, beneath passage) */}
        <div
          id={`${_id}-note-region`}
          className={classes([
            'annotated__note-region',
            'js-annotated-note-region',
            _expandedIndex === null && 'u-display-none'
          ])}
          role="region"
          aria-live="polite"
          aria-hidden={_expandedIndex === null ? 'true' : 'false'}
          tabIndex="-1"
        >
          {expandedNote && (
            <>
              <div className="annotated__note-header">
                <h4 className="annotated__note-title js-annotated-note-title">
                  {expandedNote.title}
                </h4>
                <p className="annotated__note-referent js-annotated-note-referent">
                  "{expandedNote.text}"
                </p>
              </div>
              <div
                className="annotated__note-body js-annotated-note-body"
                dangerouslySetInnerHTML={{ __html: expandedNote.body }}
              />
              <button
                className="annotated__back js-annotated-back"
                aria-label={`Back to passage, after note ${_expandedIndex + 1}`}
              >
                <span className="annotated__back-icon" aria-hidden="true">↩</span>
                <span className="annotated__back-text">Back to passage</span>
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
