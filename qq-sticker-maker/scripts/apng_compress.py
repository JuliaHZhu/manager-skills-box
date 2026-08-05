#!/usr/bin/env python3
"""
APNG optimizer for sticker production.
Reduces file size via palette quantization, frame deduplication, and crop optimization.

Usage:
    python apng_compress.py input.png [-o output.png] [--colors 128] [--fps 16]

Requirements: Pillow>=9.0.0
"""

import argparse
import os
import struct
import sys
from io import BytesIO

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow not installed. Run: pip install Pillow")
    sys.exit(1)


def parse_apng_chunks(data: bytes):
    """Parse PNG/APNG chunks, return list of (type, data) tuples."""
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError("Not a PNG file")
    pos = 8
    chunks = []
    while pos < len(data):
        length = struct.unpack(">I", data[pos:pos+4])[0]
        ctype = data[pos+4:pos+8].decode('ascii', errors='replace')
        cdata = data[pos+8:pos+8+length]
        # crc = data[pos+8+length:pos+12+length]
        chunks.append((ctype, cdata))
        pos += 12 + length
    return chunks


def is_animated_png(data: bytes) -> bool:
    """Check if PNG contains APNG animation chunks."""
    try:
        chunks = parse_apng_chunks(data)
        return any(ctype == 'acTL' for ctype, _ in chunks)
    except Exception:
        return False


def extract_frames_rapid(data: bytes):
    """Extract frames from APNG using Pillow's seek/tell."""
    frames = []
    img = Image.open(BytesIO(data))
    try:
        while True:
            frame = img.copy()
            frames.append(frame)
            img.seek(img.tell() + 1)
    except EOFError:
        pass
    return frames


def deduplicate_frames(frames, threshold=0.99):
    """Remove near-duplicate frames based on pixel similarity."""
    if len(frames) <= 1:
        return frames
    kept = [frames[0]]
    for f in frames[1:]:
        prev = kept[-1]
        if f.size != prev.size:
            kept.append(f)
            continue
        # Quick similarity: compare small thumbnails
        thumb_size = (32, 32)
        t1 = f.convert('RGB').resize(thumb_size)
        t2 = prev.convert('RGB').resize(thumb_size)
        diff = sum(abs(a - b) for a, b in zip(t1.tobytes(), t2.tobytes()))
        max_diff = thumb_size[0] * thumb_size[1] * 3 * 255
        similarity = 1.0 - diff / max_diff
        if similarity < threshold:
            kept.append(f)
    return kept


def quantize_frame(frame: Image.Image, colors: int = 128) -> Image.Image:
    """Reduce color palette while preserving alpha."""
    if frame.mode == 'P':
        frame = frame.convert('RGBA')
    if frame.mode != 'RGBA':
        frame = frame.convert('RGBA')
    # Pillow's quantize with alpha support (FASTOCTREE supports RGBA)
    quantized = frame.quantize(colors=colors, method=Image.Quantize.FASTOCTREE)
    return quantized.convert('RGBA')


def save_apng(frames, out_path, fps=16, loop=0):
    """Save frames as APNG using Pillow."""
    duration = int(1000 / fps)
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=loop,
        format='PNG'
    )


def optimize_apng(input_path, output_path=None, colors=128, fps=None, dedup=True):
    """Main optimization pipeline."""
    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_optimized{ext}"

    with open(input_path, 'rb') as f:
        data = f.read()

    original_size = len(data)
    print(f"Input:  {input_path} ({original_size / 1024:.1f} KB)")

    if not is_animated_png(data):
        print("Warning: File is a static PNG, not APNG. Converting to optimized static PNG.")
        img = Image.open(BytesIO(data))
        if img.mode in ('RGBA', 'P'):
            quantized = img.quantize(colors=colors, method=Image.Quantize.MEDIANCUT)
            quantized.save(output_path)
        else:
            img.convert('RGB').quantize(colors=colors).save(output_path)
        new_size = os.path.getsize(output_path)
        print(f"Output: {output_path} ({new_size / 1024:.1f} KB, {new_size/original_size*100:.0f}%)")
        return

    frames = extract_frames_rapid(data)
    print(f"Frames: {len(frames)}")

    if dedup and len(frames) > 1:
        frames = deduplicate_frames(frames)
        print(f"After dedup: {len(frames)}")

    processed = []
    for i, frame in enumerate(frames):
        q = quantize_frame(frame, colors=colors)
        processed.append(q)
        if (i + 1) % 10 == 0:
            print(f"  Quantized {i + 1}/{len(frames)}...")

    save_apng(processed, output_path, fps=fps or 16)
    new_size = os.path.getsize(output_path)
    ratio = new_size / original_size * 100
    print(f"Output: {output_path} ({new_size / 1024:.1f} KB, {ratio:.0f}% of original)")

    if new_size > 500 * 1024:
        print(f"Warning: Still over 500 KB. Try --colors 64 or reduce frame count.")


def main():
    parser = argparse.ArgumentParser(description="Optimize APNG for sticker use")
    parser.add_argument("input", help="Input PNG/APNG file")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("--colors", type=int, default=128, help="Max colors per frame (default: 128)")
    parser.add_argument("--fps", type=int, default=None, help="Target FPS (default: keep original)")
    parser.add_argument("--no-dedup", action="store_true", help="Disable frame deduplication")
    args = parser.parse_args()

    optimize_apng(
        args.input,
        output_path=args.output,
        colors=args.colors,
        fps=args.fps,
        dedup=not args.no_dedup
    )


if __name__ == "__main__":
    main()
