import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * grow-card component template.
 *
 * Renders the shared header partial, then one or more .ab.card objects in a
 * .grow-card__group (adding .card-group when more than one). Card visuals come
 * entirely from ab-cards.less; this template only supplies structure.
 */
export default function Card(props) {
  const {
    _variant,
    _isGroup,
    _hoverAnimate,
    _tinted,
    _items
  } = props;

  const items = _items || [];
  const isGroup = items.length > 1 || _isGroup;

  return (
    <div className="component__inner grow-card__inner">

      <templates.header {...props} />

      <div className="component__widget grow-card__widget">
        <div className={classes(['grow-card__group', isGroup && 'card-group'])}>
          {items.map((item, index) => (
            <GrowCard
              key={item._id || index}
              item={item}
              fallbackVariant={_variant}
              hoverAnimate={_hoverAnimate}
              tinted={_tinted}
            />
          ))}
        </div>
      </div>

    </div>
  );
}

/**
 * A single .ab.card.
 */
function GrowCard({ item, fallbackVariant, hoverAnimate, tinted }) {
  const graphic = item._graphic || {};
  const link = item._link || {};
  const variant = item._variant || fallbackVariant || 'neutral';

  const hasGraphic = !!graphic.src;
  const hasHeader = !!item.header;
  const hasTitle = !!item.title;
  const hasSubtitle = !!item.subtitle;
  const hasText = !!item.text;
  const hasLink = !!link.url;
  const hasFooter = !!item.footer;
  const withIcon = !!item._withIcon;

  const body = (
    <>
      {hasTitle && <h3 className="card-title">{item.title}</h3>}
      {hasSubtitle && <div className="card-subtitle">{item.subtitle}</div>}
      {hasText && (
        <div
          className="card-text"
          dangerouslySetInnerHTML={{ __html: compile(item.text) }}
        />
      )}
      {hasLink && (
        <a className="card-link" href={link.url}>{link.text || link.url}</a>
      )}
    </>
  );

  return (
    <div className={classes(['ab', 'card', variant, withIcon && 'with-icon', hoverAnimate && 'hover-animate', tinted && 'tinted'])}>

      {hasGraphic && (
        <img className="card-img-top" src={graphic.src} alt={graphic.alt || ''} />
      )}

      {hasHeader && (
        <div className="card-header">{item.header}</div>
      )}

      <div className="card-body">
        {withIcon ? (
          <>
            <span className={classes(['card-icon', item._icon && 'icon', item._icon])} aria-hidden="true" />
            <div className="card-body__text">{body}</div>
          </>
        ) : body}
      </div>

      {hasFooter && (
        <div className="card-footer">{item.footer}</div>
      )}

    </div>
  );
}
