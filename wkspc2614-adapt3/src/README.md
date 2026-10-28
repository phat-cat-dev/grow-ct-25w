# Converted Adapt Components

This directory contains your vanilla JavaScript components automatically converted into standard Adapt Framework component structure.

---

## Folder Structure

Each component is packaged as an independent Adapt plugin:
```text
adapt-contrib-[component-name]/
├── bower.json                 # Package descriptor for Adapt CLI installation
├── properties.json            # Default content configuration values
├── [component-name].schema    # JSON schema defining authoring fields
├── templates/
│   └── [component-name].hbs   # Handlebars HTML template
└── js/
    └── [component-name].js    # Backbone Model and View logic
```

---

## How the Adapt Architecture Works

Adapt uses a Model-View-Template architectural pattern separated from configuration schemas:

1. **The Schema (`[name].schema`)**: 
   * **What it does:** Defines the shape, data types (e.g., strings, arrays, objects), and structure of the component's authoring configuration.
   * **Relation to Data:** Every property defined here maps directly to fields editable by course authors in `properties.json` and the Adapt Authoring Tool.

2. **The Handlebars Template (`templates/[name].hbs`)**: 
   * **What it does:** Acts as the base HTML rendering template. It contains structural markup placeholders.
   * **Relation to Data:** It uses expressions like `{{title}}`, `{{instruction}}`, or block helpers like `{{#each items}}` to dynamically render data supplied by the model.

3. **The View & Model (`js/[name].js`)**: 
   * **What it does:** Manages component lifecycle states (`initialize`, `postRender`), user interactions (clicks, input changes, drag-and-drop), and grading/completion reporting.
   * **Relation to Framework:** It extends Adapt's core `ComponentView` and `ComponentModel` classes.

---

## Migration & Development Tips

* **Migrating Vanilla Logic:** 
  The generated view file contains the baseline skeleton. To bring over full functionality from your original vanilla `.js` files:
  * Move native DOM queries from `element.querySelectorAll(...)` to jQuery selectors using `this.$el.find(...)`.
  * Bind event listeners in the `events` hash or inside `postRender()`.
  * Map your scoring logic to update the model using `this.model.set({ score: x, isComplete: true })` and call `this.setCompletion()`.

* **Testing Locally:**
  Drop any of the generated `adapt-contrib-*` folders directly into your Adapt course's `src/components/` directory, or install them via the Adapt CLI using:
  ```bash
  adapt install ./adapt-output-plugins/adapt-contrib-[component-name]
  ```
