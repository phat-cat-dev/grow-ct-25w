// lesson-frontmatter.jsx — the lesson front matter PANEL, data-driven.
//
// Renders every learner-visible item frontmatter_spec.md §4 recommends, in the
// order the spec gives. Presentation only; pair with lesson-frontmatter.css.
// Every section is optional — pass nothing and it drops out — so the same
// component serves a full landing panel or a bare title block.
//
// List props accept string[] (rendered as a checklist) OR a string / node
// (rendered as prose), so "What to expect", "Completing this lesson" and
// "Support & accessibility" can be either.
//
//   <LessonFrontMatter
//     position="Module 2 · Lesson 3"
//     title="Designing for depth"
//     purpose="Consistent courses come from a system, not matching by hand…"
//     overview="You'll explore where colour, type and space come from…"
//     meta={[{ label: "Estimated time", value: "12 min" },
//            { label: "Level", value: "Intermediate" }]}
//     objectives={["Explain …", "Build …", "Toggle …"]}
//     startingKnowledge={["You can read var(--accent)", "You finished Lesson 2"]}
//     materials={["A recent piece of your own feedback", "Ten quiet minutes"]}
//     whatToExpect="Three short activities, then a two-question checkpoint."
//     completion="Reach the checkpoint at the end to complete the lesson."
//     support="Examples are keyboard-navigable and described in text."
//     variant="hero"
//   />
//
// Spec §4 caveat: do not state that an activity is optional, saves answers or
// affects completion unless that is actually configured in Adapt/SCORM. Pass
// only verified copy to `completion`. Admin metadata (owner/review/version) has
// no prop here on purpose — the opening is for learners.

function Lead({ text }) {
  if (!text) return null;
  return typeof text === "string" ? <p className="lesson-fm__purpose">{text}</p> : text;
}

function Prose({ title, content }) {
  if (!content || (Array.isArray(content) && content.length === 0)) return null;
  return (
    <section className="lesson-fm__group">
      {title && <p className="lesson-fm__group-title">{title}</p>}
      {Array.isArray(content) ? (
        <ul className="lesson-fm__list lesson-fm__list--check">
          {content.map((item, i) => <li className="lesson-fm__item" key={i}>{item}</li>)}
        </ul>
      ) : typeof content === "string" ? (
        <div className="lesson-fm__prose"><p>{content}</p></div>
      ) : (
        <div className="lesson-fm__prose">{content}</div>
      )}
    </section>
  );
}

function Checklist({ className, title, items = [] }) {
  if (items.length === 0) return null;
  return (
    <section className={`lesson-fm__group ${className}`}>
      {title && <p className="lesson-fm__group-title">{title}</p>}
      <ul className="lesson-fm__list lesson-fm__list--check">
        {items.map((item, i) => <li className="lesson-fm__item" key={i}>{item}</li>)}
      </ul>
    </section>
  );
}

export default function LessonFrontMatter({
  position,
  title,
  purpose,
  overview,
  meta = [],
  objectivesTitle = "By the end of this lesson, you will be able to:",
  objectives = [],
  startingKnowledgeTitle = "Before you begin",
  startingKnowledge = [],
  materialsTitle = "What you'll need",
  materials = [],
  whatToExpectTitle = "What to expect",
  whatToExpect,
  completionTitle = "Completing this lesson",
  completion,
  supportTitle = "Support & accessibility",
  support,
  variant = "hero",         // "hero" | "compact" | "plain"
  headingLevel = 1,         // 1..6 -> <h1>..<h6>
  role = "lesson",          // grow data-layer role
  className = "",
  ...rest
}) {
  const Heading = `h${Math.min(6, Math.max(1, headingLevel))}`;
  const classes = ["lesson-fm", `lesson-fm--${variant}`, className].filter(Boolean).join(" ");

  const hasDetail = startingKnowledge.length > 0 || materials.length > 0;
  const hasMore = whatToExpect || completion || support;

  return (
    <section className={classes} data-grow-role={role} aria-label="Lesson overview" {...rest}>

      <header className="lesson-fm__head">
        {position && <p className="lesson-fm__position">{position}</p>}
        {title && <Heading className="lesson-fm__title">{title}</Heading>}
        <Lead text={purpose} />
        {overview && (
          typeof overview === "string"
            ? <p className="lesson-fm__overview">{overview}</p>
            : <div className="lesson-fm__overview">{overview}</div>
        )}
        {meta.length > 0 && (
          <ul className="lesson-fm__meta" aria-label="Lesson details">
            {meta.map((item, i) => (
              <li className="lesson-fm__meta-item" key={item.label ?? i}>
                {item.label && <span className="lesson-fm__meta-key">{item.label}</span>}
                <span className="lesson-fm__meta-val">{item.value}</span>
              </li>
            ))}
          </ul>
        )}
      </header>

      {objectives.length > 0 && (
        <div className="lesson-fm__group lesson-fm__group--objectives">
          {objectivesTitle && <p className="lesson-fm__group-title">{objectivesTitle}</p>}
          <ul className="lesson-fm__list">
            {objectives.map((o, i) => <li className="lesson-fm__item" key={i}>{o}</li>)}
          </ul>
        </div>
      )}

      {hasDetail && (
        <div className="lesson-fm__grid">
          <Checklist className="lesson-fm__group--before"
                     title={startingKnowledgeTitle} items={startingKnowledge} />
          <Checklist className="lesson-fm__group--materials"
                     title={materialsTitle} items={materials} />
        </div>
      )}

      {hasMore && (
        <div className="lesson-fm__more">
          <Prose title={whatToExpectTitle} content={whatToExpect} />
          <Prose title={completionTitle} content={completion} />
          <Prose title={supportTitle} content={support} />
        </div>
      )}

    </section>
  );
}
