/*
 * lesson-page.jsx — grow lesson page as a React component.
 *
 * One of a matched set in this folder, all describing the SAME lesson:
 *   lesson-page.yaml  the data (authoring input)
 *   lesson-page.hbs   Handlebars template over that data
 *   lesson-page.jsx   this — React component over that data
 *   lesson-page.html  one rendered result (static starter)
 *
 * Props: { page } — the lesson object (see lesson-page.yaml for the shape).
 * Renders the same DOM as lesson-page.html: the lesson frontmatter is a
 * <header> INSIDE .page__body, carrying the opening prose as frontmatter__body.
 * Prose fields are plain strings here; swap to a sanitised
 * dangerouslySetInnerHTML if authors write HTML.
 */

// `as` lets the lesson hero render as <header>; nested frontmatter stays <section>.
function Frontmatter({ fm, role, as: Tag = 'section' }) {
  if (!fm) return null;
  return (
    <Tag className={`frontmatter frontmatter--${role}`} data-grow-role={role}>
      {fm.eyebrow && <p className="frontmatter__eyebrow">{fm.eyebrow}</p>}

      {fm.body && (
        <div className="frontmatter__body"><p>{fm.body}</p></div>
      )}

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

      {fm.objectives && (
        <div className="frontmatter__group frontmatter__group--objectives">
          {fm.objectivesTitle && <p className="frontmatter__group-title">{fm.objectivesTitle}</p>}
          <ul className="frontmatter__items">
            {fm.objectives.map((o, i) => (
              <li key={i} className="frontmatter__item frontmatter__item--objective">{o}</li>
            ))}
          </ul>
        </div>
      )}

      {fm.bullets && (
        <div className="frontmatter__group frontmatter__group--bullets">
          {fm.bulletsTitle && <p className="frontmatter__group-title">{fm.bulletsTitle}</p>}
          <ul className="frontmatter__items frontmatter__items--bullets">
            {fm.bullets.map((b, i) => (
              <li key={i} className="frontmatter__item frontmatter__item--bullet">{b}</li>
            ))}
          </ul>
        </div>
      )}
    </Tag>
  );
}

function Component({ c }) {
  const attrs = {
    className: `component ${c.type}`,
    'data-slot': c.slot,
    ...(c.variant ? { 'data-variant': c.variant } : {}),
  };

  let inner;
  switch (c.type) {
    case 'mcq':
      inner = (
        <fieldset className="component__widget">
          <legend className="component__title">{c.stem}</legend>
          {c.options.map((o, i) => (
            <label key={i} className="mcq__option">
              <input type="radio" name={c.slot} data-correct={o.correct || undefined} />
              <span>{o.text}</span>
            </label>
          ))}
        </fieldset>
      );
      break;
    case 'opentext':
      inner = (
        <>
          <label className="component__title">{c.prompt}</label>
          <textarea className="opentext__input" rows={4} />
        </>
      );
      break;
    case 'references':
      inner = (
        <ol className="component__body references__list">
          {c.items.map((r, i) => <li key={i}>{r}</li>)}
        </ol>
      );
      break;
    default: // text
      inner = (
        <div className="component__body">
          {c.bullets
            ? <ul>{c.bullets.map((b, i) => <li key={i}>{b}</li>)}</ul>
            : <p>{c.body}</p>}
        </div>
      );
  }

  return <div {...attrs}><div className="component__inner">{inner}</div></div>;
}

export default function LessonPage({ page }) {
  return (
    <main
      className="page contentobject"
      id={`lesson-${page.id}`}
      data-adapt-id={page.id}
      data-page-type={page.pageType}
    >
      <div className="page__inner">

        <header className="page__header asset-hero asset-hero--dots" data-hero-playing="true">
          <div className="asset-hero__art" aria-hidden="true" />
          <div className="page__header-inner asset-hero__content">
            {page.subtitle && <p className="page__subtitle asset-hero__kicker">{page.subtitle}</p>}
            <h1 className="page__title asset-hero__title">{page.title}</h1>

            {page.frontmatter && (
              <div className="page__body">
                <Frontmatter fm={page.frontmatter} role="lesson" as="header" />
              </div>
            )}
          </div>
        </header>

        <div className="article__container">
          {page.phases.map((ph) => (
            <article
              key={ph.section}
              className={`article article--${ph.section}`}
              id={ph.section}
              data-lesson-phase={ph.phase}
              data-grow-role="phase"
            >
              <div className="article__inner">
                <header className="article__header">
                  {ph.eyebrow && <p className="article__eyebrow">{ph.eyebrow}</p>}
                  {ph.title && <h2 className="article__title">{ph.title}</h2>}
                  {ph.intro && <div className="article__body"><p>{ph.intro}</p></div>}
                </header>

                <div className="block__container">
                  {ph.blocks.map((b, bi) => (
                    // Each block section is a native <details> accordion.
                    // `open` + visible by default (no-JS / reduced-motion safe);
                    // grow-accordion.js arms the trickle reveal, then fades each in
                    // and auto-opens it as trickle unlocks the step.
                    <details
                      key={bi}
                      className="block grow-accordion"
                      data-skeleton-key={b.skeletonKey}
                      data-grow-role="section"
                      data-gate-after={b.gateAfter || undefined}
                      data-reveal="trickle"
                      open
                    >
                      <summary className="block__header grow-accordion__summary">
                        {b.title && <h3 className="block__title">{b.title}</h3>}
                        <span className="grow-accordion__marker icon" aria-hidden="true" />
                      </summary>

                      <div className="block__inner grow-accordion__panel">
                        {b.instruction && <p className="block__instruction">{b.instruction}</p>}
                        <div className="component__container">
                          {b.components.map((c, ci) => <Component key={ci} c={c} />)}
                        </div>
                      </div>
                    </details>
                  ))}
                </div>
              </div>
            </article>
          ))}
        </div>

        {page.navigation && (
          <nav className="page__navigation" aria-label="Lesson navigation">
            {page.navigation.back && (
              <a href={page.navigation.back.href}>{page.navigation.back.label}</a>
            )}
            {page.navigation.continue && (
              <a
                className={`button${page.navigation.continue.primary ? ' button--primary' : ''}`}
                href={page.navigation.continue.href}
              >
                {page.navigation.continue.label}
              </a>
            )}
          </nav>
        )}

      </div>
    </main>
  );
}
