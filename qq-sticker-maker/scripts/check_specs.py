#!/usr/bin/env python3
"""
Validate image/sticker files against platform specifications.

Usage:
    python check_specs.py <file> [--platform qq|wechat|telegram]

Requirements: Pillow>=9.0.0
"""

import argparse
import os
import struct
import sys

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow not installed. Run: pip install Pillow")
    sys.exit(1)


PLATFORM_LIMITS = {
    "qq": {
        "formats": {"APNG", "WEBP", "GIF"},
        "max_size_kb": 500,
        "recommended_size": (300, 300),
        "max_duration_s": 3,
        "fps_range": (12, 24),
    },
    "wechat": {
        "formats": {"APNG", "GIF", "PNG"},
        "max_size_kb": 1024,
        "recommended_size": (240, 240),
        "max_duration_s": 5,
        "fps_range": (12, 24),
    },
    "telegram": {
        "formats": {"WEBM", "WEBP"},
        "max_size_kb": 512,
        "recommended_size": (512, 512),
        "max_duration_s": 3,
        "fps_range": (1, 30),
    },
}


def parse_apng_metadata(data: bytes):
    """Extract APNG frame count and duration from raw PNG chunks."""
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        return None
    pos = 8
    num_frames = 0
    total_delay_ms = 0
    while pos < len(data):
        if pos + 8 > len(data):
            break
        length = struct.unpack(">I", data[pos:pos+4])[0]
        ctype = data[pos+4:pos+8]
        if ctype == b'acTL':
            num_frames = struct.unpack(">I", data[pos+8:pos+12])[0]
        elif ctype == b'fcTL':
            # fcTL: sequence_number(4) + width(4) + height(4) + x_offset(4) + y_offset(4)
            # + delay_num(2) + delay_den(2) + dispose_op(1) + blend_op(1)
            delay_num = struct.unpack(">H", data[pos+24:pos+26])[0]
            delay_den = struct.unpack(">H", data[pos+26:pos+28])[0]
            delay_den = delay_den or 1000  # default if 0
            total_delay_ms += delay_num * 1000 / delay_den
        elif ctype == b'IDAT' and num_frames == 0:
            pass  # static PNG
        pos += 12 + length
    return {
        "frames": num_frames,
        "duration_ms": total_delay_ms,
        "duration_s": total_delay_ms / 1000,
        "fps": num_frames / (total_delay_ms / 1000) if total_delay_ms > 0 else 0,
    }


def get_image_info(path: str):
    """Gather all relevant metadata about an image file."""
    info = {"path": path, "exists": os.path.exists(path)}
    if not info["exists"]:
        return info

    info["size_bytes"] = os.path.getsize(path)
    info["size_kb"] = info["size_bytes"] / 1024

    with open(path, 'rb') as f:
        raw = f.read()

    # Format detection
    if raw[:8] == b'\x89PNG\r\n\x1a\n':
        # Check for APNG
        apng_meta = parse_apng_metadata(raw)
        if apng_meta and apng_meta["frames"] > 0:
            info["format"] = "APNG"
            info["animation"] = apng_meta
        else:
            info["format"] = "PNG"
            info["animation"] = None
    elif raw[:4] == b'RIFF' and raw[8:12] == b'WEBP':
        info["format"] = "WEBP"
        # WEBP animation detection via PIL
        try:
            img = Image.open(path)
            info["animation"] = {
                "frames": getattr(img, "n_frames", 1),
                "duration_ms": getattr(img, "info", {}).get("duration", 0),
            }
        except Exception:
            info["animation"] = None
    elif raw[:6] in (b'GIF87a', b'GIF89a'):
        info["format"] = "GIF"
        try:
            img = Image.open(path)
            info["animation"] = {
                "frames": getattr(img, "n_frames", 1),
                "duration_ms": getattr(img, "info", {}).get("duration", 0),
            }
        except Exception:
            info["animation"] = None
    elif raw[:4] == b'\x1aE\xdf\xa3':
        info["format"] = "WEBM"
        info["animation"] = None
    else:
        info["format"] = "UNKNOWN"
        info["animation"] = None

    # Dimensions via PIL
    try:
        img = Image.open(path)
        info["width"] = img.width
        info["height"] = img.height
        info["mode"] = img.mode
        info["aspect_ratio"] = img.width / img.height
    except Exception as e:
        info["pil_error"] = str(e)

    return info


def check_against_platform(info: dict, platform: str):
    """Compare image info against platform limits, return list of issues."""
    limits = PLATFORM_LIMITS.get(platform)
    if not limits:
        return [("error", f"Unknown platform: {platform}")]

    issues = []

    # Format check
    fmt = info.get("format", "UNKNOWN")
    if fmt not in limits["formats"]:
        issues.append(("error", f"Format '{fmt}' not supported. Allowed: {limits['formats']}"))

    # Size check
    size_kb = info.get("size_kb", 0)
    if size_kb > limits["max_size_kb"]:
        issues.append(("error", f"File size {size_kb:.1f} KB exceeds {limits['max_size_kb']} KB limit"))
    elif size_kb > limits["max_size_kb"] * 0.8:
        issues.append(("warn", f"File size {size_kb:.1f} KB is close to {limits['max_size_kb']} KB limit"))

    # Dimension check
    w = info.get("width", 0)
    h = info.get("height", 0)
    rec_w, rec_h = limits["recommended_size"]
    if w != h:
        issues.append(("warn", f"Non-square canvas: {w}×{h}. Recommended: square"))
    if w > rec_w * 1.5 or h > rec_h * 1.5:
        issues.append(("warn", f"Dimensions {w}×{h} larger than recommended {rec_w}×{rec_h}"))

    # Animation checks
    anim = info.get("animation")
    if anim and "duration_s" in anim:
        dur = anim["duration_s"]
        if dur > limits["max_duration_s"]:
            issues.append(("error", f"Duration {dur:.2f}s exceeds {limits['max_duration_s']}s limit"))
        fps = anim.get("fps", 0)
        if fps > 0 and (fps < limits["fps_range"][0] or fps > limits["fps_range"][1]):
            issues.append(("warn", f"FPS {fps:.1f} outside recommended range {limits['fps_range']}"))

    return issues


def print_report(info: dict, platform: str = None):
    """Pretty-print image info and platform checks."""
    print(f"\n{'='*50}")
    print(f"File: {info['path']}")
    print(f"{'='*50}")

    if not info.get("exists"):
        print("Error: File not found")
        return

    print(f"Format:     {info.get('format', 'N/A')}")
    print(f"Size:       {info['size_kb']:.1f} KB")
    print(f"Dimensions: {info.get('width', '?')} × {info.get('height', '?')} px")
    print(f"Mode:       {info.get('mode', 'N/A')}")

    anim = info.get("animation")
    if anim:
        print(f"Animation:  {anim.get('frames', '?')} frames")
        if 'duration_s' in anim:
            print(f"Duration:   {anim['duration_s']:.2f} s")
        if 'fps' in anim and anim['fps']:
            print(f"Est. FPS:   {anim['fps']:.1f}")

    if platform:
        print(f"\n--- Platform Check: {platform.upper()} ---")
        issues = check_against_platform(info, platform)
        if not issues:
            print("✅ All checks passed")
        else:
            for level, msg in issues:
                icon = "❌" if level == "error" else "⚠️"
                print(f"{icon} {msg}")

    print(f"{'='*50}\n")


def main():
    parser = argparse.ArgumentParser(description="Check sticker image against platform specs")
    parser.add_argument("file", help="Image file to check")
    parser.add_argument("--platform", choices=["qq", "wechat", "telegram"], default="qq",
                        help="Platform to validate against (default: qq)")
    args = parser.parse_args()

    info = get_image_info(args.file)
    print_report(info, platform=args.platform)


if __name__ == "__main__":
    main()
