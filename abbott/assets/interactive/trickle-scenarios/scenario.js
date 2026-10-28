(function (global) {
  'use strict';
  function validate(data) {
    function fail(message) { throw new Error(`Scenario: ${message}`); }
    function text(value, name, max = 4000) {
      if (typeof value !== 'string' || !value.trim() || value.length > max) fail(`${name} must be non-empty text, at most ${max} characters.`);
    }
    if (!data || typeof data !== 'object' || Array.isArray(data) || data.version !== 1) fail('expected a version 1 object.');
    text(data.id, 'id', 80); text(data.title, 'title', 200); text(data.intro, 'intro');
    if (!Array.isArray(data.nodes) || !data.nodes.length || data.nodes.length > 200) fail('provide 1-200 nodes.');
    const nodes = new Map();
    for (const node of data.nodes) {
      if (!node || typeof node !== 'object') fail('each node must be an object.');
      text(node.id, 'node id', 80);
      if (!/^[a-zA-Z0-9_-]+$/.test(node.id) || nodes.has(node.id)) fail(`invalid or duplicate node id "${node.id}".`);
      if (!['choice', 'continue', 'auto', 'ending'].includes(node.type)) fail(`${node.id}: unknown type.`);
      text(node.title, `${node.id} title`, 200); text(node.body, `${node.id} body`);
      if (node.prompt !== undefined) text(node.prompt, `${node.id} reflection prompt`, 300);
      if (node.type === 'choice') {
        if (!Array.isArray(node.choices) || node.choices.length < 2 || node.choices.length > 8) fail(`${node.id}: provide 2-8 choices.`);
        const labels = new Set();
        node.choices.forEach(choice => {
          if (!choice || typeof choice !== 'object') fail(`${node.id}: invalid choice.`);
          text(choice.label, `${node.id} choice label`, 200);
          text(choice.next, `${node.id} choice destination`, 80);
          if (labels.has(choice.label)) fail(`${node.id}: duplicate choice labels.`);
          labels.add(choice.label);
        });
        if (node.next !== undefined) fail(`${node.id}: choices, not next, define its routes.`);
      } else {
        if (node.choices !== undefined) fail(`${node.id}: only choice nodes can have choices.`);
        if (node.type !== 'ending') {
          text(node.next, `${node.id} next`, 80);
          if (node.button !== undefined) text(node.button, `${node.id} button`, 200);
        } else if (node.next !== undefined) fail(`${node.id}: ending cannot have next.`);
      }
      if (node.type === 'auto' && (!Number.isFinite(node.delayMs) || node.delayMs < 500 || node.delayMs > 30000)) fail(`${node.id}: delayMs must be 500-30000.`);
      nodes.set(node.id, node);
    }
    if (!nodes.has(data.start)) fail('start must reference an existing node.');
    const visiting = new Set(), visited = new Set();
    function visit(id) {
      if (!nodes.has(id)) fail(`missing destination "${id}".`);
      if (visiting.has(id)) fail(`cycle at "${id}"; use an ending and Restart instead.`);
      if (visited.has(id)) return;
      visiting.add(id);
      const node = nodes.get(id);
      const next = node.type === 'choice' ? node.choices.map(choice => choice.next) : node.type === 'ending' ? [] : [node.next];
      next.forEach(visit);
      visiting.delete(id); visited.add(id);
    }
    visit(data.start);
    if (visited.size !== nodes.size) fail(`unreachable nodes: ${[...nodes.keys()].filter(id => !visited.has(id)).join(', ')}.`);
    return data;
  }
  function mount(host, source) {
    validate(source);
    if (!(host instanceof HTMLElement)) throw new Error('Scenario host must be an HTML element.');
    const data = JSON.parse(JSON.stringify(source));
    const nodes = new Map(data.nodes.map(node => [node.id, node]));
    const controller = new AbortController();
    const options = { signal: controller.signal };
    let route = [], timer = null, running = false, destroyed = false;
    const make = (tag, className, text) => {
      const el = document.createElement(tag);
      if (className) el.className = className;
      if (text !== undefined) el.textContent = text;
      return el;
    };
    const header = make('header', 'trickle-heading');
    header.append(make('p', 'trickle-kicker', 'Branching scenario / one decision at a time'), make('h2', '', data.title), make('p', '', data.intro));
    const controls = make('div', 'trickle-controls');
    function button(label, action) {
      const el = make('button', '', label); el.type = 'button';
      el.addEventListener('click', action, options); return el;
    }
    const play = button('Enable timed trickle', () => {
      running = true; schedule(); update('Timed trickle enabled. Choice cards still wait for your decision.');
    });
    const pause = button('Pause timed trickle', () => stop('Timed trickle paused. Continue manually or enable it again.'));
    const restart = button('Restart / clear route and notes', () => {
      stop(); route = []; stack.replaceChildren(); append(data.start, false); update('Restarted. Previous route and reflection notes cleared.');
    });
    controls.append(play, pause, restart);
    const progress = make('p', 'trickle-progress');
    const status = make('p', 'trickle-status'); status.setAttribute('role', 'status');
    const stack = make('div', 'trickle-stack');
    host.replaceChildren(header, controls, progress, status, stack);
    host.classList.add('trickle-player');
    function current() { return route[route.length - 1]; }
    function clearTimer() { if (timer !== null) clearTimeout(timer); timer = null; }
    function update(message) {
      const node = nodes.get(current().id);
      play.disabled = running || node.type === 'ending';
      pause.disabled = !running;
      progress.textContent = `Depth ${route.length} / ${route.filter(entry => nodes.get(entry.id).type === 'choice' && entry.selected !== null).length} decisions made${node.type === 'ending' ? ' / Scenario complete' : ''}`;
      if (message) status.textContent = message;
    }
    function stop(message) { clearTimer(); running = false; if (route.length) update(message); }
    function schedule() {
      clearTimer();
      if (!running || destroyed) return;
      const entry = current(), node = nodes.get(entry.id);
      if (node.type !== 'auto') return;
      timer = setTimeout(() => { timer = null; if (running && current() === entry) advance(entry, node.next, null, false); }, node.delayMs);
    }
    function setActive(entry, active) {
      entry.actions.querySelectorAll('button').forEach(el => { el.disabled = !active; });
      entry.revisit.hidden = active;
    }
    function advance(entry, destination, selected, focus) {
      if (destroyed || current() !== entry) return;
      clearTimer();
      entry.selected = selected;
      entry.actions.querySelectorAll('button').forEach((el, index) => {
        if (nodes.get(entry.id).type === 'choice') el.setAttribute('aria-pressed', String(index === selected));
      });
      setActive(entry, false);
      append(destination, focus);
      host.dispatchEvent(new CustomEvent('trickle:progress', { bubbles: true, detail: snapshot() }));
    }
    function append(id, focus) {
      const node = nodes.get(id);
      const card = make('article', 'trickle-card');
      const title = make('h3', '', node.title); title.tabIndex = -1;
      const actions = make('div', 'trickle-choices');
      const entry = { id, selected: null, note: '', card, actions, revisit: null };
      card.append(make('p', 'trickle-kicker', `${route.length + 1} / ${node.type === 'ending' ? 'Outcome' : node.type}`), title, make('p', 'trickle-body', node.body));
      if (node.prompt) {
        const label = make('label', 'trickle-reflection', `${node.prompt} (optional, not saved)`);
        const input = make('textarea'); input.rows = 3; input.maxLength = 4000;
        input.addEventListener('input', () => { entry.note = input.value; }, options);
        label.append(input); card.append(label);
      }
      if (node.type === 'choice') {
        actions.setAttribute('role', 'group'); actions.setAttribute('aria-label', node.title);
        node.choices.forEach((choice, index) => {
          const el = button(choice.label, () => advance(entry, choice.next, index, true));
          el.setAttribute('aria-pressed', 'false'); actions.append(el);
        });
      } else if (node.type !== 'ending') actions.append(button(node.button || 'Continue', () => advance(entry, node.next, null, true)));
      entry.revisit = button(node.type === 'choice' ? 'Change this decision (clear later cards)' : 'Return here (clear later cards)', () => {
        if (destroyed) return;
        stop();
        const index = route.indexOf(entry);
        route.splice(index + 1).forEach(later => later.card.remove());
        entry.selected = null;
        entry.actions.querySelectorAll('[aria-pressed]').forEach(el => el.setAttribute('aria-pressed', 'false'));
        setActive(entry, true);
        update('Later cards and their notes cleared. Choose a new route from here.');
        title.focus({ preventScroll: true });
      });
      entry.revisit.className = 'trickle-revisit'; entry.revisit.hidden = true;
      card.append(actions, entry.revisit); route.push(entry); stack.append(card);
      if (node.type === 'ending') { clearTimer(); running = false; }
      update(node.type === 'ending' ? 'Scenario complete. Review your route, export it or restart.' : `${node.title} revealed.${node.type === 'auto' && !running ? ' Press Continue or enable timed trickle.' : ''}`);
      if (focus) title.focus({ preventScroll: true });
      schedule();
    }
    function snapshot() {
      return { version: 1, scenarioId: data.id, complete: nodes.get(current().id).type === 'ending', route: route.map(entry => ({
        node: entry.id, choice: entry.selected === null ? null : nodes.get(entry.id).choices[entry.selected].label, note: entry.note,
      })) };
    }
    document.addEventListener('visibilitychange', () => { if (document.hidden) stop('Timed trickle paused while this tab is hidden.'); }, options);
    append(data.start, false);
    return {
      get: snapshot,
      pause() { stop('Timed trickle paused.'); },
      destroy() { destroyed = true; clearTimer(); controller.abort(); host.replaceChildren(); },
    };
  }
  const api = { validate, mount };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else global.TrickleScenario = api;
})(typeof window === 'undefined' ? globalThis : window);
