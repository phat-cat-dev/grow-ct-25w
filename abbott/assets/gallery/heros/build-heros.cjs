const fs = require('node:fs');
const path = require('node:path');
const variants = [
  ['aurora', 'Module 03 / Colour', 'Seeing depth in colour', 'How warm and cool, light and dark pull shapes forward or push them back.', false],
  ['mesh', 'Maker lab', 'Learn by taking it apart', 'Inspect a model, make something of your own, then compare the result.', false],
  ['gradient', 'New course', 'Draw to think', 'A sketchbook approach to ideas: observe, mark up, revise.', true],
  ['dots', 'Workshop', 'A quiet place to practise', 'Short, low-stakes exercises you can return to any time.', false],
  ['waves', 'Science / Unit 2', 'The water cycle', 'Follow a drop as it evaporates, gathers into cloud, and falls again.', false],
  ['night', 'Capstone', 'Put it all together', 'One project that draws on everything from the course.', true],
  ['editorial', 'Reading room', 'Make space for a different perspective', 'Read closely, notice the assumptions, and bring your own questions.', false],
  ['blueprint', 'Investigation', 'Build an explanation from evidence', 'Map what you know. Test what you think. Revise what you find.', false],
  ['split', 'Your next step', 'Small experiments. Useful discoveries.', 'A practical route from a first idea to something you can test.', false],
];
const articles = [];
const waves = '<svg viewBox="0 0 400 100" preserveAspectRatio="none" aria-hidden="true"><path d="M0 60 q50 -24 100 0 t100 0 t100 0 t100 0 V100 H0Z"></path><path d="M0 72 q50 -20 100 0 t100 0 t100 0 t100 0 V100 H0Z"></path></svg>';
for (const [name, kicker, title, intro, centre] of variants) {
  const animated = !['editorial', 'blueprint', 'split'].includes(name);
  const art = name === 'waves' ? waves : name === 'night' ? '<span></span><span></span><span></span><span></span>' : '';
  const markup = `<header class="asset-hero asset-hero--${name}${centre ? ' asset-hero--centre' : ''}" data-hero-playing="false">
  <div class="asset-hero__art" aria-hidden="true">${art}</div>
  <div class="asset-hero__content">
    <span class="asset-hero__kicker">${kicker}</span>
    <h1 class="asset-hero__title">${title}</h1>
    <p class="asset-hero__intro">${intro}</p>
    <p class="asset-hero__meta">15 minutes / 3 stages / return any time</p>
    <nav class="asset-hero__actions" aria-label="Lesson links"><a class="asset-hero__link" href="#lesson-content">Start lesson</a><a class="asset-hero__link asset-hero__link--secondary" href="#lesson-outline">View outline</a></nav>
  </div>
  ${animated ? '<button class="asset-hero__motion" type="button" data-hero-motion aria-pressed="false">Play motion</button>' : ''}
</header>`;
  fs.writeFileSync(path.join(__dirname, `${name}.html`), markup + '\n');
  articles.push(`<section aria-label="${name} example"><h2>${name}</h2>${markup}</section>`);
}
fs.writeFileSync(path.join(__dirname, 'index.html'), `<!doctype html>
<html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Individual hero assets</title><link rel="stylesheet" href="./heros.css">
<style>:root { --h:202; --s:72%; --accent:hsl(var(--h) var(--s) 38%); --ink:#24313b; --ink-soft:#50616e; --surface-1:#fafcfd; --surface-2:#eaf0f5; --line:#bdcbd5; } :root[data-theme="dark"] { --ink:#edf2f6; --ink-soft:#b4c6d2; --surface-1:#172832; --surface-2:#223946; --line:#4c6473; --accent:hsl(var(--h) var(--s) 72%); color-scheme:dark; } body { margin:0; padding:1rem; background:var(--surface-2); color:var(--ink); font:1rem/1.6 system-ui,sans-serif; } main { max-width:85rem; margin:auto; } main>section { margin-block:2rem; } .controls { display:flex; flex-wrap:wrap; gap:1rem; margin-block:1rem; } .controls button { font:inherit; min-height:2.75rem; }</style></head>
<body><main><h1>Hero assets / nine independent variants</h1><p>Copy a hero fragment and include heros.css. Animated variants start still; Play motion is optional and reduced motion is always respected.</p><div class="controls"><label>Hue <input type="range" min="0" max="360" value="202" id="hue"></label><button type="button" id="theme" aria-pressed="false">Dark theme</button></div>
${articles.join('\n')}
<section id="lesson-outline" tabindex="-1"><h2>Example outline</h2><ol><li>Observe</li><li>Practise</li><li>Reflect</li></ol></section><section id="lesson-content" tabindex="-1"><h2>Example lesson destination</h2><p>Replace these fragment destinations with your own lesson links.</p></section></main>
<script src="./heros.js"></script><script>document.getElementById('hue').addEventListener('input',function(){document.documentElement.style.setProperty('--h',this.value);});document.getElementById('theme').addEventListener('click',function(){const dark=this.getAttribute('aria-pressed')!=='true';this.setAttribute('aria-pressed',String(dark));document.documentElement.dataset.theme=dark?'dark':'light';});</script></body></html>\n`);
console.log('Built 9 individual hero fragments and a preview gallery.');
