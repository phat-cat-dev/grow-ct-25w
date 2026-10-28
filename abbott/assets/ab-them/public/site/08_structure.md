# Adapt structure

## 1.0 Content model and rendering

<div class="card-doc">
  <p class="note">A structural specimen based on the local Adapt Theming Kit, not an embedded Adapt runtime. It shows the kit's page/menu hierarchy and documented BEM hooks using the studio's current colours, fonts, spacing and corners. Completion and layout classes below are illustrative, not learner tracking.</p>
  <pre>Course
└─ Content Object
   ├─ Menu → links to pages or other menus
   └─ Page
      └─ Article
         └─ Block
            └─ Component (text, graphic, question, ...)</pre>
  <p class="note">JSON describes the content. Views generate the outer wrapper, ID, author-supplied <code>_classes</code>, layout and state classes. Templates generate inner wrappers and headers; menu and component plugins own their widget markup. A menu is a sibling content object, not a wrapper around the rendered page.</p>
</div>

## 2.0 Menu and page specimen

<div class="adapt-specimen">
  <nav class="adapt-specimen-nav" aria-label="Adapt specimen navigation"><a href="#structure-demo-course-menu">Course menu</a><a href="#structure-demo-learning-page">Learning page</a><a href="#structure-demo-layout-block">Two-column block</a></nav>
  <div class="menu contentobject boxmenu" id="course-menu" data-adapt-id="studio-menu">
    <div class="menu__inner boxmenu__inner">
      <div class="menu__header"><div class="menu__header-inner">
        <p class="adapt-hook">Menu / content object · .menu__inner.boxmenu__inner</p>
        <h4 class="menu__title"><span class="menu__title-inner">A course built in layers</span></h4>
        <div class="menu__body"><div class="menu__body-inner">Menu items link to content objects. This miniature menu uses links into the specimen below.</div></div>
      </div></div>
      <div class="menu__item-container">
        <a class="adapt-menu-item" href="#structure-demo-learning-page"><span class="material-symbol" aria-hidden="true">auto_stories</span><strong>Explore the learning page</strong><span>Page → article → block → component</span></a>
        <a class="adapt-menu-item" href="#structure-demo-reflection-article"><span class="material-symbol" aria-hidden="true">school</span><strong>Reflect and continue</strong><span>A second article with an authoring modifier</span></a>
      </div>
    </div>
  </div>
  <div class="page contentobject" id="learning-page" data-adapt-id="studio-page">
    <div class="page__inner">
      <div class="page__header"><div class="page__header-inner">
        <p class="adapt-hook">Page / content object · .page__inner</p>
        <h4 class="page__title"><span class="page__title-inner">Learning happens inside the page</span></h4>
        <div class="page__body"><div class="page__body-inner">An outer page holds its header and an article container. Full-width bands belong on outer wrappers; constrained padding, cards and radius belong on inner wrappers.</div></div>
        <div class="page__instruction"><div class="page__instruction-inner">Follow the labelled layers to inspect their nesting.</div></div>
      </div></div>
      <div class="article__container">
        <div class="article" id="explore-article" data-adapt-id="studio-article-1">
          <div class="article__inner">
            <div class="article__header"><div class="article__header-inner">
              <p class="adapt-hook">Article · .article__inner</p>
              <h4 class="article__title"><span class="article__title-inner">1. Explore the structure</span></h4>
              <div class="article__body"><div class="article__body-inner">An article groups blocks and has the most vertical breathing room.</div></div>
            </div></div>
            <div class="block__container">
              <div class="block" id="layout-block" data-adapt-id="studio-block-1">
                <div class="block__inner">
                  <div class="block__header"><div class="block__header-inner">
                    <p class="adapt-hook">Block · .block__inner</p>
                    <h5 class="block__title"><span class="block__title-inner">One row, two components</span></h5>
                    <div class="block__instruction"><div class="block__instruction-inner">The header stays above .component__container; columns wrap inside that container.</div></div>
                  </div></div>
                  <div class="component__container">
                    <div class="component text is-left is-complete" data-adapt-id="studio-component-1">
                      <div class="component__inner text__inner">
                        <div class="component__header text__header">
                          <p class="adapt-hook">Component · .component.text.is-left</p>
                          <h6 class="component__title"><span class="component__title-inner">Text component</span></h6>
                          <div class="component__body"><div class="component__body-inner"><p>The generic .component__inner hook styles all components; .text__inner provides plugin-specific control.</p><p class="adapt-state">.is-complete · example state only</p></div></div>
                        </div>
                      </div>
                    </div>
                    <div class="component graphic is-right" data-adapt-id="studio-component-2">
                      <div class="component__inner graphic__inner">
                        <div class="component__header graphic__header">
                          <p class="adapt-hook">Component · .component.graphic.is-right</p>
                          <h6 class="component__title"><span class="component__title-inner">Graphic component</span></h6>
                          <div class="component__body"><div class="component__body-inner">The plugin supplies the display/widget region, not the JSON schema.</div></div>
                        </div>
                        <div class="component__widget graphic__widget"><div class="adapt-graphic" role="img" aria-label="Three nested layers representing article, block and component"><span>Article</span><span>Block</span><span>Component</span></div></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="article bg-tint" id="reflection-article" data-adapt-id="studio-article-2">
          <div class="article__inner">
            <div class="article__header"><div class="article__header-inner">
              <p class="adapt-hook">Article · author _classes: "bg-tint"</p>
              <h4 class="article__title"><span class="article__title-inner">2. Reflect and continue</span></h4>
              <div class="article__body"><div class="article__body-inner">A second article shows outer banding without changing its content structure.</div></div>
            </div></div>
            <div class="block__container"><div class="block" data-adapt-id="studio-block-2"><div class="block__inner">
              <div class="component__container">
                <div class="component text is-full is-raised" data-adapt-id="studio-component-3">
                  <div class="component__inner text__inner">
                    <div class="component__header text__header">
                      <p class="adapt-hook">.component.text.is-full · author _classes: "is-raised"</p>
                      <h6 class="component__title"><span class="component__title-inner">One full-width component</span></h6>
                      <div class="component__body"><div class="component__body-inner"><p>Unequal article, block and component spacing creates hierarchy before shadows. The full-width component stays full-width; the two-column row above stacks when space runs out.</p></div></div>
                    </div>
                  </div>
                </div>
              </div>
            </div></div></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

## 3.0 Theme imports and studio output mapping

<div class="card-doc">
  <p class="note">Current kit: two standalone starter files, not an explicit import manifest. Its README recommends zzz-fluid-baseline.less as the only owner of type/layout and zzz-overrides.less for colour, surfaces, depth and dark mode. Both files currently contain typography/layout rules, so importing both unchanged creates competing ownership. Confirm the installed Adapt/Vanilla version and actual Grunt import order before integrating; a zzz filename is an ordering convention, not proof of precedence.</p>
  <div class="adapt-table-wrap"><table class="adapt-mapping">
    <caption>Proposed Adapt package mapping — not a new export format yet</caption>
    <thead><tr><th>Import layer</th><th>Studio source</th><th>Adapt destination / constraint</th></tr></thead>
    <tbody>
      <tr><td>00 ingredients / tokens</td><td>Colour source, brand, harmony and semantic settings</td><td>Root custom properties, with explicit aliases to the installed theme's colour variables. Keep semantic meaning hues and light/dark swaps.</td></tr>
      <tr><td>10 fonts / typography</td><td>Font connectors and typography generator</td><td>Heading/body families, size formulas and component title hooks. Include external font CSS before other CSS, or package fonts locally.</td></tr>
      <tr><td>20 fluid rhythm</td><td>Spacing generator and fluid core</td><td>One owner of article/block/component spacing. Bind larger steps to article inners, medium steps to block inners and smaller gaps to component containers.</td></tr>
      <tr><td>30 structure / surfaces</td><td>Layout radius and a future Adapt adapter</td><td>Translate tokens onto .page__inner, .article__inner, .block__inner and .component__inner. Do not copy .ab.card selectors and expect Adapt markup to match.</td></tr>
      <tr><td>40 components / states</td><td>Cards, semantic appearance, icons and opt-in motion</td><td>Map to generic + plugin-specific BEM hooks and existing state classes. Preserve plugin interaction, focus, accessibility and reduced-motion behaviour.</td></tr>
      <tr><td>90 author overrides</td><td>Custom CSS and documented _classes vocabulary</td><td>Scoped opt-ins last. Validate author classes separately; do not silently reinterpret framework states.</td></tr>
    </tbody>
  </table></div>
  <p class="note">Illustrative LESS entry point for a future package; these generated filenames do not exist yet:</p>
  <pre>@import (less) "generated/00-tokens.css";
@import (less) "generated/10-typography.css";
@import (less) "generated/20-fluid.css";
@import "adapt/30-structure.less";
@import "adapt/40-components.less";
@import (less) "author/90-overrides.css";</pre>
  <p class="note">LESS <code>@import (less)</code> inlines CSS into the build; a plain CSS import can remain a browser request. Generated CSS must stay valid LESS input. Register one entry point in the installed build and keep partials outside any auto-import glob to avoid duplicate output. If a LESS variable is bridged to <code>var(--token)</code>, use it only in CSS declarations: LESS colour functions and compile-time arithmetic cannot evaluate runtime custom properties.</p>
  <pre>:root { --adapt-block-gap: var(--ab-space-item-margin); }
@block-gap: ~"var(--adapt-block-gap)";
.component__container { gap: @block-gap; }</pre>
  <p class="note">Current studio exports remain a complete single CSS bundle plus scheme JSON. CLI/API output composes the base template, ingredient overrides, connectors, colour, typography, spacing, layout, cards and custom CSS; external connector imports go first. Browser export uses the same domain generators. An Adapt-specific split export would extract domain outputs instead of importing that full bundle, then add adapters for BEM selectors and LESS-only defaults. Do not wrap existing unlayered overrides in CSS layers without deciding precedence against Vanilla.</p>
</div>

## 4.0 Review notes and integration boundary

<div class="card-doc">
  <ul>
    <li>The local generator reference is more precise than the older guide: raw component classes such as <code>.text</code>, not <code>.text-component</code>; plugin templates supply dual-BEM inners.</li>
    <li>The fluid starter flexes <code>.block__inner &gt; .component</code>, but the documented templates put components inside <code>.component__container</code>. This specimen uses the actual container and keeps the block header out of the column grid.</li>
    <li>The kit's illustrative bridge example assigns a surface token to padding. Bridge dimension tokens to padding and colour tokens to backgrounds instead.</li>
    <li>Use inner wrappers for constrained surfaces and padding, outer wrappers for bands; preserve full/left/right layout and runtime state semantics.</li>
    <li>This is a scoped structural preview, not a pixel-perfect Vanilla reproduction, plugin implementation or proof of compatibility with an installed Adapt build. No Adapt source/templates/build configuration are included in the kit.</li>
  </ul>
  <p class="note">Local sources reviewed: adapt-theming-kit/README.md, adapt-structure-generators.md, adapt-theming-guide.md, zzz-fluid-baseline.less and zzz-overrides.less. The generator notes cite core v6.85.1 and text v6.3.0; upstream versions have not been reverified here.</p>
</div>