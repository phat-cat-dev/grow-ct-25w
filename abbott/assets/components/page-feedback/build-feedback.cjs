const fs = require('node:fs');
const path = require('node:path');
const drawings = {
  conversation: `<circle cx="92" cy="86" r="58" fill="currentColor" opacity=".08"/>
<path d="M24 62C38 24 91 17 128 42M146 92c-9 35-49 51-82 37" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="3 7" stroke-linecap="round"/>
<g transform="rotate(-8 70 65)"><path d="M32 39h71q10 0 10 10v36q0 10-10 10H64L46 110V95H32q-10 0-10-10V49q0-10 10-10Z" fill="var(--feedback-paper,#fff)" stroke="currentColor" stroke-width="3"/><path d="M40 58h54M40 72h36" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></g>
<g transform="rotate(9 119 112)"><path d="M94 91h46q8 0 8 8v25q0 8-8 8h-9v13l-16-13H94q-8 0-8-8V99q0-8 8-8Z" fill="currentColor"/><path d="m103 111 8 8 18-19" fill="none" stroke="var(--feedback-paper,#fff)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></g>`,
  growth: `<circle cx="90" cy="87" r="61" fill="currentColor" opacity=".08"/>
<path d="M30 135h120M90 132V64" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
<path d="M89 103C53 105 36 81 42 59c34-1 51 18 47 44ZM92 83c-3-31 16-51 47-49 4 28-14 50-47 49Z" fill="var(--feedback-paper,#fff)" stroke="currentColor" stroke-width="3"/>
<path d="m57 74 31 29m19-36 20-19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
<path d="m47 32 3-9m98 79 9 3M25 109l-7 4" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
<circle cx="111" cy="135" r="4" fill="currentColor"/>`,
  fieldnote: `<rect x="38" y="29" width="104" height="124" rx="12" fill="currentColor" opacity=".08" transform="rotate(8 90 90)"/>
<g transform="rotate(-6 90 90)"><rect x="34" y="21" width="104" height="128" rx="10" fill="var(--feedback-paper,#fff)" stroke="currentColor" stroke-width="3"/><path d="M54 21v128M66 51h51M66 69h38M66 87h44" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="m76 120 10 9 24-25" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>
<path d="m132 98 18-33 9 5-18 33-10 7Z" fill="currentColor"/>`,
};
function illustration(kind) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180" fill="none" aria-hidden="true">${drawings[kind]}</svg>`;
}
for (const kind of Object.keys(drawings)) {
  fs.writeFileSync(path.join(__dirname, `${kind}.svg`), `${illustration(kind).replace('aria-hidden="true"', `role="img" aria-label="${kind} illustration"`)}\n`);
}
const variants = [
  { id: 'conversation', title: 'Make the next read better', kicker: 'A small response, a better resource', intro: 'Did this page help you find your next step?', yes: 'Yes, it helped', no: 'Not quite', className: '' },
  { id: 'growth', title: 'Help this lesson grow', kicker: 'Learning is a work in progress', intro: 'Was this explanation useful for your learning?', yes: 'That made sense', no: 'I need more clarity', className: ' feedback-card--growth' },
  { id: 'fieldnote', title: 'Leave a useful field note', kicker: 'Before you move on', intro: 'Did you find what you needed here?', yes: 'Found what I needed', no: 'Something is missing', className: ' feedback-card--compact' },
];
function card(variant) {
  const { id, title, kicker, intro, yes, no, className } = variant;
  return `<section class="feedback-card${className}" data-page-feedback="${id}" aria-labelledby="feedback-${id}-title">
<div class="feedback-card__art">${illustration(id)}</div>
<div class="feedback-card__body"><p class="feedback-card__kicker">${kicker}</p>
<h2 id="feedback-${id}-title">${title}</h2><p>${intro}</p>
<div class="feedback-card__choices" role="group" aria-label="Was this page helpful?">
<button type="button" data-feedback-choice="helpful" aria-pressed="false"><span aria-hidden="true">+</span> ${yes}</button>
<button type="button" data-feedback-choice="needs-work" aria-pressed="false"><span aria-hidden="true">&rarr;</span> ${no}</button></div>
<form data-feedback-form hidden><label>What worked, or what could be clearer? <span class="feedback-card__optional">(optional)</span>
<textarea rows="3" maxlength="2000" data-feedback-note placeholder="One specific suggestion is a good place to start."></textarea></label>
<p class="feedback-card__privacy">Draft only: nothing is sent or saved automatically. Avoid personal information. Download a response to keep or share it.</p>
<div class="feedback-card__actions"><button type="submit" data-feedback-export>Download response</button><button type="button" data-feedback-reset>Clear response</button></div></form>
<p class="feedback-card__status" data-feedback-status role="status">Choose a response to add an optional note.</p>
<footer class="feedback-card__footer"><a href="README.md">Contribution and integration guide</a><span>Template revised <time datetime="2026-10-18">18 October 2026</time></span>
<nav aria-label="Resource links"><a href="${id}.template.html" download>Get HTML template</a><a href="${id}.svg" download>Download illustration</a></nav></footer>
</div></section>`;
}
const styles = '<link rel="stylesheet" href="page-feedback.css">';
function page(title, body) {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title} | Feedback assets</title>${styles}</head>
<body class="feedback-demo"><main class="feedback-demo__inner"><nav aria-label="Feedback designs"><a href="index.html">All feedback designs</a></nav>${body}</main><script src="page-feedback.js"></script></body></html>\n`;
}
for (const variant of variants) {
  fs.writeFileSync(path.join(__dirname, `${variant.id}.template.html`), `${card(variant)}\n`);
  fs.writeFileSync(path.join(__dirname, `${variant.id}.html`), page(variant.title, card(variant)));
}
fs.writeFileSync(path.join(__dirname, 'index.html'), page('Page feedback cards',
  `<header class="feedback-demo__heading"><p>End-of-page / reusable components</p><h1>Keep the conversation open.</h1><p>Three original feedback designs for articles, lessons and resource pages. Token-driven, responsive and offline, with local response exports rather than a pretend submission.</p><div class="feedback-demo__themes" role="group" aria-label="Preview colour theme"><button type="button" data-feedback-theme="system" aria-pressed="true">System</button><button type="button" data-feedback-theme="light" aria-pressed="false">Light</button><button type="button" data-feedback-theme="dark" aria-pressed="false">Dark</button></div></header>${variants.map(card).join('\n')}`));
console.log('Built three feedback designs, HTML fragments and original SVG illustrations.');
