(function (global) {
  'use strict';
  const instances = new WeakMap();
  function mount(host) {
    if (!(host instanceof HTMLElement) || instances.has(host)) throw new Error('Use an unmounted learning sequence.');
    const steps = [...host.querySelectorAll('[data-learning-step]')];
    const nav = host.querySelector('[data-learning-nav]');
    const status = host.querySelector('[data-learning-status]');
    const back = host.querySelector('[data-learning-back]');
    const next = host.querySelector('[data-learning-next]');
    const complete = host.querySelector('[data-learning-complete]');
    if (!steps.length || !nav || !status || !back || !next || !complete ||
        steps.some(step => !step.dataset.label || !step.querySelector('h2,h3,h4'))) {
      throw new Error('A sequence needs labelled steps with headings, navigation, status, Back, Next and completion controls.');
    }
    const abort = new AbortController();
    const done = new Set();
    const originalNav = [...nav.childNodes];
    const originalHidden = steps.map(step => step.hidden);
    let index = 0, destroyed = false;
    const headingTabindices = new Map();
    const buttons = steps.map((step, i) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.setAttribute('aria-label', `Step ${i + 1}: ${step.dataset.label}`);
      const number = document.createElement('span');
      number.className = 'learning-number';
      number.setAttribute('aria-hidden', 'true');
      number.textContent = String(i + 1).padStart(2, '0');
      const label = document.createElement('span');
      label.className = 'expand-label';
      label.setAttribute('aria-hidden', 'true');
      const inner = document.createElement('span');
      const text = document.createElement('span');
      text.className = 'expand-label-text';
      text.textContent = step.dataset.label;
      inner.append(text); label.append(inner); button.append(number, label);
      button.addEventListener('click', () => go(i), { signal: abort.signal });
      return button;
    });
    nav.replaceChildren(...buttons);
    function snapshot() { return { index, total: steps.length, completed: [...done].sort((a, b) => a - b) }; }
    function render() {
      steps.forEach((step, i) => { step.hidden = i !== index; });
      buttons.forEach((button, i) => {
        if (i === index) button.setAttribute('aria-current', 'step');
        else button.removeAttribute('aria-current');
        button.dataset.complete = String(done.has(i));
        button.setAttribute('aria-label', `Step ${i + 1}: ${steps[i].dataset.label}${done.has(i) ? ', completed' : ''}`);
      });
      back.disabled = index === 0;
      next.disabled = index === steps.length - 1;
      complete.disabled = done.has(index);
      complete.textContent = done.has(index) ? 'Step completed' : 'Mark step complete';
      status.textContent = `Step ${index + 1} of ${steps.length} / ${done.size} completed${done.size === steps.length ? ' / Sequence complete' : ''}`;
    }
    function go(value, focus = false) {
      if (destroyed) throw new Error('This learning sequence has been destroyed.');
      if (!Number.isInteger(value) || value < 0 || value >= steps.length) throw new RangeError('Choose a valid zero-based step index.');
      index = value;
      render();
      if (focus) {
        const heading = steps[index].querySelector('h2,h3,h4');
        if (!headingTabindices.has(heading)) headingTabindices.set(heading, heading.getAttribute('tabindex'));
        heading.tabIndex = -1;
        heading.focus({ preventScroll: true });
      }
      host.dispatchEvent(new CustomEvent('learning-sequence:change', { bubbles: true, detail: snapshot() }));
    }
    back.addEventListener('click', () => go(index - 1, true), { signal: abort.signal });
    next.addEventListener('click', () => go(index + 1, true), { signal: abort.signal });
    complete.addEventListener('click', () => {
      done.add(index); render();
      if (!next.disabled) next.focus();
      else if (!back.disabled) back.focus();
      else buttons[index].focus();
      host.dispatchEvent(new CustomEvent('learning-sequence:progress', { bubbles: true, detail: snapshot() }));
    }, { signal: abort.signal });
    render();
    instances.set(host, true);
    return {
      go, get: snapshot,
      reset() { if (destroyed) throw new Error('This learning sequence has been destroyed.'); done.clear(); go(0); },
      destroy() {
        destroyed = true; abort.abort(); nav.replaceChildren(...originalNav);
        steps.forEach((step, i) => { step.hidden = originalHidden[i]; });
        headingTabindices.forEach((value, heading) => {
          if (value === null) heading.removeAttribute('tabindex');
          else heading.setAttribute('tabindex', value);
        });
        instances.delete(host);
      },
    };
  }
  global.LearningSequence = { mount };
})(window);
