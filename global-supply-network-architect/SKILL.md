---
name: global-supply-network-architect
description: Design global supply network topology balancing centralization and localization, including supply center / procurement center / distribution center placement, ERP globalization, and order intelligent routing. Use when the user discusses global supply chain expansion, overseas supply center setup, international logistics network design, or resolving the standardization-vs-personalization dilemma in global operations.
---

# global-supply-network-architect

Design global supply network topology by balancing headquarters centralization with local market personalization, and build the supporting IT and operational capabilities.

## When to Use

- The user asks about global supply chain design, overseas expansion logistics, or international supply network layout
- The user faces the "standardization vs. personalization" dilemma in global operations
- The user needs to decide where to place supply centers, procurement centers, or regional distribution centers
- The user is rolling out ERP or supply chain systems to overseas subsidiaries
- The user needs intelligent order routing across a multi-node global network

## Core Dilemma: Standardization vs. Personalization

Global supply chains must balance two forces:
- **Centralization**: economies of scale, shared resources, lower cost, unified standards
- **Localization**:贴近客户, fast response, high customer satisfaction, regulatory compliance

**Resolution principle**:共性部分集中化管理 (use headquarters platform scale); 个性化需求定制服务 (regional offices act as internal customers drawing resources from headquarters platform).

Any management system design must serve the ultimate financial goals: increase revenue, reduce transaction/operating cost, and respond rapidly to customers.

## Three-Step Hard Capability Build

### Step 1 — Global IT Standardization

Extend integrated supply chain capabilities overseas through ERP implementation.

- Prioritize pilot countries based on business volume, regulatory maturity, and IT readiness (e.g., Nigeria, Egypt, Saudi Arabia, UK, Pakistan)
- Deploy HQ experts using "cell division" and "swarm tactic" methods to replicate domestic ERP success
- Address local tax, financial, commercial policy, and regulatory requirements — do not assume one template fits all
- Scale to all feasible subsidiaries; upgrade to company-level变革项目 with 200+ cross-functional members when complexity exceeds expectations

Target outcome: standardized, IT-systemized order management, financial reporting, procurement, and payment processes across global subsidiaries.

### Step 2 — Global Supply Network Planning and Layout

Supply network planning answers: what network structure serves customer demand from product origin to market endpoint?

**Decisions required:**
- Node type, quantity, and location based on customer segments and product categories
- Logistics methods between nodes
- Spatial problem: geographic layout of factories, warehouses, and retail points balancing service level vs. cost
- Temporal problem: delivery lead time balancing customer satisfaction vs. inventory and transportation cost

**Huawei's example:**
- Pre-2005: one production base in Shenzhen, one central warehouse — insufficient for global customers
- Post-2005: four supply centers (Mexico, India, Brazil, Hungary); regional DCs (Dubai, Netherlands); four procurement centers (USA, Japan, Germany, Taiwan)
- Europe served from Hungary supply center with two-week delivery commitment
- Principle: centralized certification, decentralized procurement

### Step 3 — Global Integrated Supply Chain Operations

**Overseas demand forecasting**
- Move from domestic-volume-based allocation to localized forecasting
- Inaccurate forecasting causes either inventory waste (over-forecast) or supply shortages (under-forecast)
- Deploy Advanced Planning and Scheduling (APS) globally
- Hold monthly S&OP meetings across sales, production, and procurement to review demand-supply gaps and publish available-to-promise (ATP)

**Global order management and fulfillment**
- Deploy contract order configuration tools overseas for front-back data sharing
- Improve configuration accuracy and order response speed
- Research delivery logic, algorithms, and trade settlement methods
- Build automatic order-splitting logic: system splits orders to nearest, most convenient, and lowest-cost supply center while complying with customs regulations

**Global logistics**
- Partner with global 3PLs for factory-to-supply-center movements
- Use local 3PLs for last-mile delivery (certified and managed by local offices)
- For mega-scale operations with hundreds of 3PLs, consider 4PL to manage and optimize the transportation network

## Soft Capability Build

1. **Localization**: hire and develop local employees into business骨干; accelerate bilingual documentation and process systems
2. **International talent**: recruit professionals with global视野; make English proficiency and international adaptability requirements for roles interfacing with overseas
3. **Continuous refinement**: no single supply chain model fits all countries;激励一线员工 to innovate and optimize based on local inventory, delivery, and logistics conditions

## Key Metrics (Huawei post-transformation)

- On-time complete shipment rate: 82%
- Inventory turnover: 3.67x/year
- Customer complaint rate: 0.5%

## Boundaries & Anti-Patterns

- **Not for**: pure domestic single-market operations; short-term freight forwarding decisions
- Do not replicate domestic processes blindly overseas — local tax, customs, and regulatory differences will break the model
- ERP globalization is not just an IT project; it is a company-level transformation requiring cross-functional heavyweight teams
- Avoid over-centralization that destroys local responsiveness, or over-localization that eliminates scale advantages
- Building global supply network requires years of sustained investment (Huawei: 3 years for initial ERP rollout, 10 years and 2B+ RMB for full maturity)

## Related Skills

- `glocalization-operator` — for broader "global resource integration + local value creation" business operations beyond supply chain
- `supply-chain-digitizer` — for digital twin and intelligent optimization of the supply network
- `scor-racetrack-improver` — for structured improvement projects on global supply chain performance
- `cross-border-strategist` — for market entry strategy and international expansion planning
