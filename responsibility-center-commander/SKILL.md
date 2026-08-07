# responsibility-center-commander

## Metadata
- **Version**: 1.0.0
- **Author**: Cangjie distillation from Huawei Finance & Accounting System Handbook (5th Ed, 2023)
- **Trigger**: 责任中心 / 利润中心 / 收入中心 / 成本中心 / 费用中心 / 投资中心 / 内部结算 / 划小核算单元 / 阿米巴对比 / responsibility center / profit center
- **Category**: Finance & Management

## Purpose
Design and operate a responsibility-center management system that aligns organizational authority with economic accountability. Based on Huawei's five-layer responsibility center framework (profit, revenue, expense, cost, investment centers), this skill helps users decompose strategic targets into actionable economic responsibilities without fragmenting the customer-centric operating model.

## When to Use
- When decomposing company strategy into departmental/unit economic targets
- When designing internal transfer pricing and settlement rules
- When deciding between profit-center vs. cost-center governance for a business unit
- When evaluating whether阿米巴-style micro-profit units fit your organization
- When resolving conflicts between "sales volume first" and "profit first" units
- When building a frontline-oriented,炮火-driven operating model

## When NOT to Use
- For personal finance or household budgeting
- For statutory/legal entity consolidation (use accounting standards instead)
- For pure project-level accounting (use project-four-accounting)
- When the organization has no strategic clarity yet

## Core Framework: Five-Layer Responsibility Centers

### Layer 1 — Profit Center
**Definition**: A unit with independent or semi-independent revenue and operating decision rights, accountable for both costs and profits.

**Design Rules**:
1. **Frontline-first**: Profit centers should be at the customer-facing edge (e.g., regional offices, representative offices), not in headquarters.
2. **Single truth**: Product lines and regions share one profit number. If a product line sells through a region, both see the same profit figure to eliminate finger-pointing.
3. **No internal markup**: Internal settlement uses cost-only transfer prices. Any premium must be jointly negotiated and transparent.
4. **Autonomy scope**: Profit centers have operational decision rights but NOT strategic war-declaration rights (e.g., entering a new country remains a HQ decision).

**Types**:
- **Natural profit center**: Sells directly to external customers (e.g., regional office, BG).
- **Virtual profit center**: Serves internal customers only; requires a fair internal transfer price to simulate market behavior.

**Metrics**:
- Marginal contribution (when common costs are not allocated)
- Controllable profit (when common costs are allocated)
- Cash flow from operations

### Layer 2 — Revenue Center
**Definition**: Accountable for revenue growth and market share, NOT for profit or cash flow.

**Use Case**: Product lines (BGs) that do not directly face end customers but drive top-line through regional offices.

**Governance Mechanism**:
- Revenue centers are intentionally "aggressive" in budgeting; profit centers (regions) are intentionally "conservative."
- Finance plays the referee: organize PK sessions between BG and region, let them fight out the target, but do not pick sides.
- Performance of a revenue center is ultimately validated by market results (e.g., chip performance in end products).

### Layer 3 — Expense Center
**Definition**: Support units (R&D platforms, corporate functions) consuming budget to serve frontline units.

**Design Principle**: Do NOT over-engineer expense-center KPIs. Huawei deliberately keeps expense-center management lightweight so that 70–80% of management energy focuses on profit centers.

### Layer 4 — Cost Center
**Definition**: Units with controllable costs but no revenue authority (e.g., manufacturing, supply chain operations).

**Huawei's Approach**:
- Manufacturing is a cost center, NOT a profit center, because manufacturing adds limited value in Huawei's high-margin model.
- Priority order: Quality > Delivery > Cost.
- Manufacturing overhead is typically only 1–2% of revenue; hence optimizing it is not a strategic priority.

### Layer 5 — Investment Center
**Definition**: Accountable for returns on capital deployed (rare in Huawei; used for large infrastructure or M&A decisions).

## Key Design Principles

### 1. Customer-Centric, Not Fragmentation-Centric
Huawei explicitly rejects阿米巴 (Amoeba) management because it fragments customer focus into internal bargaining. The rule: "All internal settlement uses cost price; customer-facing units own the profit."

### 2. Dual-Track Profit Accountability
- **Regions** (frontline) are profit centers → accountable for end-to-end profit and cash flow.
- **Product Lines** (BGs) are also profit centers → but their profit is the SAME number as the region's profit for the same deal. This forces product lines to support regions rather than blame them.

### 3. Command Rights vs. Resource Rights Separation
- **Frontline** (regional office): Has command rights — calls炮火, decides tactical pricing within authorized range.
- **BG/Platform**: Has resource rights — owns the army (products, solutions) but cannot declare war.
- **Army movement requires HQ approval** (budget authorization).

### 4. Differentiated Life-Cycle Targets
Do not apply a single profit template across all units:

| Life-Cycle Stage | Target Emphasis | Example |
|------------------|-----------------|---------|
| Startup/Growth   | Revenue growth rate, market share | New country entry |
| Mature           | Absolute profit, ROI | Established European region |
| Transition       | Controllable profit, cost structure | Declining product line |

For large-base units, emphasize absolute growth; for small-base high-potential units, emphasize percentage growth.

## Operating Mechanisms

### Mechanism 1: "要货成本" Pricing
- HQ provides a unified pre-customs landed cost to all regions.
- Regions add local uncertain costs (customs clearance, delivery, engineering) to set final customer price.
- Excess profit above the landed cost does NOT go to HQ; it enters a global profit pool for secondary distribution to all employees.

### Mechanism 2: Monthly Tracking + Quarterly Review + Semi-Annual Trial Rating + Year-End Settlement
- **Monthly**: Profit center fills actuals vs. targets, explains variances, proposes corrective actions.
- **Quarterly**: Central finance synthesizes all profit center performance for management review.
- **Semi-annual**: Trial rating with preliminary bonus payout; targets may be revised if market shifts dramatically.
- **Year-end**: 12-month cumulative actuals determine final bonus, deducting semi-annual pre-payments.

### Mechanism 3: Target Management Integration
Profit centers must be paired with:
- **Target Management (MBO)**: Quantified goals negotiated between HQ and center.
- **Budget System**: Budget provides the baseline, target provides the stretch.
- **Personnel Assessment**: "考事" (evaluate the task) rather than "考人" (evaluate the person).

## Common Pitfalls

| Pitfall | Why It Happens | Antidote |
|---------|---------------|----------|
| Every department demands profit-center status | Ego and budget maximization | Reserve profit-center status for customer-facing units; keep support units as expense/cost centers |
| Internal transfer-price wars | Departments optimize local profit at company expense | Mandate cost-only internal settlement; exceptions require joint approval |
| One-size-fits-all KPIs | Laziness in design | Differentiate targets by life-cycle stage and market maturity |
| Profit center becomes a silo | Local optimization ignores global coordination | Dual-track profit (region + product line share one number) |
| Frontline has profit accountability but no decision rights | HQ distrust | Separate command rights (frontline) from resource rights (platform); give frontline pricing autonomy within guardrails |

## STOP Checkpoints
Before finalizing a responsibility-center design, verify:
1. [ ] Does every profit center have a clear customer-facing boundary?
2. [ ] Is internal settlement based on cost (not markup) by default?
3. [ ] Do product-line and regional profit numbers reconcile to the same deal-level profit?
4. [ ] Are support units deliberately kept lightweight in KPI complexity?
5. [ ] Does the frontline have both accountability AND decision rights within defined guardrails?
6. [ ] Have we differentiated targets by life-cycle stage rather than using uniform growth rates?

## Output Format
When invoked, provide:
1. **Diagnosis**: Current organizational structure mapped to the five-layer framework.
2. **Design Proposal**: Which units should be profit/revenue/expense/cost/investment centers, with rationale.
3. **Transfer-Price Rules**: Internal settlement mechanism and exception process.
4. **Target Differentiation Table**: Life-cycle-based KPI weights per unit.
5. **Governance Mechanism**: Monthly/quarterly/semi-annual/year-end review cadence.
6. **Risk List**: Top 3 pitfalls most likely to occur in this specific organization and mitigations.

## Related Skills
- `project-four-accounting` — for project-level profit tracking within a responsibility center.
- `finance-bp-operator` — for business-partner support to profit-center managers.
- `comprehensive-budget-manager` — for budget baseline setting in the target negotiation process.
- `strategy-decoding-sp-bp` — for translating SP/BP into responsibility-center targets.
