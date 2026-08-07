---
name: finance-three-pillar-architect
description: When the user needs to design or restructure an enterprise finance organization, discuss "how to set up finance departments", "COE/BP/SSC division of labor", "shared service center construction", or "how the finance system supports business". Applicable to large-enterprise finance organization design, finance function transformation, and shared service center building. Not applicable to pure financial software selection or small-business bookkeeping.
---

# finance-three-pillar-architect

## R (Reading)
> "华为集团财经组织总体也可以概括为三支柱模型，即 COE、BP 组织和 SSC。" (Ch49)
> "COE 是华为财经的'经线'，是立足于专业领域的行政管理组织……负有制定全集团政策、发布文件和制度的责任。" (Ch49)
> "BP 组织是华为财经的'纬线'，是业务伙伴和价值整合者……面向业务，以作战需求为中心，为业务提供财经集成解决方案。" (Ch49)
> "华为 SSC 始建于 2005 年……七大标准化 SSC 负责所辖区域的应付账款、销售核算和经营分析报告。" (Ch49)

## I (Interpretation)
华为财经三支柱不是简单的职能拆分，而是**纵横交织的矩阵架构**：
- **COE（经线）** = 专业能力中心 + 政策发动机。管规则、管方法论、管高层决策支持，但不直接插手业务操作。
- **BP（纬线）** = 业务嵌入型财经伙伴。管项目、管产品线、管区域经营，把财经能力注入业务决策现场。
- **SSC（共享层）** = 效率工厂 + 数据底座。管核算、管报告、管标准化作业，通过规模效应降低成本。

关键设计原则：**COE 出政策，BP 用政策打仗，SSC 把仗的结果算清楚**。

## A1 (Past Application)
华为 2005 年在马来西亚建立第一个账务 SSC，覆盖亚太部分国家；后续扩展至深圳、成都、罗马尼亚、毛里求斯、阿根廷、巴西七大区域 SSC，以及成都全球 SSC 负责资产/应收/关联交易核算。COE 中的经营管理部主导公司三张报表平衡，通过计划预算核算机制揭示经营风险；销售融资部构建全球金融资源关系，管理客户信用。区域财经 BP 作为"片联、BG、系统部的业务伙伴和价值整合者"，确保面向各客户的经营目标达成。

## A2 (Future Trigger)
- 公司要新建/拆分财务部门，不知道职能怎么划分
- 财务团队被抱怨"只懂做账不懂业务"
- 考虑建共享服务中心但担心和业务脱节
- 集团管控与一线灵活性的矛盾突出
- 需要从核算型财务向战略型财务转型

## E (Execution)
1. **诊断现状**：盘点现有财务职能，区分"规则制定""业务嵌入""交易处理"三类工作各占多少人力，识别痛点（如业务抱怨财务慢、财务抱怨业务乱）。
2. **设计三支柱分工**：
   - COE：集团层面设经营管理、资金、税务、账务政策、内控等职能，输出统一政策和基线；不直接审批单笔业务。
   - BP：按产品线/区域/客户线派驻财经人员，参与项目投标、合同评审、经营分析；考核与业务单元经营结果挂钩。
   - SSC：集中处理应付、应收、费用报销、报表编制；对数据质量和效率负责，通过 SLA 与 BP/业务衔接。
3. **建立衔接机制**：COE 制定政策时必须征求 BP 代表参与评审；BP 提出的业务例外需求通过 COE 走政策升级；SSC 的核算数据直接支撑 BP 的经营分析和 COE 的集团报告。
4. **渐进落地**：先选 1-2 个业务单元试点 BP 派驻，同时把最标准化的核算职能（如费用报销）迁入 SSC，成熟后再扩展。

## B (Boundary)
- 小微企业（<100人）没必要硬套三支柱，容易人为制造组织复杂度。
- 数字化基础极差（连基本 ERP 都没有）的企业，应先补系统再谈 SSC。
- 三支柱拆分后如果缺乏强有力的集团财经管理部统筹，容易变成"三张皮"互相扯皮。
- 本书案例基于华为 8000 人财经团队和全球 170+国家布局，直接照搬中小企业会水土不服。
