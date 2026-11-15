import React from 'react';
import { templates, compile } from 'core/js/reactHelpers';

export default function References(props) {
  const { _items } = props;
  const items = _items || [];

  return (
    <div className="component__inner grow-references__inner">
      <templates.header {...props} />
      <div className="component__widget grow-references__widget">
        <ul className="grow-references__list">
          {items.map((item, index) => (
            <li key={index} className="grow-references__item">
              <a
                href={item.href}
                className="grow-references__link"
                target="_blank"
                rel="noopener"
              >
                {compile(item.title)}
              </a>
              {item.permalink && (
                <a
                  href={item.permalink}
                  className="grow-references__permalink"
                  target="_blank"
                  rel="noopener"
                >
                  {' '}(permalink)
                </a>
              )}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
