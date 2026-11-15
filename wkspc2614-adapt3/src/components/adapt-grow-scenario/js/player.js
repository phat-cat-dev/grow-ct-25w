// DOM player shared by the preview and the Adapt component. It holds no scenario
// rules: it draws what engine.view() returns and sends actions back. All scenario
// text is inserted as text, never as HTML.
import { choose, createSession, proceed, restore, retry, serialize, setNote, view } from './engine.js';

function el(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined && text !== '') node.textContent = text;
  return node;
}

function button(label, onClick, className = 'sb-btn') {
  const b = el('button', className, label);
  b.type = 'button';
  b.addEventListener('click', onClick);
  return b;
}

const adviserName = v => v.guide.adviser.replace(/^Your/, 'your');

function reveal(label, text) {
  const details = el('details', 'sb-guide');
  details.append(el('summary', '', label), el('p', '', text));
  return details;
}

export function mountPlayer(host, scn, { saved, headingLevel = 2, onChange, onComplete, onClose } = {}) {
  const session = saved ? restore(scn, saved) : createSession(scn);
  const root = el('div', 'sb-player');
  host.replaceChildren(root);

  const heading = (text, level = headingLevel) => {
    const h = el(`h${Math.min(level, 6)}`, 'sb-title', text);
    h.tabIndex = -1;
    return h;
  };

  function changed() {
    onChange?.(serialize(session), session);
    const v = view(session);
    if (v.kind === 'ending') onComplete?.({ result: v.result, ending: v.id, attempt: session.attempt, route: v.route });
    render();
  }

  function clueBoard(v) {
    if (!v.clues.length) return null;
    const relevant = v.clues.filter(c => c.relevant);
    const box = el('details', 'sb-clues');
    box.open = relevant.length > 0;
    box.append(el('summary', '', `Clues you hold (${v.clues.length})`));
    const list = el('ul');
    for (const c of v.clues) {
      const li = el('li', c.relevant ? 'is-relevant' : '', c.text);
      if (c.relevant) li.prepend(el('strong', '', 'Useful here: '));
      list.append(li);
    }
    box.append(list);
    return box;
  }

  function measureBar(v) {
    if (!v.measures?.length) return null;
    const dl = el('dl', 'sb-measures');
    for (const m of v.measures) dl.append(el('dt', '', m.label), el('dd', '', String(m.value)));
    return dl;
  }

  function renderCard(v) {
    const frag = document.createDocumentFragment();
    if (v.layer && v.totalLayers) frag.append(el('p', 'sb-progress', `Stage ${v.layer} of ${v.totalLayers}`));
    const title = heading(v.title);
    frag.append(title);
    for (const r of v.regions) {
      if (r.region === 'prompt') continue;
      const block = el('div', `sb-region sb-region--${r.region}`);
      if (r.label) block.append(el('p', 'sb-label', r.label));
      block.append(el('p', 'sb-text', r.text));
      frag.append(block);
    }
    for (const a of v.asides) frag.append(el('p', 'sb-aside', a));
    const board = clueBoard(v);
    if (board) frag.append(board);
    const bar = measureBar(v);
    if (bar) frag.append(bar);
    if (v.guide.coach) {
      if (v.guide.mode === 'after-outcome') {
        const c = el('div', 'sb-guide sb-guide--open');
        c.append(el('p', 'sb-label', v.guide.adviser), el('p', '', v.guide.coach));
        frag.append(c);
      } else frag.append(reveal(`Ask ${adviserName(v)}: why did this happen?`, v.guide.coach));
    }
    const prompt = v.regions.find(r => r.region === 'prompt');
    if (v.reflect) {
      const label = el('label', 'sb-reflect');
      label.append(el('span', '', `${v.reflect.prompt} (private and optional)`));
      const input = el('textarea');
      input.rows = 2;
      input.maxLength = 4000;
      input.value = v.reflect.value;
      input.addEventListener('input', () => setNote(session, v.id, input.value));
      label.append(input);
      frag.append(label);
    }
    if (prompt) frag.append(el('p', 'sb-prompt', prompt.text));
    if (v.guide.nudge) frag.append(reveal(`Ask ${adviserName(v)} for a steer`, v.guide.nudge));
    if (v.decisions.length) {
      const group = el('div', 'sb-decisions');
      group.setAttribute('role', 'group');
      group.setAttribute('aria-label', prompt?.text || v.title);
      for (const d of v.decisions) {
        if (d.locked) {
          const wrap = el('div', 'sb-locked');
          const b = button(d.label, () => {}, 'sb-btn sb-decision');
          b.disabled = true;
          wrap.append(b, el('p', 'sb-hint', d.hint));
          group.append(wrap);
        } else {
          group.append(button(d.label, () => { choose(session, d.id); changed(); }, 'sb-btn sb-decision'));
        }
      }
      frag.append(group);
    }
    if (v.proceed) frag.append(button(v.proceed, () => { proceed(session); changed(); }, 'sb-btn sb-btn--primary'));
    return { frag, title };
  }

  function renderEnding(v) {
    const frag = document.createDocumentFragment();
    frag.append(el('p', `sb-banner sb-banner--${v.result}`, v.banner));
    const title = heading(v.title);
    frag.append(title);
    frag.append(el('p', 'sb-text', v.story));
    if (v.growthMessage) frag.append(el('p', 'sb-growth', v.growthMessage));
    if (v.recoveries) frag.append(el('p', 'sb-growth sb-recoveries', v.recoveries === 1 ? 'You recovered from a weaker decision on this route. That is a skill in its own right.' : `You recovered from weaker decisions ${v.recoveries} times on this route. That is a skill in its own right.`));
    const why = el('div', 'sb-region');
    why.append(el('p', 'sb-label', 'Why it ended this way'), el('p', 'sb-text', v.why));
    const next = el('div', 'sb-region sb-region--next');
    next.append(el('p', 'sb-label', v.result === 'pass' ? 'What to carry forward' : 'What to try next'), el('p', 'sb-text', v.feedForward));
    frag.append(why, next);
    const board = clueBoard(v);
    if (board) frag.append(board);
    const bar = measureBar(v);
    if (bar) frag.append(bar);
    if (v.transfer) {
      const label = el('label', 'sb-reflect');
      label.append(el('span', '', `${v.transfer} (private and optional)`));
      const input = el('textarea');
      input.rows = 2;
      input.maxLength = 4000;
      input.value = session.notes[`ending:${v.id}`] || '';
      input.addEventListener('input', () => setNote(session, `ending:${v.id}`, input.value));
      label.append(input);
      frag.append(label);
    }
    const review = el('details', 'sb-review');
    review.append(el('summary', '', 'Review your route'));
    const list = el('ol');
    for (const step of v.route) {
      const li = el('li');
      li.append(el('p', 'sb-step-choice', step.label));
      if (step.benefit) li.append(el('p', 'sb-step', `Gained: ${step.benefit}`));
      if (step.cost) li.append(el('p', 'sb-step', `Cost: ${step.cost}`));
      if (step.polarity !== 'positive' && step.tempting) li.append(el('p', 'sb-step', `Why it was tempting: ${step.tempting}`));
      if (v.showCoachInReview && step.coach) li.append(el('p', 'sb-step', `Adviser: ${step.coach}`));
      list.append(li);
    }
    review.append(list);
    frag.append(review);
    const actions = el('div', 'sb-actions');
    if (v.canRetry) actions.append(button(v.retryLabel, () => { retry(session); changed(); }, `sb-btn ${v.result === 'fail' ? 'sb-btn--primary' : ''}`));
    if (onClose) actions.append(button('Close', () => onClose(), `sb-btn ${v.result === 'pass' ? 'sb-btn--primary' : ''}`));
    frag.append(actions);
    return { frag, title };
  }

  function render() {
    const v = view(session);
    const { frag, title } = v.kind === 'ending' ? renderEnding(v) : renderCard(v);
    const card = el('section', `sb-card sb-card--${v.kind} sb-card--${v.template || v.result}`);
    card.setAttribute('data-card', v.id);
    card.append(frag);
    root.replaceChildren(card);
    // Start each card at the top of whatever is scrolling inside the modal.
    for (let n = root.parentElement; n && n !== document.body; n = n.parentElement) {
      if (n.scrollTop) n.scrollTop = 0;
      if (n.matches('dialog, .notify')) break;
    }
    title.focus({ preventScroll: true });
  }

  render();
  return {
    session,
    state: () => serialize(session),
    view: () => view(session),
    focus: () => root.querySelector('.sb-title')?.focus({ preventScroll: true }),
    destroy: () => host.replaceChildren()
  };
}
