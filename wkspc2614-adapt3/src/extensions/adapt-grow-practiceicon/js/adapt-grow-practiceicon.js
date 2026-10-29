import Adapt from 'core/js/adapt';

/**
 * GROW Practice Icon
 * --------------------------------------------------------------------------
 * Every Grow course belongs to one academic practice pathway. This puts that
 * pathway, its icon and its name, as an eyebrow above each page title and the
 * menu title.
 *
 * The pathway comes from course.json `_growPathway` ({ id, label, symbol,
 * sprite }), stamped by tools/apply-house-rules.py from the course-design
 * facetSet. The icon is a <use> into the theme's sprite
 * (assets/icons/academic-practice.sprite.svg, from tools/build-practice-icons.py),
 * so it inherits currentColor. The icon is decorative (aria-hidden); the
 * pathway name is visible text. The theme styles `.grow-practice-eyebrow`.
 */
const SVG_NS = 'http://www.w3.org/2000/svg';

class GrowPracticeIcon {

  constructor() {
    this.decorate = this.decorate.bind(this);
    Adapt.on('pageView:ready menuView:ready', this.decorate);
  }

  decorate(view) {
    const pathway = Adapt.course && Adapt.course.get('_growPathway');
    if (!pathway || !pathway.symbol || !pathway.sprite) return;
    const root = (view && view.el) || document;
    const content = root.querySelector('.page__header-content, .menu__header-content');
    if (!content || content.querySelector('.grow-practice-eyebrow')) return;

    const eyebrow = document.createElement('div');
    eyebrow.className = 'grow-practice-eyebrow';

    const icon = document.createElementNS(SVG_NS, 'svg');
    icon.setAttribute('class', 'grow-practice-eyebrow__icon');
    icon.setAttribute('aria-hidden', 'true');
    icon.setAttribute('focusable', 'false');
    const use = document.createElementNS(SVG_NS, 'use');
    use.setAttribute('href', `${pathway.sprite}#${pathway.symbol}`);
    icon.appendChild(use);

    const label = document.createElement('span');
    label.className = 'grow-practice-eyebrow__label';
    label.textContent = pathway.label || '';

    eyebrow.append(icon, label);
    content.insertBefore(eyebrow, content.firstChild);
  }

}

export default new GrowPracticeIcon();
