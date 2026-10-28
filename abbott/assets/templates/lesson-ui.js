(function () {
  document.querySelectorAll('[data-horizontal-accordion]').forEach(function (accordion) {
    var triggers = Array.from(accordion.querySelectorAll('.horizontal-trigger'));
    triggers.forEach(function (trigger, index) {
      trigger.addEventListener('click', function () {
        triggers.forEach(function (button) {
          var open = button === trigger;
          button.setAttribute('aria-expanded', String(open));
          button.parentElement.classList.toggle('is-open', open);
          button.nextElementSibling.inert = !open;
          button.nextElementSibling.querySelector('[role="region"]').hidden = !open;
        });
      });
      trigger.addEventListener('keydown', function (event) {
        var next;
        if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (index + 1) % triggers.length;
        if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (index + triggers.length - 1) % triggers.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = triggers.length - 1;
        if (next !== undefined) {
          event.preventDefault();
          triggers[next].focus();
        }
      });
    });
  });
  document.querySelectorAll('[data-lesson]').forEach(function (lesson) {
    var blocks = Array.from(lesson.querySelectorAll('[data-lesson-step]'));
    var completed = new Set();
    var status = lesson.querySelector('.lesson-status');
    var progress = lesson.querySelector('progress');
    var heading = lesson.closest('.outline-section').querySelector('h3.outline-title');
    heading.dataset.layer = 'd1';
    function update() {
      progress.value = completed.size;
      status.textContent = completed.size + ' of 3 stages completed.' + (completed.size === 3 ? ' Lesson complete. All stages remain available for review.' : ' Complete the next activity to continue.');
    }
    blocks.forEach(function (block, index) {
      block.querySelector('[data-lesson-complete]').addEventListener('click', function () {
        if (completed.has(index)) return;
        completed.add(index);
        block.classList.add('is-complete');
        this.disabled = true;
        block.querySelector('.lesson-block-state').textContent = 'Complete';
        block.querySelector('.lesson-complete-label').textContent = 'Completed — revisit this stage whenever you like.';
        var next = blocks[index + 1];
        if (next) {
          next.hidden = false;
          next.open = true;
          next.classList.add('lesson-revealed');
          next.querySelector('.lesson-block-state').textContent = 'Ready';
          next.querySelector('summary').focus({ preventScroll: true });
        }
        update();
      });
    });
    lesson.querySelector('[data-lesson-reset]').addEventListener('click', function () {
      completed.clear();
      blocks.forEach(function (block, index) {
        block.hidden = index !== 0;
        block.open = index === 0;
        block.classList.remove('is-complete', 'lesson-revealed');
        block.querySelector('[data-lesson-complete]').disabled = false;
        block.querySelector('.lesson-complete-label').textContent = '';
        block.querySelector('.lesson-block-state').textContent = index === 0 ? 'Ready' : 'Next stage';
        block.querySelectorAll('textarea').forEach(function (input) { input.value = ''; });
      });
      lesson.querySelector('.lesson-frontmatter').open = true;
      update();
      status.textContent = 'Lesson restarted. Notes cleared; aims and stage 1 are open.';
    });
  });
})();
