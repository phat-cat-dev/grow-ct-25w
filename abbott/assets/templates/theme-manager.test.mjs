import test from 'node:test';
import assert from 'node:assert/strict';
import { INITIAL_SCHEME, rgbToColour, sourceForeground, colourText } from '../public/site/components/tools/theme-manager/theme-manager.js';
import { validateScheme, schemeColour, withSchemeColour, createStudioAdapter, schemeHarmony, withSchemeHarmony, randomizeScheme } from '../public/site/components/tools/theme-manager/studio-adapter.js';
import { createNotificationService } from '../public/site/components/tools/notifications/notification-service.js';
import { createNotificationHistory } from '../public/site/components/tools/notifications/notification-history.js';
import { colorSystemCss } from '../public/site/color-system.js';

test('button appearances validate and survive independent colour edits', () => {
  for (const buttonAppearance of ['inverse', 'shaded', 'outline', 'ghost', 'soft']) {
    const config = { ...INITIAL_SCHEME, themeManager: { locked: false, buttonAppearance } };
    const next = withSchemeColour(config, { h: 120, s: 50, l: 40, gs: 12 });
    assert.equal(validateScheme(JSON.parse(JSON.stringify(next))).themeManager.buttonAppearance, buttonAppearance);
  }
  assert.throws(() => validateScheme({ ...INITIAL_SCHEME, themeManager: { locked: true, buttonAppearance: 'unknown' } }));
});

test('randomisation follows all four independent lock combinations', () => {
  for (const locked of [false, true]) {
    for (const harmonyLocked of [false, true]) {
      const config = { ...withSchemeColour(INITIAL_SCHEME, { h: 202, s: 72, l: 42, gs: 12 }), themeManager: { locked, harmonyLocked } };
      if (locked && harmonyLocked) {
        assert.throws(() => randomizeScheme(config, 'light'), /Unlock/);
        continue;
      }
      const next = randomizeScheme(config, 'light', () => .5);
      assert.equal(schemeColour(next).h === schemeColour(config).h, locked);
      assert.equal(schemeHarmony(next).preset === schemeHarmony(config).preset, harmonyLocked);
      if (harmonyLocked) assert.equal(schemeHarmony(next).count, schemeHarmony(config).count);
      assert.deepEqual(next.themeManager, config.themeManager);
    }
  }
});

test('base lock allows harmony edits without changing the selected colour', () => {
  let config = withSchemeHarmony(INITIAL_SCHEME, { preset: 'spectrum', count: 10, select: 9 });
  config.themeManager = { locked: true, harmonyLocked: false };
  const before = schemeColour(config);
  const next = withSchemeHarmony(config, { preset: 'triadic', count: 3 });
  assert.deepEqual(schemeColour(next), before);
  assert.throws(() => withSchemeHarmony(config, { h: 90 }), /Unlock the base/);
  assert.throws(() => withSchemeHarmony(config, { select: 1 }), /Unlock the base/);
});

test('harmony lock freezes preset and count independently of source and swatch selection', () => {
  const config = { ...INITIAL_SCHEME, themeManager: { locked: false, harmonyLocked: true } };
  assert.throws(() => withSchemeHarmony(config, { preset: 'triadic' }), /Unlock the harmony/);
  assert.throws(() => withSchemeHarmony(config, { count: 6 }), /Unlock the harmony/);
  const changed = withSchemeHarmony(config, { h: 120, s: 50, l: 40 });
  assert.equal(schemeHarmony(changed).base.h, 120);
  assert.equal(schemeHarmony(changed).preset, INITIAL_SCHEME.harmony);
  assert.equal(schemeHarmony(changed).count, 4);
  assert.equal(schemeHarmony(withSchemeHarmony(changed, { select: 1 })).selected, 1);
  assert.equal(withSchemeColour(config, { h: 200, s: 60, l: 40, gs: 12 }).themeManager.harmonyLocked, true);
  assert.equal(validateScheme(JSON.parse(JSON.stringify(config))).themeManager.harmonyLocked, true);
  assert.throws(() => validateScheme({ ...config, themeManager: { locked: false, harmonyLocked: 'yes' } }));
});

test('harmony presets and swatches reuse studio palettes and retain the foundation on selection', () => {
  const initial = withSchemeColour(INITIAL_SCHEME, { h: 202, s: 72, l: 42, gs: 12 });
  const triadic = withSchemeHarmony(initial, { preset: 'triadic', count: 4 }, 'light');
  assert.deepEqual(schemeHarmony(triadic).swatches.map(c => c.h), [202, 322, 82, 322]);
  const selected = withSchemeHarmony(triadic, { select: 1 }, 'light');
  assert.equal(schemeColour(selected).h, 322);
  assert.equal(schemeHarmony(selected).base.h, 202);
  assert.equal(schemeHarmony(selected).selected, 1);
  const again = withSchemeHarmony(selected, { select: 2 }, 'light');
  assert.equal(schemeColour(again).h, 82);
  assert.equal(schemeHarmony(again).base.h, 202);
  assert.ok(colorSystemCss(again.colorSystem).includes('--theme-harmony-3'));
  assert.deepEqual(schemeColour(validateScheme(JSON.parse(JSON.stringify(again)))), schemeColour(again));
});

test('harmony controls recompute selected colours and shrinking palettes clamps the selection', () => {
  let config = withSchemeHarmony(INITIAL_SCHEME, { preset: 'spectrum', count: 10 });
  config = withSchemeHarmony(config, { select: 9 });
  config = withSchemeHarmony(config, { count: 3 });
  assert.equal(config.colorSystem.harmonyHue, 3);
  assert.equal(schemeHarmony(config).swatches.length, 3);
  config = withSchemeHarmony(config, { h: 120, s: 60, l: 50 });
  assert.equal(schemeHarmony(config).base.h, 120);
  assert.equal(schemeColour(config).h, 0);
  assert.throws(() => withSchemeHarmony(config, { select: 10 }));
  assert.throws(() => withSchemeHarmony(config, { preset: 'invalid' }));
  assert.throws(() => withSchemeHarmony(config, { count: 2 }));
});

test('every studio harmony preset supports ten swatches and exact accent selection', () => {
  for (const preset of schemeHarmony(INITIAL_SCHEME).presets) {
    const config = withSchemeHarmony(INITIAL_SCHEME, { preset, count: 10 }, 'light');
    const palette = schemeHarmony(config, 'light');
    assert.equal(palette.swatches.length, 10);
    for (const index of [0, 9]) {
      const selected = withSchemeHarmony(config, { select: index }, 'light');
      const actual = schemeColour(selected);
      assert.equal(actual.h, palette.swatches[index].h);
      assert.equal(actual.s, palette.swatches[index].s);
      assert.equal(actual.l, palette.swatches[index].l);
    }
  }
});

test('notification history browses messages and preserves forward entries on new delivery', () => {
  const history = createNotificationHistory();
  assert.equal(history.canBack, false);
  assert.equal(history.canForward, false);
  history.record({ message: 'First', source: 'Theme', level: 'info' });
  history.record({ message: 'Second', source: 'Assets', level: 'error' });
  assert.equal(history.move(-1).message, 'First');
  assert.equal(history.canForward, true);
  assert.equal(history.move(1).level, 'error');
  history.move(-1);
  history.record({ message: 'Third' });
  assert.equal(history.move(-1).message, 'Second');
  assert.equal(history.move(1).message, 'Third');
  assert.equal(history.canForward, false);
  assert.throws(() => history.move(1));
});

test('source colour conversion and foreground handle primary and achromatic colours', () => {
  const red = rgbToColour([255, 0, 0]);
  assert.equal(colourText(red), 'hsl(0 100% 50%)');
  assert.equal(sourceForeground(rgbToColour([255, 255, 255])), '#000');
  assert.equal(sourceForeground(rgbToColour([0, 0, 0])), '#fff');
  assert.equal(rgbToColour([0, 255, 0]).h, 120);
  assert.equal(rgbToColour([0, 0, 255]).h, 240);
  assert.equal(rgbToColour([127, 127, 127]).s, 0);
});

test('scheme validation rejects malformed settings and returns an independent copy', () => {
  const copy = validateScheme(INITIAL_SCHEME);
  copy.overrides['--example'] = '12px';
  assert.deepEqual(INITIAL_SCHEME.overrides, {});
  for (const update of [
    { name: '../bad' }, { name: 123 }, { customCss: {} }, { themeMode: 'sepia' },
    { brandH: Infinity }, { brandS: '72' }, { colorSystem: {} },
    { themeManager: { locked: 'true' } }, { typography: { bodySize: 999 } },
  ]) assert.throws(() => validateScheme({ ...INITIAL_SCHEME, ...update }));
});

test('editing a source preserves unrelated studio settings and uses an exact fixed base', () => {
  const original = { ...INITIAL_SCHEME, customCss: '.card { padding: 2rem; }', overrides: { '--example': '12px' }, futureSetting: { retained: true } };
  const colour = { h: 145, s: 54, l: 36, gs: 9 };
  const next = withSchemeColour(original, colour);
  assert.deepEqual(schemeColour(next), colour);
  assert.equal(next.customCss, original.customCss);
  assert.deepEqual(next.futureSetting, original.futureSetting);
  assert.deepEqual(next.overrides, original.overrides);
  assert.equal(original.colorSystem, undefined);
  assert.equal(next.brandH, 145);
});

test('legacy schemes use existing studio light/dark defaults', () => {
  assert.equal(schemeColour({ ...INITIAL_SCHEME, themeMode: 'light' }).l, 38);
  assert.equal(schemeColour({ ...INITIAL_SCHEME, themeMode: 'dark' }).l, 64);
});

test('workshop accessibility preferences survive scheme colour edits and validation', () => {
  const config = { ...INITIAL_SCHEME, themeMode: 'light', themeManager: { locked: false, appearance: 'contrast', noMotion: true } };
  assert.deepEqual(withSchemeColour(config, { h: 10, s: 30, l: 40, gs: 12 }).themeManager, config.themeManager);
  assert.throws(() => validateScheme({ ...config, themeManager: { locked: true, appearance: 'unknown' } }));
  assert.throws(() => validateScheme({ ...config, themeManager: { locked: true, noMotion: 'yes' } }));
});

test('notification service broadcasts multiple tools, replays latest and unsubscribes', () => {
  const service = createNotificationService();
  const received = [];
  const unsubscribe = service.subscribe(message => received.push(message));
  service.publish({ source: 'Theme', message: 'Loaded' });
  service.publish({ source: 'Assets', message: 'Export failed', level: 'error' });
  assert.equal(received.length, 2);
  assert.equal(received[1].source, 'Assets');
  assert.ok(Object.isFrozen(received[1]));
  unsubscribe();
  service.publish({ message: 'Another tool' });
  assert.equal(received.length, 2);
  const late = [];
  service.subscribe(message => late.push(message));
  assert.equal(late[0].message, 'Another tool');
  assert.throws(() => service.publish({ message: '' }));
  assert.throws(() => service.publish({ message: 'Invalid level', level: 'warning' }));
});

test('studio adapter saves before building and returns actual artifact URLs', async () => {
  const calls = [];
  const adapter = createStudioAdapter({
    fetcher: async (path, options) => {
      calls.push({ path, options });
      return new Response(JSON.stringify({ ok: true }));
    },
  });
  assert.deepEqual(await adapter.build(INITIAL_SCHEME), {
    css: '/dist/workshop-theme/theme.css', tokens: '/dist/workshop-theme/tokens.json',
  });
  assert.deepEqual(calls.map(call => call.path), ['/api/themes/workshop-theme', '/api/build/workshop-theme']);
  assert.deepEqual(JSON.parse(calls[0].options.body), INITIAL_SCHEME);
  assert.equal(calls[0].options.method, 'POST');
  assert.equal(calls[1].options.method, 'POST');
});

test('studio adapter reports HTTP errors and never builds after a failed save', async () => {
  const calls = [];
  const adapter = createStudioAdapter({
    fetcher: async path => { calls.push(path); return new Response('Disk full', { status: 500 }); },
  });
  await assert.rejects(adapter.build(INITIAL_SCHEME), /500.*Disk full/);
  assert.equal(calls.length, 1);
});

test('studio adapter validates list, load and save responses', async () => {
  const badList = createStudioAdapter({ fetcher: async () => new Response('{"not":"a list"}') });
  await assert.rejects(badList.list(), /invalid scheme list/);
  const adapter = createStudioAdapter({ fetcher: async () => new Response('{"ok":false}') });
  await assert.rejects(adapter.save(INITIAL_SCHEME), /did not confirm/);
  await assert.rejects(adapter.load('../bad'), /valid saved scheme/);
  await assert.rejects(adapter.load('valid'), /scheme name/);
});

test('studio adapter supports a base URL and retrieves built CSS without another save', async () => {
  const calls = [];
  const adapter = createStudioAdapter({
    baseUrl: 'http://localhost:5173',
    fetcher: async path => { calls.push(path); return new Response(':root {}'); },
  });
  assert.equal(await adapter.readCss('http://localhost:5173/dist/example/theme.css'), ':root {}');
  assert.deepEqual(calls, ['http://localhost:5173/dist/example/theme.css']);
});
