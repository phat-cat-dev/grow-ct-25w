(function (global) {
  'use strict';
  let instances = 0;
  const colours = ['yellow', 'pink', 'blue', 'brand'];
  const clone = value => JSON.parse(JSON.stringify(value));
  const isText = value => typeof value === 'string' && value.length <= 4000;
  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function validateActivity(value) {
    if (!value || !/^[a-z0-9_-]+$/i.test(value.id || '') || !isText(value.title) ||
        !Array.isArray(value.groups) || !value.groups.length || !Array.isArray(value.notes) || value.notes.length > 200) {
      throw new Error('An activity needs an ID, title, groups and notes.');
    }
    const config = clone(value);
    const groups = new Set();
    for (const group of config.groups) {
      if (!/^[a-z0-9_-]+$/i.test(group.id || '') || groups.has(group.id) || !isText(group.label) || !group.label.trim()) {
        throw new Error('Groups need unique IDs and non-empty labels.');
      }
      groups.add(group.id);
    }
    const ids = new Set();
    for (const note of config.notes) {
      if (!/^[a-z0-9_-]+$/i.test(note.id || '') || ids.has(note.id) || !isText(note.text) || !note.text.trim() ||
          !groups.has(note.group) || (note.answer !== undefined && !isText(note.answer)) ||
          (note.colour !== undefined && !colours.includes(note.colour)) ||
          (note.expectedGroup !== undefined && !groups.has(note.expectedGroup)) ||
          (note.expectedOrder !== undefined && (!Number.isInteger(note.expectedOrder) || note.expectedOrder < 1 || !note.expectedGroup))) {
        throw new Error('Invalid authored note: check IDs, text, group and answer criteria.');
      }
      ids.add(note.id);
    }
    for (const group of config.groups) {
      const orders = config.notes.filter(n => n.expectedGroup === group.id && n.expectedOrder !== undefined)
        .map(n => n.expectedOrder).sort((a, b) => a - b);
      if (orders.some((value, index) => value !== index + 1)) throw new Error('Expected order must run from 1 without gaps or duplicates in each group.');
    }
    return config;
  }
  function mountNotesBoard(host, {
    activity, storageKey, onChange = () => {},
  } = {}) {
    const config = validateActivity(activity);
    if (!(host instanceof HTMLElement) || host.hasAttribute('data-notes-mounted')) throw new Error('Use an unmounted board host.');
    const id = `notes-${++instances}`;
    const key = storageKey === undefined ? `grow-notes:${location.pathname}:${config.id}` : storageKey;
    const abort = new AbortController();
    const authored = new Map(config.notes.map(note => [note.id, note]));
    let notes = config.notes.map(note => ({
      id: note.id, group: note.group, text: note.text, answer: note.answer || '',
      colour: note.colour || 'yellow', remember: false, flipped: false,
    }));
    let mode = 'learn', rememberOnly = false, editId = null, checked = false, destroyed = false;
    const feedback = new Map();
    const animations = new Set();
    let dragId = null, storageError = null;
    const snapshot = () => ({
      version: 1, activityId: config.id, mode,
      notes: notes.map(note => authored.has(note.id)
        ? { id: note.id, group: note.group, colour: note.colour, remember: note.remember }
        : { ...note, flipped: false }),
    });
    function validateProgress(value) {
      if (!value || value.version !== 1 || value.activityId !== config.id || !['learn', 'test'].includes(value.mode) ||
          !Array.isArray(value.notes) || value.notes.length > 200) throw new Error('This progress file does not match the activity.');
      const seen = new Set();
      const next = value.notes.map(note => {
        if (!note || typeof note.id !== 'string' || !/^[a-z0-9_-]+$/i.test(note.id) || seen.has(note.id) ||
            !config.groups.some(group => group.id === note.group) || !colours.includes(note.colour) || typeof note.remember !== 'boolean') {
          throw new Error('Saved notes contain an invalid ID, group, colour or remember state.');
        }
        seen.add(note.id);
        const source = authored.get(note.id) || note;
        if (!isText(source.text) || !source.text.trim() || !isText(source.answer || '')) throw new Error('Saved note text is invalid.');
        return { id: note.id, group: note.group, text: source.text, answer: source.answer || '', colour: note.colour, remember: note.remember, flipped: false };
      });
      if ([...authored.keys()].some(noteId => !seen.has(noteId))) throw new Error('Saved progress is missing an authored note.');
      return { notes: next, mode: value.mode };
    }
    if (key) {
      try {
        const saved = localStorage.getItem(key);
        if (saved) ({ notes, mode } = validateProgress(JSON.parse(saved)));
      } catch (error) { storageError = `Could not restore saved notes: ${error.message}`; }
    }
    host.classList.add('notes-board', 'textured');
    host.setAttribute('data-notes-mounted', '');
    host.innerHTML = `
      <header class="notes-board__header"><h2></h2><p data-instructions></p></header>
      <div class="notes-board__toolbar" role="group" aria-label="Notes board tools">
        <button type="button" data-action="add">Add a note</button>
        <label>Activity mode<select data-mode><option value="learn">Learning / explore</option><option value="test">Testing / try first</option></select></label>
        <label class="notes-board__check"><input type="checkbox" data-remember-only> Things to remember</label>
        <button type="button" data-action="check">Check arrangement</button>
        <button type="button" data-action="export">Export notes JSON</button>
      </div>
      <p class="notes-board__status" role="status" aria-live="polite" data-status></p>
      <form class="notes-board__editor" hidden>
        <h3 data-editor-title></h3>
        <label for="${id}-text">Note / question<textarea id="${id}-text" name="text" required maxlength="4000" rows="3"></textarea></label>
        <label for="${id}-answer">Answer / back of note (optional)<textarea id="${id}-answer" name="answer" maxlength="4000" rows="2"></textarea></label>
        <label for="${id}-colour">Colour<select id="${id}-colour" name="colour">${colours.map(c => `<option value="${c}">${c}</option>`).join('')}</select></label>
        <div><button type="submit">Save note</button><button type="button" data-action="cancel">Cancel</button></div>
      </form>
      <div class="notes-board__groups ab-corkboard textured" data-groups></div>
      <p class="notes-board__privacy">Saved only in this browser when storage is available. Export a JSON backup before clearing browser data. This is a practice activity, not a secure examination.</p>
    `;
    const find = selector => host.querySelector(selector);
    const editor = find('form');
    find('h2').textContent = config.title;
    find('[data-instructions]').textContent = config.instructions || 'Move notes into groups and use Earlier / Later to arrange them. Dragging is optional; every action is keyboard accessible.';
    function status(message, error = false) {
      find('[data-status]').textContent = message;
      find('[data-status]').dataset.error = String(error);
    }
    function announceSave(message) {
      let error = '';
      if (key) {
        try { localStorage.setItem(key, JSON.stringify(snapshot())); }
        catch (failure) { error = ` Changes are live but could not be saved: ${failure.message}`; }
      }
      status(message + error, !!error);
      const value = snapshot();
      onChange(clone(value));
      host.dispatchEvent(new CustomEvent('notes-board:change', { bubbles: true, detail: value }));
    }
    function button(name, action, noteId) {
      const node = element('button', '', name);
      node.type = 'button';
      node.dataset.action = action;
      node.dataset.note = noteId;
      return node;
    }
    function reducedMotion() {
      return matchMedia('(prefers-reduced-motion: reduce)').matches || !!host.closest('.no-motion,[data-tm-no-motion="true"]');
    }
    function animate(noteId, kind) {
      if (reducedMotion() || destroyed) return;
      const card = [...host.querySelectorAll('[data-note-card]')].find(node => node.dataset.noteCard === noteId);
      if (!card) return;
      const frames = kind === 'flip'
        ? [{ opacity: .3, transform: 'perspective(600px) rotateY(-12deg)' }, { opacity: 1, transform: 'none' }]
        : [{ opacity: .5, transform: 'translateY(-10px) rotate(-1deg)' }, { opacity: 1, transform: 'none' }];
      const animation = card.animate(frames, { duration: 220, easing: 'ease-out' });
      animations.add(animation);
      animation.finished.then(() => animations.delete(animation), error => {
        animations.delete(animation);
        if (error.name !== 'AbortError') status(`Animation failed: ${error.message}`, true);
      });
    }
    function render(focusId, focusAction) {
      find('[data-mode]').value = mode;
      find('[data-remember-only]').checked = rememberOnly;
      find('[data-action="check"]').disabled = !config.notes.some(note => note.expectedGroup);
      const groups = find('[data-groups]');
      groups.replaceChildren();
      for (const group of config.groups) {
        const column = element('section', 'notes-board__group');
        column.dataset.group = group.id;
        const title = element('h3', '', group.label);
        title.id = `${id}-group-${group.id}`;
        column.setAttribute('aria-labelledby', title.id);
        const list = element('ol', 'notes-board__list');
        const groupNotes = notes.filter(note => note.group === group.id);
        column.append(title, list);
        groupNotes.filter(note => !rememberOnly || note.remember).forEach(note => {
          const item = element('li');
          const card = element('article', `textured ab-sticky ${note.colour} notes-board__note`);
          card.dataset.noteCard = note.id;
          const heading = element('h4', '', note.text);
          heading.id = `${id}-note-${note.id}`;
          card.setAttribute('aria-labelledby', heading.id);
          const type = element('p', 'notes-board__tag', authored.has(note.id) ? 'Activity note' : 'Your note / not scored');
          const handle = button('Move', 'drag-help', note.id);
          handle.draggable = true;
          handle.title = 'Drag this handle, or use the Move to menu below.';
          handle.setAttribute('aria-label', `Move note: ${note.text.slice(0, 80)}`);
          const top = element('div', 'notes-board__note-top');
          top.append(type, handle);
          card.append(top, heading);
          if (note.answer) {
            const flip = button(note.flipped ? 'Show question' : 'Reveal answer', 'flip', note.id);
            flip.disabled = mode === 'test' && !checked;
            flip.setAttribute('aria-expanded', String(note.flipped));
            flip.setAttribute('aria-controls', `${id}-answer-${note.id}`);
            const answer = element('p', 'notes-board__answer', note.answer);
            answer.id = `${id}-answer-${note.id}`;
            answer.hidden = !note.flipped;
            card.append(flip, answer);
          }
          const remember = button(note.remember ? 'Remembering' : 'Remember this', 'remember', note.id);
          remember.setAttribute('aria-pressed', String(note.remember));
          card.append(remember);
          const move = element('label', '', 'Move to');
          const select = element('select');
          select.dataset.move = note.id;
          select.setAttribute('aria-label', `Move to group: ${note.text.slice(0, 80)}`);
          config.groups.forEach(destination => select.add(new Option(destination.label, destination.id)));
          select.value = note.group;
          move.append(select);
          const earlier = button('Earlier', 'earlier', note.id);
          const later = button('Later', 'later', note.id);
          const position = groupNotes.indexOf(note);
          earlier.disabled = position === 0;
          later.disabled = position === groupNotes.length - 1;
          const tools = element('div', 'notes-board__note-tools');
          tools.append(earlier, later);
          const colourLabel = element('label', '', 'Note colour');
          const colour = element('select');
          colour.dataset.colour = note.id;
          colours.forEach(name => colour.add(new Option(name, name)));
          colour.value = note.colour;
          colourLabel.append(colour);
          card.append(move, colourLabel, tools);
          if (!authored.has(note.id)) {
            tools.append(button('Edit', 'edit', note.id), button('Delete', 'delete', note.id));
          }
          if (feedback.has(note.id)) {
            const result = feedback.get(note.id);
            const message = element('p', 'notes-board__feedback', result.correct ? 'Correct placement and sequence.' : 'Not yet: check the group or sequence.');
            message.dataset.correct = String(result.correct);
            card.append(message);
          }
          item.append(card);
          list.append(item);
        });
        if (!list.children.length) column.append(element('p', 'notes-board__empty', rememberOnly ? 'No remembered notes in this group.' : 'Move notes here.'));
        groups.append(column);
      }
      if (focusId) {
        const card = [...host.querySelectorAll('[data-note-card]')].find(node => node.dataset.noteCard === focusId);
        const candidate = card?.querySelector(`[data-action="${focusAction}"]:not(:disabled)`) || card?.querySelector('button:not(:disabled)');
        (candidate || find('[data-remember-only]')).focus();
      }
    }
    function changed(message, noteId, action) {
      checked = false;
      feedback.clear();
      if (mode === 'test') notes.forEach(note => { note.flipped = false; });
      render(noteId, action);
      announceSave(message);
    }
    function moveNote(noteId, groupId) {
      const note = notes.find(n => n.id === noteId);
      if (!note || !config.groups.some(g => g.id === groupId)) throw new Error('Choose a valid note and destination group.');
      if (note.group === groupId) return;
      note.group = groupId;
      notes = notes.filter(n => n !== note).concat(note);
      changed(`Moved note to ${config.groups.find(g => g.id === groupId).label}.`, noteId, 'drag-help');
      animate(noteId, 'move');
    }
    function check() {
      const results = config.notes.filter(note => note.expectedGroup).map(source => {
        const note = notes.find(n => n.id === source.id);
        const ordered = notes.filter(n => n.group === source.expectedGroup && authored.get(n.id)?.expectedGroup === source.expectedGroup &&
          authored.get(n.id)?.expectedOrder !== undefined);
        const correct = note.group === source.expectedGroup &&
          (source.expectedOrder === undefined || ordered.indexOf(note) + 1 === source.expectedOrder);
        return { id: note.id, correct };
      });
      checked = true;
      results.forEach(result => feedback.set(result.id, result));
      render();
      const score = results.filter(result => result.correct).length;
      status(results.length ? `${score} of ${results.length} activity notes correct. ${score === results.length ? 'Arrangement complete.' : 'Try another arrangement.'} Answers can now be revealed.` : 'This board has no scored notes.');
      host.dispatchEvent(new CustomEvent('notes-board:check', { bubbles: true, detail: { score, total: results.length, results } }));
      return { score, total: results.length, results };
    }
    function openEditor(note) {
      editId = note?.id || null;
      editor.hidden = false;
      find('[data-editor-title]').textContent = note ? 'Edit your note' : 'Add a note';
      editor.elements.text.value = note?.text || '';
      editor.elements.answer.value = note?.answer || '';
      editor.elements.colour.value = note?.colour || 'yellow';
      editor.elements.text.focus();
    }
    host.addEventListener('click', event => {
      const control = event.target.closest('button[data-action]');
      if (!control || !host.contains(control)) return;
      const action = control.dataset.action;
      const note = notes.find(n => n.id === control.dataset.note);
      if (action === 'add') { openEditor(); return; }
      if (action === 'cancel') { editor.hidden = true; find('[data-action="add"]').focus(); return; }
      if (action === 'check') { check(); return; }
      if (action === 'export') {
        const url = URL.createObjectURL(new Blob([JSON.stringify(snapshot(), null, 2)], { type: 'application/json' }));
        const link = element('a');
        link.href = url;
        link.download = `${config.id}-notes.json`;
        link.click();
        setTimeout(() => URL.revokeObjectURL(url), 0);
        status('Notes exported. Keep this file private if it contains personal reflections.');
        return;
      }
      if (!note) return;
      if (action === 'drag-help') { status('Drag the Move handle, or choose a group in Move to. Earlier / Later changes sequence.'); return; }
      if (action === 'edit' && !authored.has(note.id)) { openEditor(note); return; }
      if (action === 'flip') {
        if (mode === 'test' && !checked) return;
        note.flipped = !note.flipped;
        render(note.id, 'flip');
        animate(note.id, 'flip');
        status(note.flipped ? `Answer: ${note.answer}` : 'Question side shown.');
      } else if (action === 'remember') {
        note.remember = !note.remember;
        render(note.id, 'remember');
        announceSave(note.remember ? 'Added to things to remember.' : 'Removed from things to remember.');
      } else if (action === 'delete' && !authored.has(note.id)) {
        notes = notes.filter(n => n !== note);
        changed('Your note was deleted. Activity notes cannot be deleted.');
        find('[data-action="add"]').focus();
      } else if (action === 'earlier' || action === 'later') {
        const siblings = notes.filter(n => n.group === note.group);
        const other = siblings[siblings.indexOf(note) + (action === 'earlier' ? -1 : 1)];
        if (!other) return;
        const a = notes.indexOf(note), b = notes.indexOf(other);
        [notes[a], notes[b]] = [notes[b], notes[a]];
        changed(`Note moved ${action}.`, note.id, action);
        animate(note.id, 'move');
      }
    }, { signal: abort.signal });
    host.addEventListener('change', event => {
      const input = event.target;
      if (input.matches('[data-mode]')) {
        mode = input.value;
        notes.forEach(note => { note.flipped = false; });
        changed(mode === 'test' ? 'Testing mode: arrange the activity notes, then check before revealing answers.' : 'Learning mode: reveal answers and explore freely.');
      } else if (input.matches('[data-remember-only]')) {
        rememberOnly = input.checked;
        render();
        status(rememberOnly ? 'Showing only things to remember. Arrangement checks still include all activity notes.' : 'Showing all notes.');
      } else if (input.dataset.move) {
        moveNote(input.dataset.move, input.value);
      } else if (input.dataset.colour) {
        const note = notes.find(n => n.id === input.dataset.colour);
        note.colour = input.value;
        render(note.id, 'remember');
        announceSave('Note colour updated.');
      }
    }, { signal: abort.signal });
    editor.addEventListener('submit', event => {
      event.preventDefault();
      const text = editor.elements.text.value.trim();
      if (!text) { status('Write a note before saving.', true); editor.elements.text.focus(); return; }
      if (!editId && notes.length >= 200) { status('This board supports up to 200 notes. Export and remove a personal note first.', true); return; }
      const noteId = editId || `user-${global.crypto.randomUUID()}`;
      const existing = notes.find(note => note.id === noteId);
      const note = {
        id: noteId, text, answer: editor.elements.answer.value.trim(), colour: editor.elements.colour.value,
        group: existing?.group || config.groups[0].id, remember: existing?.remember || false, flipped: false,
      };
      if (existing) notes[notes.indexOf(existing)] = note;
      else notes.push(note);
      rememberOnly = false;
      find('[data-remember-only]').checked = false;
      editor.hidden = true;
      changed('Your note was saved.', noteId, 'edit');
      animate(noteId, 'pin');
    }, { signal: abort.signal });
    host.addEventListener('dragstart', event => {
      const handle = event.target.closest('[draggable="true"]');
      if (!handle) return;
      dragId = handle.dataset.note;
      event.dataTransfer.setData('text/plain', `${id}:${dragId}`);
      event.dataTransfer.effectAllowed = 'move';
    }, { signal: abort.signal });
    host.addEventListener('dragover', event => {
      if (!dragId || !event.target.closest('[data-group]')) return;
      event.preventDefault();
      event.dataTransfer.dropEffect = 'move';
    }, { signal: abort.signal });
    host.addEventListener('drop', event => {
      const group = event.target.closest('[data-group]');
      if (!group || !dragId || event.dataTransfer.getData('text/plain') !== `${id}:${dragId}`) return;
      event.preventDefault();
      moveNote(dragId, group.dataset.group);
      dragId = null;
    }, { signal: abort.signal });
    host.addEventListener('dragend', () => { dragId = null; }, { signal: abort.signal });
    host.addEventListener('keydown', event => {
      if (event.key === 'Escape' && !editor.hidden) {
        editor.hidden = true;
        find('[data-action="add"]').focus();
      }
    }, { signal: abort.signal });
    render();
    status(storageError || (key ? 'Notes ready. Progress stays in this browser; export a backup when needed.' : 'Notes ready. Browser saving is disabled.'), !!storageError);
    return {
      get: () => clone(snapshot()),
      load(value) {
        const next = validateProgress(value);
        notes = next.notes;
        mode = next.mode;
        rememberOnly = false;
        editor.hidden = true;
        changed('Progress restored.');
      },
      check,
      destroy() {
        destroyed = true;
        abort.abort();
        animations.forEach(animation => animation.cancel());
        animations.clear();
        host.replaceChildren();
        host.classList.remove('notes-board', 'textured');
        host.removeAttribute('data-notes-mounted');
      },
    };
  }
  global.TexturedNotes = { mountNotesBoard, validateActivity };
})(window);
