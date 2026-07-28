#!/usr/bin/env python3
"""NeatFreak archiver — suggest/archive stale files. Never deletes."""

import os
import shutil
from pathlib import Path
from datetime import datetime, timedelta

ARCHIVE_DIR = Path("workspace/.archive")

def suggest_archive(threshold_days: int = 180) -> list:
    import sqlite3
    DB_PATH = Path("workspace/.filestates/index.db")
    if not DB_PATH.exists():
        return []
    conn = sqlite3.connect(DB_PATH)
    try:
        threshold = (datetime.now() - timedelta(days=threshold_days)).timestamp()
        rows = conn.execute(
            "SELECT path, mtime, role FROM files WHERE mtime < ? AND role IN ('doc','generated','artifact')",
            (threshold,)
        ).fetchall()
        return [
            {"path": r[0], "last_modified": datetime.fromtimestamp(r[1]).isoformat(),
             "role": r[2], "suggested_action": "archive"}
            for r in rows
        ]
    finally:
        conn.close()

def archive_file(src: str, dry_run: bool = True) -> dict:
    src_path = Path(src)
    if not src_path.exists():
        return {"ok": False, "error": "File not found"}
    dest = ARCHIVE_DIR / src_path.name
    if dry_run:
        return {"ok": True, "dry_run": True, "would_move": str(dest)}
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src_path), str(dest))
    return {"ok": True, "moved_to": str(dest)}

def main():
    import sys, json
    if len(sys.argv) > 1 and sys.argv[1] == "suggest":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 180
        print(json.dumps(suggest_archive(days), indent=2, ensure_ascii=False))
    elif len(sys.argv) > 1 and sys.argv[1] == "archive":
        f = sys.argv[2]
        dry = "--apply" not in sys.argv
        print(json.dumps(archive_file(f, dry), indent=2, ensure_ascii=False))
    else:
        print("Usage: archiver.py suggest [days] | archiver.py archive <file> [--apply]")

if __name__ == "__main__":
    main()
