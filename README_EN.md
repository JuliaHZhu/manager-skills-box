# Manager Skills Box

A curated collection of agent skills distilled from real-world management and engineering practices -- not theory, but battle-tested playbooks.

## Architecture

```
+-----------------------------------------------------+
|  P2  NeatFreak     Quality Governance               |
|       Scan / Fix / Clean -> safety-gated             |
+-----------------------------------------------------+
|  P1  CodeGraph     Code Structure                   |
|       AST -> SQLite graph -> blast radius             |
|  P1  WikiBrain     Knowledge Engine                 |
|       Ingest -> Compile -> Index -> Query              |
+-----------------------------------------------------+
|  P0  FileStates    Foundation Layer                 |
|       Snapshot / Rollback / Plan / Role tracking    |
+-----------------------------------------------------+
```

Higher layers depend on lower ones. P0 is the bedrock -- every file operation flows through it. P1 layers build capability on top. P2 governs across all layers.

## Skills

| Skill | Layer | Responsibility | Source |
|-------|-------|---------------|--------|
| **FileStates** | P0 | Track every file write with snapshots and rollback. Tag files by role (source/test/doc/config). Plan-mode: create, track, and verify task plans. | Internal toolchain |
| **CodeGraph** | P1 | Parse codebases (Python/JS/TS/Java/Go/Rust/C/C++) via Tree-sitter, build a SQLite call graph. Blast radius analysis: "what breaks if I change X?" | Internal toolchain |
| **WikiBrain** | P1 | Raw material -> structured wiki. Parallel ingestion, frontmatter indexing, FTS5 search, dead-link detection, session feedback extraction. | Internal toolchain |
| **NeatFreak** | P2 | Aggregate quality signals from all lower layers. Three safe modes: Scan (read-only), Fix (deterministic repairs), Clean (agent-supervised). | Internal toolchain |
| **hw-normalization-design** | -- | Four-layer normalization methodology: component -> board -> platform -> network architecture. | Huawei hardware platform design |
| **project-delay-prevention** | -- | Six-step anti-procrastination system for complex projects: team-building, assessment, decomposition, monitoring, coaching, and closed-loop tracking. | Huawei R&D management practice + Zeng Guofan's personnel philosophy |
| **topic-analysis-driven-design** | -- | Replace "draw-debug-redraw" loops with mandatory topic analyses (power, clock, subsystem) before any design work begins. | Huawei hardware design methodology |
| **ipd-charter-developer** | -- | Charter development methodology: treat Charter as a product, develop business plans with end-to-end cross-functional teams. | Huawei IPD Transformation Handbook (5th Ed, 2023) |
| **ipd-product-launch** | -- | Controlled product launch: phased GA, ADCP review, "one-five-one" launch method, "one-paper Zen" sales pitch. | Huawei IPD Transformation Handbook (5th Ed, 2023) |
| **ipd-lifecycle-manager** | -- | Product lifecycle management: LDCP review, version switching, EOL planning, active decline management. | Huawei IPD Transformation Handbook (5th Ed, 2023) |
| **ipd-change-management** | -- | IPD change management: rigid -> fixed -> optimized. Three-stage deployment with pilot-then-scale pattern. | Huawei IPD Transformation Handbook (5th Ed, 2023) |
| **ipd-cross-functional-team** | -- | Cross-functional team operations: IPMT/PDT structure, DCP decision reviews, dual-line reporting matrix. | Huawei IPD Transformation Handbook (5th Ed, 2023) |
| **hw-derating-design** | -- | Component derating design: steady-state and transient stress analysis, temperature limits, derating review process. | Huawei hardware R&D practice |
| **hw-halt-hass-testing** | -- | HALT/HASS accelerated reliability testing: step-stress to failure, operational/destruct limits, production screening. | Huawei hardware R&D practice |
| **hw-dfm-design** | -- | Design for Manufacturing: connector design, tolerance analysis, screw standardization, assembly time optimization. | Huawei hardware R&D practice |
| **hw-reliability-design** | -- | Hardware reliability design system: thermal, redundancy, EMC, drift, interconnect, environmental adaptation. | Huawei hardware R&D practice |
| **hw-component-failure-analysis** | -- | Component failure analysis 8-step method: electrical test, X-ray, decapsulation, SEM, FA, root cause, corrective action. | Huawei hardware R&D practice |
| **darwin-skill** | -- | Autonomous skill optimizer. 9-dimension rubric evaluation, hill-climbing optimization, independent judge agents, validation-gated design, visual result cards. | SkillLens (MSR) + SkillOpt + alchaincyf |
| **assumption-hunter** | -- | Find hidden shared assumptions in arguments. Jump out of the system (Jootsing) from Dennett's Intuition Pumps Ch8. | Daniel Dennett |
| **intentional-stance** | -- | Three-stances analysis (physical / institutional / game-theoretic) of the same phenomenon. From Dennett's Intuition Pumps Ch18. | Daniel Dennett |
| **piling-on-detector** | -- | Detect rhetorical piling-on: multiple claims bundled so refuting one seems to defeat all. From Dennett's Intuition Pumps Ch9. | Daniel Dennett |
| **reductio-ad-absurdum** | -- | Accept premises, push to absurdity, check for contradiction. From Dennett's Intuition Pumps Ch2. | Daniel Dennett |
| **mediation-model-designer** | -- | Design simple, parallel, serial, and multicategorical mediation models from theoretical hypotheses. | Hayes (2022) |
| **indirect-effect-inference** | -- | Bootstrap / Monte Carlo inference for indirect effects. Replaces obsolete Sobel test and causal steps. | Hayes (2022) |
| **moderation-prober** | -- | Probe interactions with pick-a-point and Johnson-Neyman technique. Includes simple slope visualization. | Hayes (2022) |
| **conditional-process-builder** | -- | Build conditional process (moderated mediation) models. Map conceptual diagrams to PROCESS model numbers. | Hayes (2022) |
| **effect-scaling-guide** | -- | Effect scaling guide: choose and report unstandardized, completely standardized, or partially standardized coefficients. | Hayes (2022) |
| **multicategorical-mediation** | -- | Mediation, moderation, and conditional process with 3+ group antecedents. Indicator / sequential / Helmert coding. | Hayes (2022) |
| **process-model-reporter** | -- | Publication-ready results writing. Structured reporting from regression coefficients to full results paragraphs. | Hayes (2022) |
| **antipattern-diagnostician** | -- | Diagnose common errors in mediation and moderation: Baron & Kenny, median splits, standardized dichotomous variables, etc. | Hayes (2022) |
| **triad-classification** | -- | Classify anything into Fragile / Robust / Antifragile triad. How it behaves under volatility, pressure, disorder. | Taleb -- *Antifragile* |
| **fragility-diagnosis-checklist** | -- | 10-question rapid fragility check for systems, strategies, careers, investments. | Taleb -- *Antifragile* |
| **barbell-strategy** | -- | Allocate resources to extreme safety + extreme risk, discard the middle. Portfolio, career, learning path design. | Taleb -- *Antifragile* |
| **convexity-spotting** | -- | Judge if a payoff structure is convex (limited loss, unlimited gain, volatility-friendly) or concave. | Taleb -- *Antifragile* |
| **optionality-evaluation** | -- | Assess whether an option has "free optionality" -- limited downside, unlimited upside, no precise prediction needed. | Taleb -- *Antifragile* |
| **fat-tony-heuristic** | -- | Don't predict the future; identify who is fragile right now. Switch from forecasting to fragility detection. | Taleb -- *Antifragile* |
| **via-negativa-decision** | -- | Complex decision with too many options? Eliminate the worst first via negativa (subtraction). | Taleb -- *Antifragile* |
| **lindy-filter** | -- | Use time as a filter: old and surviving is more reliable than new and shiny. Tech stack, diet, career choices. | Taleb -- *Antifragile* |
| **skin-in-the-game** | -- | Evaluate credibility by checking if the advisor/decision-maker bears the consequences of their advice. | Taleb -- *Antifragile* |
| **intervention-threshold-test** | -- | Six-step review protocol before taking action. Prefer subtraction and inaction. Do no harm. | Taleb -- *Antifragile* |
| **iatrogenics-principle** | -- | Will the proposed intervention cause more harm than benefit? Evaluate before acting. | Taleb -- *Antifragile* |
| **narrative-fallacy-immunity** | -- | Distinguish narratable knowledge from actionable knowledge. Don't be misled by post-hoc causal stories. | Taleb -- *Antifragile* |
| **extremistan-detector** | -- | Is this domain Mediocristan (normal-friendly) or Extremistan (dominated by extreme events)? Avoid wrong stats. | Taleb -- *The Black Swan* |
| **gaussian-illusion-detector** | -- | Detect fatal misuse of Gaussian / bell-curve in Extremistan fields. VaR, confidence intervals, tail risk. | Taleb -- *The Black Swan* |
| **platonification-detector** | -- | Detect over-simplified models, categories, or frameworks forced onto complex reality. Map vs territory. | Taleb -- *The Black Swan* |
| **silent-evidence-analyzer** | -- | When judging by "success stories" or "historical records", identify the unseen negative evidence that skews perception. | Taleb -- *The Black Swan* |
| **turkey-problem-detector** | -- | Detect turkey problems: misinterpreting stability as permanence. 1000 days of feeding don't predict day 1001. | Taleb -- *The Black Swan* |
| **gray-rhino-spotter** | -- | Spot high-probability, high-impact, obvious-but-ignored crises. Not unpredictable -- just not acted upon. | Wucker -- *The Gray Rhino* |
| **rhino-stage-diagnoser** | -- | Diagnose which of the five stages (denial -> muddling -> diagnosis -> panic -> action) your team is in. | Wucker -- *The Gray Rhino* |
| **rhino-classifier** | -- | Classify gray rhinos by type: recurring, charging, meta-rhino, domino, Gordian knot, disruptive. Different tactics. | Wucker -- *The Gray Rhino* |
| **denial-breaker** | -- | Break through denial and resistance. Data shock, external perspective, personalization, anti-groupthink. | Wucker -- *The Gray Rhino* |
| **procrastination-interrupter** | -- | Interrupt "muddling through" -- acknowledged but postponed crises. Manufacture urgency, shrink decision units. | Wucker -- *The Gray Rhino* |
| **panic-to-action-bridge** | -- | Move from panic to rational action. Physical pause, data anchor, pre-set protocol, divide and conquer. | Wucker -- *The Gray Rhino* |
| **measure-change-scale** | -- | Measure -> Change -> Scale. Turn epiphany into organizational capability. Systematic change management. | Wucker -- *The Gray Rhino* |
| **crisis-as-opportunity** | -- | Post-crisis reconstruction. Reframe crisis as opportunity. Stop bleeding, honest post-mortem, institutionalize. | Wucker -- *The Gray Rhino* |
| **ceg-expert-group** | -- | Commodity Expert Group (CEG) operations: cross-functional procurement decision teams, collective voting, supplier certification governance. | Huawei procurement management |
| **tqrdc-supplier-evaluation** | -- | TQRDC + ES seven-dimension supplier evaluation: Technology, Quality, Responsiveness, Delivery, Cost, Environment, Social Responsibility. | Huawei procurement management |
| **procurement-strategy-designer** | -- | Procurement strategy selection: framework agreement, limited competition, split/combine. Match strategy to material characteristics. | Huawei procurement management |
| **supplier-lifecycle-manager** | -- | End-to-end supplier lifecycle: sourcing -> certification -> selection -> performance -> CSR -> exit. With CRCPE five-step improvement. | Huawei procurement management |
| **procurement-ethics-guardian** | -- | Procurement compliance and ethics: conflict of interest, information confidentiality, gift limits, two-person rule, post-employment restrictions. | Huawei procurement management |
| **emergency-procurement-protocol** | -- | Three-tier emergency procurement: immediate repair / urgent implementation / government directive. Post-hoc audit to prevent abuse. | Huawei procurement management |
| **vmi-inventory-designer** | -- | Vendor Managed Inventory design: inventory-forward transaction models, legal framework, system integration, five-step implementation. | Huawei procurement management |
| **isc-transformation-architect** | -- | ISC integrated supply chain transformation: three-phase deployment (focus -> invent -> deploy), SCOR-based process design, organization/IT/process tri-ring model. | Huawei supply chain management |
| **scor-racetrack-improver** | -- | SCOR model + five-phase Racetrack improvement: diagnose, benchmark, map processes, prioritize projects, and implement supply chain transformation. | Huawei supply chain management |
| **supply-chain-resilience-guardian** | -- | Supply chain resilience and business continuity: chip strategy, spare-tire R&D, BCM, strategic stockpiling, and ecosystem cultivation for extreme shocks. | Huawei supply chain management |
| **consumer-supply-chain-operator** | -- | Consumer/to-C supply chain operations: CISC transformation, inventory-light fast response, NPI + EMS outsourcing, global launch execution. | Huawei supply chain management |
| **integrated-planning-conductor** | -- | Integrated planning and S&OP: planning as commander, 18-month rolling plan, strategy-driven differentiation, monthly S&OP cycle. | Huawei supply chain management |
| **strategic-sourcing-architect** | -- | Strategic sourcing and procurement strategy: five-feature sourcing, six-step strategy method, procurement iron triangle, supplier tiering. | Huawei supply chain management |
| **supply-chain-digitizer** | -- | Supply chain digital transformation: digitalization -> intelligentization -> governance, digital twin, Lingkun/Lingfeng dual-layer architecture. | Huawei supply chain management |
| **isc-plus-digital-transformer** | -- | ISC+ next-gen digital supply chain: six transformations, lightweight IT architecture, eight sub-programs, ROADS user experience. | Huawei supply chain management |
| **global-supply-network-architect** | -- | Global supply network design: standardization vs. personalization balance, supply/procurement/distribution center layout, ERP globalization. | Huawei supply chain management |
| **supply-chain-triad-collaborator** | -- | Supply chain triad alignment: R&D + Sales + Supply Chain collaboration using the Iron Triangle (AR/SR/FR) to break silos. | Huawei supply chain management |
| **strategic-sourcing-tco** | -- | Strategic sourcing and total cost of ownership: move beyond unit price to evaluate transportation, inventory, risk, quality, and sustainability. | Huawei supply chain management |
| **supplier-field-auditor** | -- | Supplier on-site audit: 8-step process, three standard forms, 10-factor evaluation framework for qualification and improvement. | Huawei supply chain management |
| **mrp-master-scheduler** | -- | MRP three-tier master scheduling: MDS-MPS-MRP planning, version switch control, exception handling, pre-shortage management. | Huawei planning management |
| **inventory-plan-controller** | -- | Inventory planning and materials control: min-max planning, ABC classification, dead-stock analysis, shortage resolution, daily closing. | Huawei planning management |
| **demand-supply-balancer** | -- | S&OP demand-supply balancing: unconstrained forecast, supply-demand-review meetings, demand smoothing, R&D and internal demand review. | Huawei planning management |
| **bom-eco-guardian** | -- | BOM engineering data and ECO control: product structure trees, item templates, BOM list types, engineering change orders, planning percentages. | Huawei planning management |
| **planning-parameter-engineer** | -- | Planning parameter configuration: lead time, lot sizing, safety stock, ABC fixed supply days, planner attributes, internal order setup. | Huawei planning management |
| **supply-chain-planning-architect** | -- | Supply chain planning system design: MRP/JIT/TOC methodology selection, planning organization architecture, ISC transformation, TOM model. | Huawei planning management |
| **inventory-health-diagnoser** | -- | Inventory health diagnosis and structure optimization: turnover rate, rational structure ratio, bad-stock root-cause analysis, dead/slow-moving material disposal. | Huawei planning management |
| **version-switch-controller** | -- | Version switch management: smooth/forced/trade-off strategies, five-link coordination, cross-department sync, dead-stock control target. | Huawei planning management |
| **bottleneck-material-allocator** | -- | Bottleneck material allocation and ATP analysis: three allocation principles, ATP forward simulation, sensitivity analysis, kitting check. | Huawei planning management |
| **production-control-operator** | -- | Production control and dispatch strategy: push/pull scheduling, task order queuing rules, shipping strategy, shortage tiered escalation, daily closing. | Huawei planning management |
| **tom-order-manager** | -- | TOM total order management: four-square closed loop, S&OP resource rationalization, business rule system, product-mix forecast decomposition, ATP allocation. | Huawei planning management |
| **rd-logistics-planner** | -- | R&D logistics and new-product supply risk: four-stage logistics, component selection five-dimension evaluation, early-delivery five-dimension risk, R&D self-purchase. | Huawei planning management |
| **five-looks-market-insight** | -- | Five-looks market insight: industry/trends, customers, competition, self-assessment, opportunity. Structured scanning before strategy design. | Huawei strategic management |
| **blm-strategic-planning** | -- | BLM (Business Leadership Model): gap analysis -> market insight -> strategic intent -> innovation focus -> business design -> execution system. | Huawei strategic management |
| **business-model-five-elements** | -- | Business model design via five elements: customer selection, value proposition, profit model, strategic control, business scope. | Huawei strategic management |
| **strategic-control-point** | -- | Strategic control point assessment: four-level profit-protection capability rating (high/medium/low/none) with upgrade paths. | Huawei strategic management |
| **strategy-decoding-sp-bp** | -- | Strategy decoding: translate SP (strategic plan) into BP (business plan), organizational KPIs, and personal PBCs. Value creation drives value distribution. | Huawei strategic management |
| **stretch-goals-capability-building** | -- | Stretch goals to force capability building: opportunity logic replaces extension-line thinking. Goals exist to create tension, not just to be hit. | Huawei strategic management |
| **org-capability-elevation** | -- | Organizational capability elevation: five management levels (business -> functional -> factor -> collaboration -> strategic) with upgrade paths. | Huawei strategic management |
| **dste-strategy-execution** | -- | DSTE (Develop Strategy to Execute): integrated SP -> BP -> budget -> KPI -> PBC -> monitoring closed-loop with annual management calendar. | Huawei strategic management |
| **cross-border-strategist** | -- | Cross-border strategy decision: 5-step framework from mistake inventory to pressure investment. B2B-to-B2C transformation playbook. | Huawei cross-border management |
| **main-channel-guardian** | -- | Main-channel boundary management: 3-dimension test, "don't do boundary-external things", platform three-no-principles. | Huawei cross-border management |
| **pressure-focus-investor** | -- | Pressure-focus investment: strategic growth point mapping, three-generation strategy reserve, pressure index calculation. | Huawei cross-border management |
| **backup-plan-architect** | -- | Backup plan architecture: 4-layer backup grading, dogfooding principle, activation trigger design. | Huawei cross-border management |
| **full-stack-vertical-integrator** | -- | Full-stack vertical integration: capability map, gap diagnosis, integration path selection, ecosystem compatibility. | Huawei cross-border management |
| **black-soil-ecosystem-builder** | -- | Black-soil ecosystem building: lower barrier, provide nutrients, balance interests, make partners win. | Huawei cross-border management |
| **crisis-deterrence-survivor** | -- | Crisis deterrence and survival: deterrence-survival dual loop, 5-stage survival switch protocol, coalition building. | Huawei cross-border management |
| **global-market-entry-strategist** | -- | Global market entry path design: rural-surrounds-city sequencing, market attractiveness x competitiveness matrix, phased focus. | Huawei internationalization |
| **brand-globalization-builder** | -- | Brand globalization: three-stage model (exhibit -> diplomacy -> certification), glocalized cross-cultural communication, B2B-to-B2C trust transfer. | Huawei internationalization |
| **glocalization-operator** | -- | Glocalization operations: global resource integration + local value creation, capability/shared center footprint, localization rate governance. | Huawei internationalization |
| **cross-culture-team-commander** | -- | Cross-cultural team building: core values translation, expat-to-local transition, TUP incentive, leadership selection principles. | Huawei internationalization |
| **global-rd-footprint-architect** | -- | Global R&D footprint design: research institutes, joint innovation centers, capability centers mapped to country comparative advantages. | Huawei internationalization |
| **global-innovation-leap-strategist** | -- | Innovation leap from follower to leader: pinprick strategy, edge-to-mainstream breakthrough, IPR and standards dominance. | Huawei internationalization |
| **intl-crisis-resilience-builder** | -- | International crisis resilience: spare-tire planning, persistence through downturns, crisis response differentiation, BT-style certification trust-building. | Huawei internationalization |
| **rd-project-classifier** | -- | R&D project four-quadrant classification: custom / new product / new tech / pre-research with differentiated management strategies. | Huawei R&D management |
| **product-manager-compass** | -- | Product manager positioning and five-competency model: demand, planning, quality, launch, and system-building capabilities. | Huawei R&D management |
| **five-force-talent-developer** | -- | R&D talent development five-force model: learning, motivation, development, qualification, and competency. | Huawei R&D management |
| **innovation-seven-principles** | -- | Huawei innovation seven principles: anti-blind, dual-drive, half-step lead, open collaboration, inherited innovation, failure tolerance, IP dominance. | Huawei R&D management |
| **blue-army-evolution** | -- | Blue army evolution path: from challenger to incubator, Femto-to-LampSite case study, five-stage conversion model. | Huawei R&D management |
| **rd-incentive-architect** | -- | R&D incentive mechanism design: mechanism-first philosophy, layered short/mid/long-term incentives, equity design framework. | Huawei R&D management |
| **position-based-pay-architect** | -- | Position-based pay architecture: job evaluation -> pay grade -> pay range -> person-job match -> pay adjustment on change. | Huawei compensation management |
| **executive-compensation-negotiator** | -- | Executive compensation negotiation: 3P1M model, LEADER negotiation framework, 5C talent matching. | Huawei compensation management |
| **result-oriented-appraiser** | -- | Result-oriented appraisal: pay for real results not fake motion, three-employee-type classification, contribution-based distribution. | Huawei compensation management |
| **compensation-strategy-evolver** | -- | Compensation strategy evolution: three-stage pay strategy (startup / growth / maturity), efficiency-first fairness balance. | Huawei compensation management |
| **award-culture-designer** | -- | Award culture design: ceremony, innovation, zero-to-takeoff awards, making awards a management instrument. | Huawei compensation management |
| **locomotive-bonus-designer** | -- | Locomotive bonus and incentive pool design: three-layer pool generation, 4:3:3 manager coefficient, individual allocation, cross-unit smoothing. | Huawei compensation management |
| **virtual-equity-governance-architect** | -- | Virtual equity governance: union-trustee platform, five-rights separation, founder control with 1% stake, holding-company firewall. | Huawei equity incentive |
| **tup-incentive-architect** | -- | TUP incentive design: 5-year deferred incremental units, 9-fixed process, labor:capital ratio control, algorithmic allocation. | Huawei equity incentive |
| **equity-lifecycle-strategist** | -- | Equity incentive lifecycle strategy: match ESOP/virtual stock/TUP/ATUP to startup/growth/maturity/crisis stages. | Huawei equity incentive |
| **equity-incentive-pain-doctor** | -- | Equity incentive pain-point diagnosis: 14 failure modes, five shareholder-type matching, recovery roadmap. | Huawei equity incentive |
| **atup-ecosystem-integrator** | -- | ATUP ecosystem integration: extend acquire-share logic to external partners, platform value pools, 2-year partner cycles. | Huawei equity incentive |
| **striver-ownership-culture** | -- | Striver ownership culture: three-tier community, annual striver certification, story-based cultural transmission. | Huawei equity incentive |
| **equity-10d-designer** | -- | 10D equity incentive design model: purpose, architecture, targets, instrument, quantity, price, timeline, source, conditions, mechanism. | Huawei equity incentive |
| **virtual-equity-architect** | -- | Virtual restricted share and TUP plan design: holding platform, pricing, vesting, exit, and governance for non-listed companies. | Huawei equity incentive |
| **knowledge-capitalization-strategist** | -- | Knowledge capitalization framework: convert intellectual labor into equity, nine incentive mechanisms, striver culture foundation. | Huawei equity incentive |
| **equity-governance-builder** | -- | Employee ownership governance architecture: shareholding platform, employee representative meeting, rotating CEO, founder veto design. | Huawei equity incentive |
| **stage-equity-matcher** | -- | Stage-based equity instrument matching: real shares, virtual shares, TUP, options aligned to startup/growth/mature stages. | Huawei equity incentive |
| **equity-saturation-governor** | -- | Equity saturation and dynamic adjustment: saturation lines, reward shares, clawback, retirement retention, exit repurchase. | Huawei equity incentive |
| **pbc-performance-contractor** | -- | PBC performance commitment design: strategy decoding -> BSC -> KPI -> personal PBC, WET three elements, SMART criteria, refresh mechanism. | Huawei performance management |
| **forced-distribution-enforcer** | -- | Forced distribution and performance result application: 5-grade absolute definition, horse-racing mechanism, layered evaluation, 10% elimination. | Huawei performance management |
| **org-performance-aligner** | -- | Organizational and personal performance alignment: DSTE+BLM+PBC docking, hat-wearing and twisted rope, budget and payroll management. | Huawei performance management |
| **rd-performance-designer** | -- | R&D performance management: benefit/efficiency/path/behavior four-dimension indicators, IPD-based R&D performance, project-based assessment. | Huawei performance management |
| **incremental-performance-driver** | -- | Incremental performance and value distribution: value creation -> evaluation -> distribution closed loop, payroll control, 3-people-5-jobs-4-pay. | Huawei performance management |
| **performance-coach-grow** | -- | Performance coaching and GROW model: coaching-style guidance, GROW four-step, performance interview, low-performer PIP management. | Huawei performance management |
| **performance-decomposition-engineer** | -- | Cross-functional performance decomposition: break final results into inter-departmental activity chains so the whole organization owns outcomes. | Huawei performance management |
| **pricing-profit-lever** | -- | Pricing profit-lever analysis: 1% price change → 10% profit impact. Quantify price/cost/volume/fixed-cost leverage effects. | Huawei finance management |
| **customer-centric-pricing** | -- | Customer-centric pricing architecture: IPD+LTC coupling, value-based pricing transition, cross-functional pricing governance. | Huawei finance management |
| **price-anchoring-strategist** | -- | Price anchoring and psychological pricing: contrast effect, second-cup-half-price patterns, diminishing-return mitigation. | Huawei finance management |
| **budget-as-weapon** | -- | Budget-as-weapon design: reframe budget from control tool to combat resource, frontline service culture, simplify approval chains. | Huawei finance management |
| **sp-budget-closure** | -- | Strategy-to-budget closed loop: SP→BP→budget alignment, forced variance explanation, rolling monitoring with traffic-light. | Huawei finance management |
| **resource-allocation-guardian** | -- | Resource allocation guardrails: expense-growth constraints, frontline tilt, efficiency metrics (AR/inventory), negative-growth regions. | Huawei finance management |
| **admin-baseline-manager** | -- | Admin baseline management: dual classification (autonomy vs standardization), country-level cost baselines, save-share/waste-burden incentives. | Huawei admin management |
| **internal-service-marketizer** | -- | Internal service marketization: basic/premium tiering, privatization + competition, dynamic rent + survival-of-the-fittest. | Huawei admin management |
| **lean-process-reformer** | -- | Lean process reform: value audit, cut non-value steps, process accountability for non-core flows, small-loop granularity. | Huawei admin management |
| **expat-welfare-designer** | -- | Expat welfare design: four-pillar overseas support (cafeteria/medical/housing/relationship), self-governance + oversight. | Huawei admin management |
| **it-value-transformer** | -- | IT positioning shift: from cost center to value center to profit center. Role redesign, performance metrics, and business-value proof. | Huawei IT management |
| **process-it-integrator** | -- | Process-IT fusion operating model: cross-functional project teams, process Owner mechanism, end-to-end flow integration. | Huawei IT management |
| **it-governance-architect** | -- | IT governance architecture: EA three-layer model, tiered decision-making, version-train demand management, balanced scorecard. | Huawei IT management |
| **business-change-it-land** | -- | Business transformation IT landing: rigid -> fixed -> optimized methodology, package-driven change, capability decoupling. | Huawei IT management |
| **roads-digital-transformer** | -- | ROADS-driven digital transformation: three architecture shifts, front-light back-heavy system, multi-cloud design. | Huawei IT management |
| **global-it-controller** | -- | Global IT control model: centralize control + distribute resources, simplify backbone + flexible endpoints, frontline-driven operations. | Huawei IT management |
| **project-four-accounting** | -- | Project four-accounting management: estimate -> budget -> account -> settle, pulling through project-level profit management with CFO empowerment. | Huawei financial management |
| **project-centric-org-transformer** | -- | Project-centric organization transformation: weak-to-strong matrix, resource marketplace, frontline empowerment, platform support, iron triangle. | Huawei project management |
| **tob-big-project-strategist** | -- | ToB big-deal strategy: five-stage win-rate funnel, three-axes prospecting + one-paper value proposition, marketing four elements, LTC end-to-end. | Huawei project management |
| **project-standard-toolkit** | -- | Standard project toolkit: ten templates, six-steps-one-method, ten charts (Gantt, burndown, WBS, RACI, PERT, decision tree, etc.). | Huawei project management |
| **project-ceo-cultivator** | -- | Project CEO development: HEROS model, business-quality-leadership triad, three-stage career path, 70-20-10 + AAR after-action review. | Huawei project management |
| **project-team-communicator** | -- | Project communication and team leadership: three principles, PL coaching, C8 cross-functional collaboration, project HRBP human-model. | Huawei project management |
| **project-process-controller** | -- | Project process and risk governance: six-stage 45 standard actions, IPD+CMMI+Agile integration, PQA process audit, four risk responses, CCB. | Huawei project management |
| **comprehensive-budget-manager** | -- | Comprehensive budget management: two-layer budget generation (opportunity-based + resource-based), elastic grant, budget-to-strategy alignment. | Huawei financial management |
| **cost-control-twist-towel** | -- | Cost control "twist-towel" methodology: three-moves four-forms combo to squeeze costs while protecting strategic investment and customer interface. | Huawei financial management |
| **ifs-finance-transformation** | -- | IFS integrated financial transformation: rule-based certainty against outcome uncertainty, business-finance integration, CFO pipeline buildout. | Huawei financial management |
| **finance-bp-operator** | -- | Finance BP operations: three-pillar model (COE/BP/SSC), "together-understand-advise" nine-character formula, five-understand capability model. | Huawei financial management |
| **plan-budget-accounting-closure** | -- | Plan-budget-accounting closure: SP/BP/PP nested loops, rolling forecast, five-cycle operating system for representative offices. | Huawei financial management |
| **responsibility-center-commander** | -- | Responsibility center operations: five-layer framework (profit/revenue/expense/cost/investment), frontline profit accountability, internal cost-only settlement. | Huawei financial management |
| **financial-statement-strategist** | -- | Financial statement strategic interpretation: three-statement narrative, six-view dashboard, soft-asset valuation, profit-quality diagnostics. | Huawei financial management |
| **expense-integrity-guardian** | -- | Expense integrity and audit: SSE automation, integrity-score audit matrix, supervisor accountability, risk-based post-audit. | Huawei financial management |
| **finance-digital-transformer** | -- | Finance digital transformation: four-stage evolution, four unifications, MCA modular consolidation, follow-the-sun closing, KCFR data governance. | Huawei financial management |
| **financial-risk-three-lines** | -- | Financial risk 4x3 architecture: three risk categories, three defense lines, three-layer review, triangular linkage, financial blue team. | Huawei financial management |
| **cfo-readiness-ladder** | -- | CFO readiness and succession: four-level development ladder, financial golden triangle, concrete-structure rotation, CEO-level standard. | Huawei financial management |
| **qualification-standard-builder** | -- | Qualification standard development: five-step method from job analysis to behavioral standards, with broadband grading and "three sentences" clarity rule. | Huawei qualification system |
| **dual-channel-career-designer** | -- | Dual-channel career design: management + professional tracks, five-level progression, top-tier pay parity, and cross-channel mobility rules. | Huawei qualification system |
| **qualification-certifier** | -- | Qualification certification design: seven-step process, evidence-based evaluation, four-grade results, and committee governance. | Huawei qualification system |
| **competency-qualification-integrator** | -- | Integrate competency models with qualification systems: iceberg-above vs iceberg-below, unified terminology, and lightweight competency deployment. | Huawei qualification system |
| **learning-path-mapper** | -- | Learning path design based on qualification gaps: 70-20-10 development, acceleration programs, and tiered growth routes. | Huawei qualification system |
| **qualification-hr-integrator** | -- | Qualification-HR integration: job-grade-pay linkage, performance boundary clarification, and promotion gatekeeping. | Huawei qualification system |
| **admin-support-qualification-architect** | -- | Support-role qualification architecture: dual-track five-level classification, unit-element behavioral standards, four-dimension threshold design. | Huawei secretary qualification system |
| **secretary-excellence-ladder** | -- | Nine-level secretary excellence ladder: from task execution to system building, with three-floor and four-realm maturity models. | Huawei secretary qualification system |
| **routine-exception-delegator** | -- | Routine vs exception separation: manager handles exceptions, support staff manages routines. Organizational time-value optimization. | Huawei secretary qualification system |
| **meeting-management-master** | -- | Meeting management full-cycle methodology: three essentials before, three services during, three actions after, plus three-check quality control. | Huawei secretary qualification system |
| **executive-support-system-designer** | -- | Executive support system design: secretary positioning, five-core duties, growth channel, and normalization service system. | Huawei secretary qualification system |
| **behavioral-standards-engineer** | -- | Behavioral standards engineering: task-to-competency translation, graded behavior description, NVQ localization, and certification focus design. | Huawei secretary qualification system |
| **industry-convergence-spotter** | -- | Industry convergence opportunity spotting: technology rhythm matching, market demand coupling, infrastructure integration. | Huawei crossover management |
| **enterprise-digital-transformer** | -- | Enterprise digital transformation: five shifts, four initiatives, four hard points, Malik curve guidance. | Huawei crossover management |
| **limit-survival-strategist** | -- | Limit survival strategy: spare-tire system, compute foundation, open ecosystem under extreme pressure. | Huawei crossover management |
| **second-curve-navigator** | -- | Second curve navigation: core capability reuse, boundary discipline, strategic patience for new businesses. | Huawei crossover management |
| **smart-meeting-operator** | -- | Smart meeting operations: pre-meeting preparation, in-meeting discipline, post-meeting closed-loop with digital tools. | Huawei crossover management |
| **cross-industry-ecosystem-builder** | -- | Cross-industry ecosystem building: XYZ stereo blueprint, open partner enablement, anchor case scaling. | Huawei crossover management |
| **qq-sticker-maker** | -- | Guide users through designing and producing animated stickers (APNG/WebP) for QQ and similar platforms, featuring scene + Emoji character composition. | Creative tool |
| **training-battle-designer** | -- | Design and operate a training-battle talent development system: strategic reserve force, heavy-brigade bootcamp, train-fight-recharge loop. | Huawei talent & leadership development |
| **strategic-reserve-force-operator** | -- | Strategic reserve force operations: selection -> training-combat -> deployment -> evaluation -> return/assignment loop for organizational blood circulation. | Huawei talent & leadership development |
| **mentor-system-builder** | -- | Full-cycle mentor system design: selection, matching, agreements, progress tracking, and incentive mechanisms. Great leaders lead leaders. | Huawei talent & leadership development |
| **training-needs-analyst** | -- | Training needs analysis via Three Hard + Three Soft framework. Align training investment with business strategy and prioritize by ROI. | Huawei talent & leadership development |
| **enterprise-university-architect** | -- | Self-sustaining corporate university design: revenue-sharing funding, part-time faculty cycles, budget autonomy, curriculum architecture. | Huawei talent & leadership development |
| **iron-triangle-organizer** | -- | Frontline iron-triangle operating model: AR+SR+FR integrated teams, platform empowerment, delegated authority. Let those who hear gunfire call shots. | Huawei talent & leadership development |
| **talent-inventory-ninebox** | -- | Nine-box talent inventory operations: performance-potential matrix, learning-agility scoring, workload analysis, position-matching dashboard. | Huawei talent & leadership development |
| **culture-institutionalizer-huawei** | -- | Huawei-style culture institutionalization: debate to consensus, habit through institutionalization, atmosphere through leadership example. | Huawei talent & leadership development |
| **elite-soldier-civilian-architect** | -- | Elite + soldier + civilian talent structure: wolf-beaver pairing, zigzag rotation, training-battle integration, three-power separation. | Huawei talent & leadership development |
| **hr-blueprint-strategist** | -- | HR top-level blueprint from Huawei Outline 2.0: organizational vitality, dual drive, cadre/talent/org three objects, platform + frontline. | Huawei talent & leadership development |
| **talent-exit-balancer** | -- | Talent exit and workforce balancing: three-axe rapid improvement, four exit pathways, new-veteran pay conflict resolution. | Huawei talent & leadership development |
| **training-effect-measurer** | -- | Training effectiveness measurement: Kirkpatrick four-level model, conversion rate methodology, linking training to business outcomes. | Huawei talent & leadership development |
| **talent-prsw-framework** | -- | Talent management PRSW framework: Peach (attraction), Rope (retention), Whip (drive), Sieve (elimination) -- systematic full-lifecycle talent management. | Huawei talent & leadership development |
| **team-chemistry-builder** | -- | Team chemistry and leadership pairing: SHL shift model, value convergence + complementary strengths, wolf vs. deputy role design. | Huawei HR management |
| **bonus-package-architect** | -- | Four-level bonus package design: company to system to organization to individual, gain-sharing vs. grant, strategic bounty system. | Huawei HR management |
| **business-stage-appraiser** | -- | Business stage differentiated appraisal: mature (profit) / growth (scale) / exploratory (milestones) three-stage target design. | Huawei HR management |
| **talent-trio-manager** | -- | Three-category talent management: commander (up/down) / expert (rotation) / staff (stability), de-Nanguo policy, role-specific assessment. | Huawei HR management |
| **mid-leadership-accelerator** | -- | Mid-level leadership acceleration: two-focus-items method, on-the-job coaching, stakeholder scoring, 3-month sprint cycles. | Huawei HR management |
| **talent-pipeline-accelerator** | -- | Talent pipeline ROI acceleration: STAR selection, three-stage nurture (bottom/top/exit), four-in-one engagement incentives. | Huawei HR management |
| **audit-deterrence-architect** | -- | Internal audit system design: independence, three-tier monitoring, BC/audit/inspection distinction, value-added audit transformation. | Huawei financial management |
| **anti-corruption-protocol** | -- | Anti-corruption compliance framework: BCG policy, gift/entertainment rules, third-party management, graduated penalties, public dismissal registry. | Huawei financial management |
| **cadre-rescue-protocol** | -- | Cadre supervision and rescue philosophy: investigation-separation principle, rescue-not-punish orientation, collective decision-making, innocence presumption. | Huawei financial management |
| **cadre-selection-architect** | -- | Cadre selection framework: four standards, four forces, nine traits, five qualities, key events, horse-race culture, frontline experience. | Huawei cadre management |
| **cadre-appointment-tribunal** | -- | Cadre appointment and three-powers separation: AT/ST structures, nomination/review/veto, appointment procedures, eight staffing principles. | Huawei cadre management |
| **cadre-performance-governor** | -- | Cadre performance governance: four-quadrant model, bottom-10% elimination, debriefing system, up-and-down mobility, three removals. | Huawei cadre management |
| **cadre-vitality-diagnoser** | -- | Cadre and organizational vitality diagnosis: mission/responsibility/capability 3-layer scan + 10 involution symptoms + 18 laziness behaviors checklist. | Huawei cadre management |
| **cadre-culling-protocol** | -- | Cadre culling and laziness governance: 13 unfit cadre types, 18 laziness behavior checklist, bottom elimination, and up-down mobility enforcement. | Huawei cadre management |
| **commander-staff-pairing** | -- | Commander-staff pairing model: wolf (offense) vs bie (management), principal vs deputy, decision-making + execution pairing. | Huawei cadre management |
| **cadre-values-guardian** | -- | Cadre values and discipline: eight requirements, hard struggle, self-critique, moral bottom line, openness-compromise-grayness. | Huawei cadre management |
| **cadre-90day-turnaround** | -- | New cadre 90-day turnaround: role cognition, management coach, Quickwin targets, five key talks, pre-assignment review. | Huawei cadre management |
| **pfc-pipeline-cultivator** | -- | PFC (Project Financial Controller) cultivation: four basic requirements, four growth directions, remedial training + exam methodology, five excellence characteristics. | Huawei financial management |
| **cost-incremental-evaluator** | -- | Cost evaluation philosophy: elastic budget vs rigid allocation, evaluate by incremental value, four-question cost review, labor-cost optimization. | Huawei financial management |
| **cost-five-focuses** | -- | Five-cost-focus management: design cost (80% determinant), procurement, quality (hidden cost), inventory, period expenses. | Huawei financial management |
| **finance-three-pillar-architect** | -- | Finance three-pillar (COE/BP/SSC) organization design and operations. | Huawei financial management |
| **three-lines-defense-builder** | -- | Three lines of defense internal control system: process ownership, risk supervision, audit cold deterrence. | Huawei financial management |
| **elastic-budget-strategist** | -- | Elastic budget and dynamic resource allocation: white paper, rolling forecast, strategic investment, management accounting. | Huawei financial management |
| **global-treasury-risk-manager** | -- | Global treasury and financial risk management: liquidity, FX, interest rate, credit, daily reconciliation. | Huawei financial management |
| **finance-business-integrator** | -- | Finance-business integration: project estimation, pre-sales finance, project CFO, BP deployment. | Huawei financial management |
| **growth-maximization-strategist** | -- | Growth maximization philosophy: deep-trench-low-dam, reasonable profit, anti-cyclical investment, barrier building. | Huawei financial management |
| **wolf-pack-culture-builder** | -- | Wolf-pack team culture and new employee onboarding: 721 rule, three-stage training, mentor integration, 271 elimination. | Huawei team & cadre management |
| **iron-army-builder** | -- | Iron army four-dimension build: deployable (frontline experience), mobile (3D rotation), capable (top-25% selection), uncorrupted (continuous struggle). | Huawei cadre management |
| **cadre-shelf-operator** | -- | Cadre shelf model: four standards, four forces with six dimensions, four experiences, four-quadrant assessment, unified selection language. | Huawei cadre management |
| **cadre-reserve-west-pointer** | -- | Cadre reserve West Point-style selection: 1/3-of-1/3 funnel, independent university tracking, three-powers oversight, continuous elimination. | Huawei cadre management |
| **cadre-battlefield-groomer** | -- | Battlefield cadre grooming: select from successful frontline teams, clear reward/punishment, results + key-behavior evaluation, heavy incentive gaps. | Huawei cadre management |
| **emt-rotating-ceo-guardian** | -- | Rotating CEO and EMT self-discipline: two mechanisms to eradicate three organizational tumors (factionalism, corruption, complacency). | Huawei cadre management |
| **ren-cadre-tenets** | -- | Ren Zhengfei ten cadre management tenets: systematic self-diagnostic framework for cadre system design. | Huawei cadre management |
| **business-review-facilitator** | -- | Business review meeting facilitation: start with gaps, find root causes with data, build processes. Three-common-failure diagnosis. | Huawei business management |
| **process-driven-org-builder** | -- | Process-driven organization design: business flow -> process -> data -> IT -> quality -> organization six-layer integration. | Huawei business management |
| **frontline-empowerment-architect** | -- | Frontline empowerment and matrix organization: four authorization principles, four maturity stages, Navy SEALs model, post-authorization supervision. | Huawei business management |
| **matrix-organization-architect** | -- | Matrix organization design: strong/balanced/weak matrix types, 1+N reporting, binary structure, committee governance, talent reuse. | Huawei business management |
| **business-transformation-navigator** | -- | Business transformation playbook: seven strategic decisions from Huawei Terminal case, zero-takeoff ritual, platform consolidation, strategic patience. | Huawei business management |
| **strength-based-team-builder** | -- | Strength-based team building: lopsided talent philosophy, wolf-and-bie pairing, complementary roles over perfect individuals. | Huawei business management |
| **ren-business-philosophy** | -- | Ren Zhengfei's twelve management tenets: survive, saline-alkali soil, red-blue army, deep-dredge/low-weir, force through one hole, grayscale, etc. | Huawei business management |
| **execution-craftsman** | -- | Huawei work methodology: SMART discipline, upper-momentum/lower-reality, responsibility to task, four standardizations, pressure principle. | Huawei business management |
| **goal-framework-navigator** | -- | Goal framework selection and operation: MBO decoding vs decomposition, BSC four perspectives, OKR with CFR, procedural justice in evaluation. | Huawei business management |
| **decision-balance-master** | -- | Decision management balancing: growth vs profit, reform vs revolution, lifeless management, half-step lead, dictatorship vs democracy. | Huawei business management |
| **management-twist-engineer** | -- | Management tension design (twist the rope): front-back, top-bottom, inside-outside three twist types for scale-efficiency paradox. | Huawei business management |
| **matter-accountability-designer** | -- | Matter accountability system design: replace person-dependent culture with process-dependent, result-oriented responsibility. | Huawei business management |
| **responsibility-center-operator** | -- | Responsibility center management: profit/cost/expense/investment center design, cost-based internal settlement, delegation + monitoring. | Huawei organization management |
| **org-synergy-architect** | -- | Organizational synergy: process integration, matrix structure, market-driven internal mechanisms, anti-involution design. | Huawei organization management |
| **result-orientation-guardian** | -- | Result-oriented management: forward KPI + backward event review, crisis decomposition, customer-process-performance triad. | Huawei organization management |
| **anti-involution-diagnoser** | -- | Involution and internal waste diagnosis: 30-type involution checklist, 10-waste framework, organizational health examination. | Huawei organization management |
| **consulting-value-maximizer** | -- | Consulting engagement value maximization: trust-first, milestone rigor, knowledge transfer, systematic consultant management. | Huawei organization management |
| **simple-org-culture-builder** | -- | Simple organization and culture building: capability in systems, three mechanisms, values-to-behavior translation, contract over loyalty. | Huawei organization management |

## Design Philosophy

Each skill follows three principles:

1. **Abstraction over domain** -- The core step framework stays abstract; domain vocabulary is swapped at the application layer.
2. **Scenario demos enrich coverage** -- A skill becomes more useful when it carries cross-domain demos (film crews, novel writing, brand planning, course design) mapped onto the same underlying steps.
3. **Actionable, not academic** -- Every skill must answer "What do I do Monday morning?" not just "What is the theory?"

Additional engineering principles:

- **Layered, not monolithic.** Each skill does one thing and depends downward.
- **Safety-gated.** NeatFreak has three explicit modes; destructive operations require agent confirmation.
- **Index once, query many.** CodeGraph and WikiBrain both build SQLite FTS5 indexes for fast retrieval.
- **Agent-native.** Designed for AI agents to use as tools -- CLI interfaces, structured output, self-contained dependencies.

## Quick Start

```bash
git clone https://github.com/JuliaHZhu/manager-skills-box.git
cd manager-skills-box
```

Each skill is self-contained under its own directory with a `SKILL.md` reference, `scripts/`, and supporting files.

### Initialize & Index

```bash
# Foundation: track your workspace files
python filestates/scripts/cli.py plan new my-task --objective="Build feature X" --goal-kind=feature

# Code: index your source tree
python codegraph/scripts/cli.py init
python codegraph/scripts/cli.py index ./src

# Knowledge: build a wiki from raw materials
python wikibrain/scripts/cli.py init
python wikibrain/scripts/cli.py ingest paper.pdf --category papers
python wikibrain/scripts/cli.py index

# Govern: scan for issues across all layers
python neatfreak/scripts/cli.py scan
```

### Key Commands

```bash
# FileStates -- never write directly again
python filestates/scripts/cli.py fs_write path/to/file.py "content" source
python filestates/scripts/cli.py fs_rewind path/to/file.py 1   # undo last write

# CodeGraph -- understand your codebase
python codegraph/scripts/cli.py search "function_name"
python codegraph/scripts/cli.py blast "critical_function" 200

# WikiBrain -- query your knowledge
python wikibrain/scripts/cli.py query "research question" 10
python wikibrain/scripts/cli.py lint

# NeatFreak -- keep it clean
python neatfreak/scripts/cli.py report
python neatfreak/scripts/cli.py fix --apply
```

## Usage

These skills are packaged for [ClawHub](https://clawhub.io) / OpenClaw-compatible agents.

Install a skill locally:
```bash
clawhub install <skill-name>
```

Or copy the `SKILL.md` and supporting files directly into your agent's skills directory.

## License

MIT-0 -- Free to use, modify, and redistribute. No attribution required.
