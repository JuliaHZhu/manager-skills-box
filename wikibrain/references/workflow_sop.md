# WikiBrain Workflow SOP

## 1. Ingest（资料摄入）

- 将原始资料（PDF/文档/网页/笔记）放入 `knowledge/raw/{category}/`
- 自动或手动转换为 Markdown
- 每次摄入更新 FileStates 索引

## 2. Compile（知识编译）

- 阅读 raw/ 中的资料
- 提取概念、实体、关系
- 在 `knowledge/wiki/` 中创建结构化页面
- 使用 YAML frontmatter 标注元数据
- 用 `[[Wiki Link]]` 建立页面间关联

## 3. Index（索引构建）

- 运行 `wikibrain index` 提取所有 frontmatter 和双链
- 构建 SQLite FTS5 全文索引
- 支持快速查询和跨页面搜索

## 4. Query（查询复用）

- 优先查索引，再读具体页面
- 避免每次全目录扫描
- 限定 category/tag 缩小范围

## 5. Lint（质量巡检）

- 定期运行 `wikibrain lint`
- 检测：孤立页面、死链、缺失元数据
- 由 agent 判断并修复不确定的问题

## 6. Output（产出物生成）

- 基于 wiki 内容生成报告、对比表、计划书
- 输出到 `knowledge/output/`
