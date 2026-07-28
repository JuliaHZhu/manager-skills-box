# Skill: WikiBrain

## Description

P1 能力层 — 知识库编译与管理。采用"一次编译，多次复用"范式：原始资料 → 结构化 wiki 页面 → 可查询/可产出。支持并行调研、会话记忆提炼和质量巡检。

## When to Use

- 需要整理/消化大量资料时
- 做深度调研、文献综述时
- 需要建立可复用的主题知识库时
- 想从会话历史中提取持久化经验时
- 需要基于知识库生成报告/计划时

## Dependencies

- **FileStates** (P0) — 追踪知识文件变更，触发增量编译

## Tools

### CLI Commands

```bash
# 初始化目录结构
python workspace/skills/wikibrain/scripts/cli.py init

# 摄入资料到 raw/
python workspace/skills/wikibrain/scripts/cli.py ingest <file_path> [category]

# 索引 wiki 页面（frontmatter + 双链）
python workspace/skills/wikibrain/scripts/cli.py index

# 查询知识库
python workspace/skills/wikibrain/scripts/cli.py query <query> [limit]

# 质量巡检
python workspace/skills/wikibrain/scripts/cli.py lint

# 提炼会话反馈
python workspace/skills/wikibrain/scripts/cli.py extract-feedback
```

## Directory Structure

```
knowledge/
├── raw/          ← 原始资料（不可变）
│   ├── papers/
│   ├── articles/
│   └── notes/
├── wiki/         ← 编译后的知识页面
│   ├── concepts/
│   ├── entities/
│   ├── _index.md
│   └── schema.md
└── output/       ← 产出物
```

## Page Template

```markdown
---
title: "Page Title"
category: concept
tags: [tag1, tag2]
created: "2026-07-28"
---

# Page Title

## Definition

## Related Concepts
- [[Other Page]]

## Sources
- 
```

## Workflow

1. **Ingest** — 收集原始资料到 `raw/`
2. **Compile** — 阅读并提炼为 `wiki/` 结构化页面
3. **Index** — 运行 indexer 建立全文索引
4. **Query** — 通过索引快速检索知识
5. **Lint** — 定期巡检质量（孤立页/死链/缺失元数据）
6. **Output** — 基于 wiki 生成报告、计划、对比表

## Rules

1. 原始资料放入 `raw/` 后不直接修改，通过编译生成 `wiki/`
2. 每个 wiki 页面必须有 YAML frontmatter（title + category）
3. 用 `[[Wiki Link]]` 建立页面间关联，避免知识孤岛
4. 查询时优先使用索引，避免全目录扫描
5. 会话中的关键纠正和偏好应通过 `extract-feedback` 写入 wiki
