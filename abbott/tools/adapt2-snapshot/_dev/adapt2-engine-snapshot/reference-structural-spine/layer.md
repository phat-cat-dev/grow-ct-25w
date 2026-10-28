

## compile order

    
### 1. mandatory — src/core/less/\*_/_.less (always compiled first, never filtered)
### 2. src[0] — src/components/_/less/\*\*/_.less
### 3. src[1] — src/extensions/_/less/\*\*/_.less ← extensions compile here
### 4. src[2] — src/menu/<menu>/\*_/_.less
### 5. src[3] — src/theme/<theme>/\*_/_.less (last — so theme overrides win the cascade)

## layer model

### l1

```
name: adapt-page-template-classes
metadata and frontmatter

```

### l2

```
name: adapt-core-
metadata and frontmatter

```

## note

You're right that the l1 generator misses extensions, and here's why, traced through the actual CSS cascade mechanism (not an import file — there isn't one).

There is no theme.less/adapt.less master file. grunt/tasks/less.js builds a virtual LESS source at build time by globbing five patterns in order and concatenating them as @import lines, then feeding that string straight to the LESS compiler (grunt/tasks/less.js:117).

The order, from grunt/config/less.js:49-59:

1. mandatory — src/core/less/\*_/_.less (always compiled first, never filtered)
2. src[0] — src/components/_/less/\*\*/_.less
3. src[1] — src/extensions/_/less/\*\*/_.less ← extensions compile here
4. src[2] — src/menu/<menu>/\*_/_.less
5. src[3] — src/theme/<theme>/\*_/_.less (last — so theme overrides win the cascade)  


Within each glob, sortLESSFilePaths() (lines 37-43) sorts alphabetically by directory, then — for files in the same folder sharing a name prefix (e.g. button.less / buttonQuestion.less) — shorter name first.

Why l1 misses this: grunt/config/less.js:56 pulls CSS straight from each extension's own less/ folder — there's no templating layer in between for extensions the way there is for components (src/core/templates/partials/component.hbs wrapping every component). The l1 generator (ab-map-structure.js) only reads src/core/templates/_.hbs + src/components/_/templates/_.jsx — i.e. it's reconstructing the  
 component holder contract (.component > .component**inner.<root>**inner), which extensions never pass through. Extensions' CSS selectors come straight from whatever class names their own less/_.less files declare, matched against whatever markup their own (non-component) templates or JS views emit — a completely separate path the generator never visits.

Filtering: which extensions actually make it into a given course's compiled CSS is controlled by includedFilter (grunt/config/less.js:45-47 → grunt/helpers.js:317-353), driven by course.json's build.includes/build.excludes — so even "has a less/ dir" isn't a guarantee it ends up in every course's adapt.css; it also depends on that course's plugin include list.

Extensions with a less/ dir (16 of 22) — these DO emit CSS into phase 3, uncaptured by l1:  
 adapt-ab-{base,close,collapse,dropdown,listgroup,modal,navigation,progress,theme,toast}, adapt-abbott-{resultsdebrief,tooltip}, adapt-contrib-{languagePicker,pageLevelProgress,resources,trickle,tutor}

Extensions with no less/ dir (6 of 22) — contribute nothing to phase 3 regardless: adapt-abbott-pass-reveal, adapt-abbott-reflective-store, adapt-contrib-{assessment,bookmarking,spoor} (spoor is SCORM-only, no visual footprint).

So if you want l1 (or a new layer) to capture extension classes faithfully, the source of truth to scan is each extension's own less/\*.less (selector declarations) cross-referenced against whatever markup actually emits those classes (mixed: some .hbs/.jsx templates, some inline via .js views) — not the component-holder templating path l1 currently walks.
