export const TYPOGRAPHY_BULLETS = {
  none: '', chevron: '›', dot: '•', arrow: '→', circle: '○', square: '▪',
  diamond: '◆', star: '★', check: '✓', plus: '+', dash: '–', doublechevron: '»',
};
export const ACADEMIC_BULLETS = {
  'academic-learning': { label: 'Learning', path: 'm422-232 207-248H469l29-227-185 267h139l-30 208ZM320-80l40-280H160l360-520h80l-40 320h240L400-80h-80Z' },
  'academic-studying': { label: 'Studying', path: 'M480-60q-72-68-165-104t-195-36v-440q101 0 194 36.5T480-498q73-69 166-105.5T840-640v440q-103 0-195.5 36T480-60Zm0-104q63-47 134-75t146-37v-276q-73 13-143.5 52.5T480-394q-66-66-136.5-105.5T200-552v276q75 9 146 37t134 75Zm0-436q-66 0-113-47t-47-113q0-66 47-113t113-47q66 0 113 47t47 113q0 66-47 113t-113 47Zm0-80q33 0 56.5-23.5T560-760q0-33-23.5-56.5T480-840q-33 0-56.5 23.5T400-760q0 33 23.5 56.5T480-680Z' },
  'academic-referencing': { label: 'Referencing', path: 'M320-320h480v-480h-80v280l-100-60-100 60v-280H320v480Zm0 80q-33 0-56.5-23.5T240-320v-480q0-33 23.5-56.5T320-880h480q33 0 56.5 23.5T880-800v480q0 33-23.5 56.5T800-240H320ZM160-80q-33 0-56.5-23.5T80-160v-560h80v560h560v80H160Z' },
  'academic-presenting': { label: 'Presenting', path: 'M840-120v-640H120v320H40v-320q0-33 23.5-56.5T120-840h720q33 0 56.5 23.5T920-760v560q0 33-23.5 56.5T840-120ZM360-400q-66 0-113-47t-47-113q0-66 47-113t113-47q66 0 113 47t47 113q0 66-47 113t-113 47Zm0-80q33 0 56.5-23.5T440-560q0-33-23.5-56.5T360-640q-33 0-56.5 23.5T280-560q0 33 23.5 56.5T360-480ZM40-80v-112q0-34 17.5-62.5T104-298q62-31 126-46.5T360-360q66 0 130 15.5T616-298q29 15 46.5 43.5T680-192v112H40Zm80-80h480v-32q0-11-5.5-20T580-226q-54-27-109-40.5T360-280q-56 0-111 13.5T140-226q-9 5-14.5 14t-5.5 20v32Z' },
  'academic-progressing': { label: 'Progressing', path: 'M80-200v-80h240v-240h240v-240h320v80H640v240H400v240H80Z' },
  'academic-writing': { label: 'Writing', path: 'M280-280h280v-80H280v80Zm0-160h400v-80H280v80Zm0-160h400v-80H280v80Zm-80 480q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm0-80h560v-560H200v560Z' },
  'academic-reflecting': { label: 'Reflecting', path: 'M314-115q-104-48-169-145T80-479q0-26 2.5-51t8.5-49l-46 27-40-69 191-110 110 190-70 40-54-94q-11 27-16.5 56t-5.5 60q0 97 53 176.5T354-185l-40 70Zm306-485v-80h109q-46-57-111-88.5T480-800q-55 0-104 17t-90 48l-40-70q50-35 109-55t125-20q79 0 151 29.5T760-765v-55h80v220H620ZM594 0 403-110l110-190 69 40-57 98q118-17 196.5-107T800-480q0-11-.5-20.5T797-520h81q1 10 1.5 19.5t.5 20.5q0 135-80.5 241.5T590-95l44 26-40 69Z' },
  'academic-criticality': { label: 'Criticality', path: 'M480-80q-33 0-56.5-23.5T400-160h160q0 33-23.5 56.5T480-80ZM320-200v-80h320v80H320Zm10-120q-69-41-109.5-110T180-580q0-125 87.5-212.5T480-880q125 0 212.5 87.5T780-580q0 81-40.5 150T630-320H330Zm24-80h252q45-32 69.5-79T700-580q0-92-64-156t-156-64q-92 0-156 64t-64 156q0 54 24.5 101t69.5 79Z' },
  'academic-starting': { label: 'Starting', path: 'm226-559 78 33q14-28 29-54t33-52l-56-11-84 84Zm142 83 114 113q42-16 90-49t90-75q70-70 109.5-155.5T806-800q-72-5-158 34.5T492-656q-42 42-75 90t-49 90Zm178-65q-23-23-23-56.5t23-56.5q23-23 57-23t57 23q23 23 23 56.5T660-541q-23 23-57 23t-57-23Zm19 321 84-84-11-56q-26 18-52 32.5T532-299l33 79Zm313-653q19 121-23.5 235.5T708-419l20 99q4 20-2 39t-20 33L538-80l-84-197-171-171-197-84 167-168q14-14 33.5-20t39.5-2l99 20q104-104 218-147t235-24ZM157-321q35-35 85.5-35.5T328-322q35 35 34.5 85.5T327-151q-25 25-83.5 43T82-76q14-103 32-161.5t43-83.5Z' },
  'academic-assessment': { label: 'Assessment', path: 'M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-80q-100 0-170-70t-70-170q0-100 70-170t170-70q100 0 170 70t70 170q0 100-70 170t-170 70Zm0-80q66 0 113-47t47-113q0-66-47-113t-113-47q-66 0-113 47t-47 113q0 66 47 113t113 47Zm0-80q-33 0-56.5-23.5T400-480q0-33 23.5-56.5T480-560q33 0 56.5 23.5T560-480q0 33-23.5 56.5T480-400Z' },
  'academic-feedback': { label: 'Feedback', path: 'M480-360q17 0 28.5-11.5T520-400q0-17-11.5-28.5T480-440q-17 0-28.5 11.5T440-400q0 17 11.5 28.5T480-360Zm-40-160h80v-240h-80v240ZM80-80v-720q0-33 23.5-56.5T160-880h640q33 0 56.5 23.5T880-800v480q0 33-23.5 56.5T800-240H240L80-80Zm126-240h594v-480H160v525l46-45Z' },
  'academic-researching': { label: 'Researching', path: 'M450-420q38 0 64-26t26-64q0-38-26-64t-64-26q-38 0-64 26t-26 64q0 38 26 64t64 26Zm193 160L538-365q-20 13-42.5 19t-45.5 6q-71 0-120.5-49.5T280-510q0-71 49.5-120.5T450-680q71 0 120.5 49.5T620-510q0 23-6.5 45.5T594-422l106 106-57 56ZM200-120q-33 0-56.5-23.5T120-200v-160h80v160h160v80H200Zm400 0v-80h160v-160h80v160q0 33-23.5 56.5T760-120H600ZM120-600v-160q0-33 23.5-56.5T200-840h160v80H200v160h-80Zm640 0v-160H600v-80h160q33 0 56.5 23.5T840-760v160h-80Z' },
};
export const TYPOGRAPHY_RATIOS = {
  'minor-second': 16 / 15, 'major-second': 9 / 8, 'minor-third': 6 / 5,
  'major-third': 5 / 4, 'perfect-fourth': 4 / 3, 'augmented-fourth': Math.SQRT2,
};
export const HEADING_HARMONIES = {
  analogous: [0, 15, 30, -15, -30, 45],
  complementary: [0, 0, 0, 180, 180, 180],
  triadic: [0, 120, 240, 0, 120, 240],
  split: [0, 150, 210, 0, 150, 210],
  square: [0, 90, 180, 270, 0, 90],
  spectrum: [0, 60, 120, 180, 240, 300],
  'golden-angle': Array.from({ length: 6 }, (_, i) => Math.round((i * 180 * (3 - Math.sqrt(5)) % 360) * 1000) / 1000),
};
export function headingSizes(size) {
  if (size === 'graded') return [2, 1.5, 1.18, 1, .875, .75];
  if (size === 'uniform') return Array(6).fill(1.15);
  if (!Object.hasOwn(TYPOGRAPHY_RATIOS, size)) throw new Error('Invalid heading size formula.');
  return Array.from({ length: 6 }, (_, i) => .875 * TYPOGRAPHY_RATIOS[size] ** (5 - i));
}
export const DEFAULT_TYPOGRAPHY = {
  scheme: 'diagonal', decoration: 'none', bullet: 'none', size: 'graded',
  reverse: false, scale: 1, applied: false, bodySize: 16, lineHeight: 1.55, readingWidth: 70,
  underlineWidth: .06, borderWidth: .18, iconSize: .72,
  caps: [false, false, false, false, false, true],
};
export function validateTypography(value = DEFAULT_TYPOGRAPHY) {
  const state = { ...DEFAULT_TYPOGRAPHY, ...value };
  const within = (n, min, max) => typeof n === 'number' && Number.isFinite(n) && n >= min && n <= max;
  if (!(['diagonal', 'grey', 'gray', 'mono', 'twotone', 'accent', 'muted'].includes(state.scheme) || Object.hasOwn(HEADING_HARMONIES, state.scheme)) ||
      !['none', 'underline', 'dashed', 'dotted', 'leftborder'].includes(state.decoration) ||
      !(Object.hasOwn(TYPOGRAPHY_BULLETS, state.bullet) || Object.hasOwn(ACADEMIC_BULLETS, state.bullet)) ||
      !(['graded', 'uniform'].includes(state.size) || Object.hasOwn(TYPOGRAPHY_RATIOS, state.size)) || typeof state.reverse !== 'boolean' || typeof state.applied !== 'boolean' ||
      !within(state.scale, .8, 1.8) || !within(state.bodySize, 12, 24) ||
      !within(state.lineHeight, 1.2, 2.2) || !within(state.readingWidth, 40, 100) ||
      !within(state.underlineWidth, .01, .3) || !within(state.borderWidth, .01, .5) ||
      !within(state.iconSize, .3, 2) ||
      !Array.isArray(state.caps) || state.caps.length !== 6 ||
      !Array.from(state.caps).every(value => typeof value === 'boolean')) {
    throw new Error('Invalid typography settings. Check heading choices and body text limits.');
  }
  return { ...state, caps: [...state.caps] };
}
export function typographyCss(value, scope) {
  const state = validateTypography(value);
  const target = scope || (state.applied ? ':root' : null);
  const brand = 'var(--brand-s, var(--s, 72%))';
  const grey = 'var(--grey-s, var(--gs, 12%))';
  const saturations = {
    diagonal: [brand, '45%', '28%', grey, grey, grey], grey: Array(6).fill(grey),
    gray: Array(6).fill('0%'), mono: Array(6).fill(brand),
    twotone: [brand, brand, '40%', '40%', grey, grey], accent: [brand, grey, grey, grey, grey, grey],
    muted: Array(6).fill(`calc(${brand} * .45)`),
  }[state.scheme] ?? Array(6).fill(brand);
  const harmony = HEADING_HARMONIES[state.scheme];
  let css = '/* Typography follows the active main colour ingredients. */\n';
  if (target) {
    const light = [40, 24, 36, 52, 60, 68];
    const dark = [68, 74, 70, 62, 54, 48];
    const sizes = headingSizes(state.size);
    const bullets = TYPOGRAPHY_BULLETS;
    const icon = ACADEMIC_BULLETS[state.bullet];
    const mask = icon ? `url("data:image/svg+xml,${encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960"><path d="${icon.path}"/></svg>`)}") center / contain no-repeat` : 'none';
    const decorations = { none: 'none', underline: 'underline solid', dashed: 'underline dashed', dotted: 'underline dotted', leftborder: 'none' };
    for (let i = 0; i < 6; i++) {
      const n = state.reverse ? 5 - i : i;
      const hue = harmony ? `calc(var(--brand-h, var(--h, 202)) + ${harmony[n]})` : `var(--theme-heading-h-${i + 1}, var(--brand-h, var(--h, 202)))`;
      const heading = `${target} h${i + 1}:not(.sec):not(.card-title):not(.accordion-header)`;
      const maximum = sizes[i] * state.scale;
      const minimum = maximum * (Object.hasOwn(TYPOGRAPHY_RATIOS, state.size) ? .85 : i < 3 ? .75 : .9);
      const fluid = `clamp(${minimum.toFixed(4)}rem, calc(${(minimum - (maximum - minimum) / 3).toFixed(4)}rem + ${((maximum - minimum) * 100 / 60).toFixed(4)}vw), ${maximum.toFixed(4)}rem)`;
      css += `${heading} {
  font-family: var(--font-heading, inherit);
  color: hsl(${hue} ${saturations[i]} var(--type-l-${i + 1}));
  font-size: ${fluid};
  line-height: 1.2;
  text-transform: ${state.caps[i] ? 'uppercase' : 'none'};
  display: ${state.bullet === 'none' ? 'block' : 'flex'};
  align-items: center;
  justify-content: flex-start;
  text-align: left;
  margin-inline: 0;
  overflow-wrap: anywhere;
  text-decoration: ${decorations[state.decoration]};
  text-decoration-thickness: ${state.underlineWidth}em;
  text-underline-offset: .2em;
  border-left: ${state.decoration === 'leftborder' ? `${state.borderWidth}rem solid currentColor` : '0'};
  padding-left: ${state.decoration === 'leftborder' ? '.5rem' : '0'};
}
${heading}::before { content: "${icon ? '' : bullets[state.bullet]}"; display: ${state.bullet === 'none' ? 'none' : 'inline-block'}; flex: none; margin-right: .4em; width: ${icon ? state.iconSize + 'em' : 'auto'}; height: ${icon ? state.iconSize + 'em' : 'auto'}; background: ${icon ? 'currentColor' : 'none'}; mask: ${mask}; -webkit-mask: ${mask}; }
`;
      css += `${target} { --type-l-${i + 1}: ${light[n]}%; }\n`;
      css += `@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) ${target === ':root' ? '' : target} { --type-l-${i + 1}: ${dark[n]}%; } }\n`;
      css += `:root[data-theme="dark"]${target === ':root' ? '' : ' ' + target} { --type-l-${i + 1}: ${dark[n]}%; }\n`;
    }
  }
  const maximum = state.bodySize / 16;
  const minimum = Math.max(.75, maximum * .875);
  css += `body { font-size: clamp(${minimum}rem, calc(${(minimum - (maximum - minimum) / 3).toFixed(4)}rem + ${((maximum - minimum) * 100 / 60).toFixed(4)}vw), ${maximum}rem); line-height: ${state.lineHeight}; }\n`;
  css += `:root p { max-inline-size: ${state.readingWidth}ch; }\n`;
  return css;
}
