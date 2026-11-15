import ComponentView from 'core/js/views/componentView';
import { notifications } from './notifications/notification-service';
import { mountNotificationBar } from './notifications/notification-bar';

// A lesson-guide "course tutor" that lists the page's sections, tracks where the
// learner is, and SPEAKS by publishing to the shared notification bar. The bar is
// the standalone notifications service, reused unchanged — this is the link the
// tutor outputs to.
class TutorView extends ComponentView {

  postRender() {
    const tutor = this.model.get('_tutor') || {};
    this.tutorName = tutor.name || 'Course tutor';
    this.messages = tutor._messages || {};
    this.spoken = new Set();

    if (tutor._showGuide !== false) this.buildGuide(tutor);
    this.mountBar();
    if (tutor.greeting) this.say(tutor.greeting, 'success');

    this.setReadyStatus();
  }

  // Sections come from the page DOM (the real articles), falling back to any
  // authored _sections so the component still renders in isolation.
  buildGuide(tutor) {
    const nav = this.$('.grow-tutor__guide')[0];
    if (!nav) return;
    const page = this.$el.closest('.page')[0];
    let sections = page
      ? [...page.querySelectorAll('.article[id]')].map(article => ({
          id: article.id,
          title: article.querySelector('.article__title')?.textContent.trim() || article.id
        }))
      : [];
    if (!sections.length && Array.isArray(tutor._sections)) {
      sections = tutor._sections.map(section => ({ id: section._id, title: section.title || section._id }));
    }
    for (const { id, title } of sections) {
      const link = document.createElement('a');
      link.href = `#${id}`;
      link.className = 'grow-tutor__link';
      link.textContent = title;
      link.addEventListener('click', event => {
        event.preventDefault();
        document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
      nav.append(link);
    }
    this.observeSections(sections, nav);
  }

  // As each section scrolls to centre: mark it current and, once, speak its message.
  observeSections(sections, nav) {
    if (typeof IntersectionObserver === 'undefined' || !sections.length) return;
    this.observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        const id = entry.target.id;
        for (const link of nav.querySelectorAll('a')) {
          if (link.hash === `#${id}`) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        }
        if (this.messages[id] && !this.spoken.has(id)) {
          this.spoken.add(id);
          this.say(this.messages[id]);
        }
      }
    }, { rootMargin: '-45% 0px -45% 0px' });
    for (const { id } of sections) {
      const element = document.getElementById(id);
      if (element) this.observer.observe(element);
    }
  }

  mountBar() {
    const host = this.$('.grow-tutor__bar')[0];
    const matchHeight = this.$('.grow-tutor__rail')[0] || this.$('.grow-tutor__intro')[0] || host;
    if (!host || !matchHeight) return;
    try {
      this.bar = mountNotificationBar(host, { service: notifications, matchHeight });
    } catch (error) {
      // the bar is optional; the tutor still works without it
    }
  }

  // Publish to the shared notification service — the tutor's "voice".
  say(message, level = 'info') {
    if (typeof message !== 'string' || !message.trim()) return;
    try {
      notifications.publish({ message, source: this.tutorName, level });
    } catch (error) {
      // never let a bad message break the component
    }
  }

  remove() {
    this.observer?.disconnect();
    this.bar?.destroy?.();
    return super.remove();
  }
}

TutorView.template = 'growTutor.jsx';

export default TutorView;
