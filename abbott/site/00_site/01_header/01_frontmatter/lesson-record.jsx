// LessonRecord.jsx — the lesson record template (lesson-record.hbs) as React.
//
// Renders exactly the same markup and class names as lesson-record.hbs, so
// lesson-record.skin.css (and lesson-record.inspect.js / .css) work unchanged.
// Presentation only: no state, no effects, no styling. Accordions are native
// <details>, cross references are plain anchors, so it works without hydration.
//
//   import LessonRecord from "./LessonRecord.jsx";
//
//   <LessonRecord record={lessonYaml} course={courseYaml} />
//
// `record`  the lesson front matter (frontmatter_spec.md section 3), as parsed.
// `course`  the course record: language, learner_pitch, voice_specification,
//           referencing_style, rights, lesson_count, outcomes[{ id, statement }].
// `closed`  optional string[] of group ids that start collapsed.
//           Default: ["lifecycle", "review"].
// `staticCount` how many leading groups are always open sections rather than
//           accordions. Default 2 (Identity, Place in the course).
// `tools`   optional node for the bar's tools slot. Leave it out to keep the
//           empty [data-lr-tools] slot that lesson-record.inspect.js fills.
//
// The view model (position, aligned flags, closed-state summaries) is derived
// here, so nothing needs to be precomputed. deriveViewModel is exported for
// tests and for anything that wants the same derived values.
//
// Treat the output as a display view of the authoritative metadata, not a second
// source of truth (frontmatter_spec.md section 5).

const KIND_LABEL = {
  define: "Defined here",
  inherit: "Inherited",
  derive: "Derived",
  internal: "Kept internal",
};

const LEGEND = [
  ["define", "Defined here (per lesson)"],
  ["inherit", "Inherited (from course)"],
  ["derive", "Derived (automatic)"],
  ["internal", "Kept internal (never shown to learners)"],
];

const count = (a) => (a || []).length;

export function deriveViewModel(record = {}, course = {}) {
  const served = new Set((record.alignment || {}).course_outcome_ids || []);
  const assessment = record.assessment || {};
  return {
    served,
    outcomes: (course.outcomes || []).map((o) => ({ ...o, aligned: served.has(o.id) })),
    position: `Lesson ${record.sequence}${course.lesson_count ? ` of ${course.lesson_count}` : ""}`,
    summaries: {
      inherited: `${course.language}, ${course.learner_pitch} pitch`,
      scope: (record.scope || {}).focus || "",
      co: `${served.size} of ${count(course.outcomes)} served by this lesson`,
      lo: `${count(record.learning_outcomes)} lesson outcomes`,
      act: `${count(record.activities)} activities`,
      assessment: `${assessment.purpose || "none"}, covers ${count(assessment.lesson_outcome_ids)} outcomes`,
      prereq: record.estimated_duration_minutes ? `${record.estimated_duration_minutes} minutes` : "No duration set",
      lifecycle: `v${record.version}, ${record.status}, owned by ${record.owner}`,
      review: `Academic review ${(record.review || {}).academic_status || "pending"}`,
      opening: (record.frontmatter || {}).eyebrow || "Before you begin",
    },
  };
}

/* ---------- small pieces ---------- */

const Empty = ({ children = "Not set" }) => <span className="lr-empty">{children}</span>;
const Code = ({ children }) => <code className="lr-code">{children}</code>;

const Row = ({ label, children }) => (
  <div className="lr-dl__row">
    <dt>{label}</dt>
    <dd>{children}</dd>
  </div>
);

const Dl = ({ children }) => <dl className="lr-dl">{children}</dl>;

function List({ items, empty = "None yet" }) {
  return (
    <ul className="lr-list">
      {count(items) ? items.map((x, i) => <li key={i}>{x}</li>) : <li className="lr-empty">{empty}</li>}
    </ul>
  );
}

function Tags({ items, code, empty = "None yet" }) {
  return (
    <ul className="lr-tags">
      {count(items) ? (
        items.map((x, i) => (
          <li className="lr-tag" key={i}>
            {code ? <Code>{x}</Code> : x}
          </li>
        ))
      ) : (
        <li className="lr-empty">{empty}</li>
      )}
    </ul>
  );
}

const Refs = ({ ids = [] }) => (
  <ul className="lr-refs">
    {ids.map((id) => (
      <li key={id}>
        <a className="lr-ref" href={`#${id}`}>{id}</a>
      </li>
    ))}
  </ul>
);

const Value = ({ value }) => (value ? <>{value}</> : <Empty />);
const When = ({ value }) => (value ? <time dateTime={value}>{value}</time> : <Empty />);

/* One section card. The first `staticCount` are always-open <section>s,
   the rest are <details> accordions. */
function Group({ n, id, kind, title, summary, note, isStatic, isOpen, children }) {
  const slug = GROUP_IDS[id] || id;
  const head = (Tag, extra) => (
    <Tag className="lr-group__summary">
      <span className="lr-group__num" aria-hidden="true">{String(n).padStart(2, "0")}</span>
      <h3 className="lr-group__title" id={`lr-h-${slug}`}>{title}</h3>
      <span className="lr-badge">{KIND_LABEL[kind]}</span>
      {extra}
    </Tag>
  );
  const body = (
    <div className="lr-group__body">
      {note && <p className="lr-note">{note}</p>}
      {children}
    </div>
  );
  const common = { "data-group": id, "data-kind": kind, "aria-labelledby": `lr-h-${slug}` };
  return (
    <li className="lr__item">
      {isStatic ? (
        <section className="lr-group lr-group--static" id={`lr-${slug}`} {...common}>
          {head("header")}
          {body}
        </section>
      ) : (
        <details className="lr-group" id={`lr-${slug}`} {...common} open={isOpen || undefined}>
          {head("summary", <span className="lr-group__sum">{summary}</span>)}
          {body}
        </details>
      )}
    </li>
  );
}

/* anchor ids that differ from the data-group name, as in lesson-record.hbs */
const GROUP_IDS = {
  "course-outcomes": "co",
  "lesson-outcomes": "lo",
  activities: "act",
  prerequisites: "prereq",
};

/* ---------- the record ---------- */

export default function LessonRecord({ record, course = {}, closed = ["lifecycle", "review"], staticCount = 2, tools }) {
  const vm = deriveViewModel(record, course);
  const r = record;
  const c = course;
  const rights = c.rights || {};
  const fm = r.frontmatter || {};
  const meta = fm.meta || {};
  const scope = r.scope || {};
  const prereq = r.prerequisites || {};
  const assessment = r.assessment || {};
  const review = r.review || {};

  let n = 0;
  const g = (props) => {
    n += 1;
    return (
      <Group
        n={n}
        isStatic={n <= staticCount}
        isOpen={!closed.includes(props.id)}
        {...props}
      />
    );
  };

  return (
    <article className="lr" data-lr-role="lesson-record" aria-labelledby="lr-title">
      <header className="lr__header">
        <p className="lr__kicker">Lesson record · {r.document_type}</p>
        <h2 className="lr__title" id="lr-title">{r.title}</h2>
        <p className="lr__summary">
          {r.summary} <Code>{r.id}</Code>
        </p>
      </header>

      <div className="lr__bar" role="group" aria-label="Key and tools">
        <ul className="lr__legend" aria-label="What each treatment means">
          {LEGEND.map(([kind, text]) => (
            <li className="lr-key" data-kind={kind} key={kind}>{text}</li>
          ))}
        </ul>
        {tools ? <div className="lr__tools">{tools}</div> : <div className="lr__tools" data-lr-tools="" hidden />}
      </div>

      <ol className="lr__groups">
        {g({
          id: "identity", kind: "define", title: "Identity",
          note: "The id is stable and never changes. The title can change as often as it needs to.",
          children: (
            <div className="lr-panel">
              <Dl>
                <Row label="Schema version">{r.schema_version}</Row>
                <Row label="Identifier"><Code>{r.id}</Code></Row>
                <Row label="Document type">{r.document_type}</Row>
                <Row label="Title">{r.title}</Row>
                <Row label="Summary">{r.summary}</Row>
                <Row label="Tags"><Tags items={r.tags} /></Row>
              </Dl>
            </div>
          ),
        })}

        {g({
          id: "place", kind: "derive", title: "Place in the course",
          note: "Breadcrumbs and the lesson position are derived from these fields. Nobody types them into the page. Sequence is presentation order, not depth.",
          children: (
            <div className="lr-panel">
              <Dl>
                <Row label="Course"><Code>{r.course_id}</Code></Row>
                <Row label="Parent"><Code>{r.parent_id}</Code></Row>
                <Row label="Hierarchy level">{r.hierarchy_level}</Row>
                <Row label="Sequence">{r.sequence}</Row>
                <Row label="Position (derived)">{vm.position}</Row>
              </Dl>
            </div>
          ),
        })}

        {g({
          id: "inherited", kind: "inherit", title: "Inherited from the course", summary: vm.summaries.inherited,
          note: "Language, pitch, voice, referencing and rights come from the course unless the lesson overrides them. The lesson does not repeat them.",
          children: (
            <div className="lr-panel">
              <Dl>
                <Row label="Language">{c.language}</Row>
                <Row label="Learner pitch">{c.learner_pitch}</Row>
                <Row label="Voice specification"><Code>{c.voice_specification}</Code></Row>
                <Row label="Referencing style">{c.referencing_style}</Row>
                <Row label="Rights holder"><Value value={rights.holder} /></Row>
                <Row label="Licence"><Value value={rights.licence} /></Row>
              </Dl>
            </div>
          ),
        })}

        {g({
          id: "scope", kind: "internal", title: "Scope", summary: vm.summaries.scope,
          note: "The boundary of this lesson. Scope exclusions stay internal. They stop the lesson growing and they are not shown to learners.",
          children: (
            <div className="lr-panel">
              <Dl>
                <Row label="Focus">{scope.focus}</Row>
                <Row label="In scope"><List items={scope.in_scope} /></Row>
                <Row label="Out of scope"><List items={scope.out_of_scope} /></Row>
              </Dl>
            </div>
          ),
        })}

        {/* 05 to 07: CO, LO and ACT are three separate cards at the same level */}
        {g({
          id: "course-outcomes", kind: "inherit", title: "Course outcomes", summary: vm.summaries.co,
          note: 'From the course record. Outcomes marked "served" are the ones this lesson is aligned to.',
          children: (
            <div className="lr-panel">
              <ul className="lr-items">
                {vm.outcomes.map((o) => (
                  <li className="lr-item" id={o.id} data-aligned={o.aligned ? "true" : "false"} key={o.id}>
                    <h4 className="lr-item__id">
                      <Code>{o.id}</Code>
                      {o.aligned && <>{" "}<span className="lr-flag">served by this lesson</span></>}
                    </h4>
                    <p className="lr-item__text">{o.statement}</p>
                  </li>
                ))}
              </ul>
            </div>
          ),
        })}

        {g({
          id: "lesson-outcomes", kind: "define", title: "Lesson outcomes", summary: vm.summaries.lo,
          note: "Each lesson outcome points up to the course outcomes it serves and names the evidence that will show it has been met.",
          children: (
            <div className="lr-panel">
              <ul className="lr-items">
                {(r.learning_outcomes || []).map((lo) => (
                  <li className="lr-item" id={lo.id} key={lo.id}>
                    <h4 className="lr-item__id"><Code>{lo.id}</Code></h4>
                    <Dl>
                      <Row label="Statement">{lo.statement}</Row>
                      <Row label="Serves"><Refs ids={lo.course_outcome_ids} /></Row>
                      <Row label="Evidence">{lo.evidence}</Row>
                    </Dl>
                  </li>
                ))}
              </ul>
            </div>
          ),
        })}

        {g({
          id: "activities", kind: "define", title: "Activities", summary: vm.summaries.act,
          note: "Every activity points back to lesson outcomes. Do not promise that an activity is optional, saves answers or affects completion until that behaviour is verified in Adapt or SCORM.",
          children: (
            <div className="lr-panel">
              <ul className="lr-items">
                {(r.activities || []).map((a) => (
                  <li className="lr-item" id={a.id} key={a.id}>
                    <h4 className="lr-item__id"><Code>{a.id}</Code></h4>
                    <Dl>
                      <Row label="Purpose">{a.purpose}</Row>
                      <Row label="Evidences"><Refs ids={a.lesson_outcome_ids} /></Row>
                    </Dl>
                  </li>
                ))}
              </ul>
            </div>
          ),
        })}

        {g({
          id: "assessment", kind: "define", title: "Assessment", summary: vm.summaries.assessment,
          children: (
            <div className="lr-panel">
              <Dl>
                <Row label="Purpose">{assessment.purpose}</Row>
                <Row label="Covers"><Refs ids={assessment.lesson_outcome_ids} /></Row>
              </Dl>
            </div>
          ),
        })}

        {g({
          id: "prerequisites", kind: "define", title: "Prerequisites and materials", summary: vm.summaries.prereq,
          note: 'Only knowledge genuinely needed here. The learner sees this as "Before you begin" and "What you will need".',
          children: (
            <div className="lr-panel">
              <Dl>
                <Row label="Knowledge"><List items={prereq.knowledge} empty="None" /></Row>
                <Row label="Required lessons"><Tags items={prereq.required_lesson_ids} code empty="None" /></Row>
                <Row label="Estimated minutes"><Value value={r.estimated_duration_minutes} /></Row>
                <Row label="Materials"><List items={r.materials_required} empty="None" /></Row>
              </Dl>
            </div>
          ),
        })}

        {g({
          id: "lifecycle", kind: "internal", title: "Lifecycle and ownership", summary: vm.summaries.lifecycle,
          note: "Who is accountable, which version this is and when it is next reviewed. Never shown in the learner opening.",
          children: (
            <div className="lr-panel">
              <Dl>
                <Row label="Version">{r.version}</Row>
                <Row label="Status"><span className="lr-pill">{r.status}</span></Row>
                <Row label="Owner">{r.owner}</Row>
                <Row label="Authors"><List items={r.authors} /></Row>
                <Row label="Reviewers"><List items={r.reviewers} /></Row>
                <Row label="Created"><When value={r.created} /></Row>
                <Row label="Updated"><When value={r.updated} /></Row>
                <Row label="Review due"><When value={r.review_due} /></Row>
                <Row label="Sources"><List items={r.sources} /></Row>
              </Dl>
            </div>
          ),
        })}

        {g({
          id: "review", kind: "internal", title: "Academic review", summary: vm.summaries.review,
          note: "Document status and review approval are separate. A draft can have a reviewer assigned without having been approved.",
          children: (
            <div className="lr-panel">
              <Dl>
                <Row label="Academic status"><span className="lr-pill">{review.academic_status}</span></Row>
                <Row label="Approved by"><Value value={review.academic_approved_by} /></Row>
                <Row label="Approved on"><When value={review.academic_approved_on} /></Row>
              </Dl>
            </div>
          ),
        })}

        {g({
          id: "opening", kind: "derive", title: "Learner opening", summary: vm.summaries.opening,
          note: "The concise introduction learners see before the lesson begins. It is a display view of the record above, not a second source of truth.",
          children: (
            <>
              <div className="lr-panel lr-preview">
                <p className="lr-preview__eyebrow">{fm.eyebrow}</p>
                <p>{fm.body}</p>
                <p className="lr-preview__meta">{meta.duration} · {meta.level}</p>
                <p><strong>{fm.objectivesTitle}</strong></p>
                <ul className="lr-list">
                  {(fm.objectives || []).map((o, i) => <li key={i}>{o}</li>)}
                </ul>
              </div>
              <div className="lr-panel">
                <h4 className="lr-subhead">Derive, do not retype</h4>
                <Dl>
                  <Row label="Duration"><Code>estimated_duration_minutes</Code></Row>
                  <Row label="Level"><Code>course.learner_pitch</Code></Row>
                  <Row label="Outcomes list"><Code>learning_outcomes[].statement</Code></Row>
                  <Row label="Position"><Code>sequence</Code> and the course lesson map</Row>
                  <Row label="Before you begin"><Code>prerequisites</Code> and <Code>materials_required</Code></Row>
                </Dl>
              </div>
            </>
          ),
        })}
      </ol>
    </article>
  );
}
