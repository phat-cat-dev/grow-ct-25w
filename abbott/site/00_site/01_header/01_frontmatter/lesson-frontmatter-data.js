/* ============================================================================
   lesson-frontmatter-data.js
   Renders a lesson record (frontmatter_spec.md section 3) as the LESSON RECORD
   PANEL. No dependencies. Pair with lesson-frontmatter-data.css.

   Usage:
     LessonFmData.mount(document.getElementById('root'), {
       record: { ...lesson front matter as a plain object... },
       course: { ...optional course context: outcomes, learner_pitch, etc... }
     });

   What it does
     - Groups the record the way the spec reasons about it (identity, place,
       inheritance, scope, outcomes, prerequisites, activities, lifecycle,
       review, learner opening) and labels each group with its spec section 5
       treatment: define, inherit, derive or keep internal.
     - Each group opens and closes with an animated disclosure.
     - "Tell the story" walks the groups in order. The spotlighted group opens,
       the rest fade back, and the last step fades the internal groups out to
       show what actually reaches the learner.
     - Lenses dim everything except one treatment.
     - Hover, focus or click a CO / LO / ACT chip to trace its alignment chain.
     - Readable or YAML view of the same data.
   ============================================================================ */
(function (global) {
  'use strict';

  var ID_RE = /^(CO|LO|ACT)\d+$/;
  var CODE_KEYS = { id: 1, course_id: 1, parent_id: 1, required_lesson_ids: 1, lesson_id: 1 };
  var PILL_KEYS = { status: 1, academic_status: 1 };

  var LABELS = {
    schema_version: 'Schema version', id: 'Identifier', document_type: 'Document type', title: 'Title',
    summary: 'Summary', tags: 'Tags', course_id: 'Course', parent_id: 'Parent', hierarchy_level: 'Hierarchy level',
    sequence: 'Sequence', language: 'Language', learner_pitch: 'Learner pitch',
    voice_specification: 'Voice specification', referencing_style: 'Referencing style', rights: 'Rights',
    holder: 'Holder', licence: 'Licence', scope: 'Scope', focus: 'Focus', in_scope: 'In scope',
    out_of_scope: 'Out of scope', alignment: 'Alignment', course_outcome_ids: 'Course outcomes',
    learning_outcomes: 'Learning outcomes', statement: 'Statement', evidence: 'Evidence',
    prerequisites: 'Prerequisites', knowledge: 'Knowledge', required_lesson_ids: 'Required lessons',
    estimated_duration_minutes: 'Estimated minutes', materials_required: 'Materials', activities: 'Activities',
    purpose: 'Purpose', lesson_outcome_ids: 'Lesson outcomes', assessment: 'Assessment', version: 'Version',
    status: 'Status', owner: 'Owner', authors: 'Authors', reviewers: 'Reviewers', created: 'Created',
    updated: 'Updated', review_due: 'Review due', sources: 'Sources', review: 'Review',
    academic_status: 'Academic status', academic_approved_by: 'Approved by', academic_approved_on: 'Approved on',
    frontmatter: 'Learner opening', eyebrow: 'Eyebrow', body: 'Body', meta: 'Meta', duration: 'Duration',
    level: 'Level', objectivesTitle: 'Objectives heading', objectives: 'Objectives'
  };

  /* Groups, in the order the spec reasons about them. `from` is 'record' or 'course'. */
  var GROUPS = [
    { id: 'identity', title: 'Identity', kind: 'define', from: 'record',
      pick: ['schema_version', 'id', 'document_type', 'title', 'summary', 'tags'],
      note: 'The id is stable and never changes. The title can change as often as it needs to.',
      sum: function (r) { return r.title + ' (' + r.id + ')'; } },
    { id: 'place', title: 'Place in the course', kind: 'derive', from: 'record',
      pick: ['course_id', 'parent_id', 'hierarchy_level', 'sequence'],
      note: 'Breadcrumbs and the lesson position are derived from these fields. Nobody types them into the page. Sequence is presentation order, not depth.',
      sum: function (r, c) { return 'Lesson ' + r.sequence + (c.lesson_count ? ' of ' + c.lesson_count : '') + ', level ' + r.hierarchy_level; } },
    { id: 'inherited', title: 'Inherited from the course', kind: 'inherit', from: 'course',
      pick: ['language', 'learner_pitch', 'voice_specification', 'referencing_style', 'rights'],
      note: 'Language, pitch, voice, referencing and rights come from the course unless the lesson overrides them. The lesson does not repeat them.',
      sum: function (r, c) { return (c.language || '') + (c.learner_pitch ? ', ' + c.learner_pitch + ' pitch' : ''); } },
    { id: 'scope', title: 'Scope', kind: 'internal', from: 'record', pick: ['scope'],
      note: 'The boundary of this lesson. Scope exclusions stay internal. They stop the lesson growing and they are not shown to learners.',
      sum: function (r) { return r.scope && r.scope.focus; } },
    { id: 'outcomes', title: 'Outcomes and alignment', kind: 'define', from: 'record',
      pick: ['alignment', 'learning_outcomes'], course: 'outcomes',
      note: 'Each lesson outcome points up to the course outcomes it serves and names the evidence that will show it has been met.',
      sum: function (r) { return (r.learning_outcomes || []).length + ' lesson outcomes, aligned to ' + ((r.alignment || {}).course_outcome_ids || []).join(' and '); } },
    { id: 'prereq', title: 'Prerequisites and materials', kind: 'define', from: 'record',
      pick: ['prerequisites', 'estimated_duration_minutes', 'materials_required'],
      note: 'Only knowledge genuinely needed here. The learner sees this as "Before you begin" and "What you will need".',
      sum: function (r) { return r.estimated_duration_minutes ? r.estimated_duration_minutes + ' minutes' : 'No duration set'; } },
    { id: 'activities', title: 'Activities and assessment', kind: 'define', from: 'record',
      pick: ['activities', 'assessment'],
      note: 'Every activity and the assessment point back to lesson outcomes. Do not promise that an activity is optional, saves answers or affects completion until that behaviour is verified in Adapt or SCORM.',
      sum: function (r) { return (r.activities || []).length + ' activities, ' + ((r.assessment || {}).purpose || 'no') + ' assessment'; } },
    { id: 'lifecycle', title: 'Lifecycle and ownership', kind: 'internal', from: 'record',
      pick: ['version', 'status', 'owner', 'authors', 'reviewers', 'created', 'updated', 'review_due', 'sources'],
      note: 'Who is accountable, which version this is and when it is next reviewed. Never shown in the learner opening.',
      sum: function (r) { return 'v' + r.version + ', ' + r.status + ', owned by ' + r.owner; } },
    { id: 'review', title: 'Academic review', kind: 'internal', from: 'record', pick: ['review'],
      note: 'Document status and review approval are separate. A draft can have a reviewer assigned without having been approved.',
      sum: function (r) { return 'Academic review ' + ((r.review || {}).academic_status || 'pending'); } },
    { id: 'opening', title: 'Learner opening', kind: 'derive', from: 'record', pick: ['frontmatter'],
      note: 'The concise introduction learners see before the lesson begins. It is a display view of the record above, not a second source of truth.',
      sum: function (r) { return (r.frontmatter && r.frontmatter.eyebrow) || 'Before you begin'; },
      derived: [
        { to: 'Duration', from: 'estimated_duration_minutes' },
        { to: 'Level', from: 'course.learner_pitch' },
        { to: 'Outcomes list', from: 'learning_outcomes[].statement' },
        { to: 'Position', from: 'sequence + course lesson map' },
        { to: 'Before you begin', from: 'prerequisites + materials_required' }
      ] }
  ];

  var KIND_LABEL = { define: 'Defined here', inherit: 'Inherited', derive: 'Derived', internal: 'Kept internal' };

  /* The story, in order. `focus` lists groups to spotlight. */
  var CHAPTERS = [
    { focus: ['identity'], title: 'A lesson starts with an identity',
      text: 'A stable id, a clear title and a short summary. The title can be reworded at any time. The id cannot, because everything else points at it.' },
    { focus: ['place', 'inherited'], title: 'It belongs to a course',
      text: 'Parent, level and sequence place the lesson in the course. Language, pitch, voice and rights flow down from the course, so the lesson never restates them.' },
    { focus: ['scope'], title: 'It draws a boundary',
      text: 'Scope says what this lesson teaches and, just as usefully, what it leaves alone. That stops the lesson expanding. The exclusions stay internal.' },
    { focus: ['outcomes'], trace: 'LO1', title: 'It makes promises',
      text: 'Each lesson outcome serves a course outcome and names its evidence. Hover or tap a chip to follow the chain from course outcome to lesson outcome to activity.' },
    { focus: ['prereq', 'activities'], trace: 'LO2', title: 'It earns them through activity',
      text: 'Prerequisites say what the learner needs first. Activities and assessment exist to produce the evidence the outcomes promised. Nothing sits here without a lesson outcome behind it.' },
    { focus: ['lifecycle', 'review'], title: 'Someone is accountable',
      text: 'Owner, authors, reviewers, version and review state. This is the audit record. It keeps the lesson trustworthy and learners never see it.' },
    { focus: ['opening'], learner: true, title: 'The learner sees a small part',
      text: 'The internal groups fade away. What remains is the opening, built from the fields above: title, position, outcomes, time and what to bring.' }
  ];

  /* ---------- helpers ---------- */
  function h(tag, attrs) {
    var el = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      var v = attrs[k];
      if (v === null || v === undefined || v === false) return;
      if (k === 'class') el.className = v;
      else if (k === 'text') el.textContent = v;
      else if (k.slice(0, 2) === 'on' && typeof v === 'function') el.addEventListener(k.slice(2), v);
      else el.setAttribute(k, v === true ? '' : v);
    });
    for (var i = 2; i < arguments.length; i++) {
      var kid = arguments[i];
      if (kid === null || kid === undefined || kid === false) continue;
      el.appendChild(typeof kid === 'string' ? document.createTextNode(kid) : kid);
    }
    return el;
  }
  function label(k) { return LABELS[k] || k.replace(/_/g, ' ').replace(/^./, function (c) { return c.toUpperCase(); }); }
  function isScalar(v) { return v === null || v === undefined || typeof v !== 'object'; }
  function isEmpty(v) { return v === null || v === undefined || v === '' || (Array.isArray(v) && !v.length); }
  function reduced() { return global.matchMedia && global.matchMedia('(prefers-reduced-motion: reduce)').matches; }

  /* ---------- YAML view ---------- */
  function yScalar(v) {
    if (v === null || v === undefined) return 'null';
    if (typeof v === 'number' || typeof v === 'boolean') return String(v);
    var s = String(v);
    if (/^[A-Za-z][A-Za-z0-9_.\/-]*$/.test(s) && !/^(true|false|null|yes|no|on|off)$/i.test(s)) return s;
    return JSON.stringify(s);
  }
  function yaml(obj, ind) {
    var pad = new Array(ind + 1).join(' '), out = [];
    Object.keys(obj).forEach(function (k) {
      var v = obj[k];
      if (Array.isArray(v)) {
        if (!v.length) out.push(pad + k + ': []');
        else if (v.every(isScalar)) out.push(pad + k + ': [' + v.map(yScalar).join(', ') + ']');
        else {
          out.push(pad + k + ':');
          v.forEach(function (it) {
            if (isScalar(it)) out.push(pad + '  - ' + yScalar(it));
            else {
              var lines = yaml(it, ind + 4).split('\n');
              lines[0] = pad + '  - ' + lines[0].trim();
              out.push(lines.join('\n'));
            }
          });
        }
      } else if (v && typeof v === 'object') { out.push(pad + k + ':'); out.push(yaml(v, ind + 2)); }
      else out.push(pad + k + ': ' + yScalar(v));
    });
    return out.join('\n');
  }

  /* ---------- mount ---------- */
  function mount(host, opts) {
    var rec = opts.record, course = opts.course || {};
    var root = h('section', {
      class: 'lesson-data', 'data-view': 'readable', 'data-lens': 'all',
      'data-grow-role': 'lesson-record', 'aria-label': 'Lesson record'
    });
    var state = { story: null, learner: false, lens: 'all', pinned: null, hover: null };
    var groups = [];

    /* ----- link graph for tracing: CO - LO - ACT ----- */
    var adj = {};
    function link(a, b) { (adj[a] = adj[a] || {})[b] = 1; (adj[b] = adj[b] || {})[a] = 1; }
    (rec.learning_outcomes || []).forEach(function (lo) {
      (lo.course_outcome_ids || []).forEach(function (co) { link(lo.id, co); });
    });
    (rec.activities || []).forEach(function (a) {
      (a.lesson_outcome_ids || []).forEach(function (lo) { link(a.id, lo); });
    });
    function chainOf(id) {
      var seen = {}, queue = [id];
      seen[id] = 1;
      while (queue.length) {
        var cur = queue.shift();
        Object.keys(adj[cur] || {}).forEach(function (n) { if (!seen[n]) { seen[n] = 1; queue.push(n); } });
      }
      return seen;
    }
    function applyTrace() {
      var id = state.pinned || state.hover;
      var set = id ? chainOf(id) : null;
      root.classList.toggle('is-tracing', !!set);
      Array.prototype.forEach.call(root.querySelectorAll('[data-ref]'), function (el) {
        var on = !!set && set[el.getAttribute('data-ref')];
        el.classList.toggle('is-traced', !!on);
        el.classList.toggle('is-untraced', !!set && !on);
      });
      Array.prototype.forEach.call(root.querySelectorAll('[data-card]'), function (el) {
        var on = !!set && set[el.getAttribute('data-card')];
        el.classList.toggle('is-traced', !!on);
        el.classList.toggle('is-untraced', !!set && !on);
      });
    }
    function ref(id) {
      var type = id.replace(/\d+$/, '');
      return h('button', {
        type: 'button', class: 'ld-ref ld-ref--' + type, 'data-ref': id,
        'aria-pressed': 'false',
        title: 'Trace ' + id,
        onmouseenter: function () { state.hover = id; applyTrace(); },
        onmouseleave: function () { state.hover = null; applyTrace(); },
        onfocus: function () { state.hover = id; applyTrace(); },
        onblur: function () { state.hover = null; applyTrace(); },
        onclick: function (e) {
          state.pinned = state.pinned === id ? null : id;
          Array.prototype.forEach.call(root.querySelectorAll('[data-ref]'), function (el) {
            el.setAttribute('aria-pressed', String(el.getAttribute('data-ref') === state.pinned));
          });
          applyTrace();
          e.stopPropagation();
        }
      }, id);
    }

    /* ----- readable values ----- */
    function renderScalar(key, v) {
      if (isEmpty(v)) return h('span', { class: 'ld-empty', text: 'Not set' });
      if (typeof v === 'string' && ID_RE.test(v)) return ref(v);
      if (PILL_KEYS[key]) return h('span', { class: 'ld-pill', text: String(v) });
      if (CODE_KEYS[key]) return h('code', { class: 'ld-code', text: String(v) });
      return document.createTextNode(String(v));
    }
    function renderValue(key, v) {
      if (isEmpty(v)) return h('span', { class: 'ld-empty', text: Array.isArray(v) ? 'None yet' : 'Not set' });
      if (Array.isArray(v)) {
        if (v.every(isScalar)) {
          var refs = v.every(function (x) { return typeof x === 'string' && ID_RE.test(x); });
          if (key === 'tags' || refs || CODE_KEYS[key]) {
            return h.apply(null, ['ul', { class: 'ld-chips' }].concat(v.map(function (x) {
              return h('li', null, refs ? ref(x) : (CODE_KEYS[key] ? h('code', { class: 'ld-code', text: x }) : h('span', { class: 'ld-tag', text: String(x) })));
            })));
          }
          return h.apply(null, ['ul', { class: 'ld-list' }].concat(v.map(function (x) { return h('li', { text: String(x) }); })));
        }
        return h.apply(null, ['div', { class: 'ld-cards' }].concat(v.map(function (it) {
          var cardId = it.id && ID_RE.test(it.id) ? it.id : null;
          var rest = {};
          Object.keys(it).forEach(function (k) { if (k !== 'id') rest[k] = it[k]; });
          return h('div', { class: 'ld-card2', 'data-card': cardId },
            cardId ? h('div', { class: 'ld-card2__head' }, ref(cardId)) : null,
            renderObject(cardId ? rest : it));
        })));
      }
      if (typeof v === 'object') return renderObject(v);
      return renderScalar(key, v);
    }
    function renderObject(o) {
      var dl = h('dl', { class: 'ld-dl' });
      Object.keys(o).forEach(function (k) {
        dl.appendChild(h('dt', { text: label(k) }));
        dl.appendChild(h('dd', null, renderValue(k, o[k])));
      });
      return dl;
    }

    function pickFrom(src, keys) {
      var o = {};
      keys.forEach(function (k) { if (k in src) o[k] = src[k]; });
      return o;
    }

    function readableFor(g, data) {
      var box = h('div', { class: 'ld-readable' });
      if (g.id === 'outcomes') {
        var cos = course.outcomes || [];
        if (cos.length) {
          box.appendChild(h('p', { class: 'ld-sublabel', text: 'Course outcomes (from the course record)' }));
          var ul = h('ul', { class: 'ld-co' });
          cos.forEach(function (co) {
            ul.appendChild(h('li', { style: 'display:contents' }, ref(co.id), h('span', { text: co.statement })));
          });
          box.appendChild(ul);
          box.appendChild(h('p', { class: 'ld-sublabel', text: 'This lesson' }));
        }
        box.appendChild(h('p', { class: 'ld-trace-hint', text: 'Hover, focus or click a chip to trace its chain. Press Escape to clear.' }));
      }
      if (g.id === 'opening') {
        var fm = rec.frontmatter || {};
        var meta = fm.meta || {};
        box.appendChild(h('div', { class: 'ld-preview' },
          h('p', { class: 'ld-preview__eyebrow', text: fm.eyebrow || '' }),
          h('p', { text: fm.body ? String(fm.body).trim() : '' }),
          h('p', { class: 'ld-empty', text: [meta.duration, meta.level].filter(Boolean).join('  ·  ') }),
          h('p', null, h('strong', { text: fm.objectivesTitle || '' })),
          h.apply(null, ['ul', { class: 'ld-list' }].concat((fm.objectives || []).map(function (x) { return h('li', { text: x }); })))));
        box.appendChild(h('p', { class: 'ld-sublabel', text: 'Derive, do not retype' }));
        box.appendChild(h.apply(null, ['ul', { class: 'ld-derived' }].concat(g.derived.map(function (d) {
          return h('li', null, h('span', { class: 'ld-derived__to', text: d.to }), h('span', { class: 'ld-derived__arrow', 'aria-hidden': 'true', text: '←' }), h('code', { text: d.from }));
        }))));
        return box;
      }
      box.appendChild(renderObject(data));
      return box;
    }

    /* ----- build groups ----- */
    var list = h('ol', { class: 'ld-groups' });
    GROUPS.forEach(function (g, i) {
      var src = g.from === 'course' ? course : rec;
      var data = pickFrom(src, g.pick);
      var bodyId = 'ld-body-' + g.id + '-' + Math.random().toString(36).slice(2, 7);
      var toggle = h('button', {
        type: 'button', class: 'ld-toggle', 'aria-expanded': 'false', 'aria-controls': bodyId,
        onclick: function () { setOpen(entry, !entry.open); }
      },
        h('span', { class: 'ld-toggle__title' }, g.title, h('span', { class: 'ld-badge', text: KIND_LABEL[g.kind] })),
        h('span', { class: 'ld-toggle__chev', 'aria-hidden': 'true' }),
        h('span', { class: 'ld-toggle__sum', text: g.sum ? (g.sum(rec, course) || '') : '' }));
      var body = h('div', { class: 'ld-body', id: bodyId, role: 'region', 'aria-label': g.title },
        h('div', { class: 'ld-body__inner' },
          h('p', { class: 'ld-note', text: g.note }),
          readableFor(g, data),
          h('pre', { class: 'ld-yaml', tabindex: '0', 'aria-label': g.title + ' as YAML', text: yaml(data, 0) })));
      var card = h('article', { class: 'ld-card' }, h('h3', { class: 'ld-card__head' }, toggle), body);
      var li = h('li', { class: 'ld-group', 'data-group': g.id, 'data-kind': g.kind }, h('div', { class: 'ld-group__shell' }, card));
      var entry = { id: g.id, kind: g.kind, el: li, toggle: toggle, open: false };
      groups.push(entry);
      list.appendChild(li);
    });

    function setOpen(g, open) {
      g.open = open;
      g.el.classList.toggle('is-open', open);
      g.toggle.setAttribute('aria-expanded', String(open));
    }
    function byId(id) { return groups.filter(function (g) { return g.id === id; })[0]; }

    /* ----- controls ----- */
    var storyBtn = h('button', { type: 'button', class: 'ld-btn ld-btn--primary', onclick: function () { state.story === null ? startStory() : endStory(); } }, 'Tell the story');

    var lensBtns = [['all', 'All'], ['define', 'Defined here'], ['inherit', 'Inherited'], ['derive', 'Derived'], ['internal', 'Kept internal']].map(function (l) {
      return h('button', {
        type: 'button', class: 'ld-chip', 'data-kind': l[0] === 'all' ? null : l[0], 'data-lens-btn': l[0],
        'aria-pressed': String(l[0] === 'all'),
        onclick: function () { if (state.story !== null) endStory(true); setLens(l[0]); }
      }, l[1]);
    });
    var viewBtns = [['readable', 'Readable'], ['yaml', 'YAML']].map(function (v) {
      return h('button', {
        type: 'button', class: 'ld-chip', 'aria-pressed': String(v[0] === 'readable'), 'data-view-btn': v[0],
        onclick: function () { setView(v[0]); }
      }, v[1]);
    });
    var learnerBtn = h('button', { type: 'button', class: 'ld-btn', 'aria-pressed': 'false', onclick: function () { if (state.story !== null) endStory(true); setLearner(!state.learner); } }, 'Learner view');
    var expandBtn = h('button', { type: 'button', class: 'ld-btn', onclick: function () { if (state.story !== null) endStory(true); groups.forEach(function (g) { setOpen(g, true); }); } }, 'Expand all');
    var collapseBtn = h('button', { type: 'button', class: 'ld-btn', onclick: function () { if (state.story !== null) endStory(true); groups.forEach(function (g) { setOpen(g, false); }); } }, 'Collapse all');

    var bar = h('div', { class: 'ld-bar', role: 'toolbar', 'aria-label': 'Lesson record controls' },
      storyBtn,
      h.apply(null, ['div', { class: 'ld-bar__group', role: 'group', 'aria-label': 'Lens' }, h('span', { class: 'ld-bar__label', text: 'Lens' })].concat(lensBtns)),
      h.apply(null, ['div', { class: 'ld-bar__group', role: 'group', 'aria-label': 'View' }, h('span', { class: 'ld-bar__label', text: 'View' })].concat(viewBtns)),
      h('div', { class: 'ld-bar__group' }, learnerBtn, expandBtn, collapseBtn));

    function setLens(lens) {
      state.lens = lens;
      root.setAttribute('data-lens', lens);
      lensBtns.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-lens-btn') === lens)); });
      groups.forEach(function (g) { g.el.classList.toggle('is-dim', lens !== 'all' && g.kind !== lens); });
      if (lens !== 'all') groups.forEach(function (g) { if (g.kind === lens) setOpen(g, true); });
    }
    function setView(v) {
      root.setAttribute('data-view', v);
      viewBtns.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-view-btn') === v)); });
    }
    function setLearner(on) {
      state.learner = on;
      learnerBtn.setAttribute('aria-pressed', String(on));
      groups.forEach(function (g) {
        var hide = on && (g.kind === 'internal' || g.kind === 'inherit');
        g.el.classList.toggle('is-hidden', hide);
        if (hide) g.el.setAttribute('inert', ''); else g.el.removeAttribute('inert');
        g.el.setAttribute('aria-hidden', hide ? 'true' : 'false');
      });
    }

    /* ----- story ----- */
    var stepEl = h('p', { class: 'ld-story__step' });
    var titleEl = h('h3', { class: 'ld-story__title' });
    var bodyEl = h('p', { class: 'ld-story__body' });
    var textEl = h('div', { class: 'ld-story__text', 'aria-live': 'polite' }, titleEl, bodyEl);
    var backBtn = h('button', { type: 'button', class: 'ld-btn', onclick: function () { goStory(state.story - 1); } }, 'Back');
    var nextBtn = h('button', { type: 'button', class: 'ld-btn ld-btn--primary', onclick: function () { state.story >= CHAPTERS.length - 1 ? endStory() : goStory(state.story + 1); } }, 'Next');
    var exitBtn = h('button', { type: 'button', class: 'ld-btn', onclick: function () { endStory(); } }, 'Exit');
    var dots = h.apply(null, ['ol', { class: 'ld-dots', 'aria-label': 'Story steps' }].concat(CHAPTERS.map(function (c, i) {
      return h('li', null, h('button', { type: 'button', 'aria-label': 'Step ' + (i + 1) + ': ' + c.title, onclick: function () { goStory(i); } }));
    })));
    var storyBar = h('div', { class: 'ld-story' }, h('div', { class: 'ld-story__shell' },
      h('div', { class: 'ld-story__card' }, stepEl, textEl, h('div', { class: 'ld-story__nav' }, backBtn, nextBtn, exitBtn, dots))));

    function startStory() {
      setLens('all');
      state.pinned = null; state.hover = null; applyTrace();
      root.setAttribute('data-story', 'on');
      storyBtn.textContent = 'Stop the story';
      goStory(0, true);
    }
    function goStory(i, instant) {
      if (i < 0 || i >= CHAPTERS.length) return;
      var c = CHAPTERS[i];
      state.story = i;
      var swap = function () {
        stepEl.textContent = 'Step ' + (i + 1) + ' of ' + CHAPTERS.length;
        titleEl.textContent = c.title;
        bodyEl.textContent = c.text;
        textEl.classList.remove('is-swapping');
      };
      if (instant || reduced()) swap(); else { textEl.classList.add('is-swapping'); setTimeout(swap, 170); }
      backBtn.disabled = i === 0;
      nextBtn.textContent = i === CHAPTERS.length - 1 ? 'Finish' : 'Next';
      Array.prototype.forEach.call(dots.querySelectorAll('button'), function (b, n) {
        if (n === i) b.setAttribute('aria-current', 'step'); else b.removeAttribute('aria-current');
      });
      setLearner(!!c.learner);
      groups.forEach(function (g) {
        var f = c.focus.indexOf(g.id) > -1;
        g.el.classList.toggle('is-focus', f);
        setOpen(g, f);
      });
      state.pinned = c.trace || null;
      Array.prototype.forEach.call(root.querySelectorAll('[data-ref]'), function (el) {
        el.setAttribute('aria-pressed', String(el.getAttribute('data-ref') === state.pinned));
      });
      applyTrace();
      var first = byId(c.focus[0]);
      if (first) setTimeout(function () {
        first.el.scrollIntoView({ behavior: reduced() ? 'auto' : 'smooth', block: 'center' });
      }, instant ? 0 : 120);
    }
    function endStory(keepState) {
      state.story = null;
      root.removeAttribute('data-story');
      storyBtn.textContent = 'Tell the story';
      groups.forEach(function (g) { g.el.classList.remove('is-focus'); });
      state.pinned = null;
      Array.prototype.forEach.call(root.querySelectorAll('[data-ref]'), function (el) { el.setAttribute('aria-pressed', 'false'); });
      applyTrace();
      if (!keepState) setLearner(false);
    }

    root.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        if (state.pinned && state.story === null) { state.pinned = null; applyTrace(); Array.prototype.forEach.call(root.querySelectorAll('[data-ref]'), function (el) { el.setAttribute('aria-pressed', 'false'); }); }
        else if (state.story !== null) endStory();
        return;
      }
      if (state.story === null) return;
      if (e.key === 'ArrowRight') { e.preventDefault(); goStory(Math.min(state.story + 1, CHAPTERS.length - 1)); }
      if (e.key === 'ArrowLeft')  { e.preventDefault(); goStory(Math.max(state.story - 1, 0)); }
    });

    /* ----- head + legend ----- */
    var head = h('header', null,
      h('p', { class: 'ld-kicker', text: 'Lesson record · ' + (rec.document_type || 'lesson') }),
      h('h2', { class: 'ld-title', text: rec.title }),
      h('p', { class: 'ld-sub' }, rec.summary + ' ', h('code', { text: rec.id })),
      h.apply(null, ['ul', { class: 'ld-legend', 'aria-label': 'What the colours mean' }].concat(
        ['define', 'inherit', 'derive', 'internal'].map(function (k) {
          return h('li', { 'data-kind': k, text: KIND_LABEL[k] + (k === 'define' ? ' (per lesson)' : k === 'inherit' ? ' (from course)' : k === 'derive' ? ' (automatic)' : ' (never shown to learners)') });
        }))));

    root.appendChild(head);
    root.appendChild(bar);
    root.appendChild(storyBar);
    root.appendChild(list);
    host.appendChild(root);

    setOpen(groups[0], true);

    return {
      el: root,
      startStory: startStory, endStory: endStory, goStory: goStory,
      setLens: setLens, setView: setView, setLearner: setLearner,
      setOpen: function (id, open) { var g = byId(id); if (g) setOpen(g, open); },
      destroy: function () { host.removeChild(root); }
    };
  }

  global.LessonFmData = { mount: mount, groups: GROUPS, chapters: CHAPTERS };
})(window);
