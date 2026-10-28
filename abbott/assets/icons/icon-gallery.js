(function () {
  'use strict';
  const host = document.querySelector('.icon-library');
  if (!host) return;
  const packs = [...host.querySelectorAll('[data-icon-pack]')];
  const cells = [...host.querySelectorAll('[data-icon]')];
  const input = host.querySelector('[data-icon-search]');
  const markup = host.querySelector('[data-icon-markup]');
  const copy = host.querySelector('[data-icon-copy]');
  const status = host.querySelector('[data-copy-status]');
  let selected = null;
  let animations = [];
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  function stopEntrance() {
    animations.forEach(animation => animation.cancel());
    animations = [];
  }
  function replayEntrance() {
    stopEntrance();
    const effect = host.querySelector('[data-icon-effect]').value;
    if (effect === 'none' || motion.matches || host.closest('.no-motion, [data-tm-no-motion="true"]')) return;
    const start = { opacity: 0 };
    const end = { opacity: 1 };
    if (effect === 'rise') { start.translate = '0 12px'; end.translate = '0 0'; }
    if (effect === 'pop') { start.scale = .85; end.scale = 1; }
    const duration = host.querySelector('[data-icon-duration]').valueAsNumber;
    const stagger = host.querySelector('[data-icon-stagger]').valueAsNumber;
    animations = cells.filter(cell => !cell.hidden).map((cell, index) =>
      cell.animate([start, end], { duration, delay: index * stagger, easing: 'ease-out', fill: 'backwards' }));
  }
  motion.addEventListener('change', stopEntrance);
  host.addEventListener('focusin', event => { if (event.target.closest('.iconcell')) stopEntrance(); });
  async function copyMarkup() {
    if (!selected) return;
    try {
      if (!navigator.clipboard?.writeText) throw new Error('Clipboard is unavailable in this browser context.');
      await navigator.clipboard.writeText(markup.value);
      status.textContent = `${selected.dataset.icon} SVG markup copied. No sprite or external font is needed.`;
    } catch (error) {
      status.textContent = `Could not copy automatically: ${error.message} Select and copy the markup below manually, or download the SVG.`;
      markup.focus({ preventScroll: true });
      markup.select();
    }
  }
  cells.forEach(cell => cell.addEventListener('click', () => {
    selected = cell;
    cells.forEach(item => item.setAttribute('aria-pressed', String(item === cell)));
    const svg = cell.querySelector('svg').cloneNode(true);
    svg.removeAttribute('aria-hidden');
    svg.setAttribute('role', 'img');
    const name = cell.dataset.icon.replace(/^ic-/, '').replaceAll('-', ' ');
    svg.setAttribute('aria-label', name);
    markup.value = new XMLSerializer().serializeToString(svg);
    host.querySelector('[data-selected-name]').textContent = `${name} / #${cell.dataset.icon}`;
    host.querySelector('[data-selected-preview]').replaceChildren(svg);
    const download = host.querySelector('[data-icon-download]');
    download.href = `${cell.dataset.icon}.svg`;
    download.hidden = false;
    copy.disabled = false;
    copyMarkup();
  }));
  copy.addEventListener('click', copyMarkup);
  function filter() {
    stopEntrance();
    const query = input.value.trim().toLowerCase().replace(/^#/, '').replaceAll(/[\s_]+/g, '-');
    let total = 0;
    packs.forEach(pack => {
      const items = [...pack.querySelectorAll('[data-icon]')];
      const count = items.reduce((sum, cell) => {
        cell.hidden = !cell.dataset.icon.includes(query);
        return sum + Number(!cell.hidden);
      }, 0);
      total += count;
      const badge = pack.querySelector('[data-pack-count]');
      badge.textContent = query ? `${count} / ${items.length}` : String(items.length);
      badge.setAttribute('aria-label', `${count} of ${items.length} icons shown`);
      pack.querySelector('.pack-empty').hidden = count !== 0;
    });
    host.querySelector('[data-search-status]').textContent = `${total} of ${cells.length} icons shown${total === 0 ? '. No matching local icons.' : '.'}`;
  }
  input.addEventListener('input', filter);
  const size = host.querySelector('[data-icon-size]');
  size.addEventListener('input', () => {
    host.style.setProperty('--icon-size', `${size.value}px`);
    host.querySelector('[data-icon-size-value]').value = `${size.value} px`;
    size.setAttribute('aria-valuetext', `${size.value} pixels`);
  });
  host.querySelector('[data-icon-circle]').addEventListener('change', event => {
    host.style.setProperty('--icon-frame-radius', event.target.checked ? '999px' : '8px');
  });
  const border = host.querySelector('[data-icon-border]');
  border.addEventListener('input', () => {
    host.style.setProperty('--icon-border-width', `${border.value}px`);
    host.querySelector('[data-icon-border-value]').value = `${border.value} px`;
    border.setAttribute('aria-valuetext', `${border.value} pixels`);
  });
  host.querySelector('[data-icon-border-style]').addEventListener('change', event => {
    host.style.setProperty('--icon-border-style', event.target.value);
  });
  for (const key of ['duration', 'stagger']) {
    const input = host.querySelector(`[data-icon-${key}]`);
    input.addEventListener('input', () => {
      host.querySelector(`[data-icon-${key}-value]`).value = `${input.value} ms`;
      input.setAttribute('aria-valuetext', `${input.value} milliseconds`);
    });
  }
  host.querySelector('[data-icon-effect]').addEventListener('change', replayEntrance);
  host.querySelector('[data-icon-replay]').addEventListener('click', replayEntrance);
  filter();
})();
