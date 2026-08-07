# process-driven-org-builder

## Metadata

- **Source**: Huawei Management Handbook (5th Ed) — Business Management, Chapter 11
- **Domain**: Organization design / Process management
- **Confidence**: High (derived from documented Huawei practice)
- **Revision**: 1.0

## When to Activate

Use when the user needs to design a customer-centric, process-driven organization; map end-to-end business flows; align organization structure with process; or discuss "流程决定组织" (process determines organization). Also triggers when IT systems fail to support business because process and org are misaligned.

**Key triggers**: 流程化组织 / process-driven organization / 业务流 / business flow / 端到端流程 / E2E process / 流程决定组织 / 流程与组织匹配 / 流程化组织建设 / process and organization alignment

**Not for**: pure IT system selection without process context, or simple departmental restructuring without business-flow analysis.

## Core Methodology

Huawei's process-driven organization is built on six integrated elements: Business Flow → Process → Data → IT → Quality → Organization. The skill guides users through each layer.

### Layer 1: Identify the Business Flow (业务流)

Business flows are objective realities, not designs. They exist whether you document them or not.

1. **Customer-to-customer principle** — Every flow that creates value starts with a customer requirement and ends with customer satisfaction and enterprise value realization.
2. **Find the shortest path** — Among all possible ways to deliver value, there is one shortest path. Your process should approximate it.
3. **Flows are not department-specific** — Do not let department boundaries fragment the flow.

Key flows in Huawei:
- IPD (Integrated Product Development): idea → product
- LTC (Lead to Cash): opportunity → cash
- ITR (Issue to Resolution): problem → solution

### Layer 2: Design the Process (流程)

Process is the representation of business flow — the固化 of best practices.

1. **Process must match flow** — The closer the process is to the actual business flow, the smoother it runs. If process contradicts flow, abolish the process.
2. **Process defines roles, not departments** — In the process, define only roles (e.g., "account manager," "solution architect"). Let the organization carry the roles. Do not bind process steps to departments.
3. **Process determines organization** — First design the process, then assign organizational units to carry the roles within it.
4. **Avoid cross-flow org attachment** — An organizational unit should not be attached to two disconnected segments of a flow. Either own one complete segment, or own multiple complete flows.

### Layer 3: Manage Data (数据)

Data is the information that runs inside the process.

1. **Data = process output** — Every activity in the process must produce data that downstream needs. If an activity produces no usable output, it is waste.
2. **Just-right information** — Each step should output exactly the information the next step needs — no more, no less.
3. **Information architecture first** — Before building IT systems, map the information architecture and data flow. IPD's early mistake was building IT before defining data, leading to chaotic tools.
4. **Guard the entry** — If garbage enters the process, the process outputs garbage. Manage the information entry point strictly.

### Layer 4: Enable with IT (IT承载)

IT is the enabler that carries the process and automates data handoffs.

1. **IT runs process, not replaces it** — Without process, IT is just expensive paper. Without IT, process relies on human transfer (slow and error-prone).
2. **Automate integration** — The ideal state is end-to-end automation: all activities and data are carried by IT, integrated from start to finish.
3. **IT for scale** — If only 20-30 people use a process, IT may not be necessary. If thousands use it, IT is mandatory.

### Layer 5: Build in Quality (质量)

Quality is defined as "conformance to requirements" (Philip Crosby). Quality requirements must be embedded in the process.

1. **Process quality → result quality** — Manage process quality to guarantee result quality.
2. **Define input/output standards per step** — Each activity must have clear deliverables and quality criteria (checklists).
3. **Enable content** — Provide tools, methods, and guides (the "how") to help each role meet the "what."
4. **Internal control built-in** — Internal control (SOD, key control points) must be embedded in the process, not bolted on afterwards.
5. **Information security built-in** — Identify core information assets based on process flow, and protect them where they are created.

### Layer 6: Match Organization (组织匹配)

Organization carries roles; process defines roles.

1. **Three design principles**:
   - Horizontal consistency: each process is executed consistently across all business units globally.
   - Vertical integration: each business unit integrates all processes it participates in.
   - E2E responsibility: every functional unit is responsible for end-to-end results, not just handoffs.

2. **Project-based execution** — The most effective way for functional units to participate in business flows is through cross-functional projects / program teams.
3. **Discipline (专业领域) concept** — Process defines "what" (deliverables). Discipline defines "how" (methods). Disciplines can be owned by functional departments.
4. **Business owner is process owner** — The business leader, not IT or a consultant, owns the process. IT and consultants provide expertise; business provides mandate and adoption.

## STOP Checkpoints

- **STOP if** the organization chart is designed before the process map. Reverse the order.
- **STOP if** a process step is named after a department (e.g., "Finance reviews"). Name it after a role or decision.
- **STOP if** IT is being built without a defined data model and information architecture.
- **STOP if** quality control is performed outside the process (post-hoc inspection only).

## Anti-Patterns (Blacklist)

| Anti-Pattern | Why It Fails | Correct Practice |
|--------------|--------------|------------------|
| Org-first design | Departments optimize locally, breaking E2E flow | Process-first, org-second |
| Process = department workflow | Creates silos and handoff delays | Process is cross-functional |
| IT without data architecture | Tools don't integrate; information chaos | Map data flow before IT |
| Quality as external audit | Finds defects too late; blame culture | Quality built into each step |
| Functional relay race | Each dept does its part, no one owns outcome | Football-team model: all play together |

## Test Prompts

See `test-prompts.json` for validation scenarios.
