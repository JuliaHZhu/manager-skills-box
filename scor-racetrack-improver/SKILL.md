---
name: scor-racetrack-improver
description: Apply the SCOR model and five-phase Racetrack improvement methodology to diagnose, benchmark, and systematically improve supply chain operations. Use when the user needs to evaluate supply chain performance, run a supply chain improvement project, benchmark against competitors, map supply chain processes, or prioritize optimization initiatives using SCOR metrics and the Racetrack framework.
---

# scor-racetrack-improver

Apply the SCOR (Supply Chain Operations Reference) model and the five-phase Racetrack improvement methodology to diagnose, benchmark, and systematically improve supply chain operations.

## When to Use

- The user mentions SCOR, supply chain improvement, supply chain diagnosis, or benchmarking
- The user needs to map AS-IS supply chain processes and design TO-BE improvements
- The user wants to prioritize supply chain projects by ROI and complexity
- The user needs to set supply chain KPIs aligned with competitive positioning
- The user is running a cross-functional supply chain transformation program

## Methodology

### Phase 0 — Identify Motivation (Pre-SCOR)

Establish top-management support. SCOR improvement is top-down by design because it requires breaking cross-department barriers.

Typical motivations:
1. Improve ROI or working capital efficiency
2. Fix S&OP (Sales & Operations Planning) process gaps
3. Maximize existing IT system capabilities
4. Reduce order fulfillment cycle time
5. Lower total supply chain management cost

Define the Improvement Program Organization:
- **Executive Sponsor**: C-level leader with authority and deep business knowledge
- **Program Champion**: Project manager who coordinates across functions (finance, production, procurement, planning)
- **Improvement Team**: Directors/leads who execute analysis and design
- **Stakeholders**: Regional and product-line executives

Output: Go/No-Go decision from executive team.

### Phase 1 — Set the Scope

1. **Business Context Summary**
   - Commercial description (products, customers, organization, supply chain topology)
   - SWOT analysis
   - Value positioning (cost leader vs. differentiation vs. agility)
   - Operational pain points
   - Key supply chain risks
   - Financial performance (three statements overview)

2. **Document Current Supply Chain**
   - Use the **Supply Chain Definition Matrix**: segment by geography, customer segment, and product group
   - Identify which supply chains matter most by sales volume, market complexity, and strategic importance
   - Draw the **Supply Chain Geographic Map**: visualize physical flow from suppliers → manufacturing → distribution → customers

3. **Improvement Program Charter** (formal contract signed by all stakeholders)
   - Scope: which supply chains are included
   - Business objectives and performance metrics
   - Improvement program objectives and supply chain performance targets
   - Program organization and roles
   - Methodology: five-phase SCOR racetrack
   - Schedule, deliverables, milestones, risks, dependencies, benefits

### Phase 2 — Configure the Supply Chain (The Core)

1. **Select Metrics** (SCOR Level 1 Attributes)
   Customer-facing:
   - Reliability: Perfect Order Fulfillment (%)
   - Responsiveness: Order Fulfillment Cycle Time (days)
   - Agility: Upside/Downside Supply Chain Adaptability, Value at Risk

   Internal-facing:
   - Cost: Supply Chain Management Cost % Revenue, COGS
   - Asset Management: Cash-to-Cash Cycle Time, Return on SC Fixed Assets, Return on Working Capital

   Practical rule: select only 1–3 metrics. Small and focused beats large and diffuse.

2. **Perform Benchmarking**
   - Define Parity (50th percentile), Advantage (70th percentile), Superior (90th percentile)
   - Ensure identical calculation methods across comparisons
   - Output: **Competitive Requirements Analysis** per supply chain segment
   - Constraint: in each supply chain, choose only ONE metric to target at Superior level, two at Advantage, and the rest at Parity

3. **Detail Gaps with SCORcard**
   - Map current performance vs. target levels
   - Quantify gap to target for each metric (e.g., current cost 8.1% vs. Superior 2.4% = 5.7% gap)

4. **Process Analysis**
   - Use **Thread Diagram** (swimlane) to map Level 1 and Level 2 SCOR processes across supply chain nodes
   - Apply **"Staple yourself to an order"**: trace one order from inquiry → quote → order → production → delivery → invoice → close
   - Use interviews (one-on-one, many-to-one, many-to-many) to capture AS-IS details
   - Classify every discovered defect into one of the five Level 1 attributes (Reliability, Responsiveness, Agility, Cost, Asset Management)
   - Quantify the impact of each defect on performance metrics using Six Sigma / TQM tools

5. **Design TO-BE**
   - Apply industry standard processes, lean thinking, or expert advice
   - For each process: add, modify, or eliminate steps
   - Test new scenarios via simulation, pilot runs, or dry runs

### Phase 3 — Optimize Projects

1. **Preliminary Project Portfolio Meeting**
   - Map every identified defect/gap to a specific improvement project
   - Link each project to SCOR Level 3 processes

2. **Financial Analysis**
   - Every project must have a quantified ROI analysis
   - Estimate financial impact on the targeted metrics

3. **Priority Sorting Matrix** (Complexity vs. Impact)
   - **Quick Wins** (high impact, low complexity): do first
   - **Major Projects** (high impact, high complexity): plan carefully
   - **Fill-ins** (low impact, low complexity): do when resources allow
   - **Avoid** (low impact, high complexity): deprioritize

   Consider project dependencies, priority, complexity, and financial impact.

### Phase 4 — Ready for Implementation

1. **Connect Level 3 to Level 4**
   - SCOR defines processes down to Level 3; Level 4 is company-specific operational steps
   - Translate each Level 3 process into concrete Level 4 activities (e.g., how orders are received: EDI, fax, phone, physical store)

2. **Storyboard / Working Instruction**
   - Document key operational steps with screenshots or visual guides
   - Create Standard Operating Procedures (SOPs) aligned with new TO-BE processes

3. **Readiness Check** (five dimensions)
   - Vision: is the target state clearly articulated?
   - Incentives: are KPIs and rewards updated to match new processes?
   - Resources: are people available and capable?
   - Skills: does the implementation team have required competencies?
   - Plan: is the detailed action plan ready?

4. **Test and Roll Out**
   - Run simulation with real data in a sandbox environment
   - Conduct pilot implementations in selected scenarios
   - Validate results before full roll-out
   - After implementation, identify the next improvement target and run the Racetrack again

## SCOR 4P Overview (Static Layer)

| P | Role | Connection |
|---|------|------------|
| **Process** | Core of SCOR; six Level-1 processes (Plan, Source, Make, Deliver, Return, Enable) decomposed to Level 2 (configuration) and Level 3 (process elements) | Solid line to Performance, Practice, People |
| **Performance** | Metrics that measure process execution (Reliability, Responsiveness, Agility, Cost, Asset Management) | Solid line to Process and Practice |
| **Practice** | Best practices that improve process performance (e.g., Order Quotation System, 3-Way Delivery Verification) | Solid line to Process and Performance; dashed line to People (some practices are tech-only) |
| **People** | Skills, experiences, and trainings required to execute Level-3 processes | Solid line to Process; dashed line to Practice |

## Key Artifacts

- Improvement Program Charter
- Supply Chain Definition Matrix
- Supply Chain Geographic Map
- Competitive Requirements Analysis / SCORcard
- Thread Diagram (swimlane)
- Preliminary Project Portfolio
- Improvement Project Charter (per project)
- Storyboard / SOP documents

## Boundaries & Anti-Patterns

- **Not for**: pure IT system selection without process change; single-department optimization that ignores end-to-end flow; one-person operational tasks
- **Requires** executive sponsorship; bottom-up SCOR projects usually fail due to cross-functional resistance
- SCOR is a reference model, not a rigid standard — Level 4 must be customized to industry, region, and company context
- Do not try to optimize all five Level-1 metrics to Superior simultaneously; SCOR explicitly recommends focusing (one Superior, two Advantage, rest Parity)
- Avoid "death by analysis": Phase 2 data collection can consume excessive time; set strict deadlines and data ownership

## Related Skills

- `global-supply-network-architect` — for designing physical supply network topology and geographic layout
- `supply-chain-digitizer` — for digital twin, algorithmic optimization, and IT serviceization of supply chain
- `strategic-sourcing-tco` — for procurement cost structure and total-cost-oriented sourcing decisions
- `lean-process-reformer` — for general process simplification outside SCOR scope
