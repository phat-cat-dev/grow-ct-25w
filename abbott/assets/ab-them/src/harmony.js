// harmony.js — the single source of truth for colour-theory presets.
// Each preset is just three HUE-ANGLE OFFSETS from the brand hue:
//   [ offset for --hue-2, offset for --hue-3, offset for --hue-4 ]
// Hue is circular and hsl() wraps past 360, so no modulo maths is needed in
// CSS; wrap() below is only for pretty-printing degrees in a UI.

export const HARMONY = {
  monochrome:    [0, 0, 0],
  complementary: [180, 180, 180],
  analogous:     [30, -30, 60],
  triadic:       [120, 240, 120],
  split:         [150, 210, 180],   // split-complementary
  tetradic:      [60, 180, 240],
  square:        [90, 180, 270],
};

export const HARMONY_NAMES = Object.keys(HARMONY);

export const wrap = (h) => ((h % 360) + 360) % 360;
