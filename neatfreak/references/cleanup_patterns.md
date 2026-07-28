# Common Cleanup Patterns

## Wiki Cleanup

| Pattern | Detection | Action |
|---------|-----------|--------|
| Orphan page | No incoming/outgoing wiki-links | Review if merge or delete |
| Dead link | `[[Target]]` where Target page missing | Fix link or create target page |
| Missing frontmatter | Page lacks `---` YAML header | Auto-add minimal frontmatter |
| Duplicate concept | Similar titles/tags | Suggest merge to agent |

## Code Cleanup

| Pattern | Detection | Action |
|---------|-----------|--------|
| Dead code | Code node with zero edges | Flag for review (don't auto-delete) |
| Stale doc | Doc file unmodified >180 days | Suggest archive |
| Unused generated | Generated artifact older than source | Suggest regenerate |

## File Cleanup

| Pattern | Detection | Action |
|---------|-----------|--------|
| Snapshot bloat | `.filestates/snapshots/` > 1GB | Suggest pruning old snapshots |
| Session accumulation | `.sessions/` > 1000 files | Suggest archive old sessions |
