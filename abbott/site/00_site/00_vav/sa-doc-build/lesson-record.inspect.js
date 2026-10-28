/* ============================================================================
   lesson-record.inspect.js
   The data layer view. Optional, no dependencies. The template never needs it.

   Adds three tools to the bar's [data-lr-tools] slot:
     Expand all / Collapse all   open or close every accordion
     Markup                      outline every element by nesting depth and open
                                 an inspector: hover or click any element to see
                                 its tag, classes, id, role, aria-* and data-*
                                 attributes, with the full tree beside it.
   In the inspector, click pins an element, Escape closes. Lines in the tree
   scroll to their element and open any closed accordion around it.
   ============================================================================ */
(function () {
  'use strict';
  var root = document.querySelector('[data-lr-role="lesson-record"]');
  if (!root) return;
  var slot = root.querySelector('[data-lr-tools]');
  var inspecting = false, current = null, pinned = null, panel = null, lines = new Map();

  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text) n.textContent = text; return n; }
  function tool(label, fn) { var b = el('button', 'lr-tool', label); b.type = 'button'; b.addEventListener('click', function () { fn(b); }); return b; }
  function details() { return Array.prototype.slice.call(root.querySelectorAll('details')); }

  /* ----- audience filter -----
     sets [data-view] on the record; the inspect.css rules then hide the groups
     that do not belong to the chosen audience. "learners" drops every internal
     group; "internal" keeps only them. The legend stays as the full key. */
  function viewFilter() {
    var group = el('div', 'lr-views'); group.setAttribute('role', 'group'); group.setAttribute('aria-label', 'Show sections by audience');
    group.appendChild(el('span', 'lr-views__label', 'Show'));
    root.setAttribute('data-view', 'all');
    var btns = [];
    [['all', 'All'], ['learners', 'Learners only'], ['internal', 'Internal only']].forEach(function (v) {
      var b = el('button', 'lr-tool', v[1]); b.type = 'button';
      b.setAttribute('data-view', v[0]);
      b.setAttribute('aria-pressed', String(v[0] === 'all'));
      b.addEventListener('click', function () {
        root.setAttribute('data-view', v[0]);
        btns.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      });
      btns.push(b);
      group.appendChild(b);
    });
    return group;
  }

  /* ----- tools ----- */
  if (slot) {
    slot.hidden = false;
    slot.appendChild(viewFilter());
    slot.appendChild(tool('Expand all', function () { details().forEach(function (d) { d.open = true; }); }));
    slot.appendChild(tool('Collapse all', function () { details().forEach(function (d) { d.open = false; }); }));
    var markup = tool('Markup', function (b) { toggle(!inspecting); b.setAttribute('aria-pressed', String(inspecting)); });
    markup.setAttribute('aria-pressed', 'false');
    slot.appendChild(markup);
  }

  /* ----- describing elements ----- */
  /* the inspector's own classes and markers are never shown as part of the markup */
  function cleanClass(n) {
    return (typeof n.className === 'string' ? n.className : '').split(/\s+/).filter(function (c) { return c && !/^lri-/.test(c) && c !== 'lr--inspect'; });
  }
  function attrsOf(n) {
    return Array.prototype.slice.call(n.attributes).filter(function (a) { return a.name !== 'data-lr-depth'; }).map(function (a) {
      return a.name === 'class' ? { name: 'class', value: cleanClass(n).join(' ') } : a;
    }).filter(function (a) { return !(a.name === 'class' && a.value === ''); });
  }
  function isAria(a) { return a.name === 'role' || a.name.indexOf('aria-') === 0; }
  function ownText(n) {
    if (n.children.length) return '';
    var t = (n.textContent || '').replace(/\s+/g, ' ').trim();
    return t.length > 38 ? t.slice(0, 38) + '…' : t;
  }
  function label(n) {
    var s = n.tagName.toLowerCase();
    if (n.id) s += '#' + n.id;
    var c = cleanClass(n)[0];
    if (c) s += '.' + c;
    return s;
  }
  function depthOf(n) { var d = 0; while (n && n !== root) { d++; n = n.parentNode; } return d; }

  /* ----- tree ----- */
  function buildTree(host) {
    host.textContent = '';
    lines.clear();
    (function walk(n, d) {
      var line = el('span', 'lri__line');
      line.style.setProperty('--d', d);
      var hasAria = false, hasClass = false;
      line.appendChild(el('span', 't', '<' + n.tagName.toLowerCase()));
      if (n.id) line.appendChild(el('span', 'i', ' #' + n.id));
      var cls = cleanClass(n);
      if (cls.length) { hasClass = true; line.appendChild(el('span', 'c', ' .' + cls.join('.'))); }
      attrsOf(n).forEach(function (a) {
        if (a.name === 'class' || a.name === 'id') return;
        var k = isAria(a) ? 'a' : (a.name.indexOf('data-') === 0 ? 'd' : 'o');
        if (k === 'a') hasAria = true;
        line.appendChild(el('span', k, ' ' + a.name + (a.value !== '' ? '="' + a.value + '"' : '')));
      });
      line.appendChild(el('span', 't', '>'));
      var txt = ownText(n);
      if (txt) line.appendChild(el('span', 'x', '  ' + txt));
      if (hasAria) line.setAttribute('data-has-aria', '');
      if (hasClass) line.setAttribute('data-has-class', '');
      line.addEventListener('mouseenter', function () { setCurrent(n, true); });
      line.addEventListener('click', function () { pin(n, true); });
      host.appendChild(line);
      lines.set(n, line);
      Array.prototype.forEach.call(n.children, function (c) { walk(c, d + 1); });
    })(root, 0);
  }

  /* ----- detail ----- */
  function showDetail(n) {
    var box = panel.querySelector('.lri__detail');
    box.textContent = '';
    if (!n) { box.appendChild(el('p', 'lri__none', 'Hover or click an element.')); return; }
    var chain = [], p = n;
    while (p && p !== root.parentNode) { chain.unshift(p); p = p.parentNode; }
    var shown = chain.slice(-6);
    var path = el('p', 'lri__path');
    if (chain.length > shown.length) path.appendChild(document.createTextNode('… > '));
    shown.forEach(function (c, i) {
      var s = el(c === n ? 'b' : 'span', null, label(c));
      path.appendChild(s);
      if (i < shown.length - 1) path.appendChild(document.createTextNode(' > '));
    });
    box.appendChild(path);
    var at = attrsOf(n);
    if (!at.length) { box.appendChild(el('p', 'lri__none', 'No attributes.')); return; }
    var table = el('table', 'lri__attrs');
    at.forEach(function (a) {
      var tr = document.createElement('tr');
      if (isAria(a)) tr.setAttribute('data-aria', '');
      tr.appendChild(el('th', null, a.name));
      tr.appendChild(el('td', null, a.value === '' ? '(present)' : a.value));
      table.appendChild(tr);
    });
    box.appendChild(table);
  }

  /* ----- highlight and pin ----- */
  function setCurrent(n, fromTree) {
    if (pinned) return;
    if (current) { current.classList.remove('lri-hl'); var ol = lines.get(current); if (ol) ol.classList.remove('is-current'); }
    current = n;
    if (n) {
      n.classList.add('lri-hl');
      var l = lines.get(n);
      if (l) { l.classList.add('is-current'); if (!fromTree) l.scrollIntoView({ block: 'nearest' }); }
    }
    showDetail(n);
  }
  function openAround(n) { var d = n.closest && n.closest('details'); while (d) { d.open = true; d = d.parentNode && d.parentNode.closest ? d.parentNode.closest('details') : null; } }
  function pin(n, fromTree) {
    if (pinned) { pinned.classList.remove('lri-pin'); var pl = lines.get(pinned); if (pl) pl.classList.remove('is-pinned'); }
    if (pinned === n) { pinned = null; setCurrent(n); return; }
    if (current) { current.classList.remove('lri-hl'); var cl = lines.get(current); if (cl) cl.classList.remove('is-current'); current = null; }
    pinned = n;
    n.classList.add('lri-pin');
    var l = lines.get(n);
    if (l) l.classList.add('is-pinned');
    if (fromTree) { openAround(n); n.scrollIntoView({ block: 'center', behavior: 'smooth' }); } else if (l) l.scrollIntoView({ block: 'nearest' });
    showDetail(n);
  }

  /* ----- toggle ----- */
  function onOver(e) { if (inspecting && root.contains(e.target)) setCurrent(e.target); }
  function onClick(e) {
    if (!inspecting || !root.contains(e.target)) return;
    if (e.target.closest('[data-lr-tools]')) return;
    e.preventDefault(); e.stopPropagation();
    pin(e.target);
  }
  function onKey(e) { if (inspecting && e.key === 'Escape') { toggle(false); if (markup) markup.setAttribute('aria-pressed', 'false'); } }

  function toggle(on) {
    inspecting = on;
    root.classList.toggle('lr--inspect', on);
    document.body.classList.toggle('lri-open', on);
    if (on) {
      Array.prototype.forEach.call(root.querySelectorAll('*'), function (n) { n.setAttribute('data-lr-depth', String(Math.min(depthOf(n) - 1, 7))); });
      root.setAttribute('data-lr-depth', '0');
      if (!panel) buildPanel();
      panel.hidden = false;
      buildTree(panel.querySelector('.lri__tree'));
      showDetail(null);
      document.addEventListener('mouseover', onOver);
      document.addEventListener('click', onClick, true);
      document.addEventListener('keydown', onKey);
    } else {
      Array.prototype.forEach.call(root.querySelectorAll('[data-lr-depth]'), function (n) { n.removeAttribute('data-lr-depth'); });
      root.removeAttribute('data-lr-depth');
      [current, pinned].forEach(function (n) { if (n) n.classList.remove('lri-hl', 'lri-pin'); });
      current = pinned = null;
      if (panel) panel.hidden = true;
      document.removeEventListener('mouseover', onOver);
      document.removeEventListener('click', onClick, true);
      document.removeEventListener('keydown', onKey);
    }
  }

  function buildPanel() {
    panel = el('aside', 'lri'); panel.setAttribute('aria-label', 'Markup inspector'); panel.hidden = true;
    var bar = el('div', 'lri__bar');
    bar.appendChild(el('strong', null, 'Markup'));
    bar.appendChild(el('span', 'lri__hint', 'Hover the page or a line. Click to pin. Escape closes.'));
    var tree = el('div', 'lri__tree'); tree.setAttribute('data-filter', 'all');
    [['all', 'All'], ['aria', 'ARIA and roles'], ['class', 'Classes']].forEach(function (f) {
      var b = el('button', null, f[1]); b.type = 'button'; b.setAttribute('aria-pressed', String(f[0] === 'all'));
      b.addEventListener('click', function () {
        tree.setAttribute('data-filter', f[0]);
        Array.prototype.forEach.call(bar.querySelectorAll('button[data-f]'), function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      });
      b.setAttribute('data-f', f[0]);
      bar.appendChild(b);
    });
    var close = el('button', null, 'Close'); close.type = 'button';
    close.addEventListener('click', function () { toggle(false); if (markup) markup.setAttribute('aria-pressed', 'false'); });
    bar.appendChild(close);
    var cols = el('div', 'lri__cols');
    cols.appendChild(el('div', 'lri__detail'));
    cols.appendChild(tree);
    panel.appendChild(bar); panel.appendChild(cols);
    document.body.appendChild(panel);
  }
})();
