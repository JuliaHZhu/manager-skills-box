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
| **qq-sticker-maker** | -- | Guide users through designing and producing animated stickers (APNG/WebP) for QQ and similar platforms, featuring scene + Emoji character composition. | Creative tool |

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
