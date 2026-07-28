#!/usr/bin/env python3
"""File operation proxy — write/append with automatic snapshot + index update."""

import os
import sys
from pathlib import Path
from index_manager import upsert_file, get_file
from snapshot import take_snapshot
from plan_manager import sync_plan_md

VALID_ROLES = {"source", "test", "doc", "config", "generated", "artifact"}

def fs_write(path: str, content: str, role: str = "source"):
    """Write file with auto-snapshot and index update."""
    if os.path.exists(path):
        take_snapshot(path)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    if role not in VALID_ROLES:
        role = "source"
    file_id = upsert_file(path, role)
    return {"ok": True, "path": path, "role": role, "file_id": file_id}

def fs_append(path: str, content: str):
    """Append to file with auto-snapshot."""
    if os.path.exists(path):
        take_snapshot(path)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)
    file_id = upsert_file(path)
    return {"ok": True, "path": path, "file_id": file_id}

def fs_rewind(path: str, steps: int = 1):
    """Rewind file to N snapshots ago."""
    from snapshot import rewind
    ok = rewind(path, steps)
    return {"ok": ok, "path": path, "steps": steps}

def fs_status(path: str = "."):
    """Show tracked files under path."""
    from index_manager import list_files
    tracked = list_files()
    prefix = os.path.abspath(path)
    matched = [f for f in tracked if os.path.abspath(f["path"]).startswith(prefix)]
    return {"path": path, "count": len(matched), "files": matched}

def fs_role_set(path: str, role: str):
    """Set file role."""
    if role not in VALID_ROLES:
        return {"ok": False, "error": f"Invalid role. Use one of: {VALID_ROLES}"}
    file_id = upsert_file(path, role)
    return {"ok": True, "path": path, "role": role, "file_id": file_id}

def fs_role_get(path: str):
    """Get file role and metadata."""
    info = get_file(path)
    if not info:
        return {"ok": False, "error": "File not tracked"}
    return {"ok": True, "path": path, "role": info.get("role"), "meta": info}

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "write":
        path = sys.argv[2]
        content = sys.argv[3] if len(sys.argv) > 3 else ""
        role = sys.argv[4] if len(sys.argv) > 4 else "source"
        print(fs_write(path, content, role))
    elif cmd == "append":
        path = sys.argv[2]
        content = sys.argv[3] if len(sys.argv) > 3 else ""
        print(fs_append(path, content))
    elif cmd == "rewind":
        path = sys.argv[2]
        steps = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        print(fs_rewind(path, steps))
    elif cmd == "status":
        path = sys.argv[2] if len(sys.argv) > 2 else "."
        print(fs_status(path))
    elif cmd == "role-set":
        path, role = sys.argv[2], sys.argv[3]
        print(fs_role_set(path, role))
    elif cmd == "role-get":
        print(fs_role_get(sys.argv[2]))
    else:
        print("Usage: fs_proxy.py <write|append|rewind|status|role-set|role-get> ...")

if __name__ == "__main__":
    main()
