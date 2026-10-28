import { notifications, createNotificationService } from '../../notifications/notification-service.js';
import { mountNotificationBar } from '../../notifications/notification-bar.js';
import { mountCourseAgent } from '../../course-agent/course-agent.js';

export async function mountLessonNav(host, { lesson, authoring = false } = {}) {
  if (!lesson || !host) throw new Error('Lesson navigation needs a host and lesson element.');
  const response = await fetch(new URL('./nav-template.html', import.meta.url));
  if (!response.ok) throw new Error(`Navigation template failed to load (${response.status}).`);
  host.innerHTML = await response.text();
  if (!authoring) host.querySelectorAll('[data-design-only]').forEach(element => element.remove());
  const controller = new AbortController();
  const { signal } = controller;
  const bar = host.querySelector('.nav__inner');
  const status = host.querySelector('[data-nav-status]');
  const modeKeys = [...host.querySelectorAll('[data-status-key]')];
  const stepKeys = [...host.querySelectorAll('[data-section-step]')];
  let mode = 'location';
  const announcement = host.querySelector('[data-nav-announcement]');
  const panels = new Map();
  const lessonTitle = lesson.querySelector('.page__title').textContent.trim();
  const sections = [
    { element: lesson.querySelector('.page__header'), id: lesson.id, title: 'Lesson Overview' },
    ...[...lesson.querySelectorAll('.article[id]')].map(element => ({
      element, id: element.id, title: element.querySelector('.article__title').textContent.trim(),
    })),
  ];
  let current = sections[0], pinned = null, activePanel = null, latest = null, alertUntil = 0;
  let themeManager = null, agent = null, themeStylesheet = null;
  const location = () => ({ lessonTitle, sectionTitle: current.title, id: current.id });

  function closePanel(returnFocus = false) {
    if (!activePanel) return;
    const trigger = host.querySelector(`[data-panel="${activePanel}"]`);
    panels.get(activePanel).hidden = true;
    trigger.setAttribute('aria-expanded', 'false');
    activePanel = null;
    if (returnFocus) trigger.focus();
  }
  function makePanel(name, title) {
    const panel = document.createElement('section');
    panel.className = 'lesson-nav__panel';
    panel.id = `lesson-${name}-panel`;
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', title);
    panel.hidden = true;
    const header = document.createElement('header');
    const heading = document.createElement('h2');
    heading.textContent = title;
    const close = document.createElement('button');
    close.type = 'button';
    close.textContent = 'Close';
    close.setAttribute('aria-label', `Close ${title}`);
    close.addEventListener('click', () => closePanel(true), { signal });
    header.append(heading, close);
    const content = document.createElement('div');
    panel.append(header, content);
    host.append(panel);
    panels.set(name, panel);
    return content;
  }
  function renderStatus() {
    let text;
    if (latest && Date.now() < alertUntil) text = `${latest.source}: ${latest.message}`;
    else if (mode === 'alerts') text = latest ? `${latest.source}: ${latest.message}` : 'No alerts';
    else text = `${lessonTitle} > ${current.title}`;
    status.textContent = text;
    status.title = text;
  }
  function updateLocation() {
    const boundary = host.getBoundingClientRect().bottom + 24;
    current = sections[0];
    for (const section of sections) {
      if (section.element.getBoundingClientRect().top <= boundary) current = section;
    }
    // Short final sections never reach the boundary, so keep a stepped-to section while it is on screen.
    const pinnedTop = pinned?.element.getBoundingClientRect().top;
    if (pinned && pinnedTop >= 0 && pinnedTop < innerHeight) current = pinned;
    else pinned = null;
    const index = sections.indexOf(current);
    stepKeys.forEach(key => { key.disabled = !sections[index + Number(key.dataset.sectionStep)]; });
    agent?.update();
    renderStatus();
  }
  function step(offset) {
    const index = sections.indexOf(current);
    const target = sections[Math.min(sections.length - 1, Math.max(0, index + offset))];
    target.element.scrollIntoView();
    pinned = target;
    navigate(target.id);
    updateLocation();
  }
  function navigate(id) {
    closePanel();
    const target = document.getElementById(id);
    target.tabIndex = -1;
    target.focus({ preventScroll: true });
  }

  const agentHost = makePanel('agent', 'Course Agent');
  agent = mountCourseAgent(agentHost, { lesson, getLocation: location, onNavigate: navigate });
  const progress = makePanel('progress', 'Page sections');
  const sectionLinks = document.createElement('nav');
  sectionLinks.setAttribute('aria-label', 'Lesson sections');
  for (const section of sections) {
    const link = document.createElement('a');
    link.href = `#${section.id}`;
    link.textContent = section.title;
    link.addEventListener('click', () => navigate(section.id), { signal });
    sectionLinks.append(link);
  }
  progress.append(sectionLinks);
  const resources = makePanel('resources', 'Course resources');
  const references = lesson.querySelector('[data-skeleton-key="lesson-references"]');
  if (references) {
    const link = document.createElement('a');
    link.href = `#${references.id}`;
    link.textContent = 'Lesson references and further reading';
    link.addEventListener('click', () => navigate(references.id), { signal });
    resources.append(link);
  } else resources.textContent = 'No lesson resources are configured.';
  const themeHost = authoring ? makePanel('theme', 'Theme Manager / design only') : null;
  const notificationHost = document.createElement('div');
  notificationHost.dataset.navNotifications = '';
  host.append(notificationHost);
  const longMessages = createNotificationService();
  const notificationBar = mountNotificationBar(notificationHost, { service: longMessages, matchHeight: bar });
  const unsubscribe = notifications.subscribe(message => {
    latest = message;
    if (`${message.source}: ${message.message}`.length > 100) {
      announcement.textContent = '';
      longMessages.publish(message);
      alertUntil = 0;
    } else {
      announcement.textContent = `${message.source}: ${message.message}`;
      alertUntil = Date.now() + 7000;
    }
    renderStatus();
  });

  host.addEventListener('click', event => {
    const button = event.target.closest('button');
    if (!button) return;
    if (button.dataset.statusKey) {
      // Location has no key: pressing the active key again returns to it.
      mode = mode === button.dataset.statusKey ? 'location' : button.dataset.statusKey;
      alertUntil = 0;
      modeKeys.forEach(key => key.setAttribute('aria-pressed', String(key.dataset.statusKey === mode)));
      renderStatus();
    } else if (button.dataset.panel) {
      const name = button.dataset.panel;
      const wasOpen = activePanel === name;
      closePanel();
      if (!wasOpen) {
        activePanel = name;
        panels.get(name).hidden = false;
        button.setAttribute('aria-expanded', 'true');
        panels.get(name).querySelector('button').focus();
      }
    } else if (button.name === 'skipButton') {
      lesson.tabIndex = -1;
      lesson.focus();
    } else if (button.dataset.sectionStep) {
      step(Number(button.dataset.sectionStep));
    }
  }, { signal });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && activePanel) {
      event.preventDefault();
      closePanel(true);
    }
  }, { signal });
  document.addEventListener('click', event => {
    if (activePanel && !host.contains(event.target)) closePanel();
  }, { signal });
  document.addEventListener('scroll', updateLocation, { passive: true, signal });
  const resize = new ResizeObserver(() => {
    document.documentElement.style.setProperty('--lesson-nav-height', `${bar.getBoundingClientRect().height}px`);
    updateLocation();
  });
  resize.observe(bar);
  // Re-renders each second so short alerts expire from the display.
  const tick = setInterval(renderStatus, 1000);
  updateLocation();

  if (authoring) {
    try {
      const stylesheet = document.createElement('link');
      stylesheet.rel = 'stylesheet';
      stylesheet.href = new URL('../../theme-manager/theme-manager.css', import.meta.url).href;
      document.head.append(stylesheet);
      themeStylesheet = stylesheet;
      const [{ mountThemeManager }, { createStudioAdapter }] = await Promise.all([
        import('../../theme-manager/theme-manager.js'), import('../../theme-manager/studio-adapter.js'),
      ]);
      themeManager = mountThemeManager(themeHost, {
        adapter: createStudioAdapter(), preview: document.body, serverTools: false,
      });
    } catch (error) {
      themeHost.textContent = `Theme Manager could not load: ${error.message}`;
      notifications.publish({ source: 'Navigation', level: 'error', message: themeHost.textContent });
    }
  }
  return {
    getLocation: location,
    destroy() {
      clearInterval(tick);
      controller.abort();
      resize.disconnect();
      unsubscribe();
      notificationBar.destroy();
      agent.destroy();
      themeManager?.destroy();
      themeStylesheet?.remove();
      document.documentElement.style.removeProperty('--lesson-nav-height');
      host.replaceChildren();
    },
  };
}
