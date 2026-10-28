import React from 'react';
import { templates, compile } from 'core/js/reactHelpers';

export default function References(props) {
  const { _items } = props;
  const items = _items || [];

  return (
    <div className="component__inner references__inner">
      <templates.header {...props} />
      <div className="component__widget references__widget">
        <ul className="references__list">
          {items.map((item, index) => (
            <li key={index} className="references__item">
              <a
                href={item.href}
                className="references__link"
                target="_blank"
                rel="noopener"
              >
                {compile(item.title)}
              </a>
              {item.permalink && (
                <a
                  href={item.permalink}
                  className="references__permalink"
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
