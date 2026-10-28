(function (global) {
  'use strict';
  const instances = new WeakMap();
  function mount(host) {
    if (!(host instanceof HTMLElement) || instances.has(host)) throw new Error('Use an unmounted lesson element.');
    const steps = [...host.querySelectorAll('[data-lesson-step]')];
    const status = host.querySelector('.lesson-status');
    const progress = host.querySelector('progress');
    const message = host.querySelector('[data-sequence-status]');
    const mode = host.querySelector('[data-sequence-mode]');
    const interval = host.querySelector('[data-sequence-interval]');
    const play = host.querySelector('[data-sequence-play]');
    const pause = host.querySelector('[data-sequence-pause]');
    if (!steps.length || !status || !progress || !message || !mode || !interval || !play || !pause ||
        steps.some(step => !step.querySelector('[data-lesson-complete]'))) {
      throw new Error('Lesson requires stages, completion controls, progress, status and sequence settings.');
    }
    const controller = new AbortController();
    const options = { signal: controller.signal };
    const journals = [];
    let revealed = 1;
    let completed = 0;
    let timer = null;
    let running = false;
    function report(text) { message.textContent = text; }
    function render() {
      progress.max = steps.length;
      progress.value = completed;
      steps.forEach((step, index) => {
        step.hidden = index >= revealed;
        step.classList.toggle('is-complete', index < completed);
        step.querySelector('[data-lesson-complete]').disabled = index !== completed;
        step.querySelector('.lesson-block-state').textContent = index < completed ? 'Complete' : index === completed ? 'Ready' : 'Awaiting earlier completion';
        step.querySelector('.lesson-complete-label').textContent = index < completed ? 'Completed. You can revisit this stage.' : '';
      });
      status.textContent = `${completed} of ${steps.length} stages completed. ${revealed} revealed.${completed === steps.length ? ' Lesson complete; all stages remain available for review.' : ''}`;
      play.disabled = mode.value !== 'trickle' || running || revealed === steps.length;
      pause.disabled = !running;
      interval.disabled = mode.value !== 'trickle';
    }
    function stop(text) {
      if (timer !== null) clearTimeout(timer);
      timer = null;
      running = false;
      render();
      if (text) report(text);
    }
    function revealNext(focus) {
      if (revealed >= steps.length) return;
      const next = steps[revealed];
      revealed += 1;
      next.hidden = false;
      next.open = true;
      next.classList.remove('lesson-revealed');
      void next.offsetWidth;
      next.classList.add('lesson-revealed');
      render();
      if (focus) next.querySelector('summary').focus({ preventScroll: true });
      host.dispatchEvent(new CustomEvent('lesson-sequence:reveal', { bubbles: true, detail: { step: revealed - 1, revealed, completed } }));
    }
    function delay() {
      if (!interval.checkValidity() || !Number.isFinite(interval.valueAsNumber)) {
        stop('Enter a reveal interval from 0.5 to 8 seconds, in 0.5-second steps.');
        interval.setAttribute('aria-invalid', 'true');
        return null;
      }
      interval.removeAttribute('aria-invalid');
      return interval.valueAsNumber * 1000;
    }
    function schedule() {
      const ms = delay();
      if (ms === null) return;
      timer = setTimeout(() => {
        timer = null;
        if (!running) return;
        revealNext(false);
        if (revealed === steps.length) stop('All stages revealed. No completion has been awarded by the timer.');
        else schedule();
      }, ms);
    }
    function complete(index) {
      if (!Number.isInteger(index) || index < 0 || index >= steps.length) throw new RangeError('Completion step must be a valid zero-based stage index.');
      if (index < completed) return;
      if (index !== completed || index >= revealed) throw new Error('Complete revealed stages in order.');
      completed += 1;
      if (mode.value === 'completion' && revealed < completed + 1) revealNext(true);
      render();
      report(completed === steps.length ? 'Lesson complete. All revealed content remains available.' : 'Stage completed.');
      host.dispatchEvent(new CustomEvent('lesson-sequence:progress', { bubbles: true, detail: { completed, revealed, total: steps.length } }));
      if (completed === steps.length) host.querySelector('[data-lesson-reset]').focus({ preventScroll: true });
    }
    function restart() {
      stop();
      revealed = 1;
      completed = 0;
      steps.forEach((step, index) => {
        step.open = index === 0;
        step.classList.remove('lesson-revealed');
      });
      render();
      report('Sequence restarted. Your notes and saved copies have not been changed.');
    }
    steps.forEach((step, index) => {
      step.open = index === 0;
      step.querySelector('[data-lesson-complete]').addEventListener('click', () => complete(index), options);
    });
    host.addEventListener('lesson:complete', event => {
      try { complete(event.detail?.step); }
      catch (error) { report(`Activity completion rejected: ${error.message}`); }
    }, options);
    host.querySelector('[data-lesson-reset]').addEventListener('click', restart, options);
    mode.addEventListener('change', () => {
      stop();
      if (mode.value === 'completion' && revealed < completed + 1) revealNext(false);
      render();
      report(mode.value === 'trickle' ? 'Timed trickle selected. Press Start trickle; reveals do not award completion.' : 'Complete stages in order to reveal the next. Previously revealed stages stay available.');
    }, options);
    play.addEventListener('click', () => {
      if (mode.value !== 'trickle' || revealed === steps.length) return;
      if (delay() === null) return;
      running = true;
      render();
      report('Trickle running. New stages fade in without moving keyboard focus.');
      schedule();
    }, options);
    pause.addEventListener('click', () => stop('Trickle paused. Revealed stages and notes are unchanged.'), options);
    interval.addEventListener('input', () => {
      if (running) { clearTimeout(timer); timer = null; schedule(); }
      else delay();
    }, options);
    document.addEventListener('visibilitychange', () => {
      if (document.hidden && running) stop('Trickle paused while the page is hidden. Press Start to resume.');
    }, options);
    host.querySelectorAll('[data-journal-card]').forEach(card => journals.push(global.JournalCard.mountJournalCard(card)));
    const api = {
      complete, restart,
      pause() { stop('Trickle paused.'); },
      get() { return { completed, revealed, total: steps.length, mode: mode.value, running }; },
      destroy() { stop(); controller.abort(); journals.forEach(journal => journal.destroy()); instances.delete(host); },
    };
    instances.set(host, api);
    render();
    return api;
  }
  global.LessonSequence = { mount, get: host => instances.get(host) };
  document.querySelectorAll('[data-lesson-template]').forEach(mount);
  const picker = document.querySelector('[data-template-picker]');
  if (picker) picker.addEventListener('change', () => {
    document.querySelectorAll('[data-template-view]').forEach(view => {
      const active = view.dataset.templateView === picker.value;
      if (!active) instances.get(view.querySelector('[data-lesson-template]')).pause();
      view.hidden = !active;
    });
  });
})(window);
