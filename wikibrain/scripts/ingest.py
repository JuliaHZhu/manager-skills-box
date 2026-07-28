#!/usr/bin/env python3
"""WikiBrain ingest — convert raw materials to markdown and stage in raw/."""

import os
import shutil
from pathlib import Path

RAW_DIR = Path("workspace/knowledge/raw")
WIKI_DIR = Path("workspace/knowledge/wiki")

def ensure_dirs():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    for sub in ("papers", "articles", "notes"):
        (RAW_DIR / sub).mkdir(exist_ok=True)

def ingest_file(src: str, category: str = "notes") -> str:
    """Copy or convert a file into raw/ category."""
    ensure_dirs()
    src_path = Path(src)
    if not src_path.exists():
        return f"Error: {src} not found"
    dest_dir = RAW_DIR / category
    dest_dir.mkdir(parents=True, exist_ok=True)
    if src_path.suffix.lower() in {".pdf", ".docx", ".pptx"}:
        # Placeholder: in production use pandoc / pdfplumber
        dest = dest_dir / (src_path.stem + ".md")
        dest.write_text(f"# {src_path.name}\n\n[Ingested from {src}]\n", encoding="utf-8")
    else:
        dest = dest_dir / src_path.name
        shutil.copy2(src, dest)
    return str(dest)

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: ingest.py <file_path> [category]")
        return
    print(ingest_file(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "notes"))

if __name__ == "__main__":
    main()
