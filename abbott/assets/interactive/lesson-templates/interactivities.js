(function () {
  'use strict';
  document.querySelectorAll('[data-lesson]').forEach(host => {
    const status = host.querySelector('[data-activity-status]');
    const report = message => { status.textContent = message; };
    host.querySelectorAll('[data-journal-card]').forEach(card => JournalCard.mountJournalCard(card));
    const type = host.dataset.lesson;
    if (type === 'journey') {
      const steps = [...host.querySelectorAll('.milestone')];
      const next = host.querySelector('[data-journey-next]');
      const progress = host.querySelector('progress');
      let completed = 0;
      function render() {
        steps.forEach((step, index) => {
          step.hidden = index > completed;
          step.dataset.complete = String(index < completed);
          step.querySelector('.num').setAttribute('aria-label', `Stage ${index + 1}${index < completed ? ', completed' : ''}`);
        });
        progress.value = completed;
        next.disabled = completed === steps.length;
        next.textContent = completed === steps.length ? 'Journey complete' : `Complete stage ${completed + 1} and continue`;
        report(`${completed} of ${steps.length} milestones completed. Self-reported practice, not a scored assessment.`);
      }
      next.addEventListener('click', () => {
        completed = Math.min(steps.length, completed + 1);
        render();
        if (completed < steps.length) {
          steps[completed].tabIndex = -1;
          steps[completed].focus();
        } else host.querySelector('[data-journey-reset]').focus();
      });
      host.querySelector('[data-journey-reset]').addEventListener('click', () => { completed = 0; render(); next.focus(); });
      render();
    }
    if (type === 'maker') {
      const cards = [...host.querySelectorAll('.grid-3 .card-body')];
      cards.forEach((card, index) => {
        const label = document.createElement('label');
        const check = document.createElement('input');
        check.type = 'checkbox';
        label.append(check, ` Station ${index + 1} complete`);
        card.append(label);
        check.addEventListener('change', () => {
          report(`${host.querySelectorAll('.grid-3 input:checked').length} of ${cards.length} stations completed. Self-reported practice.`);
        });
      });
      report('Mark each station complete as you work. Progress lasts until reload.');
    }
    if (type === 'studio') {
      const hue = host.querySelector('[data-study-hue]');
      hue.addEventListener('input', () => {
        host.style.setProperty('--h', hue.value);
        host.querySelector('[data-study-output]').value = `${hue.value} degrees`;
      });
    }
    if (type === 'board') {
      const explanations = [...host.querySelectorAll('.grid-3 .card-text')];
      const next = host.querySelector('[data-cycle-next]');
      let revealed = 0;
      function render() {
        explanations.forEach((text, index) => { text.hidden = index >= revealed; });
        next.disabled = revealed === explanations.length;
        report(`${revealed} of ${explanations.length} explanations revealed.`);
      }
      next.addEventListener('click', () => {
        revealed = Math.min(explanations.length, revealed + 1);
        render();
        const text = explanations[revealed - 1];
        text.tabIndex = -1;
        text.focus();
      });
      host.querySelector('[data-cycle-reset]').addEventListener('click', () => { revealed = 0; render(); next.focus(); });
      render();
    }
    host.querySelectorAll('[data-prompt]').forEach(button => {
      button.setAttribute('aria-pressed', 'false');
      button.addEventListener('click', () => {
        host.querySelector('[data-prompt-display]').textContent = button.dataset.prompt;
        host.querySelectorAll('[data-prompt]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
        report('Thinking prompt changed. Your notes are unchanged.');
      });
    });
  });
})();
