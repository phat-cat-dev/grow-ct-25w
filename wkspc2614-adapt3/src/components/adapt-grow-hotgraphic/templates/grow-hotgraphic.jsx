import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * grow-hotgraphic component template.
 *
 * `.grow-hotgraphic__canvas` is deliberately CHILDLESS here - the view injects
 * the fetched, decorated SVG into it imperatively in postRender()/changed().
 * React never touches that subtree on re-render (a childless vnode triggers
 * no child diff), so the live SVG, its generated class hooks AND any current
 * focus inside it all survive every model/device-change re-render. This
 * template must never read an item's `_isVisited` to paint the diagram -
 * that state lives only in the imperative classes the view applies to the
 * SVG nodes.
 *
 * `.grow-hotgraphic__list` is the narrow-band accessible fallback: a plain,
 * always-correct list of native buttons in `_items` order. Shown instead of
 * the SVG below `@ab-cq-wide` (see grow-hotgraphic.less), so a diagram with too
 * little room for its own text remains fully usable.
 */
export default function Hotgraphic(props) {

  const {
    _items,
    _diagram,
    _revealedIndex
  } = props;

  const items = _items || [];
  const diagramTitle = _diagram?.title || '';
  const revealedItem = (_revealedIndex !== null && _revealedIndex !== undefined)
    ? items[_revealedIndex]
    : null;

  return (
    <div className="component__inner grow-hotgraphic__inner">

      <templates.header {...props} />

      <div className="component__widget grow-hotgraphic__widget ab-cq">

        <div className="grow-hotgraphic__canvas" />

        <ol className="grow-hotgraphic__list" aria-label={diagramTitle}>
          {items.map((item, index) => (
            <li key={item._id || index} className="grow-hotgraphic__list-item">
              <button
                type="button"
                className={classes(['grow-hotgraphic__list-btn', 'js-grow-hotgraphic-list-item'])}
                data-grow-hotgraphic-index={index}
              >
                {item.title}
              </button>
            </li>
          ))}
        </ol>

        <div className="grow-hotgraphic__reveal" hidden={!revealedItem}>
          {revealedItem && (
            <div className="grow-hotgraphic__reveal-inner">
              <button
                type="button"
                className={classes(['grow-hotgraphic__reveal-close', 'js-grow-hotgraphic-reveal-close'])}
              >
                <span aria-hidden="true">&times;</span>
                <span className="visually-hidden">Close</span>
              </button>
              <h3 className="grow-hotgraphic__reveal-title">{revealedItem.title}</h3>
              <div
                className="grow-hotgraphic__reveal-body"
                dangerouslySetInnerHTML={{ __html: compile(revealedItem.body || '') }}
              />
            </div>
          )}
        </div>

      </div>
    </div>
  );
}
