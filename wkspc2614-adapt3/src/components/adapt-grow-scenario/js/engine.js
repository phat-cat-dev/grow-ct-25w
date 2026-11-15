// Scenario engine: pure logic with no DOM and no Adapt dependency, so the CLI,
// the preview and the Adapt component all run the same rules.
import { CARD_LAYOUTS } from './card-layouts.js';

export const POLARITIES = ['positive', 'mixed', 'negative'];
export const DEFAULT_BANNERS = { pass: 'Well done!', fail: 'Not passed yet. Try again.' };
const TOKEN = /\{\{\s*([A-Za-z0-9_.-]+)\s*\}\}/g;

export function indexScenario(scn) {
  return {
    cards: new Map(scn.cards.map(card => [card.id, card])),
    endings: new Map((scn.endings || []).map(ending => [ending.id, ending])),
    clues: new Map((scn.clues || []).map(clue => [clue.id, clue])),
    measures: new Map((scn.measures || []).map(measure => [measure.id, measure]))
  };
}

const startMeasures = scn => Object.fromEntries((scn.measures || []).map(m => [m.id, m.start ?? 0]));

export function createSession(scn) {
  return {
    scn, idx: indexScenario(scn), attempt: 1, history: [], route: [],
    cardId: scn.start, endingId: null, clues: [], visited: [scn.start],
    measures: startMeasures(scn), arrival: null, notes: {}
  };
}

// Neutral moves are navigation, such as returning to a hub. They are not judged or reported.
export function decisionSteps(session) { return session.route.filter(step => step.polarity !== 'neutral'); }

export function stats(session) {
  const counts = { positive: 0, mixed: 0, negative: 0 };
  let recoveries = 0, run = 0, previous = null, turningPoint = '';
  for (const step of decisionSteps(session)) {
    counts[step.polarity]++;
    run = step.polarity === 'positive' ? run + 1 : 0;
    if (step.polarity === 'positive' && previous && previous !== 'positive') {
      recoveries++;
      if (!turningPoint) turningPoint = step.label;
    }
    previous = step.polarity;
  }
  return { ...counts, recoveries, run, last: previous, turningPoint, length: decisionSteps(session).length };
}

// Conditions are plain data, so authors and the validator can both read them.
export function test(when, session) {
  if (when === undefined || when === null) return true;
  const s = stats(session);
  return Object.entries(when).every(([key, value]) => {
    switch (key) {
      case 'all': return value.every(c => test(c, session));
      case 'any': return value.some(c => test(c, session));
      case 'not': return !test(value, session);
      case 'clue': return session.clues.includes(value);
      case 'clues_at_least': return session.clues.length >= value;
      case 'visited': return session.visited.includes(value);
      case 'last_polarity': return s.last === value;
      case 'arrived': return session.arrival === value;
      case 'positive_at_least': return s.positive >= value;
      case 'negative_at_most': return s.negative <= value;
      case 'positive_run_at_least': return s.run >= value;
      case 'recoveries_at_least': return s.recoveries >= value;
      case 'attempt_at_least': return session.attempt >= value;
      case 'measure': return Object.entries(value).every(([id, range]) => {
        const v = session.measures[id];
        return (range.gte === undefined || v >= range.gte) && (range.lte === undefined || v <= range.lte);
      });
      default: throw new Error(`Unknown condition "${key}".`);
    }
  });
}

export const CONDITION_KEYS = ['all', 'any', 'not', 'clue', 'clues_at_least', 'visited', 'last_polarity', 'arrived',
  'positive_at_least', 'negative_at_most', 'positive_run_at_least', 'recoveries_at_least', 'attempt_at_least', 'measure'];

export function currentCard(session) { return session.idx.cards.get(session.cardId); }

export function outcomeFor(card, arrival) {
  const o = card.outcome;
  if (!o) return null;
  return o[arrival] || o.any || o[POLARITIES.find(p => o[p])] || null;
}

function clamp(measure, value) {
  const low = measure?.min ?? -Infinity, high = measure?.max ?? Infinity;
  return Math.min(high, Math.max(low, value));
}

function grant(session, ids) {
  for (const id of ids || []) if (!session.clues.includes(id)) session.clues.push(id);
}

function applyDecision(session, card, decision) {
  session.route.push({
    card: card.id, decision: decision.id, label: decision.label, polarity: decision.polarity,
    benefit: decision.benefit || '', cost: decision.cost || '', tempting: decision.tempting_because || '',
    title: card.title, coach: card.guide?.coach || '', criterion: decision.criterion || ''
  });
  for (const [id, delta] of Object.entries(decision.effects || {})) {
    session.measures[id] = clamp(session.idx.measures.get(id), (session.measures[id] ?? 0) + delta);
  }
  grant(session, decision.grants);
  session.arrival = decision.polarity;
  if (session.idx.endings.has(decision.next)) enterEnding(session, decision.next);
  else {
    session.cardId = decision.next;
    if (!session.visited.includes(decision.next)) session.visited.push(decision.next);
  }
}

function enterEnding(session, id) {
  const ending = session.idx.endings.get(id);
  session.endingId = id;
  grant(session, ending.grants);
  const s = stats(session);
  session.history.push({ attempt: session.attempt, ending: id, result: ending.result, positive: s.positive, recoveries: s.recoveries });
}

export function availableDecisions(session, card = currentCard(session)) {
  return (card.decisions || []).map(d => ({ decision: d, open: test(d.requires, session) }))
    .filter(({ decision, open }) => open || decision.locked_hint);
}

export function choose(session, decisionId) {
  if (session.endingId) throw new Error('This route has ended.');
  const card = currentCard(session);
  const found = availableDecisions(session, card).find(({ decision }) => decision.id === decisionId);
  if (!found || !found.open) throw new Error(`Decision "${decisionId}" is not available on ${card.id}.`);
  applyDecision(session, card, found.decision);
  return session;
}

// Final reckoning cards have rules rather than decisions.
export function resolveRoute(session, card = currentCard(session)) {
  const rule = (card.route || []).find(r => test(r.when, session));
  if (!rule) throw new Error(`No route rule matched on ${card.id}.`);
  return rule.ending;
}

export function proceed(session) {
  const card = currentCard(session);
  if (!card.route) throw new Error(`${card.id} has no route rules.`);
  enterEnding(session, resolveRoute(session, card));
  return session;
}

export function canRetry(session) {
  const retry = session.scn.settings?.retry || {};
  if (retry.mode === 'off') return false;
  const ending = session.endingId && session.idx.endings.get(session.endingId);
  if (ending?.result === 'pass' && retry.allow_after_pass === false) return false;
  return !retry.max_attempts || session.attempt < retry.max_attempts;
}

function rebuild(session, keep, startCard) {
  const steps = session.route.slice(0, keep);
  const carried = session.scn.settings?.retry?.carry_clues === false ? [] : session.clues.slice();
  Object.assign(session, { route: [], endingId: null, clues: [], visited: [session.scn.start], measures: startMeasures(session.scn), cardId: session.scn.start, arrival: null });
  for (const step of steps) {
    const card = session.idx.cards.get(step.card);
    applyDecision(session, card, card.decisions.find(d => d.id === step.decision));
  }
  grant(session, carried);
  if (startCard) {
    session.cardId = startCard;
    if (!session.visited.includes(startCard)) session.visited.push(startCard);
  }
}

export function retry(session) {
  if (!canRetry(session)) throw new Error('No further attempts are available.');
  const ending = session.endingId && session.idx.endings.get(session.endingId);
  const mode = session.scn.settings?.retry?.mode || 'restart';
  session.attempt++;
  if (ending?.retry_to) {
    const at = session.route.findIndex(step => step.card === ending.retry_to);
    rebuild(session, at >= 0 ? at : 0, ending.retry_to);
  } else if (mode === 'last-decision' && session.route.length) {
    const last = session.route.length - 1;
    const target = session.route[last].card;
    rebuild(session, last, target);
  } else if (mode === 'checkpoint') {
    let at = -1;
    session.route.forEach((step, i) => { if (session.idx.cards.get(step.card).checkpoint) at = i; });
    if (at >= 0) rebuild(session, at, session.route[at].card);
    else rebuild(session, 0);
  } else {
    rebuild(session, 0);
  }
  return session;
}

function growth(session) {
  const { history, attempt } = session;
  const s = stats(session);
  const messages = session.scn.settings?.growth_messages || {};
  const finishedThisAttempt = session.endingId ? 1 : 0;
  const past = history.slice(0, history.length - finishedThisAttempt);
  const previous = past[past.length - 1];
  const change = previous ? s.positive - previous.positive : null;
  const key = !previous ? 'first_attempt' : change > 0 ? 'improved' : change === 0 ? 'same' : 'lower';
  return {
    attempt,
    recoveries: s.recoveries,
    previous_positive: previous ? previous.positive : '',
    best_positive: history.length ? Math.max(...history.map(h => h.positive)) : s.positive,
    change: change === null ? '' : `${change > 0 ? '+' : ''}${change}`,
    message: messages[key] || ''
  };
}

export function resolveToken(name, session, card = currentCard(session), ending) {
  const parts = name.split('.');
  const scn = session.scn;
  const pad = n => String(n).padStart(2, '0');
  const fromStep = (step, field) => (step ? String(step[field] ?? '') : '');
  switch (parts[0]) {
    case 'scenario': {
      const s = scn.scenario;
      return { title: s.title, goal: s.goal, role: s.position?.role, adviser: s.position?.adviser?.name }[parts[1]] || '';
    }
    case 'card': return card?.[parts[1]] || '';
    case 'layer': return String(parts[1] === 'current' ? card?.layer ?? '' : scn.settings?.layers ?? '');
    case 'decision': {
      const d = (card?.decisions || []).find(x => x.id === parts[1]);
      if (!d) return '';
      const field = parts[2] || 'label';
      return String(field === 'tempting' ? d.tempting_because || '' : d[field] || '');
    }
    case 'outcome': {
      const named = POLARITIES.includes(parts[1]) || parts[1] === 'any';
      const block = named ? card?.outcome?.[parts[1]] : (card && outcomeFor(card, session.arrival));
      return block?.[parts[named ? 2 : 1]] || '';
    }
    case 'guide': return card?.guide?.[parts[1]] || '';
    case 'route': {
      const s = stats(session);
      if (parts[1] === 'step') return fromStep(decisionSteps(session)[Number(parts[2]) - 1], parts[3]);
      if (parts[1] === 'last') return fromStep(decisionSteps(session).at(-1), parts[2]);
      if (parts[1] === 'length') return String(s.length);
      if (parts[1] === 'positive_count') return String(s.positive);
      if (parts[1] === 'mixed_count') return String(s.mixed);
      if (parts[1] === 'negative_count') return String(s.negative);
      if (parts[1] === 'benefits') return decisionSteps(session).map(x => x.benefit).filter(Boolean).join('; ');
      if (parts[1] === 'costs') return decisionSteps(session).map(x => x.cost).filter(Boolean).join('; ');
      if (parts[1] === 'turning_point') return s.turningPoint;
      return '';
    }
    case 'measure': {
      const m = session.idx.measures.get(parts[1]);
      if (!m) return '';
      if (parts[2] === 'label') return m.label || m.id;
      if (parts[2] === 'change') {
        const change = session.measures[m.id] - (m.start ?? 0);
        return `${change > 0 ? '+' : ''}${change}`;
      }
      return String(session.measures[m.id]);
    }
    case 'clue': return session.clues.includes(parts[1]) ? session.idx.clues.get(parts[1])?.text || '' : '';
    case 'clues': return parts[1] === 'count' ? String(session.clues.length) : session.clues.map(id => session.idx.clues.get(id)?.text).filter(Boolean).join(' ');
    case 'attempt': return String(session.attempt);
    case 'growth': return String(growth(session)[parts[1]] ?? '');
    case 'ending': {
      const e = ending || (session.endingId && session.idx.endings.get(session.endingId));
      if (!e) return '';
      if (parts[1] === 'banner') return banner(session, e);
      return e[parts[1]] || '';
    }
    case 'note': return session.notes[parts[1]] || '';
    default: return '';
  }
}

export function fill(text, session, card, ending, depth = 0) {
  if (typeof text !== 'string') return '';
  return text.replace(TOKEN, (_, name) => {
    const value = resolveToken(name, session, card, ending);
    return depth < 3 ? fill(value, session, card, ending, depth + 1) : value;
  });
}

export function banner(session, ending) {
  const set = { ...DEFAULT_BANNERS, ...(session.scn.settings?.banners || {}) };
  return ending.banner || set[ending.result];
}

export function guidanceMode(session) {
  const g = session.scn.settings?.guidance || {};
  if (session.attempt > 1 && g.escalate_on_retry !== false) return 'after-outcome';
  return g.mode || 'on-request';
}

// A plain description of what to show. Renderers add no scenario logic of their own.
export function view(session) {
  const scn = session.scn;
  const clueList = session.clues.map(id => {
    const clue = session.idx.clues.get(id);
    const relevant = !session.endingId && (clue?.applies_at || []).includes(session.cardId);
    return { id, text: fill(clue?.text, session), relevant };
  });
  const measures = (scn.measures || []).filter(m => m.show !== false && m.show !== 'ending').map(m => ({ id: m.id, label: m.label || m.id, value: session.measures[m.id] }));
  if (session.endingId) {
    const e = session.idx.endings.get(session.endingId);
    const s = stats(session);
    const g = growth(session);
    return {
      kind: 'ending', id: e.id, result: e.result, tier: e.tier || '', banner: banner(session, e),
      title: fill(e.title, session, null, e), story: fill(e.story, session, null, e), why: fill(e.why, session, null, e),
      feedForward: fill(e.feed_forward, session, null, e), transfer: e.transfer ? fill(e.transfer, session, null, e) : '',
      growthMessage: fill(g.message, session, null, e), recoveries: s.recoveries, attempt: session.attempt,
      route: decisionSteps(session).map(step => ({ ...step, label: fill(step.label, session), benefit: fill(step.benefit, session), cost: fill(step.cost, session), coach: fill(step.coach, session) })),
      showCoachInReview: guidanceMode(session) === 'at-ending',
      clues: clueList, canRetry: canRetry(session), measures: (scn.measures || []).filter(m => m.show !== false).map(m => ({ id: m.id, label: m.label || m.id, value: session.measures[m.id] })),
      retryLabel: scn.settings?.retry?.label || 'Try again'
    };
  }
  const card = currentCard(session);
  const regions = (CARD_LAYOUTS[card.template] || CARD_LAYOUTS['standard-decision']).map(r => ({ region: r.region, label: r.label || '', text: fill(r.text, session, card) })).filter(r => r.text.trim());
  const mode = guidanceMode(session);
  const asides = (card.asides || []).filter(a => test(a.when, session)).map(a => fill(a.text, session, card));
  return {
    kind: 'card', id: card.id, template: card.template, title: fill(card.title, session, card), layer: card.layer ?? null, totalLayers: scn.settings?.layers ?? null,
    regions, asides, clues: clueList, measures,
    guide: {
      mode, adviser: scn.scenario.position?.adviser?.name || 'Your adviser',
      coach: mode === 'at-ending' ? '' : fill(card.guide?.coach, session, card),
      nudge: mode === 'at-ending' ? '' : fill(card.guide?.nudge, session, card)
    },
    reflect: card.reflect ? { prompt: fill(card.reflect, session, card), value: session.notes[card.id] || '' } : null,
    decisions: availableDecisions(session, card).map(({ decision, open }) => ({ id: decision.id, label: fill(decision.label, session, card), locked: !open, hint: open ? '' : fill(decision.locked_hint, session, card) })),
    proceed: card.route ? fill(card.proceed || 'See how it ended', session, card) : null
  };
}

export function setNote(session, cardId, text) { session.notes[cardId] = String(text).slice(0, 4000); }

// A compact flat list of integers for SCORM storage. Notes are deliberately left out.
export function serialize(session) {
  const cards = session.scn.cards, endings = session.scn.endings || [], clues = session.scn.clues || [];
  const flat = [1, session.attempt, session.endingId ? endings.findIndex(e => e.id === session.endingId) + 1 : 0, cards.findIndex(c => c.id === session.cardId)];
  flat.push(session.clues.length, ...session.clues.map(id => clues.findIndex(c => c.id === id)));
  flat.push(session.history.length);
  for (const h of session.history) flat.push(endings.findIndex(e => e.id === h.ending), h.positive, h.recoveries);
  flat.push(session.route.length);
  for (const step of session.route) {
    const c = cards.findIndex(x => x.id === step.card);
    flat.push(c, cards[c].decisions.findIndex(d => d.id === step.decision));
  }
  return flat;
}

export function restore(scn, flat) {
  const session = createSession(scn);
  if (!Array.isArray(flat) || flat[0] !== 1) return session;
  try {
    let i = 1;
    const attempt = flat[i++], endingIndex = flat[i++], cardIndex = flat[i++];
    const clueCount = flat[i++];
    const clues = flat.slice(i, i + clueCount).map(n => scn.clues[n].id); i += clueCount;
    const historyCount = flat[i++];
    const history = [];
    for (let h = 0; h < historyCount; h++, i += 3) {
      const ending = scn.endings[flat[i]];
      history.push({ attempt: h + 1, ending: ending.id, result: ending.result, positive: flat[i + 1], recoveries: flat[i + 2] });
    }
    const routeCount = flat[i++];
    const steps = [];
    for (let r = 0; r < routeCount; r++, i += 2) steps.push([flat[i], flat[i + 1]]);
    for (const [c, d] of steps) {
      const card = scn.cards[c];
      if (session.cardId !== card.id) session.cardId = card.id; // retries may resume mid-route
      session.endingId = null;
      applyDecision(session, card, card.decisions[d]);
    }
    session.cardId = scn.cards[cardIndex].id;
    session.endingId = endingIndex ? scn.endings[endingIndex - 1].id : null;
    session.attempt = attempt; session.history = history;
    grant(session, clues);
    return session;
  } catch {
    return createSession(scn); // content changed since the state was saved
  }
}
