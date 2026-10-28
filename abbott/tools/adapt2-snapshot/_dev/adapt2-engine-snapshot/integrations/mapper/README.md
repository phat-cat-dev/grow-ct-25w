# integrations/mapper/

ADAPT's first `integrations/` folder, under ADP-3 (adp-0219, FT-0013 row 3).
Landed by adp-0219 (RJ-0083).

## What this is

Three mapper profiles drafted by ADAPT's notes thread (nts N-0289),
describing M1, M2 and M3's methods for META's mapper tool (`mapper.js`,
WPK-0022). A profile describes the method and changes nothing in it.
Running the mapper against these profiles is a separate, later job.

## Source

- Mapper's UNI path: `adp-relay/threads/nts/drafts/mapper/`.
- UNI commit pinned: `9860a6adb54b5d4e4aaaea5683f11bff665a5044`.
- Each file's SHA-256 checked against nts N-0289's stated prefixes and
  suffixes before copying, all three matching:
  - `adp-m1-stated-subjects.json`: `2df7e2eb9dc86a04ad8c516a0d6178063e580774bc13ea50d0fb94e0a706a55e`
  - `adp-m2-hesa.json` (as drafted, before the fill below): `bb2ae829ed4a866ab73ebd20ab3696b5ad6854ef960a5a40d148395333566863`
  - `adp-m3-pathways.json`: `732f1881686fed3c5b4f437e194e06ef928e7ba9bc96a635666b43379e0e0df8`

## Placeholders filled, and left

- `adp-m1-stated-subjects.json`: no `<...>` placeholder in this profile.
  Copied unchanged.
- `adp-m2-hesa.json`:
  - filled: `target.pin`, with `tools/subject/core/vocab/hecos.json` and
    `tools/subject/core/vocab/cah.json`'s own SHA-256 at this sitting's
    commit.
  - left (listed, not invented): `candidates.terms`. The repository holds
    `hecos.json`'s terms, but the value this field asks for is a
    per-benchmark mapping with the benchmark's own default code removed;
    that removal depends on M2's own tagging run, which has not happened,
    so it is not a static value the repository can supply here.
- `adp-m3-pathways.json`: copied unchanged; all three `<...>` placeholders
  left (listed, not invented):
  - `target.pin`: no ruled capability cards file exists in the repository
    at this commit. The trial file it names for a trial run only,
    `adp-0212-capability-cards.json`, was also not found anywhere under the
    repository (checked by `find . -iname "*capability-cards*"`, excluding
    `archive/`, `node_modules/` and `docs/project-knowledge/`: 0 hits).
  - `candidates.terms`: term list v2 (D-0028: RJ-0031's 9 corrections and
    5 drops applied, 139 kept) does not exist in the repository. The one
    term-list file found, `tools/pathways/core/rules/pathway-term-lists.json`,
    states `"termListVersion": "1.0"`, not v2, so it is not the same list.
  - `candidates.scope`: depends on the same ruled capability cards file as
    `target.pin`, which does not exist, for the same reason.

## check-profile (R0)

Run against each file as its own command, read only, no pull:

```
node /home/abbottdev/workspace-26u/wkspc2600-UNI/mta/claude/mta-relay/sandboxes/wpk-0022/code/tools/mapper/mapper.js check-profile --profile integrations/mapper/<file>.json
```

All three passed, exit 0:

```
profile adp-m1-stated-subjects 0.1.0 (tag): ok; sha256 2df7e2eb9dc86a04ad8c516a0d6178063e580774bc13ea50d0fb94e0a706a55e
profile adp-m2-hesa 0.1.0 (tag): ok; sha256 019d103963623f6fef61608137da5f2b000c2e65ca35b6d9590c9e681a1e77f2
profile adp-m3-pathways 0.1.0 (align): ok; sha256 732f1881686fed3c5b4f437e194e06ef928e7ba9bc96a635666b43379e0e0df8
```

M2's reported hash differs from its as-drafted hash above because its
`target.pin` placeholder was filled before this run; M1 and M3 are
unchanged from the draft, so their reported hashes match the SHA-256
check above.

The UNI clone this tool ran from was at HEAD `cbdbc8d` at the time of this
run (`git -C /home/abbottdev/workspace-26u/wkspc2600-UNI rev-parse --short HEAD`,
read only, no pull). This is the clone's current commit, separate from the
`9860a6adb54b5d4e4aaaea5683f11bff665a5044` provenance commit above that the
three profile drafts themselves were read from.
