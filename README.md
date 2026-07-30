# Manager Skills Box

A layered toolbox for AI agent workspace management — file tracking, code analysis, knowledge compilation, and quality governance.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│  P2  NeatFreak     Quality Governance               │
│       Scan / Fix / Clean → safety-gated             │
├─────────────────────────────────────────────────────┤
│  P1  CodeGraph     Code Structure                   │
│       AST → SQLite graph → blast radius             │
│  P1  WikiBrain     Knowledge Engine                 │
│       Ingest → Compile → Index → Query              │
├─────────────────────────────────────────────────────┤
│  P0  FileStates    Foundation Layer                 │
│       Snapshot / Rollback / Plan / Role tracking    │
└─────────────────────────────────────────────────────┘
```

Higher layers depend on lower ones. P0 is the bedrock — every file operation flows through it. P1 layers build capability on top. P2 governs across all layers.

## Skills

| Skill | Layer | Responsibility |
|-------|-------|---------------|
| **FileStates** | P0 | Track every file write with snapshots and rollback. Tag files by role (source/test/doc/config). Plan-mode: create, track, and verify task plans. |
| **CodeGraph** | P1 | Parse codebases (Python/JS/TS/Java/Go/Rust/C/C++) via Tree-sitter, build a SQLite call graph. Blast radius analysis: "what breaks if I change X?" |
| **WikiBrain** | P1 | Raw material → structured wiki. Parallel ingestion, frontmatter indexing, FTS5 search, dead-link detection, session feedback extraction. |
| **NeatFreak** | P2 | Aggregate quality signals from all lower layers. Three safe modes: Scan (read-only), Fix (deterministic repairs), Clean (agent-supervised). |

## Quick Start

```bash
git clone https://github.com/JuliaHZhu/manager-skills-box.git
cd manager-skills-box
```

Each skill is self-contained under its own directory with a `SKILL.md` reference, `scripts/`, and supporting files.

### Initialize & Index

```bash
# Foundation: track your workspace files
python filestates/scripts/cli.py plan new my-task --objective="Build feature X" --goal-kind=feature

# Code: index your source tree
python codegraph/scripts/cli.py init
python codegraph/scripts/cli.py index ./src

# Knowledge: build a wiki from raw materials
python wikibrain/scripts/cli.py init
python wikibrain/scripts/cli.py ingest paper.pdf --category papers
python wikibrain/scripts/cli.py index

# Govern: scan for issues across all layers
python neatfreak/scripts/cli.py scan
```

### Key Commands

```bash
# FileStates — never write directly again
python filestates/scripts/cli.py fs_write path/to/file.py "content" source
python filestates/scripts/cli.py fs_rewind path/to/file.py 1   # undo last write

# CodeGraph — understand your codebase
python codegraph/scripts/cli.py search "function_name"
python codegraph/scripts/cli.py blast "critical_function" 200

# WikiBrain — query your knowledge
python wikibrain/scripts/cli.py query "research question" 10
python wikibrain/scripts/cli.py lint

# NeatFreak — keep it clean
python neatfreak/scripts/cli.py report
python neatfreak/scripts/cli.py fix --apply
```

## Design Principles

- **Layered, not monolithic.** Each skill does one thing and depends downward.
- **Safety-gated.** NeatFreak has three explicit modes; destructive operations require agent confirmation.
- **Index once, query many.** CodeGraph and WikiBrain both build SQLite FTS5 indexes for fast retrieval.
- **Agent-native.** Designed for AI agents to use as tools — CLI interfaces, structured output, self-contained dependencies.

## License

MIT © 2026 007WorkLab
