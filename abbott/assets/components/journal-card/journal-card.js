(function (global) {
  'use strict';
  function mountJournalCard(host, { storageKey } = {}) {
    if (!(host instanceof HTMLElement) || host.hasAttribute('data-journal-mounted')) throw new Error('Use an unmounted journal card.');
    const input = host.querySelector('[data-journal-text]');
    const status = host.querySelector('[data-journal-status]');
    const save = host.querySelector('[data-journal-save]');
    const exportButton = host.querySelector('[data-journal-export]');
    const cardId = host.dataset.journalCard;
    if (!input || !status || !save || !exportButton || !/^[a-z0-9_-]+$/i.test(cardId || '')) throw new Error('The journal card needs a stable ID, textarea, status, save and export controls.');
    const key = storageKey === undefined ? `grow-journal:${location.pathname}:${cardId}` : storageKey;
    const controller = new AbortController();
    let savedText = '', savedAt = null;
    function report(message, error = false) {
      status.textContent = message;
      status.dataset.error = String(error);
    }
    function snapshot() { return { version: 1, cardId, text: input.value, savedAt }; }
    host.setAttribute('data-journal-mounted', '');
    if (key) {
      try {
        const raw = localStorage.getItem(key);
        if (raw) {
          const saved = JSON.parse(raw);
          if (!saved || saved.version !== 1 || saved.cardId !== cardId || typeof saved.text !== 'string' ||
              saved.text.length > 20000 || typeof saved.savedAt !== 'string' || !Number.isFinite(Date.parse(saved.savedAt))) {
            throw new Error('Saved journal data is invalid.');
          }
          input.value = savedText = saved.text;
          savedAt = saved.savedAt;
          report(`Saved notes restored from ${new Date(savedAt).toLocaleString()}.`);
        } else report('Draft only. Press Save to keep these notes in this browser.');
      } catch (error) { report(`Could not restore your notes: ${error.message}. Existing saved data was not changed.`, true); }
    } else report('Browser saving is disabled. Export JSON to keep a copy.');
    input.addEventListener('input', () => {
      const dirty = input.value !== savedText;
      report(dirty ? 'Unsaved changes. Press Save or export a copy.' : savedAt ? 'No changes since your last save.' : 'Draft only. Not saved yet.');
      host.dispatchEvent(new CustomEvent('journal-card:change', { bubbles: true, detail: { ...snapshot(), dirty } }));
    }, { signal: controller.signal });
    save.addEventListener('click', () => {
      if (!key) { report('Browser saving is disabled. Use Export notes JSON instead.', true); return; }
      try {
        const timestamp = new Date().toISOString();
        const record = { ...snapshot(), savedAt: timestamp };
        localStorage.setItem(key, JSON.stringify(record));
        savedText = input.value;
        savedAt = timestamp;
        report(`Saved in this browser at ${new Date(timestamp).toLocaleTimeString()}.`);
        host.dispatchEvent(new CustomEvent('journal-card:save', { bubbles: true, detail: record }));
      } catch (error) { report(`Notes could not be saved: ${error.message}. Your draft is still here; export a backup.`, true); }
    }, { signal: controller.signal });
    exportButton.addEventListener('click', () => {
      const url = URL.createObjectURL(new Blob([JSON.stringify({ ...snapshot(), exportedAt: new Date().toISOString() }, null, 2)], { type: 'application/json' }));
      const link = document.createElement('a');
      link.href = url;
      link.download = `${cardId}.json`;
      link.click();
      setTimeout(() => URL.revokeObjectURL(url), 0);
      report('Current draft exported. Keep the file private if it contains personal notes.');
    }, { signal: controller.signal });
    return {
      get: snapshot,
      destroy() { controller.abort(); host.removeAttribute('data-journal-mounted'); },
    };
  }
  global.JournalCard = { mountJournalCard };
})(window);
