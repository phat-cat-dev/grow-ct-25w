#!/usr/bin/env node
// EXPERIMENT (not wired into the live gates) — the "level" data object + resolver.
//
// A course's level is normally SET BY PITCH (the onb-03 tier). But if pitch is
// left at 'none' / 'no-tier', a specific explicit L setting (the proposed
// onb-04_level gate) TAKES PRECEDENCE. This gives fine-grained FHEQ targeting
// when a course deliberately isn't pitched to one of the three named tiers.
//
//   pitch set (not none)  -> level from pitch (tier band)       setBy: 'pitch'
//   pitch none + explicitL -> level from the explicit L          setBy: 'explicit'
//   neither                -> unresolved (flagged)               setBy: 'none'

// Course pitch -> FHEQ band (the tier's nominal level; the pathway's own
// capability fheqLevels are finer and span the blurry tops around this).
const PITCH_FHEQ = { introductory: 4, intermediate: 5, advanced: 6 };
const NONE = new Set(['none', 'no-tier', '', null, undefined]);

function tierForFheq(n) {
  if (n == null) return null;
  if (n <= 4) return 'introductory';
  if (n === 5) return 'intermediate';
  return 'advanced'; // 6, 7
}

function parseL(l) {
  if (l == null) return null;
  const m = String(l).match(/(\d+)/);
  return m ? Number(m[1]) : null;
}

/**
 * Resolve the level data object.
 * @param {{pitch?:string, explicitL?:string|number}} input
 * @returns {{setBy, pitch, explicitL, resolvedFheq, resolvedTier, warning?}}
 */
function resolveLevel({ pitch, explicitL } = {}) {
  const pitchIsNone = NONE.has(pitch);
  if (!pitchIsNone) {
    return {
      setBy: 'pitch',
      pitch,
      explicitL: explicitL != null ? explicitL : null, // kept but NOT used (pitch wins)
      resolvedFheq: PITCH_FHEQ[pitch] ?? null,
      resolvedTier: pitch
    };
  }
  const n = parseL(explicitL);
  if (n != null) {
    return { setBy: 'explicit', pitch: 'none', explicitL, resolvedFheq: n, resolvedTier: tierForFheq(n) };
  }
  return { setBy: 'none', pitch: 'none', explicitL: null, resolvedFheq: null, resolvedTier: null,
    warning: 'pitch is none and no explicit L given — level unresolved' };
}

module.exports = { resolveLevel, tierForFheq, PITCH_FHEQ };

if (require.main === module) {
  const cases = [
    { pitch: 'introductory' },                 // pitch wins -> L4 / introductory
    { pitch: 'none', explicitL: 'fheq:5' },     // explicit precedence -> L5 / intermediate
    { pitch: 'advanced', explicitL: 'fheq:7' }, // pitch wins, explicit ignored -> L6 / advanced
    { pitch: 'none' }                           // unresolved -> flagged
  ];
  console.log('level resolver — worked examples:');
  for (const c of cases) console.log('  in', JSON.stringify(c), '->', JSON.stringify(resolveLevel(c)));
}
