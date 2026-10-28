(function (global) {
  'use strict';
  const instances = new WeakMap();
  function validateTopics(topics) {
    if (!Array.isArray(topics) || topics.length < 1 || topics.length > 12) throw new RangeError('Provide 1–12 confidence topics.');
    const ids = new Set();
    return topics.map(topic => {
      if (!topic || typeof topic.id !== 'string' || !/^[a-z0-9_-]+$/i.test(topic.id) || ids.has(topic.id)) throw new Error('Topic IDs must be unique letters, digits, hyphens or underscores.');
      if (typeof topic.label !== 'string' || !topic.label.trim() || topic.label.length > 160) throw new Error('Each topic needs a label of 1–160 characters.');
      ids.add(topic.id);
      return { id: topic.id, label: topic.label };
    });
  }
  function mount(host, options) {
    if (!(host instanceof HTMLElement) || instances.has(host)) throw new Error('Use an unmounted confidence-check element.');
    const topics = validateTopics(options?.topics);
    const controller = new AbortController();
    const motion = matchMedia('(prefers-reduced-motion: reduce)');
    let chart = null, destroyed = false, result = null;
    const before = new Map(), after = new Map();
    const make = (tag, text, className) => {
      const element = document.createElement(tag);
      if (text) element.textContent = text;
      if (className) element.className = className;
      return element;
    };
    const status = make('p'); status.setAttribute('role', 'status');
    const description = make('p', 'Rate how confident you feel from 1 (not yet confident) to 5 (very confident). These are self-reported ratings, not proof of skill or an assessment score.');
    const form = make('form');
    topics.forEach((topic, index) => {
      const field = make('fieldset');
      field.append(make('legend', `${index + 1}. ${topic.label}`));
      for (const [phase, store] of [['Before', before], ['After', after]]) {
        const label = make('label', phase);
        const select = make('select');
        select.required = true;
        const empty = make('option', 'Choose a rating'); empty.value = '';
        select.append(empty);
        for (let value = 1; value <= 5; value++) {
          const option = make('option', `${value}${value === 1 ? ' — Not yet confident' : value === 5 ? ' — Very confident' : ''}`);
          option.value = String(value); select.append(option);
        }
        store.set(topic.id, select); label.append(select); field.append(label);
      }
      form.append(field);
    });
    const actions = make('div', '', 'confidence-actions');
    const submit = make('button', 'Show comparison'); submit.type = 'submit';
    const exportButton = make('button', 'Export results JSON'); exportButton.type = 'button'; exportButton.disabled = true;
    const resetButton = make('button', 'Clear ratings'); resetButton.type = 'button';
    actions.append(submit, exportButton, resetButton); form.append(actions);
    const output = make('section'); output.hidden = true; output.setAttribute('aria-label', 'Confidence results');
    const heading = make('h2', 'Your confidence comparison'); heading.tabIndex = -1;
    const summary = make('p');
    const chartHost = make('div', '', 'confidence-chart');
    const canvas = make('canvas');
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', 'Before and after confidence by topic. Exact ratings are in the following table.');
    chartHost.append(canvas);
    const highlights = make('div', '', 'confidence-highlights');
    const highlightStatus = make('p'); highlightStatus.setAttribute('role', 'status');
    const tableWrap = make('div', '', 'confidence-table');
    const table = make('table');
    const caption = make('caption', 'Exact self-reported confidence ratings (1–5)');
    const head = make('thead'); const headRow = make('tr');
    for (const text of ['Topic', 'Before', 'After', 'Change']) {
      const cell = make('th', text); cell.scope = 'col'; headRow.append(cell);
    }
    head.append(headRow);
    const body = make('tbody'); table.append(caption, head, body); tableWrap.append(table);
    output.append(heading, summary, chartHost, highlights, highlightStatus, tableWrap);
    host.replaceChildren(description, form, status, output);
    const opts = { signal: controller.signal };
    function reduced() { return motion.matches || !!host.closest('.no-motion, [data-tm-no-motion="true"]'); }
    function clearResult(message) {
      chart?.destroy(); chart = null; result = null;
      output.hidden = true; exportButton.disabled = true; status.textContent = message;
    }
    function highlight(index) {
      const row = result?.ratings[index];
      if (!row) return;
      if (chart) {
        const elements = [{ datasetIndex: 0, index }, { datasetIndex: 1, index }];
        chart.setActiveElements(elements);
        const point = chart.getDatasetMeta(1).data[index].getCenterPoint();
        chart.tooltip.setActiveElements(elements, point);
        chart.update('none');
      }
      highlights.querySelectorAll('[data-topic]').forEach(button => button.setAttribute('aria-pressed', String(Number(button.dataset.topic) === index)));
      highlightStatus.textContent = `${row.label}: before ${row.before}, after ${row.after}, change ${row.change > 0 ? '+' : ''}${row.change}.`;
    }
    function renderChart() {
      if (typeof global.Chart !== 'function') {
        status.textContent = 'Chart.js could not load. Your exact results remain available in the table and JSON export.';
        chartHost.hidden = true;
        return;
      }
      chartHost.hidden = false;
      const style = getComputedStyle(host);
      const colour = name => style.getPropertyValue(name).trim();
      chart = new global.Chart(canvas, {
        type: 'bar',
        data: {
          labels: topics.map((_, index) => String(index + 1)),
          datasets: [
            { label: 'Before', data: result.ratings.map(row => row.before), backgroundColor: colour('--confidence-before'), borderWidth: 1 },
            { label: 'After', data: result.ratings.map(row => row.after), backgroundColor: colour('--confidence-after'), borderWidth: 1 },
          ],
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          animation: reduced() ? false : { duration: 350 },
          scales: {
            y: { min: 0, max: 5, ticks: { stepSize: 1 }, title: { display: true, text: 'Confidence (1–5)' } },
            x: { title: { display: true, text: 'Topic number (see table)' } },
          },
          plugins: {
            tooltip: { callbacks: { title: items => topics[items[0].dataIndex].label } },
          },
        },
      });
    }
    function showResults(event) {
      event.preventDefault();
      if (!form.reportValidity()) return;
      clearResult('');
      const ratings = topics.map(topic => {
        const a = Number(before.get(topic.id).value), b = Number(after.get(topic.id).value);
        if (![a, b].every(value => Number.isInteger(value) && value >= 1 && value <= 5)) throw new Error('Every topic needs before and after ratings from 1 to 5.');
        return { ...topic, before: a, after: b, change: b - a };
      });
      result = { version: 1, scale: { min: 1, max: 5 }, ratings };
      body.replaceChildren(); highlights.replaceChildren(); highlightStatus.textContent = '';
      ratings.forEach((row, index) => {
        const tr = make('tr'); const label = make('th', `${index + 1}. ${row.label}`); label.scope = 'row'; tr.append(label);
        for (const value of [row.before, row.after, row.change > 0 ? `+${row.change}` : row.change]) tr.append(make('td', String(value)));
        body.append(tr);
        const button = make('button', `Highlight ${index + 1}: ${row.label}`);
        button.type = 'button'; button.dataset.topic = index; button.setAttribute('aria-pressed', 'false'); highlights.append(button);
      });
      summary.textContent = 'A higher rating means you reported greater confidence; a lower rating can also reflect a more informed judgement. It does not establish learning gain or competence.';
      output.hidden = false; exportButton.disabled = false;
      status.textContent = 'Results updated. Use the highlight buttons to activate chart bars and tooltips, or read the exact table below.';
      try { renderChart(); }
      catch (error) {
        chart?.destroy(); chart = null; chartHost.hidden = true;
        status.textContent = `The chart could not render: ${error.message} Your results are still available in the table and export.`;
      }
      heading.focus({ preventScroll: true });
      host.dispatchEvent(new CustomEvent('confidence:results', { bubbles: true, detail: structuredClone(result) }));
    }
    form.addEventListener('submit', event => {
      try { showResults(event); }
      catch (error) { clearResult(`Could not calculate results: ${error.message}`); }
    }, opts);
    form.addEventListener('change', () => { if (result) clearResult('Ratings changed. Press Show comparison to update the results.'); }, opts);
    highlights.addEventListener('click', event => {
      const button = event.target.closest('[data-topic]');
      if (button) highlight(Number(button.dataset.topic));
    }, opts);
    resetButton.addEventListener('click', () => {
      form.reset(); clearResult('All ratings and results cleared.'); before.values().next().value.focus();
    }, opts);
    exportButton.addEventListener('click', () => {
      const url = URL.createObjectURL(new Blob([JSON.stringify(result, null, 2)], { type: 'application/json' }));
      const anchor = make('a'); anchor.href = url; anchor.download = 'confidence-results.json'; anchor.click();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      status.textContent = 'Results JSON exported. Keep personal reflections private.';
    }, opts);
    function syncMotion() {
      if (chart && reduced()) { chart.stop(); chart.options.animation = false; chart.update('none'); }
    }
    motion.addEventListener('change', syncMotion, opts);
    const observer = new MutationObserver(syncMotion);
    for (let node = host; node; node = node.parentElement) observer.observe(node, { attributes: true, attributeFilter: ['class', 'data-tm-no-motion'] });
    instances.set(host, true);
    return {
      get: () => result ? structuredClone(result) : null,
      highlight,
      destroy() {
        if (destroyed) return;
        destroyed = true; chart?.destroy(); controller.abort(); observer.disconnect();
        host.replaceChildren(); instances.delete(host);
      },
    };
  }
  global.ConfidenceCheck = { mount, validateTopics };
})(window);
