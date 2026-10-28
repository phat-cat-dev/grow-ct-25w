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
