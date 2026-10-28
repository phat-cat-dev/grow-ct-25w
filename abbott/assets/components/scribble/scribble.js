(function (global) {
  'use strict';
  const paths = {
    box: ['M8 10 172 7 175 124 6 127 8 10', 'M18 112 150 18 M44 120 166 32 M70 126 172 54 M96 128 176 78'],
    zigzag: ['M14 103 34 25 44 108 65 17 76 114 94 23 109 108 124 17 138 109 157 29 170 100'],
    loops: ['M12 92 C55 15 59 127 32 96 S32 14 69 55 109 132 85 102 79 3 123 51 172 135 148 101 140 32 170 50'],
    underline: ['M12 90 Q50 75 86 86 T169 82', 'M20 105 Q70 94 160 98'],
    circle: ['M163 42 C124 5 38 11 17 55 S39 126 100 118 181 63 155 32 63 4 30 42'],
    arrow: ['M15 107 C46 112 56 26 99 34 S131 82 167 29', 'M142 31 168 27 170 52'],
    crosshatch: ['M15 25 164 108 M18 60 133 120 M50 13 172 80', 'M18 105 132 16 M50 119 165 30 M18 72 92 14'],
    spiral: ['M18 92 C-2 9 167 0 168 72 S25 143 28 68 153 27 143 76 51 110 53 65 119 42 119 71 80 88 79 67 101 58 104 70'],
  };
  function mountScribble(host) {
    if (!(host instanceof HTMLElement) || host.hasAttribute('data-scribble-mounted')) throw new Error('Use an unmounted scribble host.');
    const controller = new AbortController();
    let state = { mark: 'box', speed: 1, size: 1, angle: 0 };
    host.classList.add('scribble-tool');
    host.setAttribute('data-scribble-mounted', '');
    host.innerHTML = `
      <div class="scribble-tool__controls" role="group" aria-label="Scribble controls">
        <label>Mark<select data-scribble-setting="mark">${Object.keys(paths).map(name => `<option value="${name}">${name}</option>`).join('')}</select></label>
        <label>Drawing speed<output data-scribble-value="speed"></output><input type="range" data-scribble-setting="speed" min=".25" max="3" step=".05" value="1"></label>
        <label>Size<output data-scribble-value="size"></output><input type="range" data-scribble-setting="size" min=".5" max="1.5" step=".05" value="1"></label>
        <label>Angle<output data-scribble-value="angle"></output><input type="range" data-scribble-setting="angle" min="-45" max="45" step="1" value="0"></label>
        <button type="button" data-scribble-replay>Replay scribble</button>
      </div>
      <div class="scribble-tool__stage">
        <div class="scribble-tool__example">Your text or shape stays selectable underneath.</div>
        <div class="scribble-tool__overlay"><svg class="scribble" viewBox="0 0 180 132" aria-hidden="true"></svg></div>
      </div>
      <output class="scribble-tool__settings" aria-label="Reusable scribble CSS tokens"></output>
    `;
    const svg = host.querySelector('svg');
    function validate(value) {
      if (!value || !Object.hasOwn(paths, value.mark) ||
          ![['speed', .25, 3], ['size', .5, 1.5], ['angle', -45, 45]].every(([key, min, max]) =>
            typeof value[key] === 'number' && Number.isFinite(value[key]) && value[key] >= min && value[key] <= max)) {
        throw new Error('Scribble needs a known mark, speed .25-3, size .5-1.5 and angle -45 to 45.');
      }
      return { mark: value.mark, speed: value.speed, size: value.size, angle: value.angle };
    }
    function render() {
      svg.classList.remove('is-playing');
      svg.style.setProperty('--scribble-duration', `${1.6 / state.speed}s`);
      svg.style.setProperty('--scribble-size', state.size);
      svg.style.setProperty('--scribble-angle', `${state.angle}deg`);
      svg.replaceChildren();
      paths[state.mark].forEach((data, index) => {
        const path = document.createElementNS(svg.namespaceURI, 'path');
        path.setAttribute('d', data);
        path.setAttribute('pathLength', '1');
        path.style.setProperty('--scribble-delay', `${index * .25 / state.speed}s`);
        svg.append(path);
      });
      for (const [key, value] of Object.entries(state)) {
        const input = host.querySelector(`[data-scribble-setting="${key}"]`);
        input.value = value;
        if (key !== 'mark') {
          const text = `${Number(value.toFixed(2))}${key === 'angle' ? ' deg' : 'x'}`;
          input.setAttribute('aria-valuetext', text);
          host.querySelector(`[data-scribble-value="${key}"]`).textContent = text;
        }
      }
      host.querySelector('.scribble-tool__settings').textContent = `--scribble-duration: ${(1.6 / state.speed).toFixed(3)}s; --scribble-size: ${state.size}; --scribble-angle: ${state.angle}deg;`;
    }
    function replay() {
      svg.classList.remove('is-playing');
      void svg.getBoundingClientRect();
      svg.classList.add('is-playing');
    }
    function update(event) {
      const input = event.target;
      const key = input.dataset.scribbleSetting;
      if (!key) return;
      state = validate({ ...state, [key]: key === 'mark' ? input.value : input.valueAsNumber });
      render();
      host.dispatchEvent(new CustomEvent('scribble:change', { bubbles: true, detail: { ...state } }));
    }
    host.addEventListener('input', event => {
      if (event.target.type === 'range') update(event);
    }, { signal: controller.signal });
    host.addEventListener('change', event => {
      if (event.target.tagName === 'SELECT') update(event);
    }, { signal: controller.signal });
    host.querySelector('[data-scribble-replay]').addEventListener('click', replay, { signal: controller.signal });
    render();
    return {
      get: () => ({ ...state }),
      load(value) { state = validate(value); render(); },
      replay,
      svg: () => svg.outerHTML,
      destroy() { controller.abort(); host.replaceChildren(); host.classList.remove('scribble-tool'); host.removeAttribute('data-scribble-mounted'); },
    };
  }
  global.Scribble = { mountScribble };
})(window);
