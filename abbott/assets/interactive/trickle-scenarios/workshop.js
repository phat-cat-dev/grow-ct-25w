(function () {
  'use strict';
  const examples = window.TrickleExamples;
  const picker = document.getElementById('scenario-example');
  const editor = document.getElementById('scenario-json');
  const status = document.getElementById('author-status');
  let player;
  examples.forEach(example => picker.add(new Option(example.title, example.id)));
  function report(message, error = false) { status.textContent = message; status.dataset.error = String(error); }
  function load(data) {
    TrickleScenario.validate(data);
    if (player) player.destroy();
    player = TrickleScenario.mount(document.getElementById('scenario-player'), data);
    editor.value = JSON.stringify(data, null, 2);
    report(`Loaded "${data.title}": ${data.nodes.length} nodes. First card is ready.`);
  }
  function read() {
    if (editor.value.length > 1000000) throw new Error('Scenario JSON exceeds 1 MB.');
    return TrickleScenario.validate(JSON.parse(editor.value));
  }
  function attempt(action) {
    try { action(); }
    catch (error) { report(`${error.message} Current player was not replaced.`, true); }
  }
  function download(data, name) {
    const url = URL.createObjectURL(new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' }));
    const a = document.createElement('a'); a.href = url; a.download = name; a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    report(`${name} exported. Keep notes private if they contain personal information.`);
  }
  document.getElementById('load-example').addEventListener('click', () => attempt(() => load(examples.find(example => example.id === picker.value))));
  document.getElementById('validate-json').addEventListener('click', () => attempt(() => { const data = read(); report(`Valid: ${data.nodes.length} reachable nodes, no missing routes or cycles. Player unchanged.`); }));
  document.getElementById('apply-json').addEventListener('click', () => attempt(() => load(read())));
  document.getElementById('export-json').addEventListener('click', () => attempt(() => download(read(), 'scenario.json')));
  document.getElementById('export-route').addEventListener('click', () => download({ ...player.get(), exportedAt: new Date().toISOString() }, 'scenario-route.json'));
  document.getElementById('fill-template').addEventListener('click', () => {
    const data = JSON.parse(JSON.stringify(examples[0]));
    data.id = 'your-scenario'; data.title = '[Your scenario title]'; data.intro = '[Audience, context and learning intention]';
    data.nodes.forEach(node => {
      node.title = `[Title for ${node.id}]`; node.body = '[Write the situation or consequence]';
      if (node.prompt) node.prompt = '[Reflection prompt]';
      if (node.choices) node.choices.forEach((choice, index) => { choice.label = `[Option ${index + 1}]`; });
    });
    editor.value = JSON.stringify(data, null, 2);
    report('Deep template placed in editor. Replace all bracketed text, then Validate and play. Current player unchanged.');
  });
  document.getElementById('scenario-file').addEventListener('change', async event => {
    const file = event.target.files[0];
    if (!file) return;
    try {
      if (file.size > 1000000) throw new Error('Choose a JSON file smaller than 1 MB.');
      const text = await file.text();
      TrickleScenario.validate(JSON.parse(text));
      editor.value = text;
      report('File validated and loaded into editor. Press Validate and play to replace the current player.');
    } catch (error) { report(`Could not open scenario: ${error.message} Current editor and player retained.`, true); }
    event.target.value = '';
  });
  load(examples[0]);
})();
