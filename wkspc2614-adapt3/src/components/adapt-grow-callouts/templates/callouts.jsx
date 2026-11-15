import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * grow-callouts component template.
 *
 * Renders the shared header partial, then one or more .ab.callout objects in a
 * .grow-callouts__group (adding .is-group when more than one). Callout visuals
 * come entirely from the .ab.callout system (ab-base-callout.less / the brand
 * grow-callouts.less); this template only supplies structure.
 */
export default function Callouts(props) {
  const {
    _variant,
    _isGroup,
    _items
  } = props;

  const items = _items || [];
  const isGroup = items.length > 1 || _isGroup;

  return (
    <div className="component__inner grow-callouts__inner">

      <templates.header {...props} />

      <div className="component__widget grow-callouts__widget">
        <div className={classes(['grow-callouts__group', isGroup && 'is-group'])}>
          {items.map((item, index) => (
            <GrowCallout
              key={item._id || index}
              item={item}
              fallbackVariant={_variant}
            />
          ))}
        </div>
      </div>

    </div>
  );
}

/**
 * A single .ab.callout.
 */
function GrowCallout({ item, fallbackVariant }) {
  const variant = item._variant || fallbackVariant || 'neutral';

  const hasTitle = !!item.title;
  const hasText = !!item.text;
  const withIcon = !!item._withIcon;

  return (
    <div className={classes(['ab', 'callout', variant, withIcon && 'with-icon'])}>

      {withIcon && (
        <span className={classes(['callout-icon', item._icon && 'icon', item._icon])} aria-hidden="true" />
      )}

      <div className="callout-body">
        {hasTitle && <p className="callout-title">{item.title}</p>}
        {hasText && (
          <div
            className="callout-text"
            dangerouslySetInnerHTML={{ __html: compile(item.text) }}
          />
        )}
      </div>

    </div>
  );
}
