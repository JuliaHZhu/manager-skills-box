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
| **ipd-charter-developer** | -- | Charter开发方法论：像开发产品一样开发Charter，端到端跨职能团队参与商业计划制定。 | 华为IPD变革管理手册（5版，2023） |
| **ipd-product-launch** | -- | 产品上市管理：受控上市、逐步放量、ADCP评审、"一五一"上市法、"一纸禅"销售法。 | 华为IPD变革管理手册（5版，2023） |
| **ipd-lifecycle-manager** | -- | 产品生命周期管理：LDCP评审、版本切换、退市规划、主动衰退管理。 | 华为IPD变革管理手册（5版，2023） |
| **ipd-change-management** | -- | IPD变革管理：先僵化→再固化→后优化。三阶段推行、试点验证、逐步推广。 | 华为IPD变革管理手册（5版，2023） |
| **ipd-cross-functional-team** | -- | 跨部门团队运作：IPMT/PDT组织架构、DCP决策评审、双线汇报矩阵。 | 华为IPD变革管理手册（5版，2023） |
| **hw-derating-design** | -- | 器件降额设计：稳态/瞬态应力分析、温度极限、降额审查流程。 | 华为硬件研发实践 |
| **hw-halt-hass-testing** | -- | HALT/HASS高加速试验：步进应力至失效、工作/破坏极限、生产筛选。 | 华为硬件研发实践 |
| **hw-dfm-design** | -- | 可生产性设计：连接器设计、公差分析、螺钉标准化、装配时间优化。 | 华为硬件研发实践 |
| **hw-reliability-design** | -- | 硬件可靠性设计体系：热设计、冗余、EMC、漂移、互连、环境适应性。 | 华为硬件研发实践 |
| **hw-component-failure-analysis** | -- | 元器件失效分析八步法：电测、X-Ray、开封、SEM、FA、根因、纠正措施。 | 华为硬件研发实践 |
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
| **ceg-expert-group** | -- | 物料专家团（CEG）运作方法论：跨部门采购决策组织、集体表决机制、供应商认证治理。 | 华为采购管理 |
| **tqrdc-supplier-evaluation** | -- | TQRDC + ES 七维供应商综合评价：技术、质量、响应、交付、成本、环境、社会责任。 | 华为采购管理 |
| **procurement-strategy-designer** | -- | 采购策略设计：协议供应、有限竞争、拆分组合三种策略的选择与组合应用。 | 华为采购管理 |
| **supplier-lifecycle-manager** | -- | 供应商全生命周期管理：寻源→认证→选择→绩效→CSR→退出，含CRCPE五步改进法。 | 华为采购管理 |
| **procurement-ethics-guardian** | -- | 采购合规与行为准则：利益回避、信息保密、馈赠限制、两人原则、离职限制。 | 华为采购管理 |
| **emergency-procurement-protocol** | -- | 应急采购三级响应：立即抢修/尽快实施/政府指令，事后审计防止滥用。 | 华为采购管理 |
| **vmi-inventory-designer** | -- | VMI供应商管理库存设计：库存前移交易模式、法律框架、系统对接、五步落地法。 | 华为采购管理 |
| **five-looks-market-insight** | -- | 五看市场洞察法：看行业/趋势、看客户、看竞争、看自己、看机会。战略设计前的结构化扫描。 | 华为战略管理 |
| **blm-strategic-planning** | -- | BLM业务领先模型：差距分析→市场洞察→战略意图→创新焦点→业务设计→执行体系。 | 华为战略管理 |
| **business-model-five-elements** | -- | 业务模式五要素设计：客户选择+价值主张+盈利模式+战略控制+业务范围。 | 华为战略管理 |
| **strategic-control-point** | -- | 战略控制点四级评估：高/中/低/无利润保护能力评级与升级路径。 | 华为战略管理 |
| **strategy-decoding-sp-bp** | -- | 战略解码：SP（战略规划）到BP（业务计划）分解，组织KPI与个人PBC。价值创造决定价值分配。 | 华为战略管理 |
| **stretch-goals-capability-building** | -- | 高目标倒逼能力建设：机会逻辑替代延长线思维，用差距创造"创造性张力"。 | 华为战略管理 |
| **org-capability-elevation** | -- | 组织能力升维：五层级管理能力（业务→职能→要素→协作→战略）诊断与升级路径。 | 华为战略管理 |
| **dste-strategy-execution** | -- | DSTE战略运营流程：SP→BP→预算→KPI→PBC→监控的闭环管理日历。 | 华为战略管理 |
| **global-market-entry-strategist** | -- | 全球市场进入策略师：农村包围城市路径、市场吸引力×竞争力矩阵、阶段聚焦、进入模式组合。 | 华为国际化 |
| **brand-globalization-builder** | -- | 品牌全球化建设者：三阶段模型（造势→外交→检阅）、跨文化品牌传播、B2B到B2C信任迁移。 | 华为国际化 |
| **glocalization-operator** | -- | 全球本土化运营者：全球资源整合+本地价值创造、能力中心与共享中心布局、本土化率的度。 | 华为国际化 |
| **cross-culture-team-commander** | -- | 跨文化团队指挥官：核心价值观全球传递、外派与本地化人才策略、TUP长效激励、一把手选派。 | 华为国际化 |
| **global-rd-footprint-architect** | -- | 全球研发布局架构师：研究所、联合创新中心、能力中心的三层架构与各国比较优势地图。 | 华为国际化 |
| **global-innovation-leap-strategist** | -- | 全球创新跃迁策略师：针尖战略、边缘到主流突破、压强投入、知识产权与标准卡位。 | 华为国际化 |
| **intl-crisis-resilience-builder** | -- | 国际化韧性建设者：备胎思维、低谷坚持、危机差异化响应、极限生存预案。 | 华为国际化 |
| **rd-project-classifier** | -- | 研发项目四分法：大客户定制/新产品开发/新技术开发/预研，差异化管理策略。 | 华为研发管理 |
| **product-manager-compass** | -- | 产品经理罗盘：产品经理定位与五大素质模型（需求/规划/质量/上市/体系建设）。 | 华为研发管理 |
| **five-force-talent-developer** | -- | 五力人才开发者：研发人员培养五力模型（学习力/激励力/发展力/资格力/胜任力）。 | 华为研发管理 |
| **innovation-seven-principles** | -- | 创新七原则：反对盲目创新、双轮驱动、领先半步、一杯咖啡、继承创新、宽容失败、知识产权。 | 华为研发管理 |
| **blue-army-evolution** | -- | 蓝军进化论：从Femto到LampSite的实战演进，蓝军五阶段转化模型。 | 华为研发管理 |
| **rd-incentive-architect** | -- | 研发激励架构师：机制优先论，短中长期分层激励，股权激励设计框架。 | 华为研发管理 |
| **position-based-pay-architect** | -- | 职位薪酬体系设计：以岗定级→以级定薪→人岗匹配→易岗易薪。含HAY三维度八要素法。 | 华为薪酬管理 |
| **executive-compensation-negotiator** | -- | 高管薪酬谈判：3P1M模型、LEADER谈判框架、5C人才匹配法。 | 华为薪酬管理 |
| **result-oriented-appraiser** | -- | 结果导向绩效评估：不为假动作付酬、三类劳动者划分、贡献导向分配。 | 华为薪酬管理 |
| **compensation-strategy-evolver** | -- | 薪酬战略演化：三阶段薪酬战略（初创/高速成长/成熟）、效率优先兼顾公平。 | 华为薪酬管理 |
| **award-culture-designer** | -- | 发奖文化设计：仪式感、奖励创新、从零起飞奖、让奖励成为管理手段。 | 华为薪酬管理 |
| **qq-sticker-maker** | -- | QQ 动态表情包制作工作流：场景插画 + Emoji 角色合成，APNG 动画导出与压缩。 | 创作工具 |

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
