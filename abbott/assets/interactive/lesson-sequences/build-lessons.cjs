const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..', '..', '..');
const site = path.join(root, '.dev', 'assets', 'ab-them', 'public', 'site');
const source = fs.readFileSync(path.join(site, 'source_index.html'), 'utf8');
const css = fs.readFileSync(path.join(site, 'site.css'), 'utf8');
const journal = fs.readFileSync(path.join(root, 'assets', 'components', 'journal-card', 'journal-card.html'), 'utf8');
const names = {
  guided: 'Guided field notes', workshop: 'Workshop canvas', story: 'Story scenes',
  casebook: 'Casebook', journey: 'Expedition route', studio: 'Reflective studio',
};
const cssStart = css.indexOf('.lesson-experiment {');
const endRule = '@media (prefers-reduced-motion: reduce) { .lesson-experiment .lesson-revealed { animation: none; } }';
const cssEnd = css.indexOf(endRule, cssStart);
if (cssStart < 0 || cssEnd < 0) throw new Error('Lesson layout stylesheet boundaries were not found.');
fs.writeFileSync(path.join(__dirname, 'lesson-layouts.css'), css.slice(cssStart, cssEnd + endRule.length));
function extract(id) {
  const marker = `<div class="lesson-experiment lesson-${id} page contentobject"`;
  const start = source.indexOf(marker);
  if (start < 0) throw new Error(`Missing lesson: ${id}`);
  const tags = /<div\b[^>]*>|<\/div>/g;
  tags.lastIndex = start;
  let depth = 0;
  let tag;
  while ((tag = tags.exec(source))) {
    depth += tag[0].startsWith('</') ? -1 : 1;
    if (depth === 0) return source.slice(start, tags.lastIndex);
  }
  throw new Error(`Unbalanced lesson: ${id}`);
}
function controls() {
  return `<div class="sequence-controls" aria-label="Sequential reveal settings">
<label>Reveal mode <select data-sequence-mode><option value="completion">On completion</option><option value="trickle">Timed trickle</option></select></label>
<label>Seconds between stages <input data-sequence-interval type="number" min=".5" max="8" step=".5" value="2"></label>
<button type="button" data-sequence-play>Start trickle</button><button type="button" data-sequence-pause>Pause trickle</button>
<p data-sequence-status role="status">Complete each stage to reveal the next.</p>
<p class="sequence-help">Timed reveals do not mark work complete. Completion is self-reported unless an activity supplies a completion event. Restart preserves your notes.</p></div>`;
}
function fragment(id) {
  let note = 0;
  let content = extract(id).replace(`data-lesson="${id}"`, `data-lesson-template="${id}"`)
    .replace(/<span class="lesson-depth">[\s\S]*?<\/span>/g, '')
    .replace(/<span class="[^"]*material-symbol[^"]*"[^>]*>[\s\S]*?<\/span>/g, '')
    .replace(/<(\/?)h4\b/g, '<$1h1').replace(/<(\/?)h5\b/g, '<$1h2').replace(/<(\/?)h6\b/g, '<$1h3')
    .replaceAll('aria-level="7"', 'aria-level="4"')
    .replace(/<label class="lesson-journal">[\s\S]*?<\/label>/g, () => {
      note += 1;
      return journal.replaceAll('develop-your-thought', `${id}-note-${note}`)
        .replace('Develop your thought', 'Practice notes')
        .replace(/<(\/?)h3\b/g, '<$1h4')
        .replace('Sketch ready / save your ideas', 'Save notes');
    });
  const index = content.indexOf('<div class="page__inner">');
  if (index < 0) throw new Error(`Missing page container: ${id}`);
  content = content.slice(0, index) + controls() + content.slice(index);
  return content;
}
function documentHtml(title, content) {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title} | Lesson templates</title><link rel="stylesheet" href="sequence.css"><link rel="stylesheet" href="lesson-layouts.css"><link rel="stylesheet" href="../../components/journal-card/journal-card.css"></head>
<body><main class="sequence-page"><nav class="sequence-nav" aria-label="Lesson template assets"><a href="index.html">All templates</a> | <a href="sequential.html">Sequential reveal playground</a></nav>
${content}</main><script src="../../components/journal-card/journal-card.js"></script><script src="sequence.js"></script></body></html>\n`;
}
const fragments = Object.entries(names).map(([id, title]) => {
  const content = fragment(id);
  fs.writeFileSync(path.join(__dirname, `${id}.template.html`), `${content}\n`);
  fs.writeFileSync(path.join(__dirname, `${id}.html`), documentHtml(title, content));
  return [id, content];
});
fs.writeFileSync(path.join(__dirname, 'index.html'), documentHtml('Six lesson compositions',
  `<h1>Six reusable lesson templates</h1><p>Editorial, workbench, cinematic, evidence-board, expedition and open-studio compositions. Each includes three collapsible stages, completion, sequential fading and saved journals. Media and plugin slots remain explicitly labelled placeholders.</p><p><a href="sequential.html">Try timed trickle or completion-driven fades</a></p><ul>${Object.entries(names).map(([id, title]) => `<li><a href="${id}.html">${title}</a> / <a href="${id}.template.html" download>HTML fragment</a></li>`).join('')}</ul>`));
fs.writeFileSync(path.join(__dirname, 'sequential.html'), documentHtml('Sequential reveal playground',
  `<h1>Sequential reveal playground</h1><p>Choose a composition, then reveal stages on completion or let them trickle in one after another. Switch compositions without losing this page's drafts. Progress resets on reload; press Save to persist notes.</p>
<label class="template-picker">Composition <select data-template-picker>${Object.entries(names).map(([id, title]) => `<option value="${id}"${id === 'workshop' ? ' selected' : ''}>${title}</option>`).join('')}</select></label>
${fragments.map(([id, content]) => `<div data-template-view="${id}"${id === 'workshop' ? '' : ' hidden'}>${content}</div>`).join('\n')}`));
console.log('Built six standalone lessons, six HTML fragments and sequential reveal playground.');
