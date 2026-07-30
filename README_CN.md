# Manager Skills Box

AI Agent 工作空间管理的分层工具箱 — 文件追踪、代码分析、知识编译、质量治理。

## 架构

```
┌─────────────────────────────────────────────────────┐
│  P2  NeatFreak     质量治理层                        │
│       Scan / Fix / Clean → 三级安全保障              │
├─────────────────────────────────────────────────────┤
│  P1  CodeGraph      代码感知层                       │
│       AST → SQLite 图谱 → 影响范围分析               │
│  P1  WikiBrain      知识引擎层                       │
│       摄入 → 编译 → 索引 → 查询                      │
├─────────────────────────────────────────────────────┤
│  P0  FileStates     基础层                           │
│       快照 / 回滚 / 计划 / 文件角色追踪              │
└─────────────────────────────────────────────────────┘
```

上层依赖下层。P0 是基石——所有文件操作都经过它。P1 在基础上构建能力。P2 跨层治理。

## Skills

| Skill | 层级 | 职责 | 来源 |
|-------|------|------|------|
| **FileStates** | P0 | 每次写入自动快照、支持回滚。按角色标注文件（source/test/doc/config）。计划模式：创建、追踪、验收任务计划。 | 内部工具链 |
| **CodeGraph** | P1 | 用 Tree-sitter 解析代码（Python/JS/TS/Java/Go/Rust/C/C++），构建 SQLite 调用图谱。影响范围分析："改了 X 会波及哪些模块？" | 内部工具链 |
| **WikiBrain** | P1 | 原始资料 → 结构化 wiki。并行摄入、frontmatter 索引、FTS5 全文搜索、死链检测、会话反馈提炼。 | 内部工具链 |
| **NeatFreak** | P2 | 聚合所有底层的质量信号。三种安全模式：Scan（只读检测）、Fix（确定性修复）、Clean（agent 监督下深度清理）。 | 内部工具链 |
| **hw-normalization-design** | -- | 四层归一化设计方法论：器件 → 单板 → 平台 → 网络架构。 | 华为硬件平台设计 |
| **project-delay-prevention** | -- | 研发项目防拖延六步法：从用人到计划到跟踪到闭环。 | 华为研发管理实践 + 曾国藩识人用人 |
| **topic-analysis-driven-design** | -- | 用"专题分析"取代"画图-调试-改版"，先电源/时钟/小系统，再动手画原理图。 | 华为硬件设计方法论 |

## 快速上手

```bash
git clone https://github.com/JuliaHZhu/manager-skills-box.git
cd manager-skills-box
```

每个 skill 自包含在独立目录中：`SKILL.md` 说明 + `scripts/` 脚本 + 辅助文件。

### 初始化与索引

```bash
# 基础层：追踪工作区文件
python filestates/scripts/cli.py plan new my-task --objective="构建 X 功能" --goal-kind=feature

# 代码层：索引源码树
python codegraph/scripts/cli.py init
python codegraph/scripts/cli.py index ./src

# 知识层：从原始资料构建 wiki
python wikibrain/scripts/cli.py init
python wikibrain/scripts/cli.py ingest paper.pdf --category papers
python wikibrain/scripts/cli.py index

# 治理层：扫描全栈问题
python neatfreak/scripts/cli.py scan
```

### 核心命令

```bash
# FileStates — 不再裸写文件
python filestates/scripts/cli.py fs_write path/to/file.py "内容" source
python filestates/scripts/cli.py fs_rewind path/to/file.py 1   # 回滚上一次写入

# CodeGraph — 理解代码库
python codegraph/scripts/cli.py search "函数名"
python codegraph/scripts/cli.py blast "关键函数" 200

# WikiBrain — 查询知识库
python wikibrain/scripts/cli.py query "研究问题" 10
python wikibrain/scripts/cli.py lint

# NeatFreak — 保持整洁
python neatfreak/scripts/cli.py report
python neatfreak/scripts/cli.py fix --apply
```

## 设计原则

- **分层不单体。** 每个 skill 专注一件事，依赖方向向下。
- **安全门控。** NeatFreak 三级模式明确；破坏性操作需 agent 确认。
- **一次索引，多次复用。** CodeGraph 和 WikiBrain 都构建 SQLite FTS5 索引。
- **Agent 原生。** 为 AI agent 作为工具调用而设计——CLI 接口、结构化输出、自包含依赖。

## 许可证

MIT © 2026 007WorkLab
