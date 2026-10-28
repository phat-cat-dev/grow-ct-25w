(function (global) {
  'use strict';
  function mount(host) {
    if (!(host instanceof HTMLElement) || host.hasAttribute('data-flow-mounted')) throw new Error('Use an unmounted flow card.');
    const svg = host.querySelector('.flow-diagram');
    if (!svg) throw new Error('The flow card needs an inline diagram.');
    const controller = new AbortController();
    const ns = 'http://www.w3.org/2000/svg';
    const initialMarkup = svg.innerHTML;
    const initialLabel = svg.getAttribute('aria-label');
    const initialCount = svg.querySelectorAll('.node').length;
    const initialStyle = svg.getAttribute('style');
    const shape = host.dataset.flowShape;
    const route = svg.querySelector('.runner').style.offsetPath;
    const routeMatch = route.match(/^path\(["'](.+)["']\)$/);
    if (!routeMatch) throw new Error('The diagram needs a supported SVG runner path.');
    const geometry = document.createElementNS(ns, 'path');
    geometry.setAttribute('d', routeMatch[1]);
    const corners = [];
    let totalLength = 0;
    svg.querySelectorAll('.edge').forEach(edge => {
      totalLength += edge.getTotalLength();
      const end = edge.getPointAtLength(edge.getTotalLength());
      corners.push({ distance: totalLength, x: end.x, y: end.y });
    });
    const closed = !['horizontal', 'vertical'].includes(shape);
    let downloadURL;
    const download = host.querySelector('[data-flow-download]');
    const status = host.querySelector('[data-flow-status]');
    function make(tag, attributes) {
      const element = document.createElementNS(ns, tag);
      Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, String(value)));
      return element;
    }
    function setNodeCount(count) {
      if (!Number.isInteger(count) || count < 2 || count > 12) throw new RangeError('Choose a whole number of nodes from 2 to 12.');
      const playing = svg.classList.contains('is-playing');
      const paused = svg.classList.contains('is-paused');
      svg.classList.remove('is-playing', 'is-paused');
      svg.append(geometry);
      const length = geometry.getTotalLength();
      const gap = length / (closed ? count : count - 1);
      const positions = Array.from({ length: count }, (_, i) => geometry.getPointAtLength(i * gap));
      geometry.remove();
      const minGap = Math.min(...positions.slice(1).map((point, i) => Math.hypot(point.x - positions[i].x, point.y - positions[i].y)));
      const radius = Math.min(20, minGap * .34);
      const fragment = document.createDocumentFragment();
      for (let i = 0; i < (closed ? count : count - 1); i++) {
        const start = positions[i], end = positions[(i + 1) % count];
        let d = `M${start.x} ${start.y}`;
        if (shape === 'circle') {
          d += ` A80 80 0 ${gap > length / 2 ? 1 : 0} 1 ${end.x} ${end.y}`;
        } else {
          corners.filter(corner => corner.distance > i * gap + .01 && corner.distance < (i + 1) * gap - .01)
            .forEach(corner => { d += ` L${corner.x} ${corner.y}`; });
          d += ` L${end.x} ${end.y}`;
        }
        fragment.append(make('path', { class: 'edge', pathLength: 1, d, style: `--d:${i * .12}s` }));
      }
      positions.forEach((point, i) => {
        fragment.append(make('circle', { class: `node${i === 0 ? ' key' : ''}`, cx: point.x, cy: point.y, r: radius }));
        const label = make('text', { class: 'nlabel', x: point.x, y: point.y, style: `font-size:${Math.min(13, radius * .85)}px` });
        label.textContent = String(i + 1);
        fragment.append(label);
      });
      const runner = make('circle', { class: 'runner', r: 5, style: `offset-path:${route}` });
      if (host.querySelector('[data-flow-layer]').value === 'behind') fragment.prepend(runner);
      else fragment.append(runner);
      svg.replaceChildren(fragment);
      svg.setAttribute('aria-label', `${count}-node ${shape} ${closed ? 'loop' : 'sequence'}`);
      host.querySelector('[data-flow-nodes]').value = String(count);
      if (playing) {
        void svg.getBoundingClientRect();
        svg.classList.add('is-playing');
      }
      if (paused) svg.classList.add('is-paused');
      if (status) status.textContent = `${count} nodes. ${closed ? 'Loop' : 'Sequence'} updated.`;
    }
    function prepareDownload() {
      const copy = svg.cloneNode(true);
      copy.classList.remove('is-playing', 'is-paused');
      copy.querySelector('.runner').remove();
      const styles = getComputedStyle(svg);
      copy.style.setProperty('--flow-accent', styles.getPropertyValue('--flow-accent'));
      copy.style.setProperty('--flow-paper', styles.getPropertyValue('--flow-paper'));
      copy.style.setProperty('--flow-ink', styles.getPropertyValue('--flow-ink'));
      const embedded = make('style', {});
      embedded.textContent = '.edge{fill:none;stroke:var(--flow-accent);stroke-width:4;stroke-linecap:round;opacity:.5}.node{fill:var(--flow-paper);stroke:var(--flow-accent);stroke-width:2.5}.node.key{fill:color-mix(in srgb,var(--flow-accent) 16%,var(--flow-paper))}.nlabel{fill:var(--flow-ink);font:700 13px system-ui,sans-serif;text-anchor:middle;dominant-baseline:central}';
      copy.prepend(embedded);
      if (downloadURL) URL.revokeObjectURL(downloadURL);
      downloadURL = URL.createObjectURL(new Blob([new XMLSerializer().serializeToString(copy)], { type: 'image/svg+xml' }));
      download.href = downloadURL;
    }
    host.setAttribute('data-flow-mounted', '');
    function play() {
      svg.classList.remove('is-playing', 'is-paused');
      void svg.getBoundingClientRect();
      svg.classList.add('is-playing');
      host.querySelector('[data-flow-pause]').setAttribute('aria-pressed', 'false');
    }
    host.addEventListener('click', event => {
      if (event.target.closest('[data-flow-download]')) prepareDownload();
      if (event.target.closest('[data-flow-play]')) play();
      if (event.target.closest('[data-flow-pause]')) {
        const paused = svg.classList.toggle('is-paused');
        host.querySelector('[data-flow-pause]').setAttribute('aria-pressed', String(paused));
      }
    }, { signal: controller.signal });
    host.addEventListener('change', event => {
      if (event.target.matches('[data-flow-nodes]')) setNodeCount(Number(event.target.value));
      if (event.target.matches('[data-flow-rate]')) svg.style.setProperty('--flow-rate', event.target.value);
      if (event.target.matches('[data-flow-layer]')) {
        const runner = svg.querySelector('.runner');
        if (event.target.value === 'behind') svg.prepend(runner);
        else svg.append(runner);
      }
    }, { signal: controller.signal });
    return {
      play,
      setNodeCount,
      destroy() {
        controller.abort();
        if (downloadURL) URL.revokeObjectURL(downloadURL);
        svg.classList.remove('is-playing', 'is-paused');
        svg.innerHTML = initialMarkup;
        svg.setAttribute('aria-label', initialLabel);
        if (initialStyle === null) svg.removeAttribute('style');
        else svg.setAttribute('style', initialStyle);
        host.querySelector('[data-flow-nodes]').value = String(initialCount);
        host.querySelector('[data-flow-rate]').value = '1';
        host.querySelector('[data-flow-layer]').value = 'over';
        host.querySelector('[data-flow-pause]').setAttribute('aria-pressed', 'false');
        if (status) status.textContent = '';
        if (download) download.setAttribute('href', download.getAttribute('download'));
        host.removeAttribute('data-flow-mounted');
      },
    };
  }
  global.FlowDiagrams = { mount };
  document.querySelectorAll('[data-flow-card]:not([data-flow-mounted])').forEach(mount);
})(window);
