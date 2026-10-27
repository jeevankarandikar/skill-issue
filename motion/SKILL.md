---
name: motion
description: >-
  Make a short motion video for any repo or product with the studio CLI: HTML scenes driven
  by spring physics, captured frame by frame in headless Chrome, stitched with FFmpeg and a
  synthesized score. Use for product teasers, title cards, launch clips, reels, and vertical
  or square cuts of the same scenes. Do not use for interface animation inside an app (use
  design-jeev), for AI-generated footage (use Higgsfield), or for editing existing footage.
version: 0.1.0
user-invocable: true
argument-hint: "[init | scene | gate | review | export]"
---

# Motion

A video here is a folder of plain HTML scenes inside the repo it is about. The `studio` CLI renders it. Nothing is generated at render time, so the same folder gives the same film.

## Before anything

- Check `studio doctor`. If `studio` is missing, the tool is the `studio` repository: clone it, run `npm install`, run `PLAYWRIGHT_BROWSERS_PATH=0 npx playwright install chromium-headless-shell`, then `npm link`. It needs Node 22 and FFmpeg.
- Chromium cannot start inside a macOS app sandbox, and that includes the sandbox most agent shells run in. When `doctor` says the browser is blocked, tell the user and ask for the render to run in their terminal or outside the sandbox. Do not look for another way to render.
- Look for `motion/` or any folder with a `project.json` in the repo. Read its `AGENTS.md` first. It carries the commands and rules for that project and is the more current source than this file.

## Stages

Enter at the stage the request names.

**init.** In the repo, `studio init` makes `./motion` and fills the brand pack from what the repo already holds: a logo, font files, CSS color variables, reference images and screenshots. It reports what it found and what is missing. A missing font or reference image stops the render. Never invent a brand, and never use a logo or screenshot the project does not own.

**scene.** Each scene is one HTML file that sets `window.scene = { render(t, frame, ctx) }`. `t` is seconds, and `ctx` carries `beat`, `beatIndex` and `beatPhase`. Copy the helpers from the project's `scenes/common.js`. The rules `studio lint` enforces:

- Time only comes from `render`. No `Date`, `setTimeout`, `requestAnimationFrame` or `Math.random`.
- All motion is `spring(t - delay, { from, to, k, c, m })` or a preset (`snappy`, `soft`, `bouncy`). No CSS transitions, animations, `@keyframes` or easing curves.
- Scene lengths are beats in `project.json`, so every cut lands on the beat.
- Colors and fonts come from the brand pack as CSS variables. Layouts are left-aligned. No centered all-caps text on a gradient.
- No frame sits still. Use `kick(ctx)` for a spring on every beat and `ambient()` for drift.

Sounds belong next to the visual that causes them: `window.scene.sfx = [{ t, name, gain }]`, using the same delay constants as the visual. One sound per event that matters. A typing field gets `{ name: 'type', dur, cps }`.

**gate.** `studio gate .` renders one still per scene and stops. The user approves scenes with `--approve 0,1`, then a six-frame-a-second animatic is rendered and the user approves that with `--approve-animatic`, and only then does the full film render. An approval is the user's. Record one only when the user has said it in this conversation.

**review.** `studio loop . --first` renders and scores every scene, and `studio loop .` re-renders only the scenes under 8. The score is mechanical: dead frames, motion density, beat alignment and lint. It cannot say whether the film looks good. For that, `studio review . --auto` hands contact sheets, cut strips and peak-motion strips to a fresh model that never sees the scene code, and its score can only lower the mechanical one. `studio review . --mute --auto` shows a judge the film with the sound off and asks what it understood. Do not review scenes you just wrote. Run the reviewer.

**export.** `studio verify .` measures duration, size, loudness against -16 LUFS, true peak, and the first and last frames, and writes a manifest that lists what was measured and what was not. `studio export .` writes a web MP4, WebM, poster and GIF. `studio render . --format vertical` or `square` re-cuts the same scenes.

## Reporting

Report what was measured with the number, and say what was not measured: how the film looks and how the sounds feel are the usual two. Say if the reviewer did not run. A failed render is reported as it failed, with the message.
