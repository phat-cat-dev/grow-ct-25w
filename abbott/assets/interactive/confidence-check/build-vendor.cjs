const fs = require('node:fs');
const path = require('node:path');
const root = __dirname;
fs.mkdirSync(path.join(root, 'vendor'), { recursive: true });
fs.copyFileSync(path.join(root, 'node_modules', 'chart.js', 'dist', 'chart.umd.min.js'), path.join(root, 'vendor', 'chart.umd.min.js'));
fs.copyFileSync(path.join(root, 'node_modules', 'chart.js', 'LICENSE.md'), path.join(root, 'vendor', 'Chart-LICENSE.md'));
console.log('Copied pinned Chart.js UMD build and licence for offline use.');
