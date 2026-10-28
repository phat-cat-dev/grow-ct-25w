#!/usr/bin/env node
/**
 * build-abbott-semantic-interface.js
 *
 * Merge step: drops the --ad-<group>-<c|t>-<nnnn> / --ab-<group>-<c|t>-<nnnn>
 * registry layers out of the middle and wires Adapt's rules straight onto the
 * Layer 3 semantic names, per the plan ("once we have the Layer 3 system set
 * against the registry layer we can actually just bring them together and
 * miss out the registry layer altogether").
 *
 * Reads (never writes):
 *   adapt-core-vanilla-interface-uuid.tokens.less
 *     - the registry-tokenised file (selectors + --ad-<group>-<c|t>-<nnnn> +
 *       the original simple "// property: value;" comment per declaration)
 *   ab-token-base.less
 *     - the --ab-<group>-<c|t>-<nnnn> -> --ab-<semantic> rename table
 *
 * Writes:
 *   adapt-abbott-interface.tokens.less
 *     - same selectors, same simple trailing comments, but every
 *       --ad-<group>-<c|t>-<nnnn> value is replaced directly with the bare
 *       --ab-<semantic> name (no intervening registry token, no var()
 *       wrapper - matching this document's existing symbolic-value
 *       convention, same as the uuid file it's derived from).
 *
 * Usage: node tools/build-abbott-semantic-interface.js
 */
'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const DIR = path.join(ROOT, 'undlaf-intro_261012-235924', 'adapt-less-compiles');
const SRC_UUID_TOKENS = path.join(DIR, 'adapt-core-vanilla-interface-uuid.tokens.less');
const SRC_AB_BASE = path.join(DIR, 'ab-token-base.less');
const OUT = path.join(DIR, 'adapt-abbott-interface.tokens.less');

function main() {
  const abBaseText = fs.readFileSync(SRC_AB_BASE, 'utf8');
  const uuidText = fs.readFileSync(SRC_UUID_TOKENS, 'utf8');

  // Build (group,layer,num) -> bare --ab-<semantic> name
  const semMap = new Map();
  const rowRe = /--ab-([a-z]+)-([ct])-(\d{4}):\s*var\((--ab-[a-zA-Z0-9-]+)\)/g;
  let m;
  while ((m = rowRe.exec(abBaseText))) {
    semMap.set(`${m[1]}-${m[2]}-${m[3]}`, m[4]);
  }
  if (semMap.size === 0) {
    console.error('FATAL: no rows parsed from ab-token-base.less - check its format.');
    process.exit(1);
  }

  let misses = 0;
  let subs = 0;
  const adTokenRe = /--ad-([a-z]+)-([ct])-(\d{4})/g;
  const outText = uuidText.replace(adTokenRe, (full, group, layer, num) => {
    const key = `${group}-${layer}-${num}`;
    const sem = semMap.get(key);
    if (!sem) { misses++; return full; }
    subs++;
    return sem;
  });

  if (misses > 0) {
    console.error(`FATAL: ${misses} --ad- tokens had no matching row in ab-token-base.less.`);
    process.exit(1);
  }

  const oldHeaderRe = /\/\* =====================================================\n   CORE vs VANILLA THEME[\s\S]*?===================================================== \*\//;
  const newHeader = `/* =====================================================
   ADAPT <- ABBOTT SEMANTIC INTERFACE (registry layer skipped)
   =====================================================

   Adapt's own rule structure (selectors, nesting, sections) is unchanged.
   Every declaration value is the bare --ab-<semantic> name from
   ab-token-base.less - the --ad-/--ab- registry layer that sat between them
   has been dropped out, per the plan to bring Layer 1 straight onto Layer 3
   once Layer 3 existed. Trailing comment is still just the original single
   "// property: value;" pair (full-ruleset comments live in ab-token-base.less
   only, for now).
   ===================================================== */`;
  const finalText = outText.replace(oldHeaderRe, newHeader);

  fs.writeFileSync(OUT, finalText);
  console.log(`Written: ${OUT}`);
  console.log(`--ad- tokens replaced with --ab-<semantic>: ${subs}`);
}

main();
