import React from 'react';
import { templates } from 'core/js/reactHelpers';

export default function growPageNotes(props) {
  const launch = props._launch || {};
  const icon = launch._icon || 'edit_note';
  const label = launch.text || 'Show the notes';
  return (
    <div className="component__inner grow-pagenotes__inner">
      <templates.header {...props} />
      <div className="component__widget grow-pagenotes__widget">
        <button
          type="button"
          className="grow-pagenotes__launch"
          data-icon={icon}
          style={{ '--grow-pagenotes-icon': `"${icon}"` }}
          aria-label={label}
          onClick={props.onLaunch}
        >
          <span className="grow-pagenotes__launch-label">{label}</span>
        </button>
      </div>
    </div>
  );
}
