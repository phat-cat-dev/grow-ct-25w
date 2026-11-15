import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * grow-accordion component template.
 *
 * Bootstrap-accordion-shaped markup (.ab.accordion), ARIA accordion pattern:
 * header <button> with aria-expanded + aria-controls; panel role="region"
 * labelled by its header. Visuals from the theme; this supplies structure.
 */
export default function Accordion(props) {
  const {
    _id,
    _items
  } = props;

  const items = _items || [];

  return (
    <div className="component__inner grow-accordion__inner">

      <templates.header {...props} />

      <div className="component__widget grow-accordion__widget">
        <div className="ab accordion">
          {items.map((item, index) => (
            <AccordionItem
              key={item._id || index}
              item={item}
              index={index}
              componentId={_id}
            />
          ))}
        </div>
      </div>

    </div>
  );
}

function AccordionItem({ item, index, componentId }) {
  const headerId = `${componentId}-grow-accordion-h-${index}`;
  const panelId = `${componentId}-grow-accordion-p-${index}`;
  const isOpen = !!item._isOpen;

  return (
    <div className="accordion-item">
      <h3 className="accordion-header" id={headerId}>
        <button
          type="button"
          className={classes(['accordion-button', 'grow-accordion__header-btn', !isOpen && 'collapsed'])}
          data-index={index}
          aria-expanded={isOpen.toString()}
          aria-controls={panelId}
        >
          {item.title}
        </button>
      </h3>
      <div
        id={panelId}
        role="region"
        aria-labelledby={headerId}
        className={classes(['accordion-collapse', isOpen ? 'show' : 'collapse'])}
      >
        <div
          className="accordion-body"
          dangerouslySetInnerHTML={{ __html: compile(item.body) }}
        />
      </div>
    </div>
  );
}
