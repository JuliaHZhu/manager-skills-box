---
name: qq-sticker-maker
description: Guide users through designing and producing animated stickers (APNG/WebP) for QQ and similar platforms, featuring scene + Emoji character composition. Use when the user wants to make QQ动态表情包, animated stickers, APNG表情包, 超级表情, or asks about producing scene-based memes with Emoji faces in vehicles, boats, or other illustrated environments. Also triggers on questions about APNG/WebP animation production, frame-by-frame sticker design, or optimizing animated images for messaging platforms.
---

# QQ Sticker Maker

## Overview

Guide users through the full pipeline of producing animated stickers: concept → layered assets → animation → export → compress → upload.

The signature style: illustrated scene + standard Emoji characters composited into windows, seats, or cockpits, with subtle looping animation (bob, sway, blink, drum).

## Workflow Decision Tree

```
User wants a sticker
    ├── Has a concrete idea? ──→ Yes → Step 1: Concept Design
    │                           └── No  → Brainstorm scene + Emoji combos
    │
    ├── Has static assets? ────→ Yes → Step 2: Asset Layering
    │                           └── No  → Guide asset creation (AI / draw / source)
    │
    ├── Wants to animate? ─────→ Yes → Step 3: Animation
    │                           └── No  → Export static PNG and stop
    │
    ├── Platform target? ──────→ QQ Super Emoji / 表情商城 → Step 4: QQ Specs
    │                           └── Casual group chat → Looser specs OK
    │
    └── Final delivery ────────→ Step 5: Export + Compress + Test
```

## Step 1: Concept Design

Pick **one scene** + **one to three Emoji characters**.

Scene categories that work well:
- **Transport**: train compartment, airplane cabin, rowboat, dragon boat, subway car
- **Small enclosures**: photo booth, ticket booth, drive-thru window, ferris-wheel gondola
- **Activity frames**: drum set, DJ deck, two-seater arcade game

Emoji selection rules:
- Faces with strong silhouette read better at small size (😎, 🤠, 😭, 🤯)
- Avoid subtle expressions (🙂, 😶) — they disappear at 120×120
- Mix emotional contrast for comedic effect: 😎 driving + 😱 passenger

Sketch the composition in text or ASCII to lock layer order before opening any tool:

```
[Window frame]      ← foreground layer (static)
  [😎 face]         ← character layer (animated: bob, blink)
    [train seat]    ← midground (static or parallax)
[landscape]         ← background (static or slow scroll)
```

## Step 2: Asset Layering

Every element that will move independently must be a **separate layer**.

Minimum viable layers:
1. **Background** — scene illustration, no transparency needed
2. **Character body** — if any (usually static)
3. **Character head** — the Emoji face, often isolated for rotation/tilt
4. **Props** — drumsticks, steering wheel, paddle (animated)
5. **Foreground** — window frame, door jamb, dashboard (creates depth occlusion)

Export each layer as **PNG with Alpha** at the target resolution.

Resolution guide:
- Casual use: 240×240 or 300×300
- QQ表情商城: 300×300 (recommended), max 500×500
- Telegram sticker: 512×512 (if cross-platform)

Color and style constraints:
- Flat illustration style matches Emoji aesthetic better than photorealism
- Limit palette to 64–128 colors for smaller file size
- Avoid thin lines (< 2 px) — they flicker during compression

## Step 3: Animation

Animation philosophy for stickers: **one primary motion + one secondary detail**.

Too much movement feels chaotic; too little feels broken.

### Primary motions (pick one)

| Motion | Amplitude | Duration | Easing | Tool |
|--------|-----------|----------|--------|------|
| Bob / float | 2–4 px Y | 1.5–2 s | Sine in-out | AE, Rive |
| Sway / tilt | 3–6° rotation | 2–3 s | Sine in-out | AE, Rive |
| Slide / scroll | 10–30 px X | 3–4 s | Linear loop | AE |
| Bounce | scale 95%→105% | 0.3 s | Ease out | AE |

### Secondary details (pick zero to two)

| Detail | Keyframes | Duration | Notes |
|--------|-----------|----------|-------|
| Blink | scaleY 1 → 0.1 → 1 | 3–4 frames | Every 2–4 seconds, not on loop |
| Drum / paddle | Rotation ±15° | 0.2 s | On beat, 2–4 hits per loop |
| Sweat drop | Y drift + fade | 1 s | Appear → drift down → vanish |
| Mouth flap | scaleY 1 → 1.2 | 0.1 s | 2–3 reps when "speaking" |
| Wheel spin | Rotation 360° | 0.5–1 s | Continuous or intermittent |

### Recommended tools

**After Effects (APNG pipeline)**
- Import PNG layers, parent to nulls for group control
- Use `loopOut("cycle")` for seamless loops
- Export via `Bodymovin` (Lottie) or PNG Sequence → APNG Assembler

**Rive (lightweight, iterative)**
- Draw or import SVG, set up State Machine
- Export `.riv` for real-time apps; bake to APNG for QQ
- Best for: rapid iteration, parametric variants

**Free alternatives**
- **Pencil2D**: frame-by-frame, APNG export
- **Krita**: animation timeline, excellent brush engine for hand-drawn
- **Figma + Jitter**: Figma auto-layout → Jitter for motion (no manual keyframes)

## Step 4: Export and Compression

### Format selection

| Format | Transparent | QQ Support | File Size | Quality |
|--------|-------------|------------|-----------|---------|
| **APNG** | Yes | ✅ Perfect | Medium | Lossless | ← Recommended |
| WebP | Yes | ✅ Good | Small | Near-lossless | ← Good alternative |
| GIF | Yes | ✅ Compatible | Large | 256 colors, dithered | ← Avoid if possible |
| Lottie JSON | N/A | ⚠️ Partial | Tiny | Vector crisp | → Not for QQ upload |

### APNG export pipeline

1. **Render PNG sequence** from animation tool
   - Frame rate: 16–24 fps (16 fps usually sufficient for stickers)
   - Loop: seamless (first frame == last frame for perfect loops)

2. **Assemble APNG**
   - Tool: `apngasm` (CLI) or `APNG Assembler` (GUI)
   - Command: `apngasm output.png frame*.png 16 1000`
   - Keep under 300 KB for smooth loading in chat

3. **Optimize**
   - `apngopt output.png` — reduces palette, strips metadata
   - If still too large: reduce colors to 128, drop frame rate to 12 fps, or shorten loop

### Volume limits by platform

| Platform | Max size | Dimensions | Loop | Notes |
|----------|----------|------------|------|-------|
| QQ 超级表情 | 500 KB | 300×300 recommended | ≤ 3 s | Square canvas |
| QQ 表情商城 | 500 KB | 300×300 | ≤ 3 s | Requires审核 |
| WeChat custom | ~1 MB | 240×240 | ≤ 5 s | GIF or PNG |
| Telegram | 512 KB | 512×512 | ≤ 3 s | WebM or WebP |

## Step 5: Test and Deliver

1. **Local preview**: Open APNG in browser (Chrome/Firefox natively support APNG)
2. **QQ test**: Drag into chat, send to file helper, check frame rate on mobile
3. **Add to favorites**: Long-press → 添加到表情
4. **For 表情商城**: Prepare  cover image (120×120 static PNG), description, and tags

## Quick Recipes

### Recipe: Train Compartment

```
Scene: flat green retro train, side view, 3 windows
Emoji: 😎 (driver), 😱 (passenger), 🐱 (pet)
Layers: background(train+landscape), character1, character2, character3, foreground(window frames)
Animation:
  - Primary: all characters bob Y ±3 px, 2 s sine loop
  - Secondary: 😎 blinks every 3 s; landscape scrolls X -20 px, 4 s linear loop
Export: 300×300, 16 fps, APNG, target < 300 KB
```

### Recipe: Dragon Boat Drum

```
Scene: red dragon boat, water surface, drum center
Emoji: 🤠 (drummer), 😤 (rower left), 😤 (rower right)
Layers: background(water), boat hull, drum, rowers, drummer, foreground(dragon head)
Animation:
  - Primary: boat bobs Y ±4 px, 1.5 s sine loop
  - Secondary: drumsticks rotate ±20°, 0.25 s, 4 hits per loop; water ripples scale 1→1.1
Export: 300×300, 20 fps, APNG, target < 400 KB
```

### Recipe: Photo Booth Strip

```
Scene: vintage photo booth interior, curtain, stool
Emoji: 🥸 (booth 1), 🤪 (booth 2), 😐 (booth 3), 😭 (booth 4)
Layers: booth shell, curtain, 4 Emoji heads on separate layers, foreground(frame)
Animation:
  - Primary: flash — white overlay opacity 0→100→0, 0.1 s, every 2 s
  - Secondary: each Emoji blinks at staggered intervals; curtain sways 2°
Export: 240×240, 12 fps, APNG, target < 200 KB
```

## Resources

- **Tool installation and setup**: See [references/toolchain.md](references/toolchain.md)
- **QQ platform specifications**: See [references/qq-specs.md](references/qq-specs.md)
- **Animation parameter cheat sheet**: See [references/animation-recipes.md](references/animation-recipes.md)

### scripts/

- `apng_compress.py` — Optimize APNG file size via palette reduction and frame deduplication
- `check_specs.py` — Validate image dimensions, file size, and format against platform limits
