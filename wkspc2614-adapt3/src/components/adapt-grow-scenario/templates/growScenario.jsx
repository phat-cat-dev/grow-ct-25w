import React from 'react';
import { templates } from 'core/js/reactHelpers';

export default function growScenario(props) {
  const launch = props._launch || {};
  const started = Array.isArray(props._userAnswer) && props._userAnswer.length > 0;
  const label = props._isComplete
    ? (launch.reviewText || 'Review the scenario')
    : started
      ? (launch.resumeText || 'Return to the scenario')
      : (launch.startText || 'Start the scenario');
  return (
    <div className="component__inner grow-scenario__inner">
      <templates.header {...props} />
      <div className="component__widget grow-scenario__widget">
        <button type="button" className="btn-text grow-scenario__launch" onClick={props.onLaunch}>
          {label}
        </button>
      </div>
    </div>
  );
}
