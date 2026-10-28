(function () {
  document.querySelectorAll('[data-edu-library]').forEach(function (library) {
    var demos = Array.from(library.querySelectorAll('[data-edu-demo]'));
    var styles = library.querySelector('style').textContent;
    var speed = library.querySelector('[data-edu-speed]');
    function code(demo) {
      var drawing = demo.querySelector('.edu-drawing');
      var classes = 'edu-running' + (drawing.classList.contains('edu-no-arrows') ? ' edu-no-arrows' : '');
      var iterations = demo.querySelector('[data-edu-loop]').checked ? 'infinite' : '1';
      demo.querySelector('.edu-code').value = '<style>\n' + styles + '\n</style>\n<!-- Set shared speed variables on a common ancestor. -->\n<div class="' + classes + '" style="--edu-iterations:' + iterations + '">\n' + drawing.innerHTML + '\n</div>';
    }
    function play(demo) {
      var drawing = demo.querySelector('.edu-drawing');
      drawing.classList.remove('edu-running', 'edu-paused');
      void drawing.offsetWidth;
      drawing.classList.add('edu-running');
      var button = demo.querySelector('[data-edu-pause]');
      button.disabled = matchMedia('(prefers-reduced-motion: reduce)').matches;
      button.textContent = 'Pause';
      button.setAttribute('aria-pressed', 'false');
      demo.querySelector('.edu-status').textContent = button.disabled ? 'Reduced motion: showing the completed drawing.' : 'Drawing started.';
    }
    demos.forEach(function (demo) {
      var drawing = demo.querySelector('.edu-drawing');
      var pause = demo.querySelector('[data-edu-pause]');
      var arrows = demo.querySelector('[data-edu-arrows]');
      function updateArrows() {
        arrows.disabled = !drawing.querySelector('.edu-arrow');
        drawing.classList.toggle('edu-no-arrows', !arrows.checked);
        code(demo);
      }
      demo.querySelector('[data-edu-play]').addEventListener('click', function () { play(demo); });
      pause.addEventListener('click', function () {
        var paused = drawing.classList.toggle('edu-paused');
        pause.textContent = paused ? 'Resume' : 'Pause';
        pause.setAttribute('aria-pressed', String(paused));
        demo.querySelector('.edu-status').textContent = paused ? 'Drawing paused.' : 'Drawing resumed.';
      });
      drawing.addEventListener('animationend', function (event) {
        if (event.target !== drawing.querySelector('.edu-stroke:last-child')) return;
        pause.disabled = true;
        demo.querySelector('.edu-status').textContent = 'Drawing complete. Replay whenever you like.';
      });
      demo.querySelector('[data-edu-loop]').addEventListener('change', function () {
        drawing.style.setProperty('--edu-iterations', this.checked ? 'infinite' : '1');
        code(demo);
        if (drawing.classList.contains('edu-running')) play(demo);
      });
      arrows.addEventListener('change', updateArrows);
      demo.querySelectorAll('[data-edu-line], [data-edu-box]').forEach(function (select) {
        select.addEventListener('change', function () {
          var line = demo.querySelector('[data-edu-line]').value;
          var box = demo.querySelector('[data-edu-box]').value;
          var template = demo.querySelector('template[data-line="' + line + '"][data-box="' + box + '"]');
          drawing.replaceChildren(template.content.cloneNode(true));
          updateArrows();
          play(demo);
        });
      });
      demo.querySelector('[data-edu-copy]').addEventListener('click', async function () {
        var output = demo.querySelector('.edu-code');
        if (!navigator.clipboard) {
          output.closest('details').open = true;
          output.select();
          demo.querySelector('.edu-status').textContent = 'Clipboard unavailable. Code selected; use Ctrl+C to copy.';
          return;
        }
        try {
          await navigator.clipboard.writeText(output.value);
          demo.querySelector('.edu-status').textContent = 'Reusable SVG and styles copied.';
        } catch (error) {
          output.closest('details').open = true;
          output.select();
          demo.querySelector('.edu-status').textContent = 'Copy failed: ' + error.message + '. Code selected; use Ctrl+C.';
        }
      });
      updateArrows();
    });
    speed.addEventListener('input', function () {
      library.style.setProperty('--edu-speed', this.value);
      library.querySelector('[data-edu-speed-output]').textContent = this.value + '×';
    });
    library.querySelector('[data-edu-all]').addEventListener('click', function () { demos.forEach(play); });
    library.querySelector('[data-edu-stop]').addEventListener('click', function () {
      demos.forEach(function (demo) {
        var drawing = demo.querySelector('.edu-drawing');
        if (!drawing.classList.contains('edu-running')) return;
        drawing.classList.add('edu-paused');
        var button = demo.querySelector('[data-edu-pause]');
        button.textContent = 'Resume';
        button.setAttribute('aria-pressed', 'true');
        demo.querySelector('.edu-status').textContent = 'Drawing paused.';
      });
    });
  });
})();
