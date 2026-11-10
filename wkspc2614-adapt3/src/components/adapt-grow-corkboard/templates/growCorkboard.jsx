import React from 'react';
import { templates } from 'core/js/reactHelpers';

export default function growCorkboard(props) {
  const notes = props._notes || [];
  const isBrainstorm = props._mode === 'brainstorm';
  const count = Number(props._count) || notes.length || 4;
  const entries = Array.isArray(props._entries) ? props._entries : [];

  return (
    <div className="component__inner grow-corkboard__inner">
      <templates.header {...props} />
      <div
        className={`component__widget grow-corkboard cb-count-${count}${isBrainstorm ? ' is-brainstorm' : ''}`}
        role={isBrainstorm ? 'group' : 'list'}
        aria-label={props.ariaRegion || 'Pinned notes'}
      >
        {notes.map((note, index) => {
          const colour = note._color && note._color !== 'default' ? ` ${note._color}` : '';
          const style = { transform: `rotate(${Number(note._rotation) || 0}deg)` };

          if (isBrainstorm) {
            const inputId = `${props._id}-note-${index}`;
            const heading = note.title || note.text || '';
            return (
              <div key={index} className={`grow-corkboard__note${colour}`} style={style}>
                <label
                  className="grow-corkboard__title"
                  htmlFor={inputId}
                  dangerouslySetInnerHTML={{ __html: heading }}
                />
                <textarea
                  id={inputId}
                  className="grow-corkboard__input"
                  data-index={index}
                  placeholder={note._placeholder || ''}
                  aria-label={heading.replace(/<[^>]*>/g, '')}
                  defaultValue={entries[index] || ''}
                />
              </div>
            );
          }

          return (
            <div
              key={index}
              className={`grow-corkboard__note${colour}`}
              role="listitem"
              style={style}
              dangerouslySetInnerHTML={{ __html: note.text }}
            />
          );
        })}
      </div>
    </div>
  );
}
