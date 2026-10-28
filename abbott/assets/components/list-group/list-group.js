(function () {
  'use strict';
  const groups = {
    notice: { title: 'Notice and collect', prompts: ['What stands out first?', 'Which details repeat?', 'What evidence would you collect?'] },
    try: { title: 'Try and compare', prompts: ['What is the smallest change you could test?', 'How does the result compare with your prediction?'] },
    reflect: { title: 'Reflect and apply', prompts: ['What worked, and why?', 'What would you change next time?', 'Where else could you use this approach?'] },
  };
  document.querySelectorAll('[data-list-example]').forEach(host => {
    const buttons = [...host.querySelectorAll('[data-list-group]')];
    buttons.forEach(button => button.addEventListener('click', () => {
      const group = groups[button.dataset.listGroup];
      if (!group) throw new Error(`Unknown learning group: ${button.dataset.listGroup}`);
      buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      host.querySelector('h3').textContent = group.title;
      host.querySelector('[data-list-prompts]').replaceChildren(...group.prompts.map(prompt => {
        const item = document.createElement('li');
        item.textContent = prompt;
        return item;
      }));
      host.querySelector('[data-list-status]').textContent = `${group.title} selected: ${group.prompts.length} prompts.`;
    }));
  });
})();
