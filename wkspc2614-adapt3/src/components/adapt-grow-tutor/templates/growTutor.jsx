import React from 'react';
import { templates } from 'core/js/reactHelpers';

export default function growTutor(props) {
  const tutor = props._tutor || {};
  return (
    <div className="component__inner grow-tutor__inner">
      <templates.header {...props} />
      <div className="component__widget grow-tutor grow-tutor__widget">
        <div className="grow-tutor__rail">
          <span className="grow-tutor__name">{tutor.name || 'Course tutor'}</span>
        </div>
        {tutor.intro && <p className="grow-tutor__intro">{tutor.intro}</p>}
        <nav className="grow-tutor__guide" aria-label="Lesson sections" />
        <div className="grow-tutor__bar" />
      </div>
    </div>
  );
}
