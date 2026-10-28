(function (global) {
  'use strict';
  function mount(host) {
    if (!(host instanceof HTMLElement) || host.hasAttribute('data-feedback-mounted')) throw new Error('Use an unmounted feedback card.');
    const form = host.querySelector('[data-feedback-form]');
    const note = host.querySelector('[data-feedback-note]');
    const status = host.querySelector('[data-feedback-status]');
    const choices = [...host.querySelectorAll('[data-feedback-choice]')];
    if (!form || !note || !status || choices.length !== 2 || !host.querySelector('[data-feedback-reset]')) throw new Error('Feedback card needs choices, form, note, reset and status.');
    const controller = new AbortController();
    const options = { signal: controller.signal };
    let response = null;
    function snapshot() {
      return { version: 1, cardId: host.dataset.pageFeedback, page: location.pathname, response, note: note.value };
    }
    function changed() {
      host.dispatchEvent(new CustomEvent('page-feedback:change', { bubbles: true, detail: snapshot() }));
    }
    choices.forEach(button => button.addEventListener('click', () => {
      response = button.dataset.feedbackChoice;
      choices.forEach(choice => choice.setAttribute('aria-pressed', String(choice === button)));
      form.hidden = false;
      status.textContent = 'Response selected. This is a local draft only; nothing has been sent.';
      changed();
    }, options));
    note.addEventListener('input', () => {
      status.textContent = 'Draft updated. Download your response to keep a copy; nothing has been sent.';
      changed();
    }, options);
    host.querySelector('[data-feedback-reset]').addEventListener('click', () => {
      response = null;
      form.reset();
      form.hidden = true;
      choices.forEach(choice => choice.setAttribute('aria-pressed', 'false'));
      status.textContent = 'Response and note cleared. Nothing was saved or sent.';
      choices[0].focus();
      changed();
    }, options);
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (!response) { status.textContent = 'Choose a response before downloading.'; choices[0].focus(); return; }
      const record = { ...snapshot(), exportedAt: new Date().toISOString() };
      const url = URL.createObjectURL(new Blob([JSON.stringify(record, null, 2)], { type: 'application/json' }));
      const link = document.createElement('a');
      link.href = url;
      link.download = 'page-feedback.json';
      link.click();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      status.textContent = 'Response downloaded, not submitted. Share the file through your preferred feedback channel.';
      host.dispatchEvent(new CustomEvent('page-feedback:export', { bubbles: true, detail: record }));
    }, options);
    host.setAttribute('data-feedback-mounted', '');
    return { get: snapshot, destroy() { controller.abort(); host.removeAttribute('data-feedback-mounted'); } };
  }
  global.PageFeedback = { mount };
  document.querySelectorAll('[data-page-feedback]').forEach(mount);
  document.querySelectorAll('button[data-feedback-theme]').forEach(button => button.addEventListener('click', () => {
    document.body.dataset.feedbackTheme = button.dataset.feedbackTheme;
    document.querySelectorAll('button[data-feedback-theme]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  }));
})(window);
