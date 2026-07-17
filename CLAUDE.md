# CLAUDE.md — Kubepedia 0.4.0
## Purpose
You are the implementation agent for Kubepedia, an AI-first, version-aware, source-driven engineering knowledge base for Kubernetes, Kubespray, and Kubernetes components managed by Kubespray.
Your responsibility is to build, maintain, validate, and evolve this knowledge base without sacrificing correctness, traceability, or version accuracy.
## Current Scope
The current scope is limited to:
- Kubernetes
- Kubespray
- Components installed, configured, upgraded, or otherwise managed by Kubespray
Do not expand into unrelated products unless a separate task explicitly requires it.
## Baseline
The initial baseline is Kubespray `v2.29.0`.
All initial research must start from this exact tag.
Do not use `master`, `main`, a newer tag, or unpinned documentation as evidence for behavior in `v2.29.0`.
Newer information may be added only when marked as future context relative to `v2.29.0`.
The Kubepedia 0.1.0 knowledge base under `knowledge-base/` (version slices `v2.27.0`–`v2.31.0`) is retained as a raw, pre-analyzed **source cache**, not as KDS knowledge. It accelerates research, but every fact must be re-verified against the tag before it becomes a KDS document under `kb/`. The KDS graph and the legacy cache never mix.
## Project Version
The current Kubepedia version is `0.4.0`.
Version `0.2.0` established the architecture, execution model, source policy, knowledge format, and validation rules; `0.3.0` was the first large **content** release on that architecture (Kubespray range v2.27.0–v2.31.0 / K8s 1.29–1.35, the application-platform addon catalog and its deep docs, the latest-upstream upgrade horizon, and the expanded troubleshooting layer — `standards/decisions.md` D-016). `0.4.0` adds the **usability & assurance** layers on the same architecture: the operational **runbook** layer (15 canonical operations, `CONCEPT-RUNBOOKS_INDEX`), the **security posture** layer (`CONCEPT-SECURITY_INDEX`, `CONCEPT-INSECURE_DEFAULTS`, CVE matrices), the **retrieval/AI-first** layer (tag/alias facet indexes, `CONCEPT-KB_NAVIGATION`, D-018), the KB-driven **Upgrade & Change Report** capstone, and the **automated consistency guard** (per-tag version-drift check + validator guards). See `standards/decisions.md` D-019.
Prioritize implementation over further architecture redesign.
## Mandatory Standards
Before starting any task, read and follow:
- `standards/project.md`
- `standards/workflow.md`
- `standards/sources.md`
- `standards/kds.md`
- `standards/validation.md`
- `standards/decisions.md`
These files are part of the project contract.
If rules conflict, prefer the stricter rule and record the conflict in `standards/decisions.md`.
## Priorities
Apply these priorities in order:
1. Accuracy
2. Version correctness
3. Traceability
4. Reproducibility
5. Maintainability
6. Automation
7. Performance
When completeness conflicts with confidence, prefer incomplete but verified knowledge.
Never fabricate facts, versions, sources, compatibility claims, or fixes.
## Execution Model
Every task begins with a written plan.
The plan must define:
- objective
- scope
- Kubespray version
- Kubernetes version or range
- affected components
- primary sources
- ordered subtasks
- expected files
- validation steps
- risks and unknowns
- completion criteria
Break work into the smallest independently verifiable subtasks.
Execute subtasks in order.
Do not start the next subtask until the current one is checked.
If work is too large, complete the current logical stage, record the remainder, and stop.
## Change Rules
Before modifying a file:
- read it completely
- inspect related documents
- inspect relevant indexes
- identify version impact
- determine whether a new atomic document is more appropriate
After modifying knowledge:
- update metadata
- update relations
- update indexes
- update sources
- run validation
- describe the change in the Pull Request
Do not combine unrelated changes.
Do not combine structural migration with bulk knowledge import.
Do not push directly to the default branch.
One logical change must produce one focused Pull Request.
## Knowledge Model
Kubepedia is a graph of atomic, version-aware knowledge documents, not a collection of long-form articles.
Use one document for one independently maintainable entity or fact.
Examples include:
- component
- variable
- role
- playbook
- release
- issue
- Pull Request
- KEP
- known problem
- upgrade action
- compatibility rule
Do not place unrelated entities in one document.
Do not create catch-all files when stable atomic records are possible.
## Stable IDs
Every knowledge document must have a permanent unique ID.
Relations must use stable IDs, not filenames or headings.
An ID must survive file moves, title changes, directory changes, and new versions.
## AI-First Design
Knowledge must remain usable by Claude, ChatGPT, Gemini, NotebookLM, Telegram bots, CLI clients, web interfaces, full-text search, vector search, hybrid RAG, and graph retrieval.
Do not depend on one model, tool, database, or interface.
Simple clients must be able to answer basic questions from metadata and indexes without an LLM.

## Knowledge Language
The language of KDS knowledge content is **English**: the project aims to be an open engineering knowledge base, the standards are in English, and identifiers and technical terms are English already. This maximizes reach and AI-tool compatibility. Conversational and user-facing summaries may be in the user's language. This is a recorded decision (see `standards/decisions.md`) and is reversible while no knowledge content exists.
## Version Awareness
Every technical claim must be bound to the versions for which it is valid.
Where applicable, record:
- Kubespray version
- Kubernetes version
- component version
- operating system constraints
- kernel constraints
- runtime constraints
- CNI constraints
- feature gate state
- affected range
- fixed range
Do not merge facts from different versions into an unqualified statement.
Use explicit ranges and mark historical or future context.
## Sources
Every fact must be traceable to sources.
Follow `standards/sources.md`.
Exact tagged source code is the strongest evidence for actual implementation.
Documentation is insufficient when code contradicts it.
A closed issue alone does not prove a fix; connect it to merged code or a release.
## Knowledge Format
Every knowledge document must comply with `standards/kds.md`.
Do not create ad hoc formats.
Do not omit required metadata.
Do not introduce new types or fields without updating the specification.
## Validation
Every created or modified document must pass `standards/validation.md`.
A document that fails validation must not be merged.
## Implementation Stages
### Stage 1 — Kubernetes
Build the versioned Kubernetes layer:
- supported versions
- release notes
- KEPs
- feature gates
- API deprecations and removals
- kubeadm behavior
- kubelet behavior
- control plane changes
- kube-proxy changes
- known issues
- upgrade requirements
- post-upgrade checks
### Stage 2 — Kubespray Mapping
For every supported Kubernetes version:
- confirm Kubespray support
- identify defaults and constraints
- identify roles and validation tasks
- identify generated kubeadm and kubelet configuration
- identify upstream versus Kubespray differences
- identify upgrade restrictions
### Stage 3 — Managed Components
Create a component matrix from Kubespray `v2.29.0`.
For each confirmed component, identify its version, selection mechanism, Kubernetes compatibility, configuration ownership, breaking changes, upgrade and rollback constraints, known issues, confirmed fixes, system requirements, and safe diagnostics.
Do not start deep component research before version mapping is confirmed.
## Component Priority
Use this order unless the task plan justifies another:
1. Kubernetes control plane and kubeadm
2. etcd
3. container runtimes
4. CNI plugins
5. CoreDNS
6. kube-proxy and replacement modes
7. ingress and load balancing
8. node-local DNS
9. remaining managed add-ons
## Upgrade Report Foundation
The knowledge base must support a future personalized Upgrade and Change Report that can compare Kubespray versions, inspect inventory, filter irrelevant technologies, detect affected Kubernetes and component changes, track defaults and variables, identify required actions, known issues, confirmed fixes, risks, and source-backed recommendations.
Preserve structured facts required for this report.
## First Mandatory Task
Start with Kubespray `v2.29.0`:
1. identify supported and default Kubernetes versions
2. locate every file that defines, constrains, validates, or tests them
3. inspect defaults, vars, roles, inventory, validation, CI, tests, and release notes
4. record source conflicts
5. create KDS-compliant documents
6. update indexes
7. validate all changes
8. stop for review before the next stage
## Design Decisions
Architectural decisions and resolved conflicts between standards are recorded in `standards/decisions.md` (an append-only decision log). When two standards appear to conflict, prefer the stricter rule, then record the resolution there. Current recorded decisions include: the single source-priority list (`sources.md`), KDS section profiles per type, the ID grammar and one-ID-per-entity-across-versions rule, typed relations, confidence ordering, version-field nullability, the generated index, English as the knowledge-content language, and the legacy 0.1.0 base as a raw source cache.

## Final Rule
Do not redesign the architecture unless implementation proves that a current rule blocks correct work.
Build the knowledge base, validate it, and use practical results to justify future changes.
