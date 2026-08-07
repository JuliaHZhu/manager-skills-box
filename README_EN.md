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
| **pbc-performance-contractor** | -- | PBC performance commitment design: strategy decoding -> BSC -> KPI -> personal PBC, WET three elements, SMART criteria, refresh mechanism. | Huawei performance management |
| **forced-distribution-enforcer** | -- | Forced distribution and performance result application: 5-grade absolute definition, horse-racing mechanism, layered evaluation, 10% elimination. | Huawei performance management |
| **org-performance-aligner** | -- | Organizational and personal performance alignment: DSTE+BLM+PBC docking, hat-wearing and twisted rope, budget and payroll management. | Huawei performance management |
| **rd-performance-designer** | -- | R&D performance management: benefit/efficiency/path/behavior four-dimension indicators, IPD-based R&D performance, project-based assessment. | Huawei performance management |
| **incremental-performance-driver** | -- | Incremental performance and value distribution: value creation -> evaluation -> distribution closed loop, payroll control, 3-people-5-jobs-4-pay. | Huawei performance management |
| **performance-coach-grow** | -- | Performance coaching and GROW model: coaching-style guidance, GROW four-step, performance interview, low-performer PIP management. | Huawei performance management |
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
| **mentor-system-builder** | -- | Full-cycle mentor system design: selection, matching, agreements, progress tracking, and incentive mechanisms. Great leaders lead leaders. | Huawei talent & leadership development |
| **training-needs-analyst** | -- | Training needs analysis via Three Hard + Three Soft framework. Align training investment with business strategy and prioritize by ROI. | Huawei talent & leadership development |
| **enterprise-university-architect** | -- | Self-sustaining corporate university design: revenue-sharing funding, part-time faculty cycles, budget autonomy, curriculum architecture. | Huawei talent & leadership development |
| **iron-triangle-organizer** | -- | Frontline iron-triangle operating model: AR+SR+FR integrated teams, platform empowerment, delegated authority. Let those who hear gunfire call shots. | Huawei talent & leadership development |
| **training-effect-measurer** | -- | Training effectiveness measurement: Kirkpatrick four-level model, conversion rate methodology, linking training to business outcomes. | Huawei talent & leadership development |
| **team-chemistry-builder** | -- | Team chemistry and leadership pairing: SHL shift model, value convergence + complementary strengths, wolf vs. deputy role design. | Huawei HR management |
| **bonus-package-architect** | -- | Four-level bonus package design: company to system to organization to individual, gain-sharing vs. grant, strategic bounty system. | Huawei HR management |
| **business-stage-appraiser** | -- | Business stage differentiated appraisal: mature (profit) / growth (scale) / exploratory (milestones) three-stage target design. | Huawei HR management |
| **talent-trio-manager** | -- | Three-category talent management: commander (up/down) / expert (rotation) / staff (stability), de-Nanguo policy, role-specific assessment. | Huawei HR management |
| **mid-leadership-accelerator** | -- | Mid-level leadership acceleration: two-focus-items method, on-the-job coaching, stakeholder scoring, 3-month sprint cycles. | Huawei HR management |
| **talent-pipeline-accelerator** | -- | Talent pipeline ROI acceleration: STAR selection, three-stage nurture (bottom/top/exit), four-in-one engagement incentives. | Huawei HR management |

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
