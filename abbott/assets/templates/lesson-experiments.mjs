export const LESSON_EXPERIMENTS = [
  { id: 'guided', title: 'Guided field notes', icon: 'route', layout: 'guided', description: 'A quiet reading column with a companion field-note rail.', steps: ['Read the situation', 'Explore the evidence', 'Reflect and apply'] },
  { id: 'workshop', title: 'Workshop canvas', icon: 'construction', layout: 'workshop', description: 'A full-width briefing above a two-column demonstration and practice bench.', steps: ['Watch and notice', 'Make a first attempt', 'Review your approach'] },
  { id: 'story', title: 'Story chapters', icon: 'auto_stories', layout: 'story', description: 'Large chapter bands alternate narrative and image placeholders.', steps: ['Meet the challenge', 'Find the turning point', 'Write the next chapter'] },
  { id: 'casebook', title: 'Case investigation', icon: 'search', layout: 'casebook', description: 'A case-file rail accompanies evidence cards and a decision workspace.', steps: ['Open the case file', 'Compare the clues', 'Make your decision'] },
  { id: 'journey', title: 'Milestone journey', icon: 'flag', layout: 'journey', description: 'A numbered vertical route makes each revealed stage a visible milestone.', steps: ['Orient yourself', 'Cross the practice bridge', 'Reach the checkpoint'] },
  { id: 'studio', title: 'Reflective studio', icon: 'draw', layout: 'studio', description: 'A generous visual workspace pairs with a journal, then a synthesis gallery.', steps: ['Observe and collect', 'Sketch an interpretation', 'Curate your learning'] },
];

const lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vitae justo vel arcu consequat facilisis. Suspendisse potenti. Donec eget neque at sapien cursus posuere.';
export function horizontalPanels() {
  const panels = [
    { title: 'Discover', icon: 'explore', body: () => `${scene('field', 'Notice the landscape')}${card('Start with curiosity', 'lightbulb', 'primary', `<p>${lorem}</p>`, 'tinted')}` },
    { title: 'Investigate', icon: 'search', body: () => `${card('Follow the clues', 'fingerprint', 'comment', widget('evidence'), 'tinted')}${card('Record a hypothesis', 'edit_note', 'secondary', widget('journal'))}` },
    { title: 'Make', icon: 'construction', body: () => `${card('Your workspace', 'extension', 'info', widget('activity'))}${card('Keep a working note', 'draw', 'primary', widget('journal'), 'tinted')}` },
    { title: 'Reflect', icon: 'flag', body: () => `${card('What changed?', 'psychology', 'positive', widget('journal'), 'tinted')}${card('Carry it forward', 'arrow_forward', 'primary', '<p>One insight. One experiment. One next step.</p><ul><li>What will you keep?</li><li>What will you try differently?</li></ul>')}` },
  ];
  return `<div class="lesson-experiment horizontal-example" data-horizontal-accordion><p class="note">Open a numbered rail to slide its workspace into view. One panel stays open at a time; each workspace can contain multiple components. On narrow screens the rails stack vertically.</p><div class="horizontal-panels">${panels.map((panel, i) => `<div class="horizontal-panel${i === 0 ? ' is-open' : ''}"><button type="button" class="ab btn primary ${i % 2 ? 'soft' : 'outline'} horizontal-trigger" id="sideways-trigger-${i}" aria-controls="sideways-panel-${i}" aria-expanded="${i === 0}"><span class="horizontal-number">0${i + 1}</span><span class="material-symbol" aria-hidden="true">${panel.icon}</span><span class="horizontal-title">${panel.title}</span><span class="material-symbol horizontal-chevron" aria-hidden="true">chevron_right</span></button><div class="horizontal-reveal" ${i ? 'inert' : ''}><div class="horizontal-content" id="sideways-panel-${i}" role="region" aria-labelledby="sideways-trigger-${i}" ${i ? 'hidden' : ''}><div class="horizontal-content-inner"><span class="lesson-kicker">WORKSPACE / 0${i + 1}</span><div class="horizontal-card-grid">${panel.body()}</div></div></div></div></div>`).join('')}</div></div>`;
}
function card(title, icon, family, body, treatment = 'soft') {
  return `<div class="component text" data-layer="d5"><div class="component__inner text__inner ab card ${family} ${treatment}"><div class="card-body"><div class="lesson-component-title" role="heading" aria-level="7" data-layer="d5"><span class="lesson-depth">d5 · component / lesson H4</span><span class="material-symbol" aria-hidden="true">${icon}</span>${title}</div>${body}</div></div></div>`;
}
const editions = {
  guided: ['FIELD JOURNAL / 01', 'Read the landscape', 'An editorial lesson: generous reading space, marginalia and a field exercise.'],
  workshop: ['MAKER LAB / 02', 'Learn by taking it apart', 'A working bench: inspect a model, make something, then compare the result.'],
  story: ['A STORY IN THREE ACTS / 03', 'One choice changes everything', 'An immersive chapter sequence: encounter, tension, resolution.'],
  casebook: ['CONFIDENTIAL / CASE 004', 'What does the evidence say?', 'An investigation dossier: open the sources, weigh the clues, build your case.'],
  journey: ['EXPEDITION / 05', 'A small step. A new perspective.', 'A route through three checkpoints, with a new landscape beyond each one.'],
  studio: ['OPEN STUDIO / 06', 'Make room for a new idea', 'A reflective canvas: collect impressions, develop a thought, curate a response.'],
};
const actions = {
  guided: { restart: 'secondary link btn-sm', styles: ['primary outline', 'primary soft', 'positive'], labels: ['Finish reading / turn the page', 'Save observations / continue', 'Close your field journal'], icons: ['east', 'edit_note', 'check'] },
  workshop: { restart: 'secondary outline square btn-sm', styles: ['primary square btn-lg', 'info outline square', 'positive square'], labels: ['Model inspected / start building', 'Test complete / compare results', 'Finish the workshop'], icons: ['construction', 'science', 'task_alt'] },
  story: { restart: 'primary link btn-sm', styles: ['primary pill btn-lg', 'primary outline pill', 'positive pill'], labels: ['Continue to act II', 'Decision considered / reveal the ending', 'Finish this chapter'], icons: ['arrow_forward', 'auto_stories', 'done_all'] },
  casebook: { restart: 'secondary outline btn-sm', styles: ['primary outline square', 'info soft square', 'positive square btn-lg'], labels: ['File reviewed / unseal the evidence', 'Evidence reviewed / prepare a finding', 'Submit finding / close the case'], icons: ['lock_open', 'fact_check', 'gavel'] },
  journey: { restart: 'secondary soft pill btn-sm', styles: ['primary pill', 'info outline pill btn-lg', 'positive pill btn-lg'], labels: ['Leave base camp', 'Cross the bridge / next checkpoint', 'Complete the expedition'], icons: ['hiking', 'explore', 'flag'] },
  studio: { restart: 'secondary link btn-sm', styles: ['comment soft pill', 'primary outline', 'positive soft btn-lg'], labels: ['Impressions collected / open the sketchbook', 'Sketch ready / curate your ideas', 'Finish your collection'], icons: ['gesture', 'draw', 'collections_bookmark'] },
};
function scene(kind, caption) {
  return `<figure class="lesson-scene scene-${kind}"><div class="scene-art" aria-hidden="true"><span></span><span></span><span></span><span class="material-symbol">${kind === 'case' ? 'fingerprint' : kind === 'journey' ? 'terrain' : kind === 'studio' ? 'gesture' : 'filter_hdr'}</span></div><figcaption>${caption} · media component placeholder</figcaption></figure>`;
}
function frontmatter(config) {
  const aims = card('The intention', 'target', 'primary', '<ul><li>Notice a pattern.</li><li>Test an interpretation.</li><li>Make it your own.</li></ul>');
  const route = card('Your route', 'schedule', 'secondary', `<ol>${config.steps.map(title => `<li>${title}</li>`).join('')}</ol><p>15 minutes · self-paced</p>`);
  const success = card('Take away', 'check_circle', 'positive', '<p>One useful idea. One tested approach. One next step.</p>');
  if (config.id === 'story') return `<div class="lesson-story-prologue"><span class="lesson-kicker">Previously, in your learning...</span><p>${lorem}</p></div>${aims}${route}`;
  if (config.id === 'casebook') return `<div class="lesson-case-stamp">CASE 004<br><small>STATUS: OPEN</small></div>${aims}${route}`;
  if (config.id === 'journey') return `${aims}<ol class="lesson-route-map">${config.steps.map((title, i) => `<li><span>${i + 1}</span>${title}</li>`).join('')}</ol>${success}`;
  return `${aims}${route}${success}`;
}
function widget(type) {
  if (type === 'journal') return `<label class="lesson-journal">Private practice notes (not saved)<textarea rows="4" placeholder="Lorem ipsum: capture a thought, question or next step..."></textarea></label>`;
  if (type === 'visual') return `<div class="lesson-visual" role="img" aria-label="Illustrative component widget placeholder"><span class="material-symbol" aria-hidden="true">landscape</span><span>Graphic / media widget placeholder</span><span class="lesson-visual-lines" aria-hidden="true"></span></div>`;
  if (type === 'evidence') return `<div class="lesson-evidence"><p><strong>Source A</strong> · Lorem ipsum dolor sit amet.</p><p><strong>Source B</strong> · Vivamus quis sem vitae arcu.</p><p><strong>Source C</strong> · Integer non orci sed nibh.</p></div>`;
  return `<div class="lesson-widget"><span class="material-symbol" aria-hidden="true">extension</span><p>Interactive component widget placeholder</p><p class="note">An Adapt plugin would provide the activity and its completion event here.</p></div>`;
}
function content(config, step) {
  switch (config.layout) {
    case 'guided':
      if (step === 0) return `<div class="lesson-editorial"><p class="lesson-kicker">FIELD NOTE / 01</p><p class="lesson-lede">${lorem}</p><p>${lorem}</p>${scene('field', '01 / Study the landscape')}</div><aside class="lesson-marginalia"><span class="lesson-large-number">01</span><blockquote>“Look again. What did you miss the first time?”</blockquote>${card('In the margin', 'edit_note', 'warning', widget('journal'), 'tinted')}</aside>`;
      if (step === 1) return `<div class="lesson-editorial">${scene('field', '02 / Notice the detail')}<p class="lesson-lede">${lorem}</p></div><aside class="lesson-marginalia">${card('Collect three observations', 'search', 'info', widget('journal'))}</aside>`;
      return `<div class="lesson-editorial"><blockquote class="lesson-pullquote">A useful idea is one you can carry into tomorrow.</blockquote>${card('Write your field note', 'edit_note', 'primary', widget('journal'), 'tinted')}</div>`;
    case 'workshop':
      if (step === 0) return `<div class="lesson-bench-model">${scene('model', 'Reference / exploded model')}<div class="lesson-tool-strip"><span>01 / Inspect</span><span>02 / Assemble</span><span>03 / Test</span></div></div><div class="lesson-bench-instructions">${card('The brief', 'construction', 'primary', `<p>${lorem}</p><ol><li>Examine the reference.</li><li>Identify its moving parts.</li><li>Predict what happens next.</li></ol>`, 'tinted')}${card('Tools on the bench', 'handyman', 'secondary', '<p>Model viewer · ordering activity · feedback panel</p>')}</div>`;
      if (step === 1) return `<div class="lesson-workspace">${card('Assembly area', 'dashboard_customize', 'primary', widget('activity'))}</div><aside>${card('Build notes', 'edit_note', 'warning', widget('journal'))}</aside>`;
      return `<div class="lesson-comparison">${card('Reference approach', 'architecture', 'secondary', `<p>${lorem}</p>`)}${card('Your approach', 'construction', 'positive', widget('journal'), 'tinted')}</div>`;
    case 'story':
      if (step === 0) return `<div class="lesson-cinematic">${scene('story', 'Scene one / the encounter')}<div class="lesson-story-caption"><span class="lesson-kicker">ACT I / THE ENCOUNTER</span><blockquote>At the edge of the familiar, something changes.</blockquote><p>${lorem}</p></div></div>`;
      if (step === 1) return `<div class="lesson-story-decision"><span class="lesson-kicker">ACT II / THE TURNING POINT</span><p class="lesson-pullquote">Two paths. Neither tells the whole story.</p><div class="lesson-comparison">${card('Follow the familiar', 'fork_left', 'primary', `<p>${lorem.slice(0, 110)}</p>`, 'tinted')}${card('Try another perspective', 'fork_right', 'comment', `<p>${lorem.slice(0, 110)}</p>`, 'tinted')}</div><p class="note">Branching scenario component placeholder — consider both paths before continuing.</p></div>`;
      return `<div class="lesson-story-ending"><span class="lesson-kicker">ACT III / YOUR NEXT CHAPTER</span>${card('How would you end the story?', 'history_edu', 'primary', widget('journal'), 'tinted')}</div>`;
    case 'casebook':
      if (step === 0) return `<aside class="lesson-case-file"><div class="lesson-case-stamp">EXHIBIT A</div>${scene('case', 'Archive / source image')}<p class="note">Provenance unverified · examine before drawing conclusions.</p></aside><div class="lesson-case-work">${card('Incident report', 'folder_open', 'primary', `<p>${lorem}</p><dl class="lesson-case-meta"><dt>Location</dt><dd>Lorem district</dd><dt>Time</dt><dd>09:42 / day one</dd><dt>Question</dt><dd>What changed, and why?</dd></dl>`, 'tinted')}${card('First hypothesis', 'edit_note', 'comment', widget('journal'))}</div>`;
      if (step === 1) return `<div class="lesson-evidence-board">${['Witness account', 'Timeline record', 'Material trace'].map((title, i) => card(`Exhibit ${i + 1} / ${title}`, ['forum', 'schedule', 'fingerprint'][i], ['primary', 'warning', 'comment'][i], `<details class="lesson-source"><summary>Open evidence</summary><p>${lorem}</p></details>`, 'tinted')).join('')}</div>`;
      return `<div class="lesson-verdict">${card('Your finding', 'gavel', 'primary', widget('journal'), 'tinted')}${card('Check your reasoning', 'fact_check', 'positive', '<ul><li>Which source supports your claim?</li><li>What contradicts it?</li><li>What remains unknown?</li></ul>')}</div>`;
    case 'journey':
      return `<div class="lesson-milestone" aria-hidden="true">${step + 1}</div><div class="lesson-milestone-work">${step === 0 ? `${scene('journey', 'Base camp / the route ahead')}<p class="lesson-lede">${lorem}</p><div class="lesson-travel-ticket"><span class="material-symbol" aria-hidden="true">hiking</span><div><strong>Travel light</strong><p>Bring curiosity. Leave certainty behind.</p></div></div>` : step === 1 ? `<div class="lesson-checkpoint-banner"><span class="material-symbol" aria-hidden="true">explore</span><p class="lesson-pullquote">The view changes when you try.</p></div>${card('Bridge challenge', 'extension', 'info', widget('activity'))}` : `<div class="lesson-arrival"><span class="material-symbol" aria-hidden="true">flag</span><p class="lesson-pullquote">You are here. What can you see now?</p></div>${card('A postcard to your future self', 'mail', 'primary', widget('journal'), 'tinted')}`}</div>`;
    case 'studio':
      if (step === 0) return `<div class="lesson-inspiration-wall">${scene('studio', 'Colour study / 01')}<blockquote>“Start with a question, not an answer.”</blockquote>${scene('field', 'Texture study / 02')}<div class="lesson-swatch-study" aria-label="Theme colour study"><span></span><span></span><span></span><span></span></div></div><aside class="lesson-studio-prompt">${card('Capture an impression', 'gesture', 'comment', widget('journal'), 'tinted')}</aside>`;
      if (step === 1) return `<div class="lesson-sketchbook"><span class="lesson-kicker">WORK IN PROGRESS / NO PERFECT ANSWERS</span>${card('Develop your thought', 'draw', 'primary', widget('journal'))}<p>${lorem}</p></div><aside>${card('Change the lens', 'lightbulb', 'warning', '<ul><li>What if the opposite were true?</li><li>What would you remove?</li><li>What would you keep?</li></ul>')}</aside>`;
      return `<div class="lesson-gallery">${card('01 / Keep', 'bookmark', 'primary', widget('journal'), 'tinted')}${card('02 / Rework', 'edit', 'comment', widget('journal'), 'tinted')}${card('03 / Try next', 'arrow_forward', 'positive', widget('journal'), 'tinted')}</div>`;
    default: throw new Error('Unknown lesson experiment layout');
  }
}
export function lessonExperiment(id) {
  const config = LESSON_EXPERIMENTS.find(item => item.id === id);
  if (!config) throw new Error(`Unknown lesson experiment: ${id}`);
  return `<div class="lesson-experiment lesson-${id} page contentobject" data-lesson="${id}" data-layer="d2">
  <div class="page__inner">
    <nav class="lesson-menu" aria-label="${config.title} article menu"><span class="material-symbol" aria-hidden="true">${config.icon}</span><span>Lesson menu</span><a class="ab btn primary link btn-sm" href="#lessons-demo-lesson-${id}-article">Learning article</a><button type="button" class="ab btn ${actions[id].restart}" data-lesson-reset><span class="material-symbol" aria-hidden="true">restart_alt</span>Restart lesson</button></nav>
    <header class="page__header"><span class="lesson-kicker">${editions[id][0]}</span><h4 class="page__title" data-layer="d2"><span class="lesson-depth">d2 · page title / lesson H1 · workbench H4</span>${editions[id][1]}</h4><p class="lesson-intro">${editions[id][2]}</p><span class="lesson-hero-symbol material-symbol" aria-hidden="true">${config.icon}</span></header>
    <details class="lesson-frontmatter" open><summary><span class="material-symbol" aria-hidden="true">info</span>Before you begin · lesson frontmatter</summary><div class="lesson-frontmatter-grid">
      ${frontmatter(config)}
    </div></details>
    <div class="article__container"><article class="article" id="lesson-${id}-article" data-layer="d3"><div class="article__inner">
      <header class="article__header"><h5 class="article__title"><span class="lesson-depth">d3 · article / lesson H2 · workbench H5</span>${config.title}</h5></header>
      <div class="block__container">${config.steps.map((title, i) => `<details class="block lesson-block" data-layer="d4" data-lesson-step="${i}" ${i === 0 ? 'open' : 'hidden'}><summary><h6 class="block__title"><span class="lesson-depth">d4 · block / lesson H3 · workbench H6</span><span class="material-symbol" aria-hidden="true">${['explore', 'science', 'verified'][i]}</span>${i + 1}. ${title}</h6><span class="lesson-block-state">${i === 0 ? 'Ready' : 'Next stage'}</span></summary><div class="block__inner">
      <div class="component__container lesson-composition">${content(config, i)}</div>
      <div class="lesson-completion"><button type="button" class="ab btn ${actions[id].styles[i]}" data-lesson-complete><span class="material-symbol" aria-hidden="true">${actions[id].icons[i]}</span>${actions[id].labels[i]}</button><span class="lesson-complete-label"></span></div>
      </div></details>`).join('')}</div>
    </div></article></div>
    <footer class="lesson-footer"><progress max="3" value="0" aria-label="${config.title} completed stages"></progress><p class="lesson-status" role="status">0 of 3 stages completed. Lesson aims and stage 1 are open.</p><p class="note">Layout prototype · simulated completion, not Adapt tracking. Notes are not saved.</p></footer>
  </div></div>`;
}
