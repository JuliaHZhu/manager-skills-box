#!/usr/bin/env python3
"""Snapshot and rewind engine for FileStates."""

import os
import shutil
from pathlib import Path
from datetime import datetime
from index_manager import ensure_db, get_file, DB_PATH

SNAP_DIR = Path("workspace/.filestates/snapshots")

def snapshot_path(file_id: int, file_hash: str) -> Path:
    SNAP_DIR.mkdir(parents=True, exist_ok=True)
    return SNAP_DIR / f"{file_id}_{file_hash}.snap"

def take_snapshot(path: str) -> str:
    ensure_db()
    import sqlite3
    from index_manager import upsert_file
    file_id = upsert_file(path)
    if not file_id or not os.path.exists(path):
        return ""
    conn = sqlite3.connect(DB_PATH)
    try:
        row = conn.execute("SELECT hash FROM files WHERE id=?", (file_id,)).fetchone()
        h = row[0] if row else ""
        if not h:
            return ""
        sp = snapshot_path(file_id, h)
        if not sp.exists():
            shutil.copy2(path, sp)
            conn.execute(
                "INSERT INTO snapshots(file_id, hash, snap_path, created_at) VALUES (?, ?, ?, ?)",
                (file_id, h, str(sp), datetime.now().isoformat())
            )
            conn.commit()
        return str(sp)
    finally:
        conn.close()

def list_snapshots(path: str):
    ensure_db()
    import sqlite3
    conn = sqlite3.connect(DB_PATH)
    try:
        file_id = None
        row = conn.execute("SELECT id FROM files WHERE path=?", (path,)).fetchone()
        if row:
            file_id = row[0]
        if not file_id:
            return []
        rows = conn.execute(
            "SELECT hash, snap_path, created_at FROM snapshots WHERE file_id=? ORDER BY created_at DESC",
            (file_id,)
        ).fetchall()
        return [{"hash": r[0], "path": r[1], "created_at": r[2]} for r in rows]
    finally:
        conn.close()

def rewind(path: str, steps: int = 1):
    snaps = list_snapshots(path)
    if not snaps or steps < 1 or steps > len(snaps):
        return False
    target = snaps[steps - 1]
    snap_file = Path(target["path"])
    if snap_file.exists():
        shutil.copy2(snap_file, path)
        from index_manager import upsert_file
        upsert_file(path)
        return True
    return False
