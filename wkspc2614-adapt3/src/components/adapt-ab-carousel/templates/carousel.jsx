import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * ab-carousel component template.
 *
 * Bootstrap-carousel-shaped markup (.ab.carousel). Accessible carousel pattern:
 * roledescription carousel/slide, non-current slides aria-hidden, controls and
 * indicators as native buttons, polite live region when not auto-scrolling.
 */
export default function Carousel(props) {
  const {
    _items,
    _activeIndex,
    _shouldAutoScroll,
    ariaRegion
  } = props;

  const items = _items || [];
  const active = _activeIndex || 0;

  return (
    <div className="component__inner ab-carousel__inner">

      <templates.header {...props} />

      <div className="component__widget ab-carousel__widget">
        <div className="ab carousel" aria-roledescription="carousel" aria-label={ariaRegion}>

          <div className="carousel-inner" aria-live={_shouldAutoScroll ? 'off' : 'polite'}>
            {items.map((item, index) => (
              <CarouselSlide
                key={item._id || index}
                item={item}
                index={index}
                total={items.length}
                isActive={index === active}
              />
            ))}
          </div>

          <button type="button" className="carousel-control-prev ab-carousel__prev">
            <span className="carousel-control-prev-icon" aria-hidden="true" />
            <span className="visually-hidden">Previous</span>
          </button>
          <button type="button" className="carousel-control-next ab-carousel__next">
            <span className="carousel-control-next-icon" aria-hidden="true" />
            <span className="visually-hidden">Next</span>
          </button>

          <div className="carousel-indicators">
            {items.map((item, index) => (
              <button
                key={item._id || index}
                type="button"
                data-index={index}
                className={classes(['ab-carousel__indicator', index === active && 'active'])}
                aria-current={(index === active).toString()}
                aria-label={`Slide ${index + 1}`}
              />
            ))}
          </div>

        </div>
      </div>

    </div>
  );
}

function CarouselSlide({ item, index, total, isActive }) {
  const graphic = item._graphic || {};
  const hasGraphic = !!graphic.src;
  const hasTitle = !!item.title;
  const hasCaption = !!item.caption;

  return (
    <div
      role="group"
      aria-roledescription="slide"
      aria-label={`${index + 1} of ${total}`}
      aria-hidden={(!isActive).toString()}
      className={classes(['carousel-item', isActive && 'active'])}
    >
      {hasGraphic && (
        <img className="ab-carousel__image" src={graphic.src} alt={graphic.alt || ''} />
      )}
      {(hasTitle || hasCaption) && (
        <div className="carousel-caption">
          {hasTitle && <h3>{item.title}</h3>}
          {hasCaption && (
            <div dangerouslySetInnerHTML={{ __html: compile(item.caption) }} />
          )}
        </div>
      )}
    </div>
  );
}
