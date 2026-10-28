(function (global) {
  'use strict';
  function mountTypingChat(host, { messages, title = 'A guided reflection' } = {}) {
    if (!(host instanceof HTMLElement) || host.hasAttribute('data-chat-mounted')) throw new Error('Use an unmounted chat host.');
    if (!Array.isArray(messages) || !messages.length || messages.length > 100 ||
        messages.some(message => !message || !['guide', 'learner'].includes(message.speaker) ||
          typeof message.text !== 'string' || !message.text.trim() || message.text.length > 4000)) {
      throw new Error('Provide up to 100 guide/learner messages with non-empty text.');
    }
    const script = messages.map(message => ({ ...message }));
    const controller = new AbortController();
    const media = matchMedia('(prefers-reduced-motion: reduce)');
    let index = 0, frame = null, finish = null, destroyed = false;
    host.classList.add('textured', 'typing-chat');
    host.setAttribute('data-chat-mounted', '');
    host.innerHTML = `
      <h3></h3>
      <p>Scripted learning conversation / no live agent connection.</p>
      <ol class="typing-chat__messages" aria-label="Scripted conversation"></ol>
      <div class="typing-chat__controls">
        <button type="button" data-chat="next">Next message</button>
        <button type="button" data-chat="skip" disabled>Show full message</button>
        <button type="button" data-chat="replay">Replay conversation</button>
      </div>
      <p class="typing-chat__status" role="status" aria-live="polite">Ready. Play the next scripted message.</p>
    `;
    host.querySelector('h3').textContent = title;
    const find = selector => host.querySelector(selector);
    function reduced() {
      return media.matches || !!host.closest('.no-motion,[data-tm-no-motion="true"]');
    }
    function next() {
      if (destroyed || finish || index >= script.length) return;
      const message = script[index++];
      const item = document.createElement('li');
      item.className = 'typing-chat__bubble';
      item.dataset.speaker = message.speaker;
      const speaker = document.createElement('strong');
      speaker.className = 'typing-chat__speaker';
      speaker.textContent = message.speaker === 'guide' ? 'Scripted guide' : 'Example learner';
      const content = document.createElement('span');
      content.setAttribute('aria-hidden', 'true');
      const accessible = document.createElement('span');
      accessible.hidden = true;
      const dots = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      dots.setAttribute('viewBox', '0 0 90 30');
      dots.setAttribute('aria-hidden', 'true');
      dots.classList.add('sequential-dots', 'is-playing');
      [15, 45, 75].forEach((x, n) => {
        const circle = document.createElementNS(dots.namespaceURI, 'circle');
        circle.setAttribute('cx', x);
        circle.setAttribute('cy', 15);
        circle.setAttribute('r', 5);
        circle.style.setProperty('--dot-index', n);
        dots.append(circle);
      });
      const caret = document.createElement('span');
      caret.className = 'typing-chat__cursor';
      caret.setAttribute('aria-hidden', 'true');
      caret.hidden = true;
      item.append(speaker, dots, content, accessible, caret);
      find('ol').append(item);
      find('[data-chat="next"]').disabled = true;
      find('[data-chat="skip"]').disabled = false;
      find('[role="status"]').textContent = 'Revealing a scripted message.';
      const letters = Array.from(message.text);
      finish = () => {
        cancelAnimationFrame(frame);
        content.textContent = message.text;
        accessible.textContent = message.text;
        accessible.hidden = false;
        dots.remove();
        caret.remove();
        finish = null;
        find('[data-chat="next"]').disabled = index >= script.length;
        const skip = find('[data-chat="skip"]');
        if (document.activeElement === skip) find(index >= script.length ? '[data-chat="replay"]' : '[data-chat="next"]').focus();
        skip.disabled = true;
        find('[role="status"]').textContent = `${speaker.textContent}: ${message.text}${index === script.length ? ' Conversation complete.' : ''}`;
        host.dispatchEvent(new CustomEvent('typing-chat:message', { bubbles: true, detail: { ...message, index: index - 1 } }));
      };
      if (reduced()) { finish(); return; }
      const start = performance.now();
      function tick(now) {
        if (destroyed) return;
        if (reduced()) { finish?.(); return; }
        const count = Math.max(0, Math.floor((now - start - 900) / 24));
        if (count > 0) { dots.setAttribute('hidden', ''); caret.hidden = false; }
        content.textContent = letters.slice(0, count).join('');
        if (count >= letters.length) finish();
        else frame = requestAnimationFrame(tick);
      }
      frame = requestAnimationFrame(tick);
    }
    host.addEventListener('click', event => {
      const action = event.target.closest('[data-chat]')?.dataset.chat;
      if (action === 'next') next();
      if (action === 'skip') finish?.();
      if (action === 'replay') {
        cancelAnimationFrame(frame);
        finish = null;
        index = 0;
        find('ol').replaceChildren();
        find('[data-chat="next"]').disabled = false;
        find('[data-chat="skip"]').disabled = true;
        find('[role="status"]').textContent = 'Conversation reset. Play the next scripted message.';
      }
    }, { signal: controller.signal });
    media.addEventListener('change', () => { if (media.matches) finish?.(); }, { signal: controller.signal });
    return {
      next,
      destroy() {
        destroyed = true;
        cancelAnimationFrame(frame);
        finish = null;
        controller.abort();
        host.replaceChildren();
        host.classList.remove('textured', 'typing-chat');
        host.removeAttribute('data-chat-mounted');
      },
    };
  }
  global.TexturedChat = { mountTypingChat };
})(window);
