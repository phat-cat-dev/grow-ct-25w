const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..', '..', '..');
const source = fs.readFileSync(path.join(root, '.dev', 'assets', 'assets-grow', 'TOSORT', 'gallery', 'templates.html'), 'utf8');
const journal = fs.readFileSync(path.join(root, 'assets', 'components', 'journal-card', 'journal-card.html'), 'utf8');
const names = {
  journey: 'Milestone journey', maker: 'Maker lab', studio: 'Colour study',
  notebook: 'Thinking notebook', board: 'Water cycle', editorial: 'Reading and reflection',
};
const style = source.match(/<style>([\s\S]*?)<\/style>/);
if (!style) throw new Error('Template stylesheet not found.');
fs.writeFileSync(path.join(__dirname, 'template-layout.css'), style[1]);
function notes(id) {
  return journal.replaceAll('develop-your-thought', `lesson-${id}`)
    .replace('Develop your thought', `${names[id]} notes`)
    .replace('Sketch ready / save your ideas', 'Save notes');
}
function documentHtml(title, body) {
  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title} | Interactive lesson assets</title>
<link rel="stylesheet" href="template-layout.css">
<link rel="stylesheet" href="../../components/journal-card/journal-card.css">
<link rel="stylesheet" href="interactivities.css"></head>
<body><main class="wrap">${body}</main>
<script src="../../components/journal-card/journal-card.js"></script>
<script src="interactivities.js"></script></body></html>\n`;
}
for (const [id, title] of Object.entries(names)) {
  const match = source.match(new RegExp(`<section class="tpl" data-tpl="${id}"[\\s\\S]*?<\\/section>`));
  if (!match) throw new Error(`Missing template: ${id}`);
  let content = match[0].replace(' hidden', '')
    .replace(/<span class="[^"]*material-symbol[^"]*"[^>]*>[\s\S]*?<\/span>/g, '')
    .replace(/<label class="lesson-journal">[\s\S]*?<\/label>/g, '');
  content = content.replace(/<a class="ab btn primary">Complete and continue<\/a>/,
    '<button type="button" class="ab btn primary" data-journey-next>Complete and continue</button>');
  let controls = '';
  if (id === 'journey') controls = '<progress max="3" value="0" aria-label="Completed milestones"></progress><button type="button" data-journey-reset>Restart journey</button>';
  if (id === 'studio') controls = '<label>Study hue <input type="range" min="0" max="360" value="202" data-study-hue></label><output data-study-output>202 degrees</output>';
  if (id === 'notebook') controls = '<p>Choose a thinking prompt (your notes will not be replaced).</p><button type="button" data-prompt="What would you try first, and why?">First move</button><button type="button" data-prompt="What if the opposite were true?">Challenge it</button><button type="button" data-prompt="What evidence would change your mind?">Evidence</button><p data-prompt-display>What would you try first, and why?</p>';
  if (id === 'board') controls = '<button type="button" data-cycle-next>Reveal the next stage</button><button type="button" data-cycle-reset>Hide explanations</button>';
  if (id === 'editorial') controls = '<p>Choose a lens for your reading.</p><button type="button" data-prompt="What has the artist placed in the foreground?">Foreground</button><button type="button" data-prompt="How does the horizon change the sense of depth?">Horizon</button><button type="button" data-prompt="How might the scene change from another viewpoint?">Viewpoint</button><p data-prompt-display>What do you notice first?</p>';
  const body = `<nav class="asset-nav" aria-label="Asset navigation"><a href="index.html">All lesson interactivities</a></nav>
<div class="frame" data-lesson="${id}">${content}
<div class="activity-controls">${controls}<p role="status" data-activity-status></p></div>
${notes(id)}</div>`;
  fs.writeFileSync(path.join(__dirname, `${id}.html`), documentHtml(title, body));
}
fs.writeFileSync(path.join(__dirname, 'index.html'), documentHtml('Lesson interactivities',
  `<div class="frame"><h1>Lesson interactivities</h1><p>Six independent, offline lesson assets. Notes are saved only when you press Save; progress and controls reset on reload.</p><ul>${Object.entries(names).map(([id, name]) => `<li><a href="${id}.html">${name}</a></li>`).join('')}</ul></div>`));
console.log('Built six lesson interactivities and gallery.');
