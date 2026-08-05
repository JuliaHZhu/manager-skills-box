# Toolchain Reference

## Recommended Tools by Stage

### Asset Creation

| Tool | Type | Cost | Best For | Export |
|------|------|------|----------|--------|
| **Midjourney** | AI image | $10/mo | Scene backgrounds, flat illustration | PNG |
| **Figma** | Vector/UI | Free | Layer composition, precise layout | PNG/SVG |
| **Photoshop** | Raster | $20/mo | Photo manipulation, complex masking | PNG |
| **Procreate** | Tablet | $12 one-time | Hand-drawn illustration, texture | PNG |
| **Krita** | Raster | Free | Open-source alternative to Photoshop | PNG |

### Animation

| Tool | Type | Cost | Best For | Export |
|------|------|------|----------|--------|
| **After Effects** | Timeline | $20/mo | Professional motion, complex parenting | PNG seq / Lottie |
| **Rive** | Real-time | Free tier | Interactive/iterative, light files | .riv / PNG seq |
| **Pencil2D** | Frame | Free | Traditional frame-by-frame | APNG / GIF |
| **Krita** | Frame | Free | Hand-drawn animation, excellent brushes | PNG seq |
| **Figma + Jitter** | Auto | Free tier | Quick motion without keyframes | GIF / MP4 |

### APNG Assembly and Optimization

| Tool | Platform | Command / Usage |
|------|----------|-----------------|
| **apngasm** | CLI (Linux/Mac) | `apngasm output.png frame*.png 16 1000` |
| **APNG Assembler** | GUI (Windows) | Drag PNG sequence, set frame delay |
| **apngopt** | CLI | `apngopt output.png` — lossless recompression |
| **ImageMagick** | CLI | `convert -delay 6 -loop 0 frame*.png output.png` |
| **iSparta** | GUI (cross) | Drag folder, auto-assemble + compress |
| **Squoosh** | Web | squoosh.app — WebP/PNG optimization |

### apngasm Installation

```bash
# Ubuntu/Debian
sudo apt-get install apngasm

# macOS
brew install apngasm

# From source
git clone https://github.com/apngasm/apngasm.git
cd apngasm && mkdir build && cd build
cmake .. && make && sudo make install
```

### ImageMagick APNG Export

```bash
# Assemble PNG sequence to APNG, 16 fps (delay 6 = 6/100 s ≈ 16.7 fps)
convert -delay 6 -loop 0 frame_*.png -strip output.apng

# Optimize file size
convert output.apng -colors 128 -strip optimized.apng
```

## File Format Deep Dive

### APNG Structure

APNG is a PNG extension storing multiple frames with control chunks (`fcTL`, `fdAT`). Compatible PNG decoders show frame 1; APNG-aware decoders animate.

Critical parameters:
- **Frame delay**: numerator/denominator in `fcTL` chunk. Delay = num/denom seconds.
- **Dispose op**: `0` = none, `1` = background, `2` = previous
- **Blend op**: `0` = source, `1` = over

For stickers: use dispose=0, blend=1 (standard overlay).

### WebP Animation

WebP supports lossy and lossless animation with better compression than APNG.

```bash
# Encode animated WebP from PNG sequence
img2webp -loop 0 -d 60 frame_*.png -o output.webp

# -d 60 = 60 ms delay = ~16.7 fps
# -loop 0 = infinite
```

QQ support for animated WebP varies by version; APNG is the safest universal choice.

### GIF vs APNG Comparison

| Aspect | GIF | APNG |
|--------|-----|------|
| Max colors | 256 | Unlimited (truecolor + alpha) |
| Transparency | Binary (on/off) | Full alpha channel |
| Compression | LZW | Deflate (better) |
| File size (same content) | 2–5× larger | Smaller |
| Platform support | Universal | Modern browsers + QQ |

Always prefer APNG for new stickers unless targeting very old platforms.
