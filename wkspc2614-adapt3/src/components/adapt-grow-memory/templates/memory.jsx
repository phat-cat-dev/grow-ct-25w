import React from 'react';
import { templates } from 'core/js/reactHelpers';

/**
 * Memory match component template.
 *
 * Renders the header (displayTitle / body / instruction), a polite live region,
 * the shuffled grid of tile buttons, and a visual win-message line.
 *
 * Tiles are native <button>s for free keyboard support. Each face-down tile
 * gets its accessible name from the `tileLabel` global; the view rewrites the
 * name (and announces) as tiles are turned, matched or turned back. The icon /
 * text faces are aria-hidden decoration — the button's name carries the meaning.
 */
export default function Memory(props) {
  const {
    _isEnabled,
    _deck = [],
    _columns = 0,
    _globals = {}
  } = props;

  const ariaRegion = _globals.ariaRegion || '';
  const tileLabelTemplate = _globals.tileLabel || 'Tile {{number}}';

  const interpolate = (template, values) => (template || '').replace(
    /\{\{(\w+)\}\}/g,
    (match, key) => (values[key] !== undefined && values[key] !== null ? values[key] : match)
  );

  // 0 columns = responsive auto-fit (CSS). A positive value fixes the column count.
  const boardStyle = _columns > 0
    ? { gridTemplateColumns: `repeat(${_columns}, minmax(0, 1fr))` }
    : undefined;

  return (
    <div className="component__inner memory__inner">

      <templates.header {...props} />

      <div className="component__widget memory__widget">

        {/* Polite live region: reveals, match / no-match outcomes, and the win. */}
        <div
          className="memory__live js-memory-live"
          aria-live="polite"
          aria-atomic="true"
        />

        <div
          className="memory__board js-memory-board"
          role="group"
          aria-label={ariaRegion}
          style={boardStyle}
        >
          {_deck.map(tile => (
            <button
              key={tile._index}
              type="button"
              className="memory__tile js-memory-tile"
              data-index={tile._index}
              data-pair={tile._pair}
              data-label={tile.label}
              aria-label={interpolate(tileLabelTemplate, { number: tile._number })}
              disabled={!_isEnabled}
            >
              <span className="memory__face" aria-hidden="true">
                {tile.icon
                  ? <span className="memory__icon">{tile.icon}</span>
                  : null}
                {tile.text
                  ? <span className="memory__text">{tile.text}</span>
                  : null}
              </span>
            </button>
          ))}
        </div>

        {/* Visual win message (announced separately via the live region). */}
        <div className="memory__feedback js-memory-feedback" aria-hidden="true" />

      </div>

    </div>
  );
}
