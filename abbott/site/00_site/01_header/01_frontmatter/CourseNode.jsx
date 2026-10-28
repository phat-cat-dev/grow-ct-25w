// CourseNode.jsx — the course node from the learner's point of view.
//
// The course is one coherent concept, so the front page is a concept map and the
// lesson menu at once: the concept sits in the centre and the lessons sit around
// it. Click a lesson, an outcome or a key idea and the map fades back to show
// what connects to it. A plain list view carries the same menu, and it is the
// only view on small screens.
//
// Reads the course record from course_frontmatter_spec.md section 4. Presentation
// only: pair with course-node.css. It shows the learner items from spec section 7
// and nothing administrative (owner, authors, reviewers, version, status, scope
// exclusions, assumptions and misconceptions stay out).
//
//   <CourseNode
//     course={courseRecord}                  // parsed course front matter
//     lessonSummaries={{ "lesson-x-01": "One line about the lesson." }}
//     conceptLabels={{ "concept-other": "Other concept" }}
//     hrefFor={(lesson) => `#/${lesson.lesson_id}`}
//   />
//
// Props
//   course           course record (required)
//   lessonSummaries  { [lesson_id]: string } one line per lesson for the menu
//   conceptLabels    { [concept node id]: string } labels for related concepts
//   hrefFor          (lessonMapEntry) => url. Default "#" + lesson_id
//   progress         { [lesson_id]: "complete" | "current" } from the host, only
//                    when the host has verified it. Omitted: no state is shown.
//   completion       string | node. Verified completion copy only.
//   headingLevel     1..6 for the course title, default 1
//   defaultView      "map" (default) | "list"
//   className        extra class
//
// Spec section 7: do not promise that a lesson is optional, saves answers,
// unlocks the next lesson or affects completion unless that behaviour is verified.
// The component never implies any of it. Order is shown as a suggested path.

import { useId, useMemo, useState } from "react";

const ROLE_LABEL = {
  introduces: "Introduces the idea",
  develops: "Builds the idea",
  applies: "Puts it into practice",
  synthesises: "Pulls it together",
  assesses: "Checks your understanding",
};

const RELATION_LABEL = {
  requires: "Worth knowing first",
  broader: "Part of",
  narrower: "Includes",
  related: "Related to",
  contrasts_with: "Not to be confused with",
  applies: "Builds on",
};
const RELATION_ORDER = ["requires", "broader", "narrower", "applies", "related", "contrasts_with"];

const PROGRESS_LABEL = { complete: "Completed", current: "Up next" };

/* ---------- derived values (exported so a host can reuse them) ---------- */

export function formatMinutes(min) {
  if (!min && min !== 0) return null;
  if (min < 60) return `${min} min`;
  const h = Math.floor(min / 60);
  const m = min % 60;
  return m ? `${h} h ${m} min` : `${h} h`;
}

function humanise(id = "") {
  return id.replace(/^concept-/, "").replace(/[-_]/g, " ").replace(/^./, (c) => c.toUpperCase());
}

/* Ring layout in a 160 x 110 box. Nodes start at the top and run clockwise. */
const BOX = { w: 160, h: 110, cx: 80, cy: 55, rx: 52, ry: 38, nodeW: 30, nodeH: 15, hubR: 17 };

function ringPoint(i, n) {
  const a = -Math.PI / 2 + (i * 2 * Math.PI) / Math.max(n, 1);
  return { x: BOX.cx + BOX.rx * Math.cos(a), y: BOX.cy + BOX.ry * Math.sin(a) };
}

/* Trim a segment so it starts and ends at the edges of the shapes, not the centres. */
function trim(from, to, fromShape, toShape, gap = 1.2) {
  const dx = to.x - from.x;
  const dy = to.y - from.y;
  const len = Math.hypot(dx, dy) || 1;
  const edge = (shape) => {
    if (shape === "hub") return BOX.hubR + gap;
    const tx = dx === 0 ? Infinity : BOX.nodeW / 2 / Math.abs(dx / len);
    const ty = dy === 0 ? Infinity : BOX.nodeH / 2 / Math.abs(dy / len);
    return Math.min(tx, ty) + gap;
  };
  const a = edge(fromShape);
  const b = edge(toShape);
  return {
    x1: from.x + (dx / len) * a,
    y1: from.y + (dy / len) * a,
    x2: to.x - (dx / len) * b,
    y2: to.y - (dy / len) * b,
  };
}

export function deriveCourseView(course = {}, { lessonSummaries = {}, conceptLabels = {} } = {}) {
  const lessons = [...(course.lesson_map || [])]
    .sort((a, b) => (a.sequence ?? 0) - (b.sequence ?? 0))
    .map((l, i, all) => ({
      ...l,
      index: i,
      position: l.sequence ?? i + 1,
      total: all.length,
      summary: l.summary || lessonSummaries[l.lesson_id] || null,
      point: ringPoint(i, all.length),
    }));
  const byId = Object.fromEntries(lessons.map((l) => [l.lesson_id, l]));
  const outcomes = course.outcomes || [];
  const terms = (course.concept || {}).key_terms || [];

  const summed = lessons.reduce((n, l) => n + (l.estimated_duration_minutes || 0), 0);
  const totalMinutes = (course.delivery || {}).estimated_duration_minutes || summed || null;

  /* what each focus lights up */
  const touching = {};
  lessons.forEach((l) => {
    const set = new Set([l.lesson_id]);
    (l.requires_lesson_ids || []).forEach((id) => byId[id] && set.add(id));
    lessons.forEach((o) => (o.requires_lesson_ids || []).includes(l.lesson_id) && set.add(o.lesson_id));
    touching[l.lesson_id] = set;
  });
  const serving = (co) => new Set(lessons.filter((l) => (l.course_outcome_ids || []).includes(co)).map((l) => l.lesson_id));
  const teaching = (t) => new Set(lessons.filter((l) => (l.concept_term_ids || []).includes(t)).map((l) => l.lesson_id));

  /* related concepts, in learner words */
  const relations = RELATION_ORDER.map((p) => ({
    predicate: p,
    label: RELATION_LABEL[p],
    items: ((course.concept || {}).relations || [])
      .filter((r) => r.predicate === p)
      .map((r) => ({ label: conceptLabels[r.target] || humanise(r.target), note: r.note })),
  })).filter((g) => g.items.length);

  /* spokes and prerequisite arrows */
  const hub = { x: BOX.cx, y: BOX.cy };
  const spokes = lessons.map((l) => ({ id: l.lesson_id, ...trim(hub, l.point, "hub", "node") }));
  const needs = [];
  lessons.forEach((l) =>
    (l.requires_lesson_ids || []).forEach((id) => {
      if (byId[id]) needs.push({ from: id, to: l.lesson_id, ...trim(byId[id].point, l.point, "node", "node") });
    })
  );

  return { lessons, byId, outcomes, terms, totalMinutes, touching, serving, teaching, relations, spokes, needs };
}

/* ---------- pieces ---------- */

function Meta({ items }) {
  const shown = items.filter((i) => i.value);
  if (!shown.length) return null;
  return (
    <ul className="course-node__meta" aria-label="Course details">
      {shown.map((i) => (
        <li className="course-node__meta-item" key={i.label}>
          <span className="course-node__meta-key">{i.label}</span>
          <span className="course-node__meta-val">{i.value}</span>
        </li>
      ))}
    </ul>
  );
}

function Checklist({ title, items, className }) {
  if (!items || !items.length) return null;
  return (
    <section className={`course-node__group ${className || ""}`}>
      <h3 className="course-node__group-title">{title}</h3>
      <ul className="course-node__checks">
        {items.map((x, i) => <li key={i}>{x}</li>)}
      </ul>
    </section>
  );
}

/* ---------- the course node ---------- */

export default function CourseNode({
  course,
  lessonSummaries,
  conceptLabels,
  hrefFor = (l) => `#${l.lesson_id}`,
  progress,
  completion,
  headingLevel = 1,
  defaultView = "map",
  className = "",
}) {
  const uid = useId();
  const v = useMemo(() => deriveCourseView(course, { lessonSummaries, conceptLabels }), [course, lessonSummaries, conceptLabels]);
  const [view, setView] = useState(defaultView);
  const [focus, setFocus] = useState(null); // { type: "lesson" | "outcome" | "term", id }

  const c = course || {};
  const concept = c.concept || {};
  const fm = c.frontmatter || {};
  const meta = fm.meta || {};
  const Heading = `h${Math.min(6, Math.max(1, headingLevel))}`;
  const Sub = `h${Math.min(6, Math.max(1, headingLevel) + 1)}`;

  const toggle = (type, id) => setFocus((f) => (f && f.type === type && f.id === id ? null : { type, id }));

  const active = useMemo(() => {
    if (!focus) return null;
    if (focus.type === "lesson") return v.touching[focus.id];
    if (focus.type === "outcome") return v.serving(focus.id);
    return v.teaching(focus.id);
  }, [focus, v]);

  const lit = (id) => !active || active.has(id);
  const selected = focus && focus.type === "lesson" ? v.byId[focus.id] : null;
  const term = focus && focus.type === "term" ? v.terms.find((t) => t.id === focus.id) : null;
  const outcome = focus && focus.type === "outcome" ? v.outcomes.find((o) => o.id === focus.id) : null;

  const needsFirst = (l) => (l.requires_lesson_ids || []).map((id) => v.byId[id]).filter(Boolean);
  const termsOf = (l) => v.terms.filter((t) => (l.concept_term_ids || []).includes(t.id));
  const outcomesOf = (l) => v.outcomes.filter((o) => (l.course_outcome_ids || []).includes(o.id));
  const stateOf = (l) => (progress ? progress[l.lesson_id] : undefined);

  const hasBefore = ((c.audience || {}).prerequisites || {}).knowledge?.length || (c.delivery || {}).materials_required?.length;
  const support = c.support || {};

  return (
    <section
      className={["course-node", className].filter(Boolean).join(" ")}
      data-grow-role="course"
      data-view={view}
      aria-labelledby={`${uid}-title`}
      onKeyDown={(e) => e.key === "Escape" && setFocus(null)}
    >
      {/* opening */}
      <header className="course-node__head">
        {fm.eyebrow && <p className="course-node__eyebrow">{fm.eyebrow}</p>}
        <Heading className="course-node__title" id={`${uid}-title`}>{c.title}</Heading>
        {fm.body && <p className="course-node__overview">{String(fm.body).trim()}</p>}
        <Meta
          items={[
            { label: "Estimated time", value: meta.duration || formatMinutes(v.totalMinutes) },
            { label: "Lessons", value: v.lessons.length ? String(v.lessons.length) : null },
            { label: "Level", value: meta.level },
          ]}
        />
        {concept.through_line && (
          <blockquote className="course-node__throughline">
            <span className="course-node__throughline-key">The question running through this course</span>
            {concept.through_line}
          </blockquote>
        )}
      </header>

      {/* outcomes: also a filter for the map */}
      {v.outcomes.length > 0 && (
        <section className="course-node__section course-node__outcomes" aria-labelledby={`${uid}-outcomes`}>
          <Sub className="course-node__h" id={`${uid}-outcomes`}>{fm.objectivesTitle || "By the end of this course, you will be able to:"}</Sub>
          <ul className="course-node__outcome-list">
            {v.outcomes.map((o) => (
              <li key={o.id}>
                <button
                  type="button"
                  className="course-node__outcome"
                  aria-pressed={!!focus && focus.type === "outcome" && focus.id === o.id}
                  onClick={() => toggle("outcome", o.id)}
                >
                  <span className="course-node__outcome-text">{o.statement}</span>
                  <span className="course-node__outcome-hint">Show lessons</span>
                </button>
              </li>
            ))}
          </ul>
        </section>
      )}

      {/* the concept map and lesson menu */}
      <section className="course-node__section course-node__lessons" aria-labelledby={`${uid}-lessons`}>
        <div className="course-node__bar">
          <Sub className="course-node__h" id={`${uid}-lessons`}>{(fm.menu || {}).title || "Lessons"}</Sub>
          <div className="course-node__view-toggle" role="group" aria-label="Lesson view">
            {[["map", "Map"], ["list", "List"]].map(([k, label]) => (
              <button key={k} type="button" className="course-node__view-btn" aria-pressed={view === k} onClick={() => setView(k)}>
                {label}
              </button>
            ))}
          </div>
        </div>

        {/* map view */}
        <div className="course-node__map" data-active={active ? "true" : "false"}>
          <svg className="course-node__svg" viewBox={`0 0 ${BOX.w} ${BOX.h}`} aria-hidden="true" focusable="false">
            <defs>
              <marker id={`${uid}-arrow`} viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto-start-reverse">
                <path d="M0 0 L6 3 L0 6 z" className="course-node__arrowhead" />
              </marker>
            </defs>
            {v.spokes.map((s, i) => (
              <line
                key={s.id}
                className={`course-node__spoke${lit(s.id) ? "" : " is-dim"}`}
                x1={s.x1} y1={s.y1} x2={s.x2} y2={s.y2}
                pathLength="1"
                style={{ "--i": i }}
              />
            ))}
            {v.needs.map((n) => (
              <line
                key={`${n.from}>${n.to}`}
                className={`course-node__need${active && active.has(n.from) && active.has(n.to) ? " is-lit" : ""}${lit(n.from) && lit(n.to) ? "" : " is-dim"}`}
                x1={n.x1} y1={n.y1} x2={n.x2} y2={n.y2}
                markerEnd={`url(#${uid}-arrow)`}
              />
            ))}
          </svg>

          <div className="course-node__hub" style={{ left: `${(BOX.cx / BOX.w) * 100}%`, top: `${(BOX.cy / BOX.h) * 100}%` }}>
            <span className="course-node__hub-key">The central idea</span>
            <span className="course-node__hub-label">{concept.label || c.title}</span>
          </div>

          {v.lessons.map((l, i) => {
            const st = stateOf(l);
            return (
              <button
                key={l.lesson_id}
                type="button"
                className={`course-node__node${lit(l.lesson_id) ? "" : " is-dim"}${selected && selected.lesson_id === l.lesson_id ? " is-selected" : ""}`}
                data-role={l.role}
                data-state={st}
                aria-pressed={!!selected && selected.lesson_id === l.lesson_id}
                aria-describedby={`${uid}-detail`}
                onClick={() => toggle("lesson", l.lesson_id)}
                style={{ left: `${(l.point.x / BOX.w) * 100}%`, top: `${(l.point.y / BOX.h) * 100}%`, "--i": i }}
              >
                <span className="course-node__num" aria-hidden="true">{l.position}</span>
                <span className="course-node__node-body">
                  <span className="course-node__node-title">{l.title}</span>
                  <span className="course-node__node-role">{st ? PROGRESS_LABEL[st] : ROLE_LABEL[l.role] || ""}</span>
                </span>
              </button>
            );
          })}
        </div>

        {/* detail: what the current focus is, in words */}
        <div className="course-node__detail" id={`${uid}-detail`} aria-live="polite" data-empty={focus ? "false" : "true"}>
          {selected ? (
            <>
              <p className="course-node__detail-key">Lesson {selected.position} of {selected.total}{selected.role ? ` · ${ROLE_LABEL[selected.role]}` : ""}</p>
              <h3 className="course-node__detail-title">{selected.title}</h3>
              {selected.summary && <p className="course-node__detail-text">{selected.summary}</p>}
              <dl className="course-node__facts">
                {selected.estimated_duration_minutes ? (<><dt>Time</dt><dd>{formatMinutes(selected.estimated_duration_minutes)}</dd></>) : null}
                {termsOf(selected).length > 0 && (<><dt>Ideas introduced</dt><dd>{termsOf(selected).map((t) => t.term).join(", ")}</dd></>)}
                {outcomesOf(selected).length > 0 && (<><dt>Moves you towards</dt><dd>{outcomesOf(selected).map((o) => o.statement).join(" ")}</dd></>)}
                {needsFirst(selected).length > 0 && (
                  <>
                    <dt>Suggested before this</dt>
                    <dd>
                      {needsFirst(selected).map((n, i) => (
                        <span key={n.lesson_id}>
                          {i > 0 && ", "}
                          <button type="button" className="course-node__link" onClick={() => toggle("lesson", n.lesson_id)}>{n.title}</button>
                        </span>
                      ))}
                    </dd>
                  </>
                )}
              </dl>
              <a className="course-node__open" href={hrefFor(selected)}>Open lesson {selected.position}</a>
            </>
          ) : term ? (
            <>
              <p className="course-node__detail-key">Key idea</p>
              <h3 className="course-node__detail-title">{term.term}</h3>
              <p className="course-node__detail-text">{term.definition}</p>
              <p className="course-node__detail-note">Lit up: the lessons that teach this idea.</p>
            </>
          ) : outcome ? (
            <>
              <p className="course-node__detail-key">Course outcome</p>
              <h3 className="course-node__detail-title">{outcome.statement}</h3>
              <p className="course-node__detail-note">Lit up: the lessons that move you towards it.</p>
            </>
          ) : (
            <p className="course-node__detail-hint">Select a lesson, an outcome or a key idea to see how they connect. Press Escape to clear.</p>
          )}
        </div>

        {/* list view: the same menu as plain content */}
        <ol className="course-node__list">
          {v.lessons.map((l) => {
            const st = stateOf(l);
            return (
              <li className={`course-node__row${lit(l.lesson_id) ? "" : " is-dim"}`} key={l.lesson_id} data-role={l.role} data-state={st}>
                <span className="course-node__num" aria-hidden="true">{l.position}</span>
                <div className="course-node__row-body">
                  <a className="course-node__row-title" href={hrefFor(l)}>{l.title}</a>
                  <p className="course-node__row-meta">
                    {[st ? PROGRESS_LABEL[st] : null, ROLE_LABEL[l.role], formatMinutes(l.estimated_duration_minutes)].filter(Boolean).join(" · ")}
                  </p>
                  {l.summary && <p className="course-node__row-text">{l.summary}</p>}
                </div>
              </li>
            );
          })}
        </ol>
      </section>

      {/* key ideas */}
      {v.terms.length > 0 && (
        <section className="course-node__section course-node__terms" aria-labelledby={`${uid}-terms`}>
          <Sub className="course-node__h" id={`${uid}-terms`}>Key ideas</Sub>
          <ul className="course-node__chips">
            {v.terms.map((t) => (
              <li key={t.id}>
                <button
                  type="button"
                  className="course-node__chip"
                  aria-pressed={!!focus && focus.type === "term" && focus.id === t.id}
                  onClick={() => toggle("term", t.id)}
                >
                  {t.term}
                </button>
              </li>
            ))}
          </ul>
        </section>
      )}

      {/* where the concept sits */}
      {v.relations.length > 0 && (
        <section className="course-node__section course-node__context" aria-labelledby={`${uid}-context`}>
          <Sub className="course-node__h" id={`${uid}-context`}>Where this idea sits</Sub>
          <dl className="course-node__rels">
            {v.relations.map((g) => (
              <div className="course-node__rel" key={g.predicate} data-predicate={g.predicate}>
                <dt>{g.label}</dt>
                <dd>
                  <ul className="course-node__rel-list">
                    {g.items.map((it) => (
                      <li key={it.label}>
                        {it.label}
                        {it.note && <span className="course-node__rel-note"> ({it.note})</span>}
                      </li>
                    ))}
                  </ul>
                </dd>
              </div>
            ))}
          </dl>
        </section>
      )}

      {/* before you begin */}
      {hasBefore ? (
        <div className="course-node__grid">
          <Checklist className="course-node__group--before" title="Before you begin" items={((c.audience || {}).prerequisites || {}).knowledge} />
          <Checklist className="course-node__group--materials" title="What you'll need" items={(c.delivery || {}).materials_required} />
        </div>
      ) : null}

      {/* completion and support: only what has been supplied and verified */}
      {(completion || support.accessibility_statement || support.help_contact) && (
        <div className="course-node__more">
          {completion && (
            <section className="course-node__group">
              <h3 className="course-node__group-title">Completing this course</h3>
              <div className="course-node__prose">{typeof completion === "string" ? <p>{completion}</p> : completion}</div>
            </section>
          )}
          {(support.accessibility_statement || support.help_contact) && (
            <section className="course-node__group">
              <h3 className="course-node__group-title">Support and accessibility</h3>
              <div className="course-node__prose">
                {support.accessibility_statement && <p>{support.accessibility_statement}</p>}
                {support.help_contact && <p>{support.help_contact}</p>}
              </div>
            </section>
          )}
        </div>
      )}
    </section>
  );
}
