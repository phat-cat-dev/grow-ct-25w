# Tooltip  (`abbottTooltip`)

- plugin: `adapt-abbott-tooltip` (extension)
- targetAttribute: `(n/a)`
- framework: `>=5.19.1`
- used in this course: no

## Authorable properties

_properties.schema not present in this checkout (contrib plugin — fetched at `adapt install`)._

## JSX template(s)

_No template in this checkout (contrib plugin templates arrive at `adapt install`)._

## Live example (from this course)

_No instance of this component in the sampled course._

## Files a component like this needs

- `bower.json` — name, `component` (the type string used in JSON), `targetAttribute` (the `_config` key), `displayName`, `main` (the JS entry).
- `properties.schema` — JSON Schema (draft-04) of authorable fields; drives the authoring UI and validation.
- `js/<Name>Model.js` + `js/<Name>View.js` + `js/<name>.js` (registers the component with Adapt).
- `templates/<name>.jsx` — the React template (modern Adapt renders components with JSX, not Handlebars).
- `less/<name>.less` — styles (compiled globally; see adapt-ab-theme for the committed-CSS pattern).
