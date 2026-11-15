import React from 'react';
import { templates } from 'core/js/reactHelpers';

export default function Sandbox(props) {
  return (
    <div className="component__inner grow-sandbox__inner">
      <templates.header {...props} />
      <div className="grow-sandbox__box">
        Sandbox component rendered.
      </div>
    </div>
  );
}
