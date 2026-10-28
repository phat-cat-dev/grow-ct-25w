(function () {
  'use strict';
  const presets = {
    inquiry: [
      ['Notice', 'What do you notice?', 'Describe a situation before trying to explain it. Separate what you observed from what you inferred.'],
      ['Question', 'Ask a useful question.', 'Identify one uncertainty that matters. What evidence would help you investigate it?'],
      ['Investigate', 'Compare the evidence.', 'Find two possible explanations. Consider the strengths and limits of the evidence for each.'],
      ['Explain', 'Build your explanation.', 'Connect your claim to the evidence. State what remains uncertain and what you would examine next.'],
    ],
    practice: [
      ['Orient', 'Know what success looks like.', 'Choose a skill and describe the features of a successful performance.'],
      ['Observe', 'Study a worked example.', 'Notice the decisions an experienced person makes, not just the final result.'],
      ['Try', 'Make a first attempt.', 'Try the task yourself. Record where you needed help or made an assumption.'],
      ['Feedback', 'Use feedback selectively.', 'Compare your attempt with the success criteria. Choose one specific improvement.'],
      ['Retry', 'Try again with intention.', 'Repeat the task using your improvement. Explain what changed and what still needs practice.'],
    ],
    reflection: [
      ['Recall', 'Return to a specific moment.', 'Describe an experience and the choice you made. Keep the account concrete.'],
      ['Interpret', 'Make sense of the experience.', 'What shaped your choice? Consider another interpretation before drawing a conclusion.'],
      ['Transfer', 'Choose your next action.', 'Explain what you will do differently in a future situation and how you will review its effect.'],
    ],
  };
  const host = document.querySelector('.learning-sequence');
  const container = host.querySelector('[data-steps]');
  const nav = host.querySelector('[data-learning-nav]');
  const countInput = document.querySelector('[data-count]');
  const sessions = new Map();
  let active = null, player = null, elements = [];
  function switchTo(key, count) {
    if (player) {
      const state = player.get();
      const previous = sessions.get(active);
      if (previous?.state) state.completed.push(...previous.state.completed.filter(i => i >= state.total));
      sessions.set(active, { elements, state });
      player.destroy();
    }
    active = key;
    let session = sessions.get(key);
    if (!session) {
      session = { elements: Array.from({ length: 10 }, (_, index) => {
        const [label, title, body] = presets[key][index] ??
          [`Step ${index + 1}`, `Extend your learning / ${index + 1}`, 'Add your own activity, practice task or reflection prompt for this step.'];
        const step = document.createElement('section');
        step.dataset.learningStep = ''; step.dataset.label = label;
        const heading = document.createElement('h2'); heading.textContent = title;
        const text = document.createElement('p'); text.textContent = body;
        const prompt = document.createElement('label'); prompt.textContent = 'Your thinking (optional, not saved)';
        const input = document.createElement('textarea'); input.rows = 3;
        prompt.append(input); step.append(heading, text, prompt);
        return step;
      }) };
    }
    elements = session.elements;
    const total = count ?? session.state?.total ?? presets[key].length;
    countInput.value = total;
    container.replaceChildren(...elements.slice(0, total));
    player = LearningSequence.mount(host);
    if (session.state) {
      for (const index of session.state.completed) {
        if (index >= total) continue;
        player.go(index);
        host.querySelector('[data-learning-complete]').click();
      }
      player.go(Math.min(session.state.index, total - 1));
    }
  }
  countInput.addEventListener('change', () => {
    if (!countInput.checkValidity() || !Number.isInteger(countInput.valueAsNumber)) {
      countInput.setAttribute('aria-invalid', 'true');
      host.querySelector('[data-learning-status]').textContent = 'Enter a whole number of steps from 1 to 10.';
      return;
    }
    countInput.removeAttribute('aria-invalid');
    if (player.get().total === countInput.valueAsNumber) return;
    switchTo(active, countInput.valueAsNumber);
  });
  document.querySelector('[data-preset]').addEventListener('change', event => switchTo(event.target.value));
  document.querySelector('[data-labels]').addEventListener('change', event => { nav.dataset.labels = event.target.checked ? 'always' : 'auto'; });
  switchTo('inquiry');
})();
