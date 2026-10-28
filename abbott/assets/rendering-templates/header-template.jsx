/*
 * header-template.jsx — lesson/page hero header (React component).
 *
 * Matched set: header-template.yaml (data + type scale) · header-template.html.
 * Type sizes come from CSS using GROW --ab-core-text-clamp-* tokens (see the
 * .html <style> or the grow theme). The frontmatter shows body (overview prose),
 * meta (key/value), objectives AND bullets.
 */

function Group({ title, items, modifier }) {
  if (!items || !items.length) return null;
  const isBullets = modifier === 'bullets';
  return (
    <div className={`frontmatter__group frontmatter__group--${modifier}`}>
      {title && <p className="frontmatter__group-title">{title}</p>}
      <ul className={`frontmatter__items${isBullets ? ' frontmatter__items--bullets' : ''}`}>
        {items.map((t, i) => (
          <li key={i} className={`frontmatter__item frontmatter__item--${isBullets ? 'bullet' : 'objective'}`}>{t}</li>
        ))}
      </ul>
    </div>
  );
}

function Frontmatter({ fm }) {
  if (!fm) return null;
  return (
    <header className="frontmatter frontmatter--lesson" data-grow-role="lesson">
      {fm.eyebrow && <p className="frontmatter__eyebrow">{fm.eyebrow}</p>}
      {fm.body && <div className="frontmatter__body"><p>{fm.body}</p></div>}

      {fm.meta && (
        <dl className="frontmatter__list">
          {Object.entries(fm.meta).map(([key, value]) => (
            <div key={key} className={`frontmatter__item frontmatter__item--${key}`}>
              <dt className="frontmatter__label">{key}</dt>
              <dd className="frontmatter__value">{value}</dd>
            </div>
          ))}
        </dl>
      )}

      <Group title={fm.objectivesTitle} items={fm.objectives} modifier="objectives" />
      <Group title={fm.bulletsTitle} items={fm.bullets} modifier="bullets" />
    </header>
  );
}

export default function Header({ header }) {
  return (
    <header
      className={`page__header asset-hero asset-hero--${header.variant || 'dots'}`}
      data-hero-playing="true"
    >
      <div className="asset-hero__art" aria-hidden="true" />
      <div className="page__header-inner asset-hero__content">
        {header.kicker && <p className="page__subtitle asset-hero__kicker">{header.kicker}</p>}
        <h1 className="page__title asset-hero__title">{header.title}</h1>
        {header.frontmatter && (
          <div className="page__body"><Frontmatter fm={header.frontmatter} /></div>
        )}
      </div>
    </header>
  );
}
