(function () {
  'use strict';
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-chalk-pattern-library]').forEach(library => {
    const styles = library.querySelector('[data-pattern-animation]').textContent;
    const demos = [...library.querySelectorAll('[data-edu-demo]')];
    const master = library.querySelector('[data-edu-speed]');
    function markup(demo) {
      const drawing = demo.querySelector('.edu-drawing');
      const svg = drawing.querySelector('svg').cloneNode(true);
      svg.classList.add('edu-running');
      if (!demo.querySelector('[data-edu-arrows]').checked) svg.classList.add('edu-no-arrows');
      svg.style.setProperty('--edu-speed', master.value);
      svg.style.setProperty('--edu-local-speed', demo.querySelector('[data-pattern-speed]').value);
      svg.style.setProperty('--edu-iterations', demo.querySelector('[data-edu-loop]').checked ? 'infinite' : '1');
      const style = document.createElementNS('http://www.w3.org/2000/svg', 'style');
      style.textContent = styles;
      svg.prepend(style);
      return new XMLSerializer().serializeToString(svg);
    }
    function updateCode(demo) { demo.querySelector('.edu-code').value = markup(demo); }
    function report(demo, text) { demo.querySelector('.edu-status').textContent = text; }
    function play(demo) {
      const drawing = demo.querySelector('.edu-drawing');
      drawing.classList.remove('edu-running', 'edu-paused');
      void drawing.offsetWidth;
      drawing.classList.add('edu-running');
      const pause = demo.querySelector('[data-edu-pause]');
      pause.disabled = reduced.matches;
      pause.textContent = 'Pause';
      pause.setAttribute('aria-pressed', 'false');
      report(demo, reduced.matches ? 'Reduced motion: finished artwork shown.' : 'Drawing started.');
    }
    demos.forEach(demo => {
      const drawing = demo.querySelector('.edu-drawing');
      const pause = demo.querySelector('[data-edu-pause]');
      const arrows = demo.querySelector('[data-edu-arrows]');
      const localSpeed = demo.querySelector('[data-pattern-speed]');
      const loop = demo.querySelector('[data-edu-loop]');
      function updateArrows() {
        arrows.disabled = !drawing.querySelector('.edu-arrow');
        drawing.classList.toggle('edu-no-arrows', !arrows.checked);
        updateCode(demo);
      }
      demo.querySelector('[data-edu-play]').addEventListener('click', () => play(demo));
      pause.addEventListener('click', () => {
        const paused = drawing.classList.toggle('edu-paused');
        pause.textContent = paused ? 'Resume' : 'Pause';
        pause.setAttribute('aria-pressed', String(paused));
        report(demo, paused ? 'Drawing paused.' : 'Drawing resumed.');
      });
      drawing.addEventListener('animationend', event => {
        const visible = [...drawing.querySelectorAll('.edu-stroke')].filter(stroke => getComputedStyle(stroke).display !== 'none');
        if (event.target !== visible[visible.length - 1]) return;
        pause.disabled = true;
        report(demo, 'Drawing complete. Replay whenever you like.');
      });
      arrows.addEventListener('change', updateArrows);
      loop.addEventListener('change', () => {
        drawing.style.setProperty('--edu-iterations', loop.checked ? 'infinite' : '1');
        updateCode(demo);
        if (drawing.classList.contains('edu-running')) play(demo);
      });
      localSpeed.addEventListener('input', () => {
        drawing.style.setProperty('--edu-local-speed', localSpeed.value);
        localSpeed.nextElementSibling.value = `${localSpeed.value}x`;
        localSpeed.setAttribute('aria-valuetext', `${localSpeed.value} times speed`);
        updateCode(demo);
      });
      demo.querySelectorAll('[data-edu-line], [data-edu-box]').forEach(select => select.addEventListener('change', () => {
        const line = demo.querySelector('[data-edu-line]').value;
        const box = demo.querySelector('[data-edu-box]').value;
        const template = demo.querySelector(`template[data-line="${line}"][data-box="${box}"]`);
        if (!template) throw new Error(`Missing line/box template: ${line}/${box}`);
        drawing.replaceChildren(template.content.cloneNode(true));
        updateArrows();
        play(demo);
      }));
      demo.querySelector('[data-edu-copy]').addEventListener('click', async () => {
        updateCode(demo);
        const output = demo.querySelector('.edu-code');
        try {
          if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable.');
          await navigator.clipboard.writeText(output.value);
          report(demo, 'Self-contained animated SVG copied.');
        } catch (error) {
          output.closest('details').open = true;
          output.focus({ preventScroll: true });
          output.select();
          report(demo, `Could not copy: ${error.message} Code selected for manual copying; SVG download is also available.`);
        }
      });
      demo.querySelector('[data-pattern-download]').addEventListener('click', () => {
        const url = URL.createObjectURL(new Blob([markup(demo)], { type: 'image/svg+xml' }));
        const link = document.createElement('a');
        link.href = url;
        link.download = 'chalk-pattern.svg';
        link.click();
        setTimeout(() => URL.revokeObjectURL(url), 1000);
        report(demo, 'Current SVG exported with speed, repeat and arrow settings.');
      });
      reduced.addEventListener('change', () => {
        if (reduced.matches) {
          pause.disabled = true;
          report(demo, 'Reduced motion: finished artwork shown.');
        } else {
          drawing.classList.remove('edu-running', 'edu-paused');
          pause.disabled = true;
          report(demo, 'Ready. Press Draw to start again.');
        }
      });
      updateArrows();
      report(demo, 'Ready. Press Draw to animate; artwork is shown complete until then.');
    });
    master.addEventListener('input', () => {
      library.style.setProperty('--edu-speed', master.value);
      library.querySelector('[data-edu-speed-output]').value = `${master.value}x`;
      master.setAttribute('aria-valuetext', `${master.value} times speed`);
      demos.forEach(updateCode);
    });
    library.querySelector('[data-edu-all]').addEventListener('click', () => demos.forEach(play));
    const stop = library.querySelector('[data-edu-stop]');
    stop.addEventListener('click', () => {
      const active = demos.filter(demo => !demo.querySelector('[data-edu-pause]').disabled);
      const shouldPause = active.some(demo => !demo.querySelector('.edu-drawing').classList.contains('edu-paused'));
      active.forEach(demo => {
        const drawing = demo.querySelector('.edu-drawing');
        const pause = demo.querySelector('[data-edu-pause]');
        drawing.classList.toggle('edu-paused', shouldPause);
        pause.textContent = shouldPause ? 'Resume' : 'Pause';
        pause.setAttribute('aria-pressed', String(shouldPause));
        report(demo, shouldPause ? 'Drawing paused.' : 'Drawing resumed.');
      });
      stop.textContent = shouldPause ? 'Resume all' : 'Pause all';
    });
  });
})();
