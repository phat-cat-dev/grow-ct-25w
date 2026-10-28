import Adapt from 'core/js/adapt';

/**
 * GROW Menu Card Marks
 * --------------------------------------------------------------------------
 * Drops a large, faint Material Symbol into the bottom-right of each boxmenu
 * card. The glyph is a Material Symbols *ligature* (e.g. "rocket_launch") set
 * as the element's text; the theme styles `.grow-card-mark` (menuItemCard.less).
 *
 * Fixed ROLES (repeat as intended): the opening page -> rocket_launch, any
 * confidence check -> query_stats, the final test -> assignment_turned_in, the
 * closing page -> emoji_events. LESSON cards get a fitting glyph from a keyword
 * hint where one matches, otherwise a stable hash pick from a big pool - and
 * either way de-duplicated, so no two lessons on one menu share a glyph.
 */
class GrowCardMarks {

  constructor() {
    this.decorate = this.decorate.bind(this);
    Adapt.on('menuView:ready pageView:ready', this.decorate);
  }

  decorate() {
    const hash = (str) => { let h = 0; for (let i = 0; i < str.length; i++) h = (h * 31 + str.charCodeAt(i)) >>> 0; return h; };

    // Fixed roles - allowed to repeat across the menu, so NOT de-duplicated.
    const WELCOME = 'rocket_launch';
    const SUMMARY = 'emoji_events';
    const CONFIDENCE = 'query_stats';
    const TEST = 'assignment_turned_in';

    // A big, characterful pool for lesson cards (all valid Material Symbols).
    const POOL = [
      'lightbulb', 'psychology', 'neurology', 'menu_book', 'auto_stories', 'school',
      'edit_note', 'draw', 'fact_check', 'quiz', 'science', 'biotech', 'emoji_objects',
      'travel_explore', 'hub', 'smart_toy', 'model_training', 'diversity_3', 'forum',
      'balance', 'tips_and_updates', 'local_library', 'history_edu', 'interests',
      'route', 'insights', 'bolt', 'extension', 'category', 'construction', 'flag',
      'workspace_premium', 'verified', 'rule', 'terminal', 'data_object', 'gavel'
    ];

    // Keyword hints (first match wins): give a lesson a glyph that fits its
    // topic. Each is a short preference list, tried in order, skipped if used.
    const HINTS = [
      [/prompt/i, ['edit_note', 'draw', 'terminal']],
      [/what ai|what is|generative|understand/i, ['smart_toy', 'neurology', 'psychology']],
      [/partner|literacy|\btool|machine/i, ['smart_toy', 'hub', 'psychology']],
      [/misconduct|integrit|honest|declar|plagiar/i, ['balance', 'gavel', 'verified']],
      [/categor/i, ['category', 'extension', 'hub']],
      [/technique|routine|habit|method|design/i, ['model_training', 'construction', 'route']],
      [/fail|risk|critical|reading|reliab|trust|bias/i, ['fact_check', 'flag', 'rule']]
    ];

    const used = new Set();
    const take = (prefs) => { for (const g of prefs) if (g && !used.has(g)) { used.add(g); return g; } return null; };

    const items = Array.from(document.querySelectorAll('#wrapper .boxmenu-item'));
    const n = items.length;
    items.forEach((item, i) => {
      const inner = item.querySelector('.boxmenu-item__inner');
      if (!inner || inner.querySelector('.grow-card-mark')) return;
      const title = (item.querySelector('.boxmenu-item__title') || item).textContent.trim();
      const seed = hash(title + '#' + i);

      let icon;
      if (/confidence/i.test(title)) icon = CONFIDENCE;
      else if (/summative|final\s+(course\s+)?test|course\s+test/i.test(title)) icon = TEST;
      else if (i === 0) icon = WELCOME;
      else if (i === n - 1) icon = SUMMARY;
      else {
        // lesson / other page: a fitting hint if any, else the hashed pool,
        // both de-duplicated so the menu's lesson glyphs are all distinct.
        let prefs = [];
        for (const [re, gl] of HINTS) { if (re.test(title)) { prefs = gl; break; } }
        const off = seed % POOL.length;
        const rotated = POOL.slice(off).concat(POOL.slice(0, off));
        icon = take(prefs) || take(rotated) || POOL[off];
      }

      const mark = document.createElement('span');
      mark.className = 'grow-card-mark';
      mark.setAttribute('aria-hidden', 'true');
      mark.textContent = icon;
      mark.style.setProperty('--rot', ((seed % 25) - 12) + 'deg');
      mark.style.setProperty('--dx', (((seed >> 3) % 6) * 2) + 'px');
      mark.style.setProperty('--dy', (((seed >> 6) % 6) * 2) + 'px');
      mark.style.setProperty('--mark-size', (7 * (1.10 + ((seed >> 9) % 6) / 100)).toFixed(2) + 'rem');
      inner.appendChild(mark);
    });
  }

}

export default new GrowCardMarks();
