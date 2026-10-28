export default function PageHeader({
  kicker = "Maker lab / 02",
  depth = "d1 / page",
  title = "Learn by taking it apart",
  intro = "A working bench: inspect a model, make something, then compare the result.",
}) {
  return (
    <header className="asset-page-header">
      <span className="asset-page-header__kicker">{kicker}</span>
      <h2 className="asset-page-header__title">
        <span className="asset-page-header__depth">{depth}</span>
        {title}
      </h2>
      <p className="asset-page-header__intro">{intro}</p>
      <svg className="asset-page-header__glyph" viewBox="0 0 64 64" aria-hidden="true" focusable="false">
        <path d="M10 52 52 10l6 6-42 42Zm5-5 5 5m3-13 5 5m3-13 5 5m3-13 5 5M12 10l42 42-6 6L6 16Z" fill="none" stroke="currentColor" strokeWidth="3" strokeLinejoin="round" />
      </svg>
    </header>
  );
}
