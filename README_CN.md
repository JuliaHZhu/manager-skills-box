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
| **scor-racetrack-improver** | -- | SCOR模型+跑道图五阶段改善：诊断、对标、流程映射、项目优先级排序、供应链转型实施。 | 华为供应链管理 |
| **supply-chain-digitizer** | -- | 供应链数字化转型：数字化→数智化→数治化三阶段，数字孪生，灵鲲/灵蜂双层智能架构。 | 华为供应链管理 |
| **global-supply-network-architect** | -- | 全球供应网络架构设计：标准化与个性化平衡，供应/采购/配送中心布局，ERP全球化推广。 | 华为供应链管理 |
| **supply-chain-triad-collaborator** | -- | 供应链三协同与铁三角：研发+销售+供应链协同，以铁三角（AR/SR/FR）打破部门墙。 | 华为供应链管理 |
| **strategic-sourcing-tco** | -- | 战略采购与总成本决策：从单价谈判转向全成本视角（运输/库存/风险/质量/可持续）。 | 华为供应链管理 |
| **supplier-field-auditor** | -- | 供应商现场审核作业：八步流程、三类表单、十维评价框架，用于准入审核与改善推动。 | 华为供应链管理 |
| **five-looks-market-insight** | -- | 五看市场洞察法：看行业/趋势、看客户、看竞争、看自己、看机会。战略设计前的结构化扫描。 | 华为战略管理 |
| **blm-strategic-planning** | -- | BLM业务领先模型：差距分析→市场洞察→战略意图→创新焦点→业务设计→执行体系。 | 华为战略管理 |
| **business-model-five-elements** | -- | 业务模式五要素设计：客户选择+价值主张+盈利模式+战略控制+业务范围。 | 华为战略管理 |
| **strategic-control-point** | -- | 战略控制点四级评估：高/中/低/无利润保护能力评级与升级路径。 | 华为战略管理 |
| **strategy-decoding-sp-bp** | -- | 战略解码：SP（战略规划）到BP（业务计划）分解，组织KPI与个人PBC。价值创造决定价值分配。 | 华为战略管理 |
| **stretch-goals-capability-building** | -- | 高目标倒逼能力建设：机会逻辑替代延长线思维，用差距创造"创造性张力"。 | 华为战略管理 |
| **org-capability-elevation** | -- | 组织能力升维：五层级管理能力（业务→职能→要素→协作→战略）诊断与升级路径。 | 华为战略管理 |
| **dste-strategy-execution** | -- | DSTE战略运营流程：SP→BP→预算→KPI→PBC→监控的闭环管理日历。 | 华为战略管理 |
| **cross-border-strategist** | -- | 跨界战略决策师：错误清单→产业节点→战略空间→独立运作→压强投入五步框架，B2B转B2C转型手册。 | 华为跨界管理 |
| **main-channel-guardian** | -- | 主航道边界守护者：三维检验法、不做边界外的事、平台三不原则。 | 华为跨界管理 |
| **pressure-focus-investor** | -- | 压强原则投资者：战略生长点地图、三代战略储备、压强指数计算。 | 华为跨界管理 |
| **backup-plan-architect** | -- | 备胎战略架构师：四层备胎分级、狗食自吃原则、转正触发机制设计。 | 华为跨界管理 |
| **full-stack-vertical-integrator** | -- | 全栈垂直整合者：能力地图绘制、缺失层诊断、整合路径选择、生态兼容策略。 | 华为跨界管理 |
| **black-soil-ecosystem-builder** | -- | 黑土地生态建设者：降低门槛、提供养分、平衡利益、让伙伴成功四步法。 | 华为跨界管理 |
| **crisis-deterrence-survivor** | -- | 危机威慑与极限生存者：威慑-生存双循环、五阶段切换协议、阵营构建三步法。 | 华为跨界管理 |
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
| **locomotive-bonus-designer** | -- | 火车头奖金与激励包设计：三层奖金生成、4:3:3业绩系数、组织到个人分配、削峰填谷。 | 华为薪酬管理 |
| **pbc-performance-contractor** | -- | PBC绩效承诺设计与拆解：战略解码→BSC→KPI→个人PBC，WET三要素，SMART标准，刷新机制。 | 华为绩效管理 |
| **forced-distribution-enforcer** | -- | 强制分布与绩效结果应用：5等级绝对定义、赛马机制、分层分级评价、10%末位淘汰。 | 华为绩效管理 |
| **org-performance-aligner** | -- | 组织绩效与个人绩效对齐：DSTE+BLM+PBC对接、戴帽子与拧麻花、预算与工资包管理。 | 华为绩效管理 |
| **rd-performance-designer** | -- | 研发体系绩效管理：效益/效率/路径/行为四维指标、IPD体系下研发绩效、项目制考核。 | 华为绩效管理 |
| **incremental-performance-driver** | -- | 增量绩效与价值分配：价值创造→评价→分配闭环、工资包管理、3人干5活拿4工资。 | 华为绩效管理 |
| **performance-coach-grow** | -- | 绩效辅导与GROW模型：教练式辅导、GROW四步法、绩效面谈、低绩效员工PIP管理。 | 华为绩效管理 |
| **performance-decomposition-engineer** | -- | 绩效过程分解工程师：把最终结果拆解为跨部门活动体系，让研产销服全链条为结果负责。 | 华为绩效管理 |
| **pricing-profit-lever** | -- | 定价利润杠杆分析：1%价格变化撬动10%利润，量化价格/成本/销量/固定成本四项杠杆效应。 | 华为财经管理 |
| **customer-centric-pricing** | -- | 客户利益导向定价体系：IPD+LTC耦合、价值定价转型、跨部门定价治理机制。 | 华为财经管理 |
| **price-anchoring-strategist** | -- | 价格锚点与心理定价：对比效应、第二杯半价模式、收益递减规避策略。 | 华为财经管理 |
| **budget-as-weapon** | -- | 预算作战化设计：预算从管控工具重塑为作战资源、一线服务文化、简化审批链。 | 华为财经管理 |
| **sp-budget-closure** | -- | 战略预算闭环：SP→BP→预算对齐、强制差异说明、红绿灯滚动监控。 | 华为财经管理 |
| **resource-allocation-guardian** | -- | 资源配置约束与倾斜：费用增长上限、向一线倾斜、效率指标（应收/存货）、负增长区域策略。 | 华为财经管理 |
| **admin-baseline-manager** | -- | 行政基线管理：二元分类（自治类vs标准化类）+ 国家颗粒度基线设计 + 节约分享/浪费分担激励机制。 | 华为行政管理 |
| **internal-service-marketizer** | -- | 内部服务市场化：基础保障与增值服务分层 + 私有化/竞争机制 + 动态租金/末位淘汰。 | 华为行政管理 |
| **lean-process-reformer** | -- | 流程简化与责任制：价值审计砍掉无价值步骤 + 非主干流程责任制 + 小循环颗粒度控制。 | 华为行政管理 |
| **expat-welfare-designer** | -- | 海外员工保障体系设计：食堂/医疗/住宿/关系润滑四支柱 + 伙委会自治 + 因国施策。 | 华为行政管理 |
| **it-value-transformer** | -- | IT价值定位转型：从成本中心到价值中心到利润中心，角色重塑与绩效重构。 | 华为IT管理 |
| **process-it-integrator** | -- | 流程IT一体化运作：跨部门项目组、流程Owner机制、端到端流程贯通。 | 华为IT管理 |
| **it-governance-architect** | -- | IT治理架构设计：EA三层架构、分层分级决策、版本火车、平衡计分卡。 | 华为IT管理 |
| **business-change-it-land** | -- | 业务变革IT落地：先僵化再固化后优化、软件包驱动、流程与能力解耦。 | 华为IT管理 |
| **roads-digital-transformer** | -- | ROADS驱动数字化转型：三大架构转变、前轻后重作业系统、多云架构。 | 华为IT管理 |
| **global-it-controller** | -- | 全球IT管控模式：集中控制分散资源、主干简捷末端灵活、一线驱动。 | 华为IT管理 |
| **project-four-accounting** | -- | 项目四算管理：概算→预算→核算→决算拉通，项目利润中心设计与CFO赋能。 | 华为财务管理 |
| **comprehensive-budget-manager** | -- | 全面预算管理：一次预算（机会点）+二次预算（资源配置）双层生成、弹性授予、预算对准战略。 | 华为财务管理 |
| **cost-control-twist-towel** | -- | 费用拧毛巾与成本管控：三招四式组合拳，保战略保客户前提下从内部运营挤水分。 | 华为财务管理 |
| **ifs-finance-transformation** | -- | IFS财经变革落地：以规则的确定对付结果的不确定，业财融合，CFO队伍建设。 | 华为财务管理 |
| **finance-bp-operator** | -- | 财务BP运作：三支柱模型（COE/BP/SSC），"在一起懂业务提建议"九字诀，五懂能力模型。 | 华为财务管理 |
| **plan-budget-accounting-closure** | -- | 计划预算核算闭环：SP/BP/PP三层嵌套闭环、滚动预测、代表处五循环运营体系。 | 华为财务管理 |
| **responsibility-center-commander** | -- | 责任中心指挥官：五层责任中心框架（利润/收入/费用/成本/投资中心）、前线利润问责、内部成本价结算。 | 华为财务管理 |
| **financial-statement-strategist** | -- | 财报战略解读师：三张表战略叙事、财报六看、软资产评估、利润质量诊断。 | 华为财务管理 |
| **expense-integrity-guardian** | -- | 费用诚信守护者：SSE自动化、诚信分值审计矩阵、主管问责制、风险导向事后审计。 | 华为财务管理 |
| **finance-digital-transformer** | -- | 财经数字化变革师：四阶段进化、四统一、MCA模块化合并、日不落结账、KCFR数据治理。 | 华为财务管理 |
| **financial-risk-three-lines** | -- | 财经风险三道防线：4×3风险架构（三类风险/三道防线/三层审结/三角联动）、财务蓝军。 | 华为财务管理 |
| **cfo-readiness-ladder** | -- | CFO继任准备阶梯：四级发展阶梯、财务金三角、混凝土结构轮岗、CEO级标准。 | 华为财务管理 |
| **qualification-standard-builder** | -- | 任职资格标准开发五步法：从职位分析到行为标准定义，含宽带化设计与"三句话讲清差异"原则。 | 华为任职资格体系 |
| **dual-channel-career-designer** | -- | 双通道职业发展设计：管理+专业双通道、五级晋升、顶端待遇拉平、跨通道转换机制。 | 华为任职资格体系 |
| **qualification-certifier** | -- | 任职资格认证设计：七步认证流程、证据导向评价、四等结果、专委会治理。 | 华为任职资格体系 |
| **competency-qualification-integrator** | -- | 素质模型与任职资格整合：冰山上下的定位、统一术语、轻量素质落地。 | 华为任职资格体系 |
| **learning-path-mapper** | -- | 基于任职资格的学习路径图设计：70-20-10培养、加速成长方案、分层成长路线。 | 华为任职资格体系 |
| **qualification-hr-integrator** | -- | 任职资格与HR体系整合：以岗定级定薪、绩效边界厘清、晋升门槛设计。 | 华为任职资格体系 |
| **admin-support-qualification-architect** | -- | 行政支持类任职资格架构设计：双通道五级分类、单元-要素行为标准、四维度门槛设计。 | 华为秘书任职资格体系 |
| **secretary-excellence-ladder** | -- | 九段秘书卓越工作法：从任务执行到体系建设，含三层楼境界与四重成熟度模型。 | 华为秘书任职资格体系 |
| **routine-exception-delegator** | -- | 例行与例外管理分离设计：经理管例外、秘书管例行，组织时间价值优化。 | 华为秘书任职资格体系 |
| **meeting-management-master** | -- | 会议管理全流程方法论：会前三要点、会中三服务、会后三件事，外加查三遍质控。 | 华为秘书任职资格体系 |
| **executive-support-system-designer** | -- | 高管支持体系设计：秘书定位、五项核心职责、成长通道、规范化服务体系。 | 华为秘书任职资格体系 |
| **behavioral-standards-engineer** | -- | 行为标准工程师：任务到能力转化、分级行为描述、NVQ本土化、认证重点设计。 | 华为秘书任职资格体系 |
| **industry-convergence-spotter** | -- | 产业融合机会识别：技术节奏匹配度、市场需求耦合度、基础设施整合度三维评估。 | 华为跨界管理 |
| **enterprise-digital-transformer** | -- | 企业数字化转型建筑师：五转四举措四难点、Malik曲线、数据治理打底。 | 华为跨界管理 |
| **limit-survival-strategist** | -- | 极限生存战略家：备胎体系、算力底座、生态开放，极端压力下的战略韧性构建。 | 华为跨界管理 |
| **second-curve-navigator** | -- | 第二曲线导航员：核心能力复用、边界克制、战略耐心培育新业务。 | 华为跨界管理 |
| **smart-meeting-operator** | -- | 智能会议运营家：会前准备×会中纪律×会后闭环，数字化会议效率提升。 | 华为跨界管理 |
| **cross-industry-ecosystem-builder** | -- | 跨产业生态构建师：XYZ立体版图、开放伙伴赋能、标杆案例规模化。 | 华为跨界管理 |
| **qq-sticker-maker** | -- | QQ 动态表情包制作工作流：场景插画 + Emoji 角色合成，APNG 动画导出与压缩。 | 创作工具 |
| **training-battle-designer** | -- | 训战结合设计师：训战闭环、战略预备队、重装旅训战营、选拔制非培养制。 | 华为人才发展与领导力 |
| **strategic-reserve-force-operator** | -- | 战略预备队运作机制：选拔→训战→实战→鉴定→回流闭环，组织换血与能力转换平台。 | 华为人才发展与领导力 |
| **mentor-system-builder** | -- | 导师制建设者：导师七角色、选拔匹配、协议过程、考核激励、晋升绑定。 | 华为人才发展与领导力 |
| **training-needs-analyst** | -- | 培训需求分析师：三硬三软六维框架、差距分析、培训ROI排序、过滤非培训问题。 | 华为人才发展与领导力 |
| **enterprise-university-architect** | -- | 企业大学架构师：获取分享制自运营、兼职讲师梯队、有偿服务、课程架构。 | 华为人才发展与领导力 |
| **iron-triangle-organizer** | -- | 铁三角组织者：AR+SR+FR一线作战单元、平台赋能、让听得见炮火的人决策。 | 华为人才发展与领导力 |
| **talent-inventory-ninebox** | -- | 九宫格人才盘点运营：绩效潜能矩阵、学习力四维评价、工作定量分析、岗位匹配度矩阵。 | 华为人才发展与领导力 |
| **culture-institutionalizer-huawei** | -- | 华为式文化建设三阶段：讨论达成共识、规范固化习惯、领导以身作则营造文化氛围。 | 华为人才发展与领导力 |
| **elite-soldier-civilian-architect** | -- | 精英+精兵+职员人才结构：素质绩效经验三达标、狼狈合作、之字形成长、训战结合、三权分立。 | 华为人才发展与领导力 |
| **hr-blueprint-strategist** | -- | HR顶层设计与纲要2.0：组织充满活力、物质精神双驱动、干部/人才/组织三对象、平台+业务团队。 | 华为人才发展与领导力 |
| **talent-exit-balancer** | -- | 人才退出与新老平衡：三板斧快速提效、四方案退出路径、新老员工薪酬矛盾化解。 | 华为人才发展与领导力 |
| **training-effect-measurer** | -- | 培训效果评估师：柯氏四级评估、培训转化率、对照组归因、课程淘汰机制。 | 华为人才发展与领导力 |
| **talent-prsw-framework** | -- | 人才管理PRSW框架：桃子（吸引）、绳子（留住）、鞭子（驱动）、筛子（淘汰）全周期管理。 | 华为人才发展与领导力 |
| **team-chemistry-builder** | -- | 班子搭配设计师：SHL班次模型、价值趋同优势互补、正职狼副职狈、冲锋型人才动态使用。 | 华为HR管理 |
| **bonus-package-architect** | -- | 奖金包架构师：四层级奖金包（公司-体系-组织-个人）、获取分享制、战略性悬赏制、兑换与调节机制。 | 华为HR管理 |
| **business-stage-appraiser** | -- | 业务阶段评估师：三段论绩效目标设计（成熟业务考利润、成长业务考增量、拓展业务考关键节点）。 | 华为HR管理 |
| **talent-trio-manager** | -- | 三类人才管理者：主官（大起大落）、专家（循环实战）、职员（稳定胜任）、去南郭化、干什么考什么。 | 华为HR管理 |
| **mid-leadership-accelerator** | -- | 中层领导力加速器：两项聚焦实战法、在岗教练、利益相关者评分、三个月迭代周期。 | 华为HR管理 |
| **talent-pipeline-accelerator** | -- | 人才梯队加速器：STAR精准选才、三段育才（底部淘汰+顶部保留+退出机制）、四位一体有效激励。 | 华为HR管理 |
| **audit-deterrence-architect** | -- | 审计威慑体系设计：审计独立性、三级监控体系、BC/审计/稽查职能边界、增值型审计转型。 | 华为财经管理 |
| **anti-corruption-protocol** | -- | 反腐败合规协议：BCG政策、礼品与招待规则、第三方廉洁管理、梯度处罚、公开除名查询。 | 华为财经管理 |
| **cadre-rescue-protocol** | -- | 干部监管与挽救协议：查处分离原则、挽救导向、集体决策、无罪推定、适度问责。 | 华为财经管理 |
| **cadre-selection-architect** | -- | 干部选拔架构师：四条标准、四力、九条、五项素质、关键事件、赛马文化、一线经验。 | 华为干部管理 |
| **cadre-appointment-tribunal** | -- | 干部任命与三权分立：AT/ST、建议/评议/否决、任用程序、配备八原则。 | 华为干部管理 |
| **cadre-performance-governor** | -- | 干部绩效治理：四象限、末位10%淘汰、述职体系、能上能下、三个祛除。 | 华为干部管理 |
| **cadre-vitality-diagnoser** | -- | 干部活力与组织健康诊断：使命感/责任感/能力三层次扫描+组织内卷十大表现+18种惰怠行为清单。 | 华为干部管理 |
| **cadre-culling-protocol** | -- | 干部淘汰与惰怠治理：13类不称职干部识别、18种惰怠行为清单、能上能下与末位淘汰落地。 | 华为干部管理 |
| **commander-staff-pairing** | -- | 狼狈主官配置：狼与狈、正副职搭配、决断力与执行力、主官主管模型。 | 华为干部管理 |
| **cadre-values-guardian** | -- | 干部作风与价值观：八条要求、艰苦奋斗、自我批判、品德底线、开放妥协灰度。 | 华为干部管理 |
| **cadre-90day-turnaround** | -- | 新干部90天转身：角色认知、管理教练、Quickwin、五次关键谈话、任前审视。 | 华为干部管理 |
| **pfc-pipeline-cultivator** | -- | PFC（项目财务控制）培养体系：四项基本要求、四种成长方向、补课+考试培养法、优秀PFC五特征。 | 华为财经管理 |
| **cost-incremental-evaluator** | -- | 成本增量评价：弹性预算vs量入为出、按增量价值评价成本、四问成本审查、人工成本优化。 | 华为财经管理 |
| **cost-five-focuses** | -- | 五大成本聚焦管理：设计成本（决定80%后续成本）、采购成本、质量成本（隐性成本）、库存成本、期间费用。 | 华为财经管理 |
| **finance-three-pillar-architect** | -- | 财经三支柱架构师：COE/BP/SSC 组织设计与运作，经线政策中心+纬线业务伙伴+共享效率底座。 | 华为财经管理 |
| **three-lines-defense-builder** | -- | 内控三道防线构建：流程责任制（业务主管是第一责任人）、风险监管体系、审计冷威慑。 | 华为财经管理 |
| **elastic-budget-strategist** | -- | 弹性预算与动态资源配置：预算白皮书六要素、滚动预测弹性授予、战略投入集团承担、管理核算方案。 | 华为财经管理 |
| **global-treasury-risk-manager** | -- | 全球资金与财务风险管控：全球融资体系、日清日结、流动性/汇率/利率/信用四风险、本地化结算中心。 | 华为财经管理 |
| **finance-business-integrator** | -- | 财务融入业务：项目概算、售前财经设计、项目CFO派驻、BP一线嵌入、账务贴近业务场景。 | 华为财经管理 |
| **growth-maximization-strategist** | -- | 成长最大化经营哲学：深淘滩低作堰、合理利润率、反周期投入、力出一孔、客户TCO与行业壁垒。 | 华为财经管理 |
| **wolf-pack-culture-builder** | -- | 狼性团队文化搭建：721法则、新员工三阶段培训、导师制融入、271末位淘汰。 | 华为干部与团队管理 |
| **iron-army-builder** | -- | 铁军打造四维模型：派得出（一线历练）、动得了（三维流动）、打得赢（绩效前25%）、不变质（持续奋斗）。 | 华为干部管理 |
| **cadre-shelf-operator** | -- | 干部货架化运营：四条标准、四力六大内涵、四种经验、四象限盘点、统一选人语言。 | 华为干部管理 |
| **cadre-reserve-west-pointer** | -- | 后备干部西点式培养：1/3选1/3淘汰漏斗、大学独立跟踪、三权分立监察、持续竞争上岗。 | 华为干部管理 |
| **cadre-battlefield-groomer** | -- | 战场选拔将军：从成功一线团队选拔、赏罚分明、责任结果+关键行为评价、激励强挂钩。 | 华为干部管理 |
| **emt-rotating-ceo-guardian** | -- | 轮值CEO与EMT自律宣言：铲除组织三大毒瘤（山头主义、腐败、惰怠）的两大机制。 | 华为干部管理 |
| **ren-cadre-tenets** | -- | 任正非干部管理思想十条：系统化干部管理自检框架。 | 华为干部管理 |

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
