#!/usr/bin/env python3
"""Code indexer — AST extraction via tree-sitter CLI or regex fallback."""

import os
import re
import sqlite3
import subprocess
import json
from pathlib import Path
from schema import ensure_codegraph_schema, DB_PATH

# Regex fallbacks for common patterns
PATTERNS = {
    "python": {
        "function": re.compile(r"^(?:\s*@[\w\.]+\s*)*\s*def\s+(\w+)\s*\("),
        "class": re.compile(r"^(?:\s*@[\w\.]+\s*)*\s*class\s+(\w+)\s*[\(:]"),
        "import": re.compile(r"^\s*(?:from\s+([\w\.]+)\s+import|import\s+([\w\.]+))"),
    },
    "javascript": {
        "function": re.compile(r"(?:function\s+(\w+)|(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?\(|(\w+):\s*(?:async\s*)?\()"),
        "class": re.compile(r"class\s+(\w+)\s*"),
        "import": re.compile(r"import\s+.*?\s+from\s+['\"]([^'\"]+)['\"]|require\(['\"]([^'\"]+)['\"]\)"),
    },
    "typescript": {
        "function": re.compile(r"(?:function\s+(\w+)|(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?\(|(\w+):\s*(?:async\s*)?\()"),
        "class": re.compile(r"class\s+(\w+)\s*"),
        "import": re.compile(r"import\s+.*?\s+from\s+['\"]([^'\"]+)['\"]"),
    },
}

EXT_MAP = {
    ".py": "python", ".js": "javascript", ".ts": "typescript",
    ".jsx": "javascript", ".tsx": "typescript", ".java": "java",
    ".go": "go", ".rs": "rust", ".cpp": "cpp", ".c": "c",
    ".h": "c", ".hpp": "cpp",
}

def detect_language(path: str) -> str:
    return EXT_MAP.get(Path(path).suffix.lower(), "")

def extract_regex(path: str, lang: str):
    """Fallback AST extraction via regex."""
    nodes = []
    edges = []
    if lang not in PATTERNS:
        return nodes, edges
    pat = PATTERNS[lang]
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except Exception:
        return nodes, edges
    for i, line in enumerate(lines, 1):
        for kind, rx in pat.items():
            m = rx.search(line)
            if m:
                name = next((g for g in m.groups() if g), "")
                if name:
                    nodes.append({
                        "kind": kind,
                        "name": name,
                        "start_line": i,
                        "end_line": i,
                        "signature": line.strip(),
                        "body": "",
                        "language": lang,
                    })
    return nodes, edges

def extract_ast(path: str, lang: str):
    """Try tree-sitter CLI first, fallback to regex."""
    # Attempt tree-sitter parse if available
    try:
        result = subprocess.run(
            ["tree-sitter", "parse", path],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0 and result.stdout:
            # Tree-sitter output is not JSON by default; use regex fallback for now
            pass
    except Exception:
        pass
    return extract_regex(path, lang)

def index_project(src_dir: str = "workspace/src", incremental: bool = True):
    ensure_codegraph_schema()
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent / "filestates" / "scripts"))
    from index_manager import ensure_db, DB_PATH as FS_DB, upsert_file, file_hash
    ensure_db()
    conn = sqlite3.connect(DB_PATH)
    try:
        src_path = Path(src_dir)
        if not src_path.exists():
            print(f"Source dir not found: {src_dir}")
            return
        files = list(src_path.rglob("*"))
        total = 0
        for f in files:
            if not f.is_file():
                continue
            lang = detect_language(str(f))
            if not lang:
                continue
            fpath = str(f)
            # Ensure file is tracked in filestates
            fid = upsert_file(fpath, "source")
            if incremental:
                old = conn.execute("SELECT hash FROM files WHERE id=?", (fid,)).fetchone()
                new_h = file_hash(fpath)
                if old and old[0] == new_h:
                    continue
            nodes, edges = extract_ast(fpath, lang)
            # Clear old nodes for this file
            conn.execute("DELETE FROM code_nodes WHERE file_id=?", (fid,))
            nid_map = {}
            for n in nodes:
                cur = conn.execute(
                    "INSERT INTO code_nodes(file_id, kind, name, start_line, end_line, signature, body, language) VALUES (?,?,?,?,?,?,?,?)",
                    (fid, n["kind"], n["name"], n["start_line"], n["end_line"], n["signature"], n["body"], n["language"])
                )
                nid_map[(n["kind"], n["name"])] = cur.lastrowid
            total += len(nodes)
        conn.commit()
        print(f"Indexed {total} nodes from {src_dir}")
    finally:
        conn.close()

if __name__ == "__main__":
    import sys
    src = sys.argv[1] if len(sys.argv) > 1 else "workspace/src"
    index_project(src)
