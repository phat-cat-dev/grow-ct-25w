const fs = require('node:fs');
const path = require('node:path');
const source = fs.readFileSync(path.resolve(__dirname, '..', '..', '..', '.dev', 'assets', 'gallery', 'grow-stacks.html'), 'utf8');
const style = source.match(/<style>([\s\S]*?)<\/style>/);
const stacks = [...source.matchAll(/<div class="stack">([\s\S]*?<div class="note">[\s\S]*?<\/div>)\s*<\/div>/g)];
if (!style || stacks.length !== 2) throw new Error('Expected a stylesheet and two complete stack diagrams.');
fs.writeFileSync(path.join(__dirname, 'stack-layout.css'), style[1]);
const names = ['adapt-core-base', 'grow-core-base'];
function asset(match, index) {
  const name = names[index];
  const content = match[1].replace(/<div class="layer ([^"]+)"><div class="nm">([\s\S]*?)<\/div><div class="ds">([\s\S]*?)<\/div><\/div>/g,
    '<details class="layer $1" open><summary class="nm">$2</summary><div class="ds">$3</div></details>');
  return `<section class="stack" data-stack="${name}">
${content}
<div class="stack-controls">
<button type="button" data-step>Walk through layers</button>
<button type="button" data-show-all>Show all layers</button>
<button type="button" data-collapse>Close explanations</button>
<label>Visual profile <select data-profile><option value="default">Default</option><option value="compact">Compact violet</option><option value="airy">Airy green</option></select></label>
<p class="profile-note">Visual token demonstration only: this does not compile LESS or change the underlying architecture.</p>
<progress value="0" max="1" aria-label="${name} layers visited"></progress>
<p role="status" data-stack-status></p>
</div>
<form class="stack-check">
<h3>Check your understanding</h3>
<label>Who owns the mechanical structure in ${name}?
<select name="owner" required><option value="">Choose an answer</option><option value="adapt">Adapt's native structure</option><option value="grow">Grow's structure merged with Adapt's required structure</option><option value="profile">The customer style profile</option></select></label>
<button type="submit">Check answer</button>
<button type="button" data-check-reset>Try again</button>
<p role="status" data-check-status></p>
</form></section>`;
}
function documentHtml(title, content) {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title} | Interactive stacks</title><link rel="stylesheet" href="stack-layout.css"><link rel="stylesheet" href="stacks.css"></head>
<body><main class="wrap"><nav aria-label="Stack assets"><a href="index.html">Compare both</a> | <a href="adapt-core-base.html">Adapt stack</a> | <a href="grow-core-base.html">Grow stack</a></nav>
<h1>${title}</h1><p>Explore each layer, walk through the build order and check your understanding. Controls and practice answers reset on reload.</p>
<div class="stacks">${content}</div></main><script src="stacks.js"></script></body></html>\n`;
}
const assets = stacks.map(asset);
assets.forEach((content, index) => fs.writeFileSync(path.join(__dirname, `${names[index]}.html`), documentHtml(names[index], content)));
fs.writeFileSync(path.join(__dirname, 'index.html'), documentHtml('Two stacks, one Grow interface', assets.join('\n')));
console.log('Built two independent interactive stacks and comparison gallery.');
