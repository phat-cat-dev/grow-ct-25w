# media — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec)
**Verified against:** `src/components/adapt-contrib-media/properties.schema` (Adapt 5.56.2)
**Grounded in:** `c-135` — Adapt demo scaffold instance (`courses/academic-writing-introductory`). **No authored lesson instance exists yet** (no L0x-prefixed media component in the pilot). The worked example below is therefore illustrative of the schema shape, not an authored voice model; treat it with caution until a real instance is built.
**Relationship to other documents:** references the Voice Specification and the Tier Specification; restates none. This is the audio/video container.

---

## 1. Purpose & when to reach for it

Routing is decided upstream in **Mapping Artefact Part 4**. Media is the **audio/video player**: the standard component for embedding video or audio with playback controls.

Component-specific "reach for it / don't":

- **Reach for media** for any video or audio that the learner plays: explainer videos, recorded lectures, audio explanations, demonstrations.
- **Reach for media** when the teaching move genuinely requires rich media — not as a default.
- **Don't use media as a substitute for text.** If the content can be effectively delivered as prose, use `text`. Video is high-friction (requires sound, takes time, can't be skimmed).
- **Don't embed external YouTube/Vimeo without checking accessibility.** If using external sources, ensure captions are available.

Media is a heavier component than text or graphic. Use it when the medium genuinely adds value — demonstrations, tone of voice, visual processes — not just to "make it more engaging".

---

## 2. The annotated JSON shape

**[LB]** marks a load-bearing field.

```jsonc
{
  "_id": "c-135",
  "_parentId": "b-125",
  "_type": "component",
  "_component": "media",
  "_classes": "",
  "_layout": "full",                      // "full" | "left" | "right"

  "title": "Media",                       // internal / tracking
  "displayTitle": "",                     // learner-facing heading
  "body": "<p>Watch this video to see the process in action.</p>", // introductory prose
  "instruction": "Select the play button to start the video.", // [LB] §15.4

  "_media": {                             // [LB] the media source
    "mp4": "course/en/video/example.mp4", // local MP4 file
    "ogv": "",                            // optional OGV fallback
    "webm": "",                           // optional WEBM fallback
    "mp3": "",                            // for audio-only
    "source": "",                         // external URL (YouTube, Vimeo)
    "type": "",                           // "video/youtube" | "video/vimeo" if external
    "poster": "course/en/video/poster.jpg", // [LB] thumbnail image before play
    "cc": [                               // [LB] closed captions
      {
        "srclang": "en",
        "src": "course/en/video/example.vtt"
      }
    ]
  },

  "_setCompletionOn": "play",             // [LB] "inview" | "play" | "ended"
  "_useClosedCaptions": true,             // [LB] enable captions UI
  "_startLanguage": "en",                 // default caption language
  "_showVolumeControl": true,             // show volume slider (desktop only)
  "_startVolume": "80%",                  // default volume
  "_allowFullScreen": true,               // allow fullscreen mode
  "_aspectRatio": "landscape",            // "landscape" | "portrait" | "square"
  "_pauseWhenOffScreen": false,           // auto-pause when scrolled away
  "_playsinline": false,                  // iOS inline playback
  "_preventForwardScrubbing": false,      // prevent skipping ahead
  "_offsetMediaControls": false,          // move controls below video

  "_transcript": {                        // [LB] transcript options
    "_setCompletionOnView": true,         // viewing transcript can trigger completion
    "_inlineTranscript": true,            // show transcript toggle below video
    "_externalTranscript": false,         // show link to external transcript file
    "inlineTranscriptButton": "Transcript",
    "inlineTranscriptCloseButton": "Close Transcript",
    "inlineTranscriptBody": "Full transcript text goes here…", // [LB] the transcript
    "transcriptLinkButton": "Transcript",
    "transcriptLink": ""                  // path to external transcript file
  },

  "_playerOptions": {},                   // advanced MediaElement.js options

  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

Global aria strings (`ariaRegion`, `playText`, `pauseText`, `tracksText`, etc.) inherit from `course.json` `_globals`; leave defaults unless overriding.

---

## 3. Authoring guardrails (hard rules)

1. **Every video must have captions.** Populate `_media.cc` with a VTT file for accessibility. Set `_useClosedCaptions: true`.
2. **Every video should have a transcript.** Use `_transcript._inlineTranscript: true` and populate `inlineTranscriptBody`. This is essential for deaf learners and useful for all learners who want to skim or search.
3. **Always provide a poster image.** `_media.poster` shows before playback; a blank poster is poor UX.
4. **Choose `_setCompletionOn` deliberately.**
   - `"play"` — component completes when learner starts playback (most common for optional video).
   - `"ended"` — component completes only when video finishes (use for required viewing).
   - `"inview"` — completes on scroll-in (use sparingly; doesn't require engagement).
5. **Avoid `_preventForwardScrubbing` unless genuinely required.** Blocking skip-ahead frustrates learners and is rarely pedagogically justified.
6. **For external sources (YouTube, Vimeo), set `source` and `type`.** But prefer self-hosted video where possible for SCORM offline packaging.

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `body` | Introductory prose | §15.1 |
| `displayTitle` | Heading (if used) | §5 |
| `instruction` | Activity instruction | §15.4 |
| `_transcript.inlineTranscriptBody` | Full transcript; written prose | §15.1 (or §15.6 if technical) |

Video/audio content itself should follow programme voice (§7 tone, §6 address) — but that's a production matter, not a JSON schema matter.

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

Media carries no assessment dimension. Tier affects **content complexity and vocabulary** in the video/audio itself and in any transcript. Register for `body` and transcript follows **Voice Spec §16**.

---

## 6. Accessibility requirements

- **Captions are mandatory.** Provide a VTT file in `_media.cc`. Enable `_useClosedCaptions`.
- **Transcript is strongly recommended.** `_transcript._inlineTranscript: true` with full `inlineTranscriptBody`.
- **`poster` image should have context.** Although the poster itself doesn't take alt text in the schema, the component's `body` should orient the learner to what they'll see.
- **Volume control.** Not available on mobile (OS-level); desktop volume starts at `_startVolume`.
- **Global aria strings** (`playText`, `pauseText`, etc.) default sensibly; override if needed for clarity.

---

## 7. Known gotchas & findings

- **Mobile playback differences.** Mobile devices often use native players; some options (volume control, inline playback) are ignored.
- **YouTube/Vimeo embed limitations.** External embeds may not work offline in SCORM packages. Prefer self-hosted video.
- **`_setCompletionOn: "ended"` can frustrate.** If the learner watches 90% and closes, they may lose completion. Consider `"play"` for lower-stakes video.
- **File sizes.** Video is heavy. Optimise for web delivery; consider 720p maximum for e-learning.
- **Demo scaffold only in pilot.** `c-135` is Adapt demo content. The first real authored media must provide proper captions and transcript.

---

## 8. Worked example

**Note:** No authored lesson instance exists yet. The example below is from the Adapt demo scaffold (`c-135`), reproduced to show schema shape. It is **ILLUSTRATIVE**, not a voice model.

```json
{
  "_id": "c-135",
  "_parentId": "b-125",
  "_type": "component",
  "_component": "media",
  "_classes": "",
  "_layout": "full",
  "title": "Media",
  "displayTitle": "Media",
  "body": "Sometimes we need to make use of rich media to really drive home a point, bring a complex subject to life or simply use audio to literally do the talking. This is when the <b>Media</b> component comes to the fore.<br><br>Component can be either single or spanned.",
  "instruction": "Select the play button to start the video.",
  "_setCompletionOn": "play",
  "_useClosedCaptions": true,
  "_allowFullScreen": true,
  "_pauseWhenOffScreen": false,
  "_playsinline": false,
  "_preventForwardScrubbing": false,
  "_startLanguage": "en",
  "_showVolumeControl": true,
  "_startVolume": "80%",
  "_aspectRatio": "landscape",
  "_offsetMediaControls": false,
  "_media": {
    "mp4": "course/en/video/c-40.mp4",
    "poster": "course/en/video/c-40.jpg",
    "cc": [
      {
        "srclang": "en",
        "src": "course/en/video/c-40.vtt"
      }
    ]
  },
  "_transcript": {
    "_setCompletionOnView": true,
    "_inlineTranscript": true,
    "_externalTranscript": false,
    "inlineTranscriptButton": "Transcript",
    "inlineTranscriptCloseButton": "Close Transcript",
    "inlineTranscriptBody": "Responsive design means you can create a course once but view it on a wide range of browsers, devices or operating systems. This is achieved by using fluid layouts to ensure the presentation of content is tailored to suit the size of the screen. This means you can start a course on your laptop and finish it later on your mobile or tablet. We call it Adapt",
    "transcriptLinkButton": "Transcript",
    "transcriptLink": ""
  },
  "_playerOptions": {
    "alwaysShowControls": true,
    "toggleCaptionsButtonWhenOnlyOne": true,
    "iPadUseNativeControls": true,
    "iPhoneUseNativeControls": true,
    "AndroidUseNativeControls": true,
    "features": ["playpause", "current", "progress", "duration", "tracks", "volume", "fullscreen"]
  },
  "_pageLevelProgress": { "_isEnabled": true, "_isCompletionIndicatorEnabled": true }
}
```

**Positive features (demo scaffold does some things right):**

- Captions provided (`cc` array with VTT file).
- Inline transcript enabled with `inlineTranscriptBody` populated.
- Poster image provided.

**Gaps vs programme spec:**

- `body` text is generic demo content, not programme voice.
- Transcript is demo text, not programme content.
- The first authored media must follow Voice Spec for all copy.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **media** component. Register and content-type voice live in the **Voice Specification**; accessibility requirements are grounded in **§14**; tier register lives in the **Tier Specification** and **§16**; teaching-move routing lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of media authoring spec — v0.1 (illustrative example — no authored instance yet).*
