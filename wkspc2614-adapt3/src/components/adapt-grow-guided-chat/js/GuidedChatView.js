import ComponentView from 'core/js/views/componentView';

// A scripted learning conversation that types itself out one message at a time.
// No live agent — the script is authored data. Controls: Next, Show full message
// (skip the typing), Replay. Reduced motion shows each message in full at once.
class GuidedChatView extends ComponentView {

  preRender() {
    const chat = this.model.get('_chat') || {};
    this.speed = Number(chat._typeSpeed) > 0 ? Number(chat._typeSpeed) : 26; // ms per char
    this.autoAdvance = chat._autoAdvance === true;
  }

  postRender() {
    this.reduced = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.bubbles = Array.from(this.$('.grow-guided-chat__bubble'));
    this.$next = this.$('[data-chat="next"]');
    this.$skip = this.$('[data-chat="skip"]');
    this.$status = this.$('.grow-guided-chat__status');
    this.$next.on('click', () => this.advance());
    this.$skip.on('click', () => this.finishTyping());
    this.$('[data-chat="replay"]').on('click', () => this.replay());
    this.replay();
    this.setReadyStatus();
  }

  replay() {
    this.clearTimer();
    this.index = -1;
    this.current = null;
    for (const bubble of this.bubbles) {
      bubble.hidden = true;
      const typed = bubble.querySelector('.grow-guided-chat__typed');
      if (typed) typed.textContent = '';
      bubble.querySelector('.grow-guided-chat__cursor')?.remove();
    }
    this.setStatus('');
    this.advance();
  }

  advance() {
    this.clearTimer();
    this.index += 1;
    if (this.index >= this.bubbles.length) return this.complete();
    const bubble = this.bubbles[this.index];
    bubble.hidden = false;
    this.type(bubble);
  }

  type(bubble) {
    const typed = bubble.querySelector('.grow-guided-chat__typed');
    const full = bubble.dataset.text || bubble.querySelector('.grow-guided-chat__sr')?.textContent || '';
    const name = bubble.querySelector('.grow-guided-chat__speaker')?.textContent || '';
    this.setStatus(`${name}: ${full}`);
    this.$next.prop('disabled', true);
    this.current = { typed, full };

    if (this.reduced) { typed.textContent = full; return this.messageDone(); }

    this.$skip.prop('disabled', false);
    typed.textContent = '';
    const cursor = document.createElement('span');
    cursor.className = 'grow-guided-chat__cursor';
    cursor.setAttribute('aria-hidden', 'true');
    bubble.append(cursor);
    let i = 0;
    this.timer = setInterval(() => {
      typed.textContent = full.slice(0, ++i);
      if (i >= full.length) { this.clearTimer(); this.messageDone(); }
    }, this.speed);
  }

  finishTyping() {
    if (!this.current) return;
    this.clearTimer();
    this.current.typed.textContent = this.current.full;
    this.messageDone();
  }

  messageDone() {
    this.clearTimer();
    this.$('.grow-guided-chat__cursor').remove();
    this.$skip.prop('disabled', true);
    if (this.index >= this.bubbles.length - 1) return this.complete();
    this.$next.prop('disabled', false);
    if (this.autoAdvance) this.advance();
  }

  complete() {
    this.$next.prop('disabled', true);
    this.$skip.prop('disabled', true);
    const prefix = (this.$status.text() || '').trim();
    this.setStatus(`${prefix} Conversation complete.`.trim());
  }

  setStatus(text) { this.$status.text(text); }
  clearTimer() { if (this.timer) { clearInterval(this.timer); this.timer = null; } }
  remove() { this.clearTimer(); return super.remove(); }
}

GuidedChatView.template = 'growGuidedChat.jsx';

export default GuidedChatView;
