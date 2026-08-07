# Product Manager Cultivator

Build a product manager cultivation system that selects candidates with dual market-and-R&D DNA, develops them through a resource pool and role-cognition curriculum, and holds them accountable with lifecycle-differentiated KPIs and investment-risk controls.

## When to Use

When the user needs to:
- Design a product manager selection and development pipeline for hardware, B2B, or complex-product industries
- Move from "tech-only" or "sales-only" PMs to leaders who can orchestrate end-to-end product success
- Create a role-cognition curriculum that clarifies what a PM actually owns versus what they merely coordinate
- Align PM incentives with product lifecycle stage (introduction vs. growth vs. maturity)
- Prevent PM investment decisions from becoming uncontrolled bets

## Core Concepts

**Dual DNA**: The ideal PM has both frontline market experience (customer relationships, competitive intelligence) and R&D depth (technical feasibility, development process). One without the other produces either unrealistic promises or market-blind products.

**Resource Pool**: A virtual organization that maintains a bench of PM-capable talent. New PMs are appointed from the pool; active PMs remain in the pool for continuous learning and peer exchange.

**Role Cognition**: A structured course where experienced PMs guide candidates through the PM's responsibility boundaries — what they dominate, what they organize, what they assist — across marketing, R&D, production, supply chain, and sales.

**Lifecycle-Differentiated KPIs**: The weight of sales, profit, quality, and customer satisfaction metrics changes based on whether the product is in introduction, growth, or maturity stage.

## Operating Procedure

### Step 1: Define PM Selection Criteria

**Minimum qualifications**:
- Demonstrated success in at least one frontline role (sales, technical support, or key account management) AND at least one R&D or delivery role
- Project management certification or equivalent experience
- Financial literacy: can read P&L, build a business case, and manage a budget

**Selection process**:
1. **Pool nomination**: Functional managers nominate candidates based on performance and potential
2. **Portfolio review**: Candidate presents 1–2 products or projects they shaped
3. **Panel interview**: Mix of senior PMs, R&D leaders, and sales leaders assess cross-functional judgment
4. **Role-cognition prerequisite**: Complete the PM role-cognition workshop before formal appointment

**Exclusion**: Do not appoint pure academics or fresh graduates as PMs for complex products. Internet-style "PM with no domain experience" works only when the product has no hardware, no supply chain, and no long delivery cycle.

### Step 2: Build the PM Resource Pool

Structure the pool as a virtual community:
- **Membership**: All current PMs + nominated candidates + recently retired senior PMs (advisors)
- **Activities**: Monthly seminar on a chosen topic (cost reduction, market entry, technology acquisition); quarterly cross-product review where PMs critique each other's plans
- **Governance**: A PM Management Office (virtual) maintains the pool, tracks assignments, and identifies development gaps
- **Rotation in**: Candidates join the pool 6–12 months before expected PM appointment
- **Rotation out**: PMs who fail two consecutive reviews return to the pool for retraining or exit

### Step 3: Design Role-Cognition Curriculum

The core course is not finance or IPD theory — it is **role cognition**.

**Workshop structure**:
- **Small groups** (6–8 people) with an experienced PM as facilitator
- **Scenario-based discussion**: For each stage of the product lifecycle, discuss:
  - What is the PM's decision right? (e.g., feature priority, pricing within band, launch timing)
  - What is the PM's organizational right? (e.g., convene cross-functional meetings, escalate blockers)
  - What is the PM's assist responsibility? (e.g., support sales with technical briefings, support R&D with customer feedback)
- **Boundary clarification**: Use real historical cases where PMs overstepped or under-stepped
- **Output**: Each participant drafts a personal "PM responsibility charter" signed by their functional manager

**Supporting courses** (shorter, modular):
- Product economics and investment return analysis
- Customer requirement translation and IPD interface
- Supply chain and manufacturing basics for PMs
- Communication and stakeholder management

### Step 4: Set Lifecycle-Differentiated KPIs

Weight KPIs by product stage:

| KPI | Introduction | Growth | Maturity |
|-----|-------------|--------|----------|
| **Sales revenue** | 20% | 40% | 35% |
| **Profit margin** | 10% | 25% | 35% |
| **Product quality / defect rate** | 30% | 20% | 15% |
| **Customer satisfaction / NPS** | 25% | 10% | 10% |
| **Market share / new customer acquisition** | 15% | 5% | 5% |

**Rationale**:
- **Introduction**: Quality and customer trust matter more than immediate sales; early defects destroy brand
- **Growth**: Scale is paramount; profit can be sacrificed for market share if strategy demands
- **Maturity**: Efficiency and profit extraction are key; maintain quality at lower cost

**Investment authority limits**:
- Define monetary thresholds by PM seniority (e.g., junior PMs can approve <$100K; senior PMs <$1M; above requires investment committee)
- Require business case with risk analysis for investments above threshold
- Post-investment audit: Did actual results match projections? Systematic偏差 analysis improves future estimates

### Step 5: Manage PM Risk and Pressure

PM is a high-risk, high-reward role:
- **Reward**: PMs have a separate bonus/equity line tied to product P&L. Top PMs can earn 10× more than mediocre ones.
- **Risk**: Two consecutive underperforming reviews = removal from PM role.
- **Support mechanisms**:
  - Clear RACI across the product chain so PM does not absorb all blame for functional failures
  - Monthly PM circle where PMs share pressure points and solutions
  - Executive sponsor assigned to each major product line for escalation

**Failure post-mortem**: When a product investment fails (e.g., misread market, wrong technology bet), conduct a no-blame review. Document lessons in a case study with the PM's authorship. Protect the PM from personal stigma if decision process was sound.

### Step 6: Continuously Refresh the Pool

- **Annual review**: Each PM's product performance, capability growth, and peer feedback are assessed
- **Pool expansion**: Identify new candidates from successful project managers, key account managers, and senior engineers
- **Knowledge legacy**: Retiring PMs must produce a written "product lineage history" and mentor one successor
- **External infusion**: Periodically hire PMs from adjacent industries to prevent inbreeding

## Anti-Patterns

- **PM as coordinator only**: If the PM has no decision rights and no P&L accountability, they are a project administrator, not a product manager.
- **One-size-fits-all KPIs**: Applying mature-product metrics to a launch-phase product guarantees either sandbagging or demoralization.
- **No investment limits**: Giving PMs unchecked spending authority invites reckless bets.
- **Ignoring market DNA**: Promoting only R&D stars to PM roles produces brilliant products no one wants to buy.
- **No failure recovery**: Firing or边缘化 every PM whose product fails destroys willingness to take necessary risks.

## Test Prompts

See `test-prompts.json`.
