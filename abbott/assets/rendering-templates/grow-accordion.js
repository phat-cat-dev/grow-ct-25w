/* grow-accordion.js — arm the trickle reveal for block-section accordions.
 *
 * Progressive enhancement: do nothing and every <details data-reveal="trickle">
 * stays open and visible. Call mountGrowReveal() to hide un-revealed sections
 * and reveal them (fade in + auto-open) one at a time — driven either by
 * scroll (default, a scrollspy) or manually by Adapt trickle.
 *
 *   import mountGrowReveal from './grow-accordion.js';
 *   const r = mountGrowReveal(document);                 // scroll-driven
 *   const r = mountGrowReveal(root, { driver: 'manual' });// trickle-driven
 *   // then on each trickle step unlock:
 *   Adapt.on('trickle:unlock', view => r.reveal(view.$el[0]));
 */
export function mountGrowReveal(root = document, opts = {}) {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const blocks = Array.from(root.querySelectorAll('[data-reveal="trickle"]'));

  // No JS-worthy state: leave everything open + visible.
  if (!blocks.length || reduced) {
    blocks.forEach((b) => { b.open = true; });
    return { reveal() {}, revealNext() {}, blocks };
  }

  const host = root.classList ? root : document.documentElement;
  host.classList.add('grow-reveal-armed');           // CSS now hides un-revealed blocks
  blocks.forEach((b) => { b.open = false; b.classList.remove('is-revealed'); });

  function reveal(block) {
    if (!block || block.classList.contains('is-revealed')) return;
    block.classList.add('is-revealed');              // fade / slide in
    requestAnimationFrame(() => { block.open = true; }); // auto-open (height animates)
  }

  let i = 0;
  function revealNext() { if (i < blocks.length) reveal(blocks[i++]); }

  if (opts.driver !== 'manual' && 'IntersectionObserver' in window) {
    // Default: scrollspy — reveal each section as it enters the viewport.
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { reveal(e.target); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -30% 0px' });
    blocks.forEach((b) => io.observe(b));
    reveal(blocks[0]);                               // first section shows immediately
  }

  return { reveal, revealNext, blocks };
}

export default mountGrowReveal;
