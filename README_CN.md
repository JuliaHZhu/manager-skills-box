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
| **darwin-skill** | -- | 自主 Skill 优化器。9 维评分 rubric、定向优化、独立 judge agent、验证门控设计、可视化结果卡片。 | SkillLens (MSR) + SkillOpt + alchaincyf |
| **assumption-hunter** | -- | 找出论证中被默认的隐藏假设。跳出系统（Jootsing），源自丹尼特《直觉泵》Ch8。 | Daniel Dennett |
| **intentional-stance** | -- | 三视角分析同一现象：物理/制度/博弈。源自丹尼特《直觉泵》Ch18。 | Daniel Dennett |
| **piling-on-detector** | -- | 检测"故意堆积"：多个主张打包，驳倒一个就当全驳倒。源自丹尼特《直觉泵》Ch9。 | Daniel Dennett |
| **reductio-ad-absurdum** | -- | 接受前提，推到荒谬，检验矛盾。源自丹尼特《直觉泵》Ch2。 | Daniel Dennett |
| **mediation-model-designer** | -- | 设计简单、并行、串行及多分类中介模型。从理论假设到统计方程与PROCESS模型选择。 | Hayes (2022) |
| **indirect-effect-inference** | -- | Bootstrap / Monte Carlo 间接效应推断。取代过时的Sobel检验与因果步骤法。 | Hayes (2022) |
| **moderation-prober** | -- | pick-a-point / Johnson–Neyman 交互探测。含条件效应可视化与简单斜率图。 | Hayes (2022) |
| **conditional-process-builder** | -- | 构建条件过程（有调节的中介）模型。将概念图映射到PROCESS模型编号。 | Hayes (2022) |
| **effect-scaling-guide** | -- | 效应量标准化指南：非标准化/完全标准化/部分标准化的选择与报告。 | Hayes (2022) |
| **multicategorical-mediation** | -- | 多分类前因变量的中介、调节与条件过程分析。指示/顺序/Helmert编码。 | Hayes (2022) |
| **process-model-reporter** | -- | 期刊标准结果写作。从回归系数到完整结果段落的结构化报告。 | Hayes (2022) |
| **antipattern-diagnostician** | -- | 中介与调节分析常见误区诊断：Baron&Kenny、中位数分割、完全标准化二分类变量等。 | Hayes (2022) |
| **triad-classification** | -- | 三元结构分类：脆弱 / 强韧 / 反脆弱。评估事物在波动/压力下的表现。 | 塔勒布《反脆弱》 |
| **fragility-diagnosis-checklist** | -- | 脆弱性诊断清单：10个问题快速评估系统/策略/职业/投资是否脆弱。 | 塔勒布《反脆弱》 |
| **barbell-strategy** | -- | 杠铃策略：极端安全+极端冒险，抛弃中间态。投资组合、职业规划、学习路径。 | 塔勒布《反脆弱》 |
| **convexity-spotting** | -- | 凸性识别：判断收益结构是凸性（损失有限/收益无限）还是凹性（波动有害）。 | 塔勒布《反脆弱》 |
| **optionality-evaluation** | -- | 可选性评估：判断选项是否拥有"免费选择权"——下行有限、上行无限。 | 塔勒布《反脆弱》 |
| **fat-tony-heuristic** | -- | 胖子托尼启发法：不预测未来，只识别谁在当前状态下是脆弱的。 | 塔勒布《反脆弱》 |
| **via-negativa-decision** | -- | 否定法决策：选项太多时，用排除法先消除最坏的选项。 | 塔勒布《反脆弱》 |
| **lindy-filter** | -- | 林迪效应筛选：古老而存活的事物比新潮事物更可靠。技术栈、学习方法、职业方向。 | 塔勒布《反脆弱》 |
| **skin-in-the-game** | -- | 切身利益检验：评估建议/决策的可信度——建议者是否承担后果。 | 塔勒布《反脆弱》 |
| **intervention-threshold-test** | -- | 干预阈值测试：六步审查协议评估行动必要性，优先"减法"和"不行动"。 | 塔勒布《反脆弱》 |
| **iatrogenics-principle** | -- | 医源性原则：评估拟议行动是否可能带来比收益更大的伤害。 | 塔勒布《反脆弱》 |
| **narrative-fallacy-immunity** | -- | 叙述谬误免疫：区分"可叙述的知识"与"可行动的知识"，防止被事后故事误导。 | 塔勒布《反脆弱》 |
| **extremistan-detector** | -- | 极端斯坦探测器：判断领域属于平均斯坦还是极端斯坦，避免错误统计直觉。 | 塔勒布《黑天鹅》 |
| **gaussian-illusion-detector** | -- | 高斯幻觉检测器：识别在极端斯坦中误用正态分布/钟形曲线的致命危险。 | 塔勒布《黑天鹅》 |
| **platonification-detector** | -- | 柏拉图化检测器：识别把现实削足适履塞进理论模型的危险。地图≠领土。 | 塔勒布《黑天鹅》 |
| **silent-evidence-analyzer** | -- | 沉默证据分析器：基于"成功案例"做判断时，识别未被记录的反面证据。 | 塔勒布《黑天鹅》 |
| **turkey-problem-detector** | -- | 火鸡问题检测器：识别把稳定性误认为永久性的错误，1000天喂食≠第1001天安全。 | 塔勒布《黑天鹅》 |
| **gray-rhino-spotter** | -- | 灰犀牛识别器：识别显而易见却被忽视的高概率危机。不是"能否"而是"何时"。 | 渥克《灰犀牛》 |
| **rhino-stage-diagnoser** | -- | 五阶段诊断器：判断团队处于否认/得过且过/诊断/恐慌/行动哪个阶段。 | 渥克《灰犀牛》 |
| **rhino-classifier** | -- | 灰犀牛分类器：按类型分类（反复出现/发起冲锋/元犀牛/多米诺/戈尔迪之结/革新颠覆）。 | 渥克《灰犀牛》 |
| **denial-breaker** | -- | 打破否认器：打破"不会的，没那么严重"的心理防线。数据冲击/外部视角/反群体思维。 | 渥克《灰犀牛》 |
| **procrastination-interrupter** | -- | 得过且过打断器：打断"再等等"的拖延状态。制造紧迫感/缩小决策单元/明确责任。 | 渥克《灰犀牛》 |
| **panic-to-action-bridge** | -- | 恐慌到行动桥：从恐慌回到理性。物理暂停/数据锚定/预设机制/分而治之。 | 渥克《灰犀牛》 |
| **measure-change-scale** | -- | 测量-改变-规模化：把顿悟时刻变成持续的组织能力。系统变革落地框架。 | 渥克《灰犀牛》 |
| **crisis-as-opportunity** | -- | 危机即机遇：灾后重建。止血→复盘→重新定义→不可浪费的行动→制度化。 | 渥克《灰犀牛》 |

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
