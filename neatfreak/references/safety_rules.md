# NeatFreak Safety Rules

## Absolute Prohibitions

1. **Never delete source code** (`role='source'` or `role='test'`) without explicit human confirmation.
2. **Never delete config files** (`role='config'`) — they may contain secrets or environment-specific settings.
3. **Never auto-merge wiki pages** — only suggest merges; agent must review content for contradictions.
4. **Never modify files outside `workspace/`** — stay within the designated work area.
5. **Never auto-archive files modified within 30 days** — protect recent work.

## Safe Auto-Fixes (Deterministic)

- Adding missing YAML frontmatter to wiki pages
- Fixing obvious markdown formatting errors
- Correcting malformed `[[wiki-links]]` (when target exists)

## Require Agent Judgment

- Deleting or merging wiki pages
- Archiving files older than 180 days
- Refactoring code based on orphan detection
- Any action that changes `role='source'` files
