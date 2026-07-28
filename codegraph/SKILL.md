# Skill: CodeGraph

## Description

P1 能力层 — 代码结构感知。利用 Tree-sitter（或正则回退）解析项目代码的 AST，构建 SQLite 代码图谱，支持影响范围分析（Blast Radius）、多词搜索和代码溯源。

## When to Use

- 需要理解一个代码项目的结构时
- 修改代码前想评估影响范围（"改了 X 会波及哪些模块？"）
- 搜索特定函数/类/方法定义
- 做代码 review 或架构分析时

## Dependencies

- **FileStates** (P0) — 用于检测文件变更做增量更新

## Tools

### CLI Commands

```bash
# 初始化/确保数据库 schema
python workspace/skills/codegraph/scripts/cli.py init

# 索引项目代码（默认 workspace/src）
python workspace/skills/codegraph/scripts/cli.py index [src_dir]

# 影响范围分析 — 查找与某节点关联的所有代码
python workspace/skills/codegraph/scripts/cli.py blast <node_name> [max_nodes]

# 代码搜索 — 多词搜索函数/类/方法
python workspace/skills/codegraph/scripts/cli.py search <query> [limit]
```

## Database Schema

共享 `workspace/.filestates/index.db`：

- `code_nodes` — 代码节点（函数/类/方法/导入）
- `code_edges` — 调用/引用关系（有向边）
- `code_fts` — FTS5 全文索引（name + signature + body）

## Workflow

1. **Index** — 首次使用时索引项目代码
2. **Query** — 用 `search` 查找目标代码
3. **Analyze** — 用 `blast` 评估修改影响范围
4. **Update** — 代码变更后重新 `index`（增量更新，只处理变更文件）

## Rules

1. 索引前确保 FileStates 已初始化
2. 支持 Python / JavaScript / TypeScript / Java / Go / Rust / C / C++
3. 增量更新：利用 FileStates hash 检测，只重解析变更文件
4. Blast Radius 默认上限 500 节点，防止大图爆炸
