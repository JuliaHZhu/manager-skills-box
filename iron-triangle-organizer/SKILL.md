---
name: iron-triangle-organizer
description: Design and implement a frontline "iron triangle" operating model — where customer-facing teams integrate Account Manager, Solution Manager, and Delivery Manager into a unified decision-making cell. Covers organizational transformation from functional silos to integrated frontline teams, with platform empowerment and delegated authority. Based on Huawei's transformation to "let those who hear the gunfire call the shots." Use when the user needs to restructure frontline teams for faster customer response.
---

# iron-triangle-organizer

## When to Activate

Trigger when the user mentions:
- 铁三角 / iron triangle
- 让听得见炮火的人决策 / let those who hear gunfire call shots
- 一线呼唤炮火 / frontline calls for fire support
- 客户经理+解决方案+交付 / account + solution + delivery
- 前轻后重 / light front, heavy back
- 一线组织变革 / frontline org transformation
- 平台赋能一线 / platform empowering frontline

## Core Philosophy

> "让听得见炮火的人呼唤炮火，让呼唤炮火的人指挥炮火。"

华为铁三角的本质是**把决策权、资源调配权前移到离客户最近的地方**，打破职能部门的围墙，让一线成为利润中心。

## The Iron Triangle: Three Roles, One Team

| Role | 中文 | Core Responsibility | Key Skill |
|---|---|---|---|
| **Account Manager (AR)** | 客户经理 | 客户关系、商务谈判、回款 | 客户洞察与关系经营 |
| **Solution Manager (SR)** | 解决方案经理 | 技术方案设计、需求匹配 | 解决方案架构与整合 |
| **Delivery Manager (FR)** | 交付经理 | 项目交付、实施落地、客户满意 | 项目执行与风险管控 |

### Operating Principles

1. **共同目标**：三人共享同一个客户/项目的经营目标（收入、利润、满意度）
2. **共同决策**：关键决策三人共同商议，不是单一角色说了算
3. **共同担责**：项目成败三人同责，打破“销售签单、交付背锅”的割裂
4. **平台赋能**：后方平台（研发、供应链、财务、法务）按一线需求提供支撑

## Organizational Transformation Path

### Before: Functional Silos

```
客户 ← 销售部 ← 技术部 ← 交付部 ← 财务部
      （各自为政，客户被踢皮球）
```

### After: Integrated Frontline + Platform Support

```
        ┌─────────────────────┐
        │   铁三角（一线作战单元）  │
        │  AR + SR + FR = 一个团队  │
        └──────────┬──────────┘
                   │ 呼唤炮火
        ┌──────────┴──────────┐
        │   后方平台（重装旅/资源池） │
        │ 研发 供应链 财务 法务 人力   │
        │ 按一线需求快速响应支撑      │
        └─────────────────────┘
```

## Key Design Elements

### 1. 一线授权 (Frontline Authority)

| Decision Type | Authority Level |
|---|---|
| 客户报价（标准折扣内） | 铁三角自主决策 |
| 客户报价（超折扣） | 铁三角申请 → 平台快速审批 |
| 方案变更（标准范围内） | 铁三角自主决策 |
| 重大方案变更 | 铁三角 + 平台专家会审 |
| 资源调配（标准资源池） | 铁三角直接调用 |
| 特殊资源需求 | 铁三角呼唤 → 平台响应 |

### 2. 平台响应机制 (Platform Response)

- **呼唤炮火**：一线通过系统发出资源/支持请求
- **限时响应**：平台部门必须在规定时间内响应（如24小时）
- **按贡献结算**：平台部门的绩效与对一线的支持效果挂钩
- **重装旅支援**：重大战役由重装旅（专家池）直接派驻支援

### 3. 考核与激励 (Incentive Design)

- **铁三角作为一个整体考核**，不是AR、SR、FR分别考核
- 考核指标：客户满意度、项目利润、回款率、新机会挖掘
- 奖金分配由铁三角内部自行商议，公司不干涉

## Implementation Stages

| Stage | Action | Duration |
|---|---|---|
| **试点** | 选择1-2个关键客户/区域组建铁三角 | 3-6个月 |
| **固化** | 跑通流程、明确权责、建立系统支撑 | 6-12个月 |
| **推广** | 复制到所有关键客户/区域 | 12-24个月 |
| **深化** | 后方平台按铁三角需求重组 | 24-36个月 |

## Implementation Checklist

- [ ] 识别关键客户/区域（从最重要的开始试点）
- [ ] 为每个铁三角选配AR+SR+FR（能力互补、性格匹配）
- [ ] 明确铁三角的共同目标（经营指标而非职能指标）
- [ ] 设计授权清单：哪些决策铁三角可以自主做
- [ ] 建立平台响应SLA（响应时限、升级路径）
- [ ] 改造考核：从个人/部门考核 → 铁三角整体考核
- [ ] 建立呼唤炮火的信息系统/流程
- [ ] 设计平台部门的内部结算机制（一线为服务付费）

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| 铁三角只有形式、没有授权 | 一线还是请示汇报，响应速度无改善 |
| AR独大、SR/FR变成跟班 | 失去三角制衡，决策质量下降 |
| 平台部门不愿放权 | 一线呼唤炮火，平台装听不见 |
| 考核仍按部门分别进行 | 三角内部互相推诿，没有共同利益 |
| 全员同时推广、没有试点 | 问题爆发时无法调头，变革失败 |

## Example Interaction

**User**: 我们销售签单后交付总是出问题，销售和交付互相甩锅，怎么破？

**Skill Response**:
> 这是典型的“铁路警察各管一段”问题。铁三角就是专门解决这个的。
>
> **核心逻辑**：让签单的人和交付的人**从一开始就坐在一起**。
>
> 改造方案：
> 1. **组建铁三角**：针对TOP 10大客户，每个客户配一个AR（销售）+ SR（方案）+ FR（交付），三人绑定
> 2. **共同目标**：不再考核AR“签了多少单”，而是考核三角整体“客户利润+满意度+回款”
> 3. **交付前置**：FR从商机阶段就参与，评估交付可行性，SR设计方案时FR在场
> 4. **共同背锅**：项目出问题，三角一起复盘；不是“销售乱承诺”，而是“我们当时怎么一起评估的”
> 5. **奖金池共享**：项目奖金先打到三角账户，三人自行商议分配
>
> **关键提醒**：不要一开始就全员推广。选1-2个最有代表性的客户试点，跑通后再复制。试点期间最大的阻力通常来自平台部门（财务、法务、供应链）不愿放权——需要最高层明确表态支持。