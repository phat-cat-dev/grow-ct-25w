import React from 'react';
import { templates } from 'core/js/reactHelpers';

export default function growAnimations(props) {
  const marks = props._marksHtml || [];
  const layout = props._markLayout || 'inline';
  return (
    <div className="component__inner grow-animations__inner">
      <templates.header {...props} />
      <div className={`component__widget grow-animations__widget grow-animations--${layout}`}>
        {marks.map((html, index) => (
          <span
            key={index}
            className="grow-animations__mark"
            dangerouslySetInnerHTML={{ __html: html }}
          />
        ))}
      </div>
    </div>
  );
}
