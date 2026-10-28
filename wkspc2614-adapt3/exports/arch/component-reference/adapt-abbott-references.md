# References  (`references`)

- plugin: `adapt-abbott-references` (component)
- targetAttribute: `_references`
- framework: `>=5.19.1`
- used in this course: yes

## Authorable properties

| field | type | req | default | title / help |
|---|---|---|---|---|
| `_component` | string |  | "references" |   |
| `_supportedLayout` | string |  | "full" |   |
| `instruction` | string |  | "" |  Optional instruction text shown above the list. |
| `_items` | array | yes |  |   |
| `title` | string | yes |  |  Display text for the reference. |
| `href` | string | yes |  |  Clickable URL to the resource itself. Always populated with a real link; whether that link is confirmed or still a placeholder is stated separately in _hrefStatus, not encoded in this field. |
| `_hrefStatus` | string | yes |  |  Whether href above is a real, confirmed link or a placeholder awaiting the real one. Replaces the old convention of writing href as a bare '#' to mean 'not confirmed yet' (RF-3, open-decisions.md, superseded in part): href is always a populated value now, and this field carries the confirmation state explicitly instead. |
| `type` | string | yes | "book" |  Free-text category, e.g. 'book' or 'external'. Not a locked enum, add new values as needed. |
| `permalink` | string |  |  |  Optional university library catalogue permalink for the same resource. Independent of href, not a fallback. |

## JSX template(s)

**references.jsx**

```jsx
import React from 'react';
import { templates, compile } from 'core/js/reactHelpers';

export default function References(props) {
  const { _items } = props;
  const items = _items || [];

  return (
    <div className="component__inner references__inner">
      <templates.header {...props} />
      <div className="component__widget references__widget">
        <ul className="references__list">
          {items.map((item, index) => (
            <li key={index} className="references__item">
              <a
                href={item.href}
                className="references__link"
                target="_blank"
                rel="noopener"
              >
                {compile(item.title)}
              </a>
              {item.permalink && (
                <a
                  href={item.permalink}
                  className="references__permalink"
                  target="_blank"
                  rel="noopener"
                >
                  {' '}(permalink)
                </a>
              )}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
```

## Live example (from this course)

```json
{
  "_id": "L01-c-55",
  "_parentId": "L01-b-55",
  "_type": "component",
  "_component": "references",
  "_classes": "",
  "_layout": "full",
  "title": "Lesson Sources",
  "displayTitle": "Lesson Sources",
  "body": "",
  "instruction": "This lesson draws on the following source.",
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_isCompletionIndicatorEnabled": false
  },
  "_items": [
    {
      "title": "See pages 28 to 34 of Chapter 3, 'Defining learning at university', of Excelling at University by Dennis and Abbott (2026).",
      "href": "#",
      "type": "book",
      "permalink": ""
    }
  ]
}
```

## Files a component like this needs

- `bower.json` — name, `component` (the type string used in JSON), `targetAttribute` (the `_config` key), `displayName`, `main` (the JS entry).
- `properties.schema` — JSON Schema (draft-04) of authorable fields; drives the authoring UI and validation.
- `js/<Name>Model.js` + `js/<Name>View.js` + `js/<name>.js` (registers the component with Adapt).
- `templates/<name>.jsx` — the React template (modern Adapt renders components with JSX, not Handlebars).
- `less/<name>.less` — styles (compiled globally; see adapt-ab-theme for the committed-CSS pattern).
