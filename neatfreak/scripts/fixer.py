#!/usr/bin/env python3
"""NeatFreak fixer — auto-fix deterministic issues only."""

import os
import re
from pathlib import Path
from scanner import scan_all

LINK_RE = re.compile(r"\[\[(.*?)\]\]")

def fix_missing_frontmatter(path: str) -> bool:
    p = Path(path)
    if not p.exists():
        return False
    text = p.read_text(encoding="utf-8")
    if text.startswith("---"):
        return False
    title = p.stem.replace("-", " ").replace("_", " ").title()
    fm = f"---\ntitle: \"{title}\"\ncategory: note\ncreated: \"{__import__('datetime').datetime.now().isoformat()}\"\n---\n\n"
    p.write_text(fm + text, encoding="utf-8")
    return True

def apply_safe_fixes(dry_run: bool = True) -> list:
    issues = scan_all()
    results = []
    for i in issues:
        if i["type"] == "missing-meta":
            if dry_run:
                results.append({"action": "would-fix-frontmatter", "path": i["path"]})
            else:
                ok = fix_missing_frontmatter(i["path"])
                results.append({"action": "fix-frontmatter", "path": i["path"], "ok": ok})
    return results

def main():
    import sys, json
    dry = "--apply" not in sys.argv
    results = apply_safe_fixes(dry_run=dry)
    print(json.dumps(results, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
