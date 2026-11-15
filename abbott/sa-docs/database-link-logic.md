# Database link logic

How each citation database's per-chapter deep link is structured, and how
much of that structure can be derived rather than pasted by hand. Source
data lives in `tools/compile-references.js` (`CHAPTER_SECTIONS`,
`CHAPTER_METSEARCH`, `EBSCO_READER`, `chapterHref()`) and the redirect
page's config block (`redirect/redirects-excelling.html`).

## EBSCO

Every EBSCO chapter link produced by `chapterHref()` has the same shape:

```
https://research.ebsco.com/c/{customer}/ebook-viewer/pdf/{recordId}/section/lp_{N}
```

Two of those four parts are **book-level constants** - fixed once per book,
identical across all 14 chapter links:

- `{customer}` - `5swjy4`. Cardiff Met's EBSCO tenant/customer id. The same
  for every EBSCO reader link this institution has, for any book, not just
  this one.
- `{recordId}` - `jh27fa6lnj`. This specific title's record id inside
  EBSCO's catalogue (*Excelling at University*, 2026 digital edition). A
  different book would have a different `recordId`, but still the same
  `customer`.

The only part that varies **per chapter** is the trailing `lp_{N}` - a
"logical page" / section index into the underlying PDF, as EBSCO's own
reader numbers it. This is exactly the one number pasted in by hand for each
row of `CHAPTER_SECTIONS`:

```js
const CHAPTER_SECTIONS = {
  1: 'lp_1',  2: 'lp_9',   3: 'lp_27',  4: 'lp_44',  5: 'lp_59',
  6: 'lp_75', 7: 'lp_95',  8: 'lp_113', 9: 'lp_135', 10: 'lp_184',
  11: 'lp_200', 12: 'lp_220', 13: 'lp_231', 14: 'lp_246'
};
```

### How every `lp_N` can be derived from one offset

`lp_N` is not an arbitrary id - it tracks the chapter's **start page in the
print book**, offset by a constant. Cross-checking all 14 values against
each chapter's printed start page (recovered from the Primo CDI id's
`_<seq>_<page>` tail, see `canon-old/cite/*-chapter.record.json`'s
`unresolved` notes, and mirrored in `CHAPTER_METSEARCH`'s permalink suffixes)
gives:

| Chapter | `lp_N` | Print start page | Offset (page − N) |
|---|---|---|---|
| 1  | lp_1   | 16  | 15 |
| 2  | lp_9   | 24  | 15 |
| 3  | lp_27  | 42  | 15 |
| 4  | lp_44  | 59  | 15 |
| 5  | lp_59  | 74  | 15 |
| 6  | lp_75  | 90  | 15 |
| 7  | lp_95  | 110 | 15 |
| 8  | lp_113 | 128 | 15 |
| 9  | lp_135 | 150 | 15 |
| 10 | lp_184 | 199 | 15 |
| 11 | lp_200 | 215 | 15 |
| 12 | lp_220 | 235 | 15 |
| 13 | lp_231 | 246 | 15 |
| 14 | lp_246 | 261 | 15 |

The offset is **exactly 15 for every chapter, with zero variance**. That
15 is almost certainly the count of front-matter pages in the PDF before
Chapter 1's first page (half-title, title page, copyright, series page,
table of contents, etc.) - EBSCO's `lp_` counter starts at page 1 of the
PDF file itself, while the book's own printed page numbers only start once
the front matter ends.

So, given:

- `lp_1 = 1` (Chapter 1's own section id, the one fixed starting point), and
- that chapter's print start page = 16,

every other chapter's `lp_N` reduces to one arithmetic step:

```
lp_N  =  chapter's print start page  −  15
```

In other words, the entire 14-row `CHAPTER_SECTIONS` table can be
regenerated from a single known pair (`lp_1` ↔ print page 16) plus each
chapter's print start page - which is exactly the number already sitting in
the table of contents / `CHAPTER_METSEARCH` permalink suffixes - instead of
opening the EBSCO reader and copying each section id out by hand.

**Caveat:** this offset is an empirical fit confirmed against this one
book's current EBSCO upload (14/14 exact matches), not a documented EBSCO
rule. It holds only as long as EBSCO doesn't re-paginate or re-upload this
title with a different front-matter length. If a chapter's EBSCO link ever
404s, re-verify the offset against the reader directly rather than assuming
it still holds.

## MetSearch

Every MetSearch permalink (`CHAPTER_METSEARCH`, not yet wired into
`chapterHref()`) has the same shape:

```
https://metsearch.cardiffmet.ac.uk/permalink/{networkInst}/{vid}/{recordKey}
```

e.g. for Chapter 1:

```
https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_11_16
```

Three parts are **institution/book-level constants**, identical across all
14 permalinks:

- `{networkInst}` - `44WHELF_CMU`. An Alma/Primo Network Zone code: `WHELF`
  is the Wales Higher Education Libraries Forum, the shared library
  consortium Cardiff Met's Alma/Primo instance runs inside; `CMU` is Cardiff
  Met's own short code within that shared network. Institution-level - the
  same for any MetSearch permalink Cardiff Met issues, for any book.
- `{vid}` - `1kul06t`. The Primo "view id" - the specific discovery-layer
  view configuration Ex Libris assigned Cardiff Met. Also institution-level,
  not book- or chapter-specific.
- `cdi_proquest_ebookcentralchapters_32353950` (the first two underscore-
  joined segments of `{recordKey}`) - `cdi_proquest_ebookcentralchapters` is
  a fixed scheme prefix meaning "a ProQuest Ebook Central chapter record
  inside Ex Libris's Central Discovery Index"; `32353950` is ProQuest Ebook
  Central's own id for *this* book. Book-level - the same for all 14
  chapters of this title, but different for a different book.

The only parts that vary **per chapter** are the last two underscore-joined
numbers in `{recordKey}` - `..._{seq}_{page}`:

```js
const CHAPTER_METSEARCH = {
  1:  '...chapters_32353950_11_16',   2:  '...chapters_32353950_12_24',
  3:  '...chapters_32353950_13_42',   4:  '...chapters_32353950_14_59',
  5:  '...chapters_32353950_15_74',   6:  '...chapters_32353950_16_90',
  7:  '...chapters_32353950_17_110',  8:  '...chapters_32353950_18_128',
  9:  '...chapters_32353950_19_150',  10: '...chapters_32353950_20_199',
  11: '...chapters_32353950_21_215',  12: '...chapters_32353950_22_235',
  13: '...chapters_32353950_23_246',  14: '...chapters_32353950_24_261'
};
```

### How every `_{seq}_{page}` pair can be derived

`{page}` is the exact same **print start page** used in the EBSCO section
above (no offset at all - MetSearch's trailing number *is* the print page
number). `{seq}` tracks the chapter's own position in this book's full
table-of-contents sequence, which includes front-matter entries (half-title,
series page, contents, etc.) ahead of Chapter 1. Cross-checking all 14
values:

| Chapter | `seq` | `page` | `seq − chapter` |
|---|---|---|---|
| 1  | 11 | 16  | 10 |
| 2  | 12 | 24  | 10 |
| 3  | 13 | 42  | 10 |
| 4  | 14 | 59  | 10 |
| 5  | 15 | 74  | 10 |
| 6  | 16 | 90  | 10 |
| 7  | 17 | 110 | 10 |
| 8  | 18 | 128 | 10 |
| 9  | 19 | 150 | 10 |
| 10 | 20 | 199 | 10 |
| 11 | 21 | 215 | 10 |
| 12 | 22 | 235 | 10 |
| 13 | 23 | 246 | 10 |
| 14 | 24 | 261 | 10 |

`seq − chapter` is **exactly 10 for every chapter, with zero variance** -
i.e. 10 table-of-contents entries (front matter) precede Chapter 1's own
entry at position 11. So the whole 14-row `CHAPTER_METSEARCH` table reduces
to one arithmetic step per chapter, given only the chapter number and its
print start page:

```
seq   =  chapter number  +  10
page  =  chapter's print start page   (same value as the EBSCO section)
```

**Caveat:** unlike the EBSCO offset, this `seq`/`page` split is explicitly
flagged in canon as an *inference*, not a documented Ex Libris/CDI format
(`canon-old/cite/*-chapter.record.json`'s `unresolved` notes: "looks like a
sequence position and a start page... but that format is undocumented").
The arithmetic above fits all 14 known data points exactly, but treat it the
same way as the EBSCO offset - re-verify against a live MetSearch search
rather than assuming it still holds if a permalink ever changes shape.
