# QQ Platform Specifications

## QQ Super Emoji (超级表情)

Used in chat by tapping the Emoji panel → Super Emoji tab.

| Spec | Requirement |
|------|-------------|
| Format | APNG (recommended), WebP, GIF |
| Resolution | 240×240 to 300×300 (square) |
| Max size | 500 KB |
| Duration | ≤ 3 seconds per loop |
| Frame rate | 12–24 fps |
| Loop | Infinite or ≤ 3 cycles |
| Color depth | 8-bit per channel (24-bit + 8-bit alpha) |
| Max colors | 256 recommended for small file size |

## QQ Sticker Shop (表情商城)

For published sticker packs available in the QQ store.

### Sticker specs (per image)

| Spec | Requirement |
|------|-------------|
| Format | APNG |
| Resolution | 300×300 px |
| Max size | 500 KB |
| Duration | ≤ 3 seconds |
| Frame rate | 12–24 fps |

### Pack metadata

| Asset | Spec |
|-------|------|
| Pack cover | 120×120 px static PNG |
| Pack banner | 750×300 px static PNG |
| Pack name | ≤ 8 Chinese characters |
| Description | ≤ 50 characters |
| Sticker count | 8, 16, or 24 |
| Artist name | Required |

### Review checklist

- [ ] No copyrighted characters or brands
- [ ] No political, violent, or adult content
- [ ] All stickers same dimension
- [ ] Total pack size < 12 MB
- [ ] Cover image clearly represents pack style

## WeChat Custom Stickers (微信自定义表情)

Drag-and-drop or add from chat.

| Spec | Requirement |
|------|-------------|
| Format | GIF, PNG (static), APNG |
| Resolution | 240×240 recommended |
| Max size | ~1 MB (unenforced but affects load) |
| Duration | ≤ 5 seconds |
| Loop | Infinite |

Note: WeChat does not have an official sticker shop for individual creators (only enterprise accounts).

## Telegram Stickers

For cross-platform distribution.

| Spec | Requirement |
|------|-------------|
| Format | WebM (animated), WebP (static) |
| Resolution | 512×512 px |
| Max size | 512 KB |
| Duration | ≤ 3 seconds |
| Frame rate | 30 fps max |

Use `@Stickers` bot to upload packs.

## Troubleshooting QQ Upload Failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| "文件过大" | > 500 KB | Reduce colors, drop frames, shrink canvas |
| "格式不支持" | Wrong extension or encoding | Ensure .png with APNG chunks, not plain PNG |
| 播放卡顿 | Too many frames or high resolution | Cap at 300×300, 16 fps, 48 frames max |
| 黑边/白边 | Alpha channel premultiply issue | Export straight alpha, not premultiplied |
| 颜色失真 | Indexed color with dither | Use truecolor APNG, or carefully optimize palette |
