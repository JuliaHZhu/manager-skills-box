# Manager Skills Box

A curated collection of agent skills distilled from real-world management and engineering practices -- not theory, but battle-tested playbooks.

---

## Skills

| Skill | Description | Source |
|-------|-------------|--------|
| **project-delay-prevention** | Six-step anti-procrastination system for complex projects: team-building, assessment, decomposition, monitoring, coaching, and closed-loop tracking. | Huawei R&D management practice + Zeng Guofan's personnel philosophy |
| **topic-analysis-driven-design** | Replace "draw-debug-redraw" loops with mandatory topic analyses (power, clock, subsystem) before any design work begins. | Huawei hardware design methodology |
| **hw-normalization-design** | Four-layer normalization methodology: component -> board -> platform -> network architecture. | Huawei hardware platform design |
| **filestates** | Lightweight file-state tracking with snapshot, plan, and archive management for project artifacts. | Internal toolchain |
| **codegraph** | Code dependency graph analysis with blast-radius indexing for refactoring and review. | Internal toolchain |
| **wikibrain** | Structured knowledge-base indexing with concept/entity pages and session extraction. | Internal toolchain |
| **neatfreak** | Automated workspace cleanup with safety rules, pattern matching, and archival reporting. | Internal toolchain |

---

## Design Philosophy

Each skill follows three principles:

1. **Abstraction over domain** -- The core step framework stays abstract; domain vocabulary is swapped at the application layer.
2. **Scenario demos enrich coverage** -- A skill becomes more useful when it carries cross-domain demos (film crews, novel writing, brand planning, course design) mapped onto the same underlying steps.
3. **Actionable, not academic** -- Every skill must answer "What do I do Monday morning?" not just "What is the theory?"

---

## Usage

These skills are packaged for [ClawHub](https://clawhub.io) / OpenClaw-compatible agents.

Install a skill locally:
```bash
clawhub install <skill-name>
```

Or copy the `SKILL.md` and supporting files directly into your agent's skills directory.

---

## License

MIT-0 -- Free to use, modify, and redistribute. No attribution required.
