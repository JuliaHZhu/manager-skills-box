# Animation Parameter Cheat Sheet

## Motion Primitives

All values assume 300×300 canvas. Scale proportionally for other sizes.

### Bob / Float (Vertical oscillation)

```
Property: Position Y
Amplitude: 2–4 px (subtle), 6–10 px (exaggerated)
Duration: 1.5–2.5 s
Easing: Sine in-out (smooth) or Ease in-out (natural)
Loop: cycle
Notes: Use odd number of half-cycles to avoid visual stutter
```

### Sway / Tilt (Rotation)

```
Property: Rotation Z
Amplitude: 3–6° (subtle), 10–15° (cartoon)
Duration: 2–3 s
Easing: Sine in-out
Loop: cycle
Notes: Add scaleX 98%→102% for pseudo-3D depth
```

### Slide / Scroll (Horizontal)

```
Property: Position X
Amplitude: 20–40% of canvas width
Duration: 3–6 s
Easing: Linear (seamless loop) or Ease in-out (ping-pong)
Loop: cycle or ping-pong
Notes: Duplicate background for infinite scroll illusion
```

### Bounce (Scale impact)

```
Property: Scale X/Y
Amplitude: 95%→105% or 90%→110%
Duration: 0.2–0.4 s
Easing: Ease out (sharp attack, slow decay)
Loop: usually triggered, not continuous
Notes: Squash and stretch: scaleX 110% when scaleY 90%
```

### Blink (Eye simulation)

```
Property: Scale Y
Keyframes: 1 → 0.05 → 1
Duration: 3–4 frames at target fps (≈ 0.15–0.25 s)
Interval: Every 2–4 seconds (randomized, not looped)
Notes: Hold closed frame for 1 frame for crisp blink
```

### Drum / Paddle (Rotation on anchor)

```
Property: Rotation Z (anchor at handle end)
Amplitude: ±15° to ±30°
Duration: 0.15–0.25 s per hit
Easing: Ease out
Pattern: Hit → hold → return, 2–4 hits per measure
Notes: Add motion blur or speed lines for impact frames
```

## Compound Recipes

### Train Ride

```
Layers: train body, Emoji1, Emoji2, background(landscape), foreground(window)

Train body:
  - Position Y: sine, ±3 px, 2 s

Emoji heads (parented to train body):
  - Same bob as train (inherited)
  - Individual blink: scaleY, every 3 s offset by 0.5 s each

Background landscape:
  - Position X: linear, -30 px per second, reset every 4 s

Window foreground:
  - Static (provides depth occlusion)

Total: 48 frames @ 16 fps = 3 s loop
```

### Boat on Water

```
Layers: water, boat hull, characters, foreground(railing)

Water:
  - Scale X: 1 → 1.03 → 1, sine, 1.5 s
  - Multiple wave layers at different frequencies (1.5 s, 2.1 s, 2.7 s)

Boat hull (parent):
  - Position Y: sine, ±4 px, 2 s
  - Rotation Z: sine, ±2°, 2 s (lag water by 0.2 s for realism)

Characters:
  - Inherit boat motion
  - Individual secondary: paddle rotation or drum hits

Total: 64 frames @ 20 fps = 3.2 s, trimmed to 3 s
```

### DJ Deck / Control Panel

```
Layers: deck, Emoji(headphones), hands, foreground(meters)

Emoji head:
  - Rotation Z: ±5°, sine, 1 s (head bob to beat)
  - Scale Y: blink on snare hit

Hands:
  - Position X/Y: keyed to 4/4 beat, 0.5 s per measure
  - Rotation: ±10° on slider moves

Meters (foreground):
  - Scale Y: random flicker 0.3–1.0, 0.1 s intervals
  - Color: green → yellow → red thresholds

Total: 36 frames @ 12 fps = 3 s
```

## Timing Formulas

### Converting BPM to frame delays

```
frames_per_beat = fps * 60 / BPM

Examples:
  120 BPM @ 16 fps → 8 frames per beat
  120 BPM @ 24 fps → 12 frames per beat
  100 BPM @ 16 fps → 9.6 ≈ 10 frames per beat
```

### Seamless loop math

For a motion to loop perfectly, the animation duration must be an integer multiple of the frame interval:

```
loop_duration = frame_count / fps

Example for 3 s loop:
  @ 16 fps → 48 frames
  @ 20 fps → 60 frames
  @ 24 fps → 72 frames
```

First frame and last frame should be **identical** (or the last frame is omitted since APNG loops back to frame 0).

## Anti-Patterns

| Pattern | Why It Fails | Fix |
|---------|--------------|-----|
| Everything moves at same frequency | Looks robotic | Offset layer timings by 0.2–0.5 s |
| Linear motion without easing | Mechanical, cheap | Always add easing, even on small moves |
| Blink every exact 2.0 s | Uncanny regularity | Randomize interval 2.0–4.0 s |
| 30+ fps for simple motion | Wasted file size | 12–16 fps sufficient for most stickers |
| Complex 3D rotation | Flat style breaks | Keep rotation to 2D plane (Z-axis only) |
| Full canvas transparency changes | Compression nightmare | Minimize transparent pixel changes between frames |
