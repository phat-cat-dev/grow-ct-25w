import React from 'react';
import { compile } from 'core/js/reactHelpers';

export default function Callout(props) {
  const { title, body, _calloutType } = props;
  return (
    <div className="component__inner grow-callout__inner">
      <aside
        className={`grow-callout grow-callout--${_calloutType || 'info'}`}
        data-component="grow-callout"
      >
        {title &&
          <h3 className="grow-callout__title">{title}</h3>
        }
        <div
          className="grow-callout__body"
          dangerouslySetInnerHTML={{ __html: compile(body || '', props) }}
        />
      </aside>
    </div>
  );
}
