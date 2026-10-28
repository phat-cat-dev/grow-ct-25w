/*
 * menu-template.jsx — GROW's own icon-based course menu (React component).
 *
 * Matched set in this folder, all describing the SAME menu:
 *   menu-template.yaml  the data (authoring input)
 *   menu-template.jsx   this — component over that data, incl. ProgressMeter
 *   menu-template.html  one rendered result (generated from this JSX)
 *
 * This is OUR menu — not adapt-contrib-boxMenu — and OUR progress meter, not
 * adapt-contrib-pageLevelProgress. The meter is a plain SVG ring whose size WE
 * set (--meter-size), so the nav/menu layout is no longer governed by Adapt's
 * pageLevelProgress markup. At runtime, `state` and `value` bind to core
 * completion data (adaptModel `_isComplete` / `_isVisited` bubbling).
 */

// --- OUR progress meter: an SVG ring, sized by the caller (not Adapt). --------
function ProgressMeter({ value = 0, size = 44, stroke = 4, label }) {
  const r = (size - stroke) / 2;
  const circumference = 2 * Math.PI * r;
  const offset = circumference * (1 - Math.max(0, Math.min(100, value)) / 100);
  return (
    <span
      className="progress-meter"
      style={{ '--meter-size': `${size}px` }}
      role="img"
      aria-label={label || `${value}% complete`}
    >
      <svg className="progress-meter__svg" viewBox={`0 0 ${size} ${size}`} width={size} height={size} aria-hidden="true">
        <circle className="progress-meter__track" cx={size / 2} cy={size / 2} r={r} fill="none" strokeWidth={stroke} />
        <circle
          className="progress-meter__value"
          cx={size / 2}
          cy={size / 2}
          r={r}
          fill="none"
          strokeWidth={stroke}
          strokeDasharray={circumference.toFixed(2)}
          strokeDashoffset={offset.toFixed(2)}
          strokeLinecap="round"
          transform={`rotate(-90 ${size / 2} ${size / 2})`}
        />
      </svg>
      <span className="progress-meter__pct" aria-hidden="true">{value}%</span>
    </span>
  );
}

function MenuItem({ item, meterSize }) {
  const isLocked = item.state === 'locked';
  const className = ['menu__item', 'grow-menu__item', `is-${item.state}`].join(' ');
  return (
    <li className={className} data-adapt-id={item.id} data-state={item.state}>
      <a
        className="menu__item-link grow-menu__link"
        href={isLocked ? undefined : `#/id/${item.id}`}
        aria-disabled={isLocked || undefined}
        aria-current={item.state === 'in-progress' ? 'step' : undefined}
      >
        <span className="grow-menu__icon" aria-hidden="true">
          <span className={`icon ${item.icon}`} />
        </span>

        <span className="grow-menu__text">
          {item.subtitle && <span className="grow-menu__subtitle">{item.subtitle}</span>}
          <span className="grow-menu__title">{item.title}</span>
        </span>

        {isLocked ? (
          <span className="grow-menu__lock icon icon-lock" aria-label="Locked" role="img" />
        ) : (
          <ProgressMeter value={item.progress} size={meterSize} label={`${item.title}: ${item.progress}% complete`} />
        )}
      </a>
    </li>
  );
}

export default function Menu({ menu }) {
  const size = menu.meterSize || 44;
  return (
    <nav className={(menu.classes || ['menu']).join(' ')} aria-label={menu.title}>
      {menu.title && <h1 className="menu__title grow-menu__heading">{menu.title}</h1>}
      <ul className="menu__items grow-menu__items">
        {menu.items.map((item) => (
          <MenuItem key={item.id} item={item} meterSize={size} />
        ))}
      </ul>
    </nav>
  );
}
