/*
 * nav-template.jsx — course navigation bar as a React component.
 *
 * Matched set in this folder, all describing the SAME nav:
 *   nav-template.yaml  the data (authoring input)
 *   nav-template.jsx   this — React component over that data
 *   nav-template.html  one rendered result (static reference)
 *
 * Renders core Adapt NavigationView markup. Adapt wires behaviour off
 * name / data-event / data-order / data-tooltip-id and the js-* classes, so
 * those hooks are preserved verbatim. Buttons render in `order` sequence.
 */

function Icon({ icon }) {
  if (!icon) return null;
  const cls = typeof icon === 'string' ? `icon ${icon}` : 'icon';
  return <span className={cls} aria-hidden="true" />;
}

function ProgressIndicator({ progress }) {
  return (
    <div className="pagelevelprogress__indicator-wrapper">
      <span
        className={`pagelevelprogress__indicator-outer ${(progress.state || []).join(' ')}`}
        style={{ '--adapt-pagelevelprogress-percentage': `${progress.percentage}%` }}
      >
        <span className="pagelevelprogress__indicator">
          <span className="pagelevelprogress__indicator-inner">
            <span className="pagelevelprogress__indicator-bar" />
            <span className="aria-label">{progress.ariaLabel}</span>
          </span>
        </span>
      </span>
    </div>
  );
}

function StatusKeys({ modes, side }) {
  return (
    <div className={`nav__status-keys nav__status-keys--${side}`} role="group" aria-label="Status display">
      {modes.filter(mode => mode.side === side).map(mode => (
        <button key={mode.value} type="button" data-status-key={mode.value} aria-label={`Show ${mode.label}`} title={mode.label} aria-pressed={false}>
          <span className="nav__symbol" aria-hidden="true">{mode.symbol}</span>
        </button>
      ))}
    </div>
  );
}

function StepKey({ step }) {
  return (
    <button type="button" className="nav__step" data-section-step={step.offset} aria-label={step.label} title={step.label}>
      <span className="nav__symbol" aria-hidden="true">{step.symbol}</span>
    </button>
  );
}

function NavButton({ b, authoring }) {
  if (b.kind === 'status') {
    return (
      <div className="nav__spacer nav__status" data-order={b.order} aria-label="Navigation status display">
        <StepKey step={b.steps[0]} />
        <output className="nav__screen" data-nav-status="" aria-live="off">{b.text}</output>
        <StepKey step={b.steps[1]} />
        <StatusKeys modes={b.modes} side="end" />
        <span className="nav__sr" role="status" data-nav-announcement="" />
      </div>
    );
  }
  if (b.kind === 'spacer') {
    return <div className="nav__spacer" aria-hidden="true" data-order={b.order} />;
  }

  const className = ['btn-icon', 'nav__btn', ...(b.classes || [])].join(' ');

  return (
    <button
      type="button"
      className={className}
      name={b.name}
      role={b.kind === 'link' ? 'link' : undefined}
      data-order={b.order}
      data-event={b.event || undefined}
      data-tooltip-id={b.tooltipId || undefined}
      aria-haspopup={b.haspopup || undefined}
      aria-label={b.ariaLabel || b.label || undefined}
      title={b.label || undefined}
      data-panel={b.panel || undefined}
      data-design-only={b.designOnly ? '' : undefined}
      aria-controls={b.panel ? `lesson-${b.panel}-panel` : undefined}
      aria-expanded={b.panel ? 'false' : undefined}
    >
      {b.symbol ? <span className={`icon nav__symbol ${typeof b.icon === 'string' ? b.icon : ''}`} aria-hidden="true">{b.symbol}</span> : <Icon icon={b.icon} />}
      {b.kind === 'progress' && <ProgressIndicator progress={b.progress} />}
      {b.label && <span className="nav__btn-label" aria-hidden="true">{b.label}</span>}
    </button>
  );
}

export default function Nav({ nav, authoring = false }) {
  const buttons = nav.buttons.filter(button => authoring || !button.designOnly).slice().sort((a, b) => (a.order ?? 0) - (b.order ?? 0));
  const render = b => <NavButton key={b.name || b.kind} b={b} authoring={authoring} />;
  return (
    <div role="navigation" aria-label="Course navigation" className={['nav', ...(nav.classes || [])].join(' ')}>
      <div className="nav__inner">
        <div className="nav__start">{buttons.filter(b => b.order < 40).map(render)}</div>
        {buttons.filter(b => b.kind === 'status').map(render)}
        <div className="nav__tools">{buttons.filter(b => b.order > 40).map(render)}</div>
      </div>
    </div>
  );
}
