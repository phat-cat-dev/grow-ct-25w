export const FONT_FAMILIES = ['Inter', 'Roboto', 'Open Sans', 'Lato', 'Montserrat', 'Poppins', 'Source Sans 3', 'Nunito Sans', 'DM Sans', 'Work Sans', 'Merriweather', 'Lora', 'Playfair Display', 'Source Serif 4', 'Roboto Slab', 'IBM Plex Mono'];
export const DEFAULT_CONNECTORS = { headingFont: 'Inter', bodyFont: 'Inter', symbolStyle: 'Outlined', symbolWeight: 400, symbolFill: 0, symbolSize: 32 };

export function connectorAssets(settings = DEFAULT_CONNECTORS) {
  const config = { ...DEFAULT_CONNECTORS, ...settings };
  if (![config.headingFont, config.bodyFont].every(font => FONT_FAMILIES.includes(font)) ||
      !['Outlined', 'Rounded', 'Sharp'].includes(config.symbolStyle) ||
      ![100, 200, 300, 400, 500, 600, 700].includes(config.symbolWeight) ||
      ![0, 1].includes(config.symbolFill) ||
      !Number.isInteger(config.symbolSize) || config.symbolSize < 20 || config.symbolSize > 48) {
    throw new Error('Invalid Google font or symbol settings.');
  }
  const families = [...new Set([config.headingFont, config.bodyFont])];
  const fontsUrl = 'https://fonts.googleapis.com/css2?' +
    families.map(font => 'family=' + encodeURIComponent(font).replaceAll('%20', '+') + ':wght@400;500;600;700').join('&') + '&display=swap';
  const symbolsUrl = 'https://fonts.googleapis.com/css2?family=Material+Symbols+' + config.symbolStyle +
    ':opsz,wght,FILL,GRAD@20..48,100..700,0..1,0&display=block';
  const css = `:root {
  --font-heading: "${config.headingFont}", ${/Serif|Lora|Merriweather|Playfair|Slab/.test(config.headingFont) ? 'serif' : 'sans-serif'};
  --font-body: "${config.bodyFont}", ${/Serif|Lora|Merriweather|Playfair|Slab/.test(config.bodyFont) ? 'serif' : 'sans-serif'};
  --font-ui: var(--font-body);
}
body { font-family: var(--font-body); }
h1, h2, h3, h4, h5, h6 { font-family: var(--font-heading); }
.material-symbol {
  font-family: "Material Symbols ${config.symbolStyle}";
  font-weight: normal;
  font-style: normal;
  font-size: ${config.symbolSize}px;
  line-height: 1;
  display: inline-block;
  letter-spacing: normal;
  text-transform: none;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
  font-feature-settings: "liga";
  -webkit-font-smoothing: antialiased;
  font-variation-settings: 'FILL' ${config.symbolFill}, 'wght' ${config.symbolWeight}, 'GRAD' 0, 'opsz' ${config.symbolSize};
}`;
  return { config, urls: [fontsUrl, symbolsUrl], css };
}

export function connectorImports(urls) {
  return urls.map(url => '@import url("' + url + '");').join('\n') + '\n';
}
