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
