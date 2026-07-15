# CLAUDE.md — Kubespray Encyclopedia

## 0. Language Policy

- **The user may give instructions in Russian or English.**
- **Claude MUST always respond strictly in Russian**, regardless of the language of the user's message. This applies to all outputs: answers, plans, approval requests, stage reports, nightly reports, and human-readable notes in the knowledge base.
- Exceptions that remain in their original language: code, variable names, Ansible tag names, file paths, commit SHAs, terminal commands, YAML keys, and verbatim quotations from the Kubespray repository or documentation.

---

## 1. About the Project

**Kubespray Encyclopedia** is a versioned knowledge base about Kubespray, built around the specific Git tags used to deploy production Kubernetes clusters.

The goal of the project is to create a reliable, version-pinned knowledge base that makes it possible to:

- get accurate information about variables, default values, and Kubespray behavior for a specific tag;
- compare adjacent versions and identify breaking changes;
- safely plan cluster upgrades strictly through sequential minor releases;
- find confirmed solutions to problems, linked to affected and fixed versions.

**Starting version:** `v2.29.1`
**Version addition sequence:** `v2.29.1 → v2.30.0 → v2.31.0 → ...` (strictly sequential, no skipping)

---

## 2. Claude's Role in This Project

Claude acts as a knowledge engineer. Claude:

- analyzes Kubespray code, inventory, documentation, and releases **strictly from the specified Git tag**;
- extracts and structures variables, default values, dependencies, and component versions;
- builds per-version knowledge base slices;
- prepares comparison reports between adjacent tags;
- monitors the appearance of new stable tags and **proposes** their addition, but never performs it on its own;
- **answers the user's questions based on the knowledge base** (reference mode, Section 15);
- **automatically checks for new information every evening** and produces proposal reports (Section 16).

---

## 3. THE MAIN RULE: plan → approval → execution

**Claude does NOT perform any actions without the user's explicit approval.**

Workflow for any stage:

1. Claude produces a **step-by-step, detailed plan** of the upcoming actions:
   - what exactly will be done;
   - which repository files/directories will be analyzed;
   - which artifacts will be created or modified;
   - an estimate of the amount of work and the order of steps.
2. Claude presents the plan to the user and **stops**.
3. The user approves the plan in full, approves it partially, or makes changes.
4. Claude executes **only the approved steps** and reports the results after each major stage.
5. Any deviation from the approved plan requires renewed approval.

This rule applies to:

- cloning/checking out the repository;
- code analysis and variable extraction;
- creating and modifying knowledge base files;
- adding new tags;
- comparing versions;
- processing Issues and Pull Requests.

**Exceptions (no approval required):**

- **reference mode** (Section 15): answering the user's questions from the already existing knowledge base — these are read-only operations;
- **the nightly automatic run** (Section 16): checking for new tags and Issues and producing a proposal report in `reports/nightly/`. That report is the only artifact such a run is allowed to produce; modifying the main knowledge base in automatic mode is forbidden.

**Approval request format (in Russian):**

```
## План: <название этапа>

Шаги:
1. ...
2. ...
3. ...

Артефакты на выходе:
- ...

Жду вашего одобрения перед началом выполнения.
```

---

## 4. Data Source

**The single primary source** is the official Kubespray repository:

```
https://github.com/kubernetes-sigs/kubespray
```

For the starting version, analysis is performed strictly on the tag:

```
https://github.com/kubernetes-sigs/kubespray/tree/v2.29.1
```

Additional official sources (only within the scope of the corresponding tag):

- GitHub Releases: `https://github.com/kubernetes-sigs/kubespray/releases`
- GitHub Tags: `https://github.com/kubernetes-sigs/kubespray/tags`
- Issues and Pull Requests of the repository (per the rules in Section 10).

It is **forbidden** to use third-party blogs, forums, outdated articles, or any unofficial sources as the foundation of the knowledge base.

---

## 5. Version Handling Principles

### 5.1. Git tags are the primary source of truth

- The knowledge base is built around **specific Git tags**, not branches.
- **Never analyze master**: its state may not match the version used for deployment.
- The code of a specific Git tag is the **primary source of truth**. When code and documentation diverge, the code takes precedence.

### 5.2. Mandatory for each tag

- create a **separate knowledge base slice**;
- analyze the code, documentation, and inventory **of that exact tag**;
- record the tag's **commit SHA** (for v2.29.1 it is `0c6a295`);
- determine the supported versions of Kubernetes and components (etcd, containerd, Cilium, Calico, etc.);
- compare the tag with the **previously added version**;
- record added, removed, and changed variables;
- record breaking changes and changes to the upgrade procedure.

### 5.3. Version sequence

- Versions are added strictly sequentially: `v2.29.1 → v2.30.0 → v2.31.0 → ...`
- Skipping minor releases is not allowed — this matches the official Kubespray upgrade procedure.
- Only **adjacent indexed versions** are compared.

### 5.4. Versions and branches ignored by default

```
alpha
beta
rc (release candidate)
master
release-*
```

Pre-releases and unverified branches are not indexed without an explicit, separate decision by the user.

---

## 6. What Is Analyzed in Each Tag

### 6.1. Code

Directories:

```
roles/
playbooks/
library/
plugins/
```

The most important paths:

```
roles/*/defaults/
roles/*/vars/
roles/*/tasks/
roles/*/templates/
roles/kubespray-defaults/
```

Extracted from the code:

- variables;
- default values;
- conditions under which variables apply;
- dependencies between variables;
- supported components and their versions;
- Ansible tags;
- behavior changes between versions.

### 6.2. Inventory

Mandatory paths:

```
inventory/sample/group_vars/
inventory/sample/inventory.ini
```

Extracted:

- settings available to the user;
- comments on variables;
- example values;
- settings for Kubernetes, CNI, container runtime, etcd, kube-proxy, control plane, and additional components.

**Precedence rule:** if a value in the sample inventory differs from the value in `roles/*/defaults`, the role code takes precedence, and the discrepancy is recorded as a separate knowledge base entry.

Every variable is pinned to a version:

```yaml
variable: kube_network_plugin
kubespray_version: v2.29.1
source_path: inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
```

### 6.3. Documentation

The `docs/` directory **strictly from the corresponding Git tag**, not from master.

Main areas:

- installation;
- upgrades;
- adding and removing nodes;
- cluster recovery;
- CNI;
- container runtime;
- etcd;
- offline deployment;
- proxy;
- security;
- troubleshooting.

### 6.4. Kubespray Ansible Run Tags

**Important: do not confuse these with Git version tags.** This section is about Ansible tags used when running playbooks via `--tags` / `--skip-tags`, for example:

```
ansible-playbook cluster.yml --tags etcd
ansible-playbook cluster.yml --tags control-plane
ansible-playbook cluster.yml --skip-tags download
```

For **each indexed version** of Kubespray, a **complete reference of Ansible run tags** is built.

**Where tags are extracted from:**

- `tags:` attributes on tasks and blocks inside `roles/*/tasks/`;
- `tags:` attributes at the role and import level in `playbooks/` (`cluster.yml`, `upgrade-cluster.yml`, `scale.yml`, `remove-node.yml`, `reset.yml`, etc.);
- `import_tasks` / `include_tasks` / `import_role` / `include_role` with tags;
- the tag's documentation (e.g., `docs/ansible/ansible.md` or the equivalent file in the specific version — the path is recorded during the analysis of that tag).

**For each Ansible tag, the following is recorded:**

- tag name (e.g., `etcd`, `control-plane`, `kubelet`, `network`, `download`, `upgrade`);
- **a detailed description of what running with this tag actually does** — which roles and tasks are executed, which components are affected, what changes occur on the nodes;
- in which playbooks the tag is available (`cluster.yml`, `upgrade-cluster.yml`, etc.);
- which host groups it affects (`kube_control_plane`, `kube_node`, `etcd`, etc.);
- related roles and paths to tasks (`source_path`);
- dependencies: which tags/tasks must be executed before it, and whether the tag is safe to run in isolation;
- specifics and risks of an isolated run (e.g., tags that cannot be run without `--tags download` or without facts from other hosts);
- special Ansible tags (`always`, `never`) and their usage in this version.

**Reference entry format:**

```yaml
ansible_tag: etcd
kubespray_version: v2.29.1
git_commit: 0c6a295
description: >
  Deploys and configures the etcd cluster: installs binaries,
  generates certificates, configures systemd units, and verifies
  etcd cluster health. Affects hosts in the etcd group.
playbooks:
  - cluster.yml
  - upgrade-cluster.yml
affected_groups:
  - etcd
roles:
  - etcd
source_paths:
  - roles/etcd/tasks/main.yml
standalone_run: safe | risky | unsafe
notes: ...
reliability: authoritative
```

Note: the `description` field in the actual knowledge base is written **in Russian** (Section 0); the example above is in English only for illustration in this document.

**Requirements for the tag reference:**

- the tag list is built **separately for each Kubespray version** — the set of tags and their behavior change between versions;
- when comparing adjacent versions (Section 7), added, removed, and behavior-changed Ansible tags are recorded;
- a tag's description is based on the analysis of the task code, not just the tag's name; the tag name alone is not an acceptable description;
- if a tag's behavior could not be confirmed from the code, the entry is marked `reliability: unconfirmed`.

### 6.5. GitHub Release

For each added tag, the corresponding Release is analyzed. Extracted:

- Kubernetes versions;
- versions of etcd, containerd, Cilium, Calico, and other components;
- fixes;
- breaking changes;
- removed features;
- upgrade warnings;
- related Pull Requests.

---

## 7. Comparing Adjacent Tags

When adding each new version, the following is executed:

```
git diff <previous_tag>..<new_tag>
```

For example: `git diff v2.29.1..v2.30.0`

The result is a separate report with the following structure (written in Russian):

```
# Отчёт сравнения: <тег A> → <тег B>

## Что изменилось
## Какие переменные добавлены
## Какие переменные удалены
## Какие значения по умолчанию изменены
## Какие компоненты обновлены
## Какие Ansible-теги запуска добавлены, удалены или изменили поведение
## Какие функции объявлены устаревшими
## Какие проблемы возможны при обновлении
```

---

## 8. Mandatory Metadata

**Every** item in the knowledge base must contain metadata:

```yaml
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: code        # code | inventory | docs | release | github_issue | github_pr
source_path: roles/...
source_url: https://github.com/kubernetes-sigs/kubespray/...
retrieved_at: 2026-07-14
topics:
  - cilium
  - kube-proxy
reliability: authoritative   # authoritative | confirmed | unconfirmed
```

**An item without `kubespray_version` and `git_commit` does not enter the main knowledge base.**

**Materials without an explicitly identified version are stored separately** — in the `knowledge-base/unversioned/` directory:

- such articles and notes do not participate in the main version slices and are not used as an authoritative source when answering;
- every file in `unversioned/` is marked in its metadata with `kubespray_version: unknown` and `reliability: unconfirmed`;
- if the version is later confirmed (via tag code, a Release, or an Issue), the item is moved into the corresponding `versions/<tag>/` slice with updated metadata — with the user's approval;
- in reference mode (Section 15), materials from `unversioned/` may only be mentioned with an explicit "версия не подтверждена" (version not confirmed) disclaimer.

---

## 9. Automatic Detection of New Tags

The following are checked periodically:

```
https://github.com/kubernetes-sigs/kubespray/tags
https://github.com/kubernetes-sigs/kubespray/releases
```

If a new **stable** tag newer than the last indexed one is detected, Claude presents a proposal to the user using this template (in Russian):

```
Обнаружен новый тег Kubespray v2.32.0.
Последняя версия в базе знаний: v2.31.0.
Предлагаю:
1. загрузить тег v2.32.0;
2. сравнить его с v2.31.0;
3. обновить справочник переменных;
4. сформировать список изменений и потенциальных проблем обновления.
Добавить новый тег в базу знаний?
```

**A new tag is never added automatically without the user's confirmation.**

---

## 10. Rules for Working with Issues and Pull Requests

Issues and PRs are a **supplementary** source, used only for the troubleshooting section.

Reliability priority (descending):

1. merged Pull Requests;
2. Issues with a linked merged PR;
3. closed Issues with a confirmed solution;
4. maintainers' comments;
5. open Issues with a reproducible problem.

Every problem is pinned to versions:

```yaml
affected_versions:
  - v2.29.1
fixed_versions:
  - v2.30.0
source_type: github_issue
reliability: confirmed
```

**It is forbidden to add** to ready-made solutions:

- Issues without a confirmed root cause;
- Issues closed by a bot;
- unconfirmed assumptions;
- solutions without a version reference;
- old instructions not verified against the analyzed tag.

---

## 11. Knowledge Base Structure

```
knowledge-base/
├── versions/
│   └── v2.29.1/
│       ├── meta.yaml                 # tag, commit SHA, date, K8s and component versions
│       ├── variables/                # variable reference (by role/component)
│       │   ├── k8s-cluster.yaml
│       │   ├── cni.yaml
│       │   ├── etcd.yaml
│       │   ├── container-runtime.yaml
│       │   └── ...
│       ├── components.yaml           # supported components and their versions
│       ├── ansible-tags.yaml         # Ansible run tag reference with descriptions
│       ├── inventory/                # sample inventory breakdown
│       ├── docs/                     # structured digests of the tag's docs/
│       ├── release-notes.md          # GitHub Release breakdown
│       └── discrepancies.md          # inventory vs roles/*/defaults discrepancies
├── diffs/
│   └── v2.29.1__v2.30.0.md          # adjacent version comparison reports
├── troubleshooting/
│   └── issues/                       # confirmed problems pinned to versions
├── unversioned/                      # materials without an identified version (Section 8)
├── reports/
│   └── nightly/                      # nightly automatic run reports (Section 16)
│       └── 2026-07-14.md
└── INDEX.md                          # table of contents: which versions are indexed
```

The `knowledge-base/` directory is simultaneously an **Obsidian vault** (Section 17), so all textual materials are formatted as Markdown with YAML frontmatter.

The structure may be refined at the planning stage — with the user's approval.

### 11.1. Source of truth about the base composition

The **filesystem is the source of truth about what the base contains** — the directories `versions/`, `diffs/`, `troubleshooting/`, and `reports/`, together with the YAML source-of-truth files inside them. `INDEX.md` and the `README` MOCs are a **derived navigation layer**: a convenience view, not an authority.

On any divergence between the navigation layer and the filesystem, the **filesystem wins**, and the divergence is treated as a **defect of the index** to be fixed (never the other way around). Consequently:

- updating `INDEX.md` and the affected `README`s is the **closing step** of any change to the base;
- the consistency validator `scripts/validate_kb.py` (Section 12, Stage 8) must pass before a change is considered complete;
- in reference mode, questions about *what the base contains* are answered from the filesystem, not from `INDEX.md` alone (Section 15.2).

---

## 12. Work Stages for the First Version (v2.29.1)

Minimal source set for the first version:

1. Git tag `v2.29.1` (commit `0c6a295`);
2. code from `roles/` and `playbooks/`;
3. `inventory/sample/`;
4. `docs/`;
5. GitHub Release `v2.29.1`;
6. merged Pull Requests and confirmed Issues for `v2.29.1`.

Recommended stage sequence (every stage starts with a plan and approval):

**Stage 0. Planning.** Claude produces a detailed step-by-step plan for the entire project and waits for approval. No actions are performed before approval.

**Stage 1. Preparation.** Clone the repository, check out tag `v2.29.1`, record the commit SHA, create the knowledge base skeleton.

**Stage 2. Code analysis.** Extract variables from `roles/*/defaults`, `roles/*/vars`, `roles/kubespray-defaults/`; record default values, conditions, dependencies, component versions, and Ansible tags.

**Stage 3. Ansible run tag analysis.** Extract all Ansible tags from `playbooks/` and `roles/*/tasks/`; build the version's tag reference per the rules of Section 6.4: a detailed description of each tag's actions, affected roles, host groups, dependencies, and standalone-run safety.

**Stage 4. Inventory analysis.** Break down `inventory/sample/group_vars/` and `inventory.ini`; pin variables to paths; record discrepancies with role defaults.

**Stage 5. Documentation analysis.** Structured digests of the tag's `docs/` per the areas in Section 6.3.

**Stage 6. Release analysis.** Break down GitHub Release `v2.29.1`: component versions, breaking changes, warnings.

**Stage 7. Troubleshooting.** Select merged PRs and confirmed Issues for `v2.29.1` per the rules of Section 10.

**Stage 8. Validation.** Verify that every item contains the mandatory metadata; verify the completeness of the Ansible tag reference; build `INDEX.md`. Then run `scripts/validate_kb.py` and resolve every reported divergence before the version is considered added — the script treats the filesystem as authoritative (Section 11.1) and fails on any index/filesystem inconsistency (missing/phantom versions or diffs, stale counters, broken wiki-links, version mixing, missing metadata).

After v2.29.1 is complete — proceed to `v2.30.0`, then `v2.31.0` (the repository's current Quick Start already uses the v2.31.0 image), and onward through sequential stable tags.

---

## 13. Forbidden Actions (Summary)

- ❌ Performing any actions without an approved plan.
- ❌ Analyzing master or `release-*` branches instead of tags.
- ❌ Indexing alpha/beta/rc versions without the user's explicit decision.
- ❌ Adding new tags to the base automatically.
- ❌ Skipping minor releases when adding versions and when comparing.
- ❌ Adding materials without `kubespray_version` and `git_commit`.
- ❌ Using unofficial sources as the foundation of the knowledge base.
- ❌ Adding unconfirmed solutions, Issues without a root cause, bot-closed Issues, or solutions without a version reference to troubleshooting.
- ❌ Mixing data from different versions within one knowledge base slice.
- ❌ Describing Ansible run tags by their name alone, without analyzing the task code they execute.
- ❌ Reusing one version's Ansible tag reference for another version without re-analysis.
- ❌ Modifying the main knowledge base during the nightly automatic run — only a report in `reports/nightly/` is allowed.
- ❌ Placing materials without a confirmed version into `versions/` slices — they belong in `unversioned/`.
- ❌ Giving reference-mode answers without stating the Kubespray version the information applies to.
- ❌ Responding to the user in any language other than Russian (Section 0).

---

## 14. Response and Report Style

- **Always respond in Russian** (Section 0), even when the user writes in English.
- Be specific: state paths, versions, commit SHAs.
- Every fact in the knowledge base must be verifiable: a file path within the tag or a link to an official source.
- When uncertain — explicitly mark `reliability: unconfirmed` and never present an assumption as a fact.
- At the end of every stage — a brief report (in Russian): what was done, which artifacts were created, what comes next.

---

## 15. Reference Mode: Answering Questions from the Knowledge Base

The knowledge base is not only the result of the work but also a **working tool**: the user launches console Claude (Claude Code) in the project directory and asks questions, and Claude answers based on the knowledge base.

### 15.1. When the mode activates

If the user's message is a **question about Kubespray** (variables, run tags, component behavior, upgrade procedures, errors) rather than a knowledge-base-building task, Claude operates in reference mode. No plan approval is required — these are read-only operations. Answers are given **in Russian**.

### 15.2. Answer lookup procedure

1. Determine which Kubespray version the question refers to:
   - if the version is stated in the question — use its slice;
   - if not stated — use the **latest indexed version** from `INDEX.md` and explicitly say so in the answer;
   - if the requested version is not in the base — report this and offer the nearest indexed one.
2. Start with `INDEX.md`, then move to the `versions/<tag>/` slice — first the structured references (`variables/`, `ansible-tags.yaml`, `components.yaml`), then `docs/`, `release-notes.md`, `troubleshooting/`. `INDEX.md` is a navigation layer, not the source of truth about composition: when the question is *which versions are indexed* (or whether a diff/slice exists), confirm it by listing the filesystem (`versions/`, `diffs/`), which is authoritative per Section 11.1 — do not rely on `INDEX.md` alone.
3. If the answer is not in the base — say so honestly. It is permitted to suggest checking the tag's code in the repository, but it is **forbidden to present the model's training knowledge as knowledge base content**.

### 15.3. Answer requirements

- always state the Kubespray version the answer applies to;
- cite the source: the knowledge base file and/or the `source_path` within the tag's repository;
- when using materials from `unversioned/` — an explicit "версия не подтверждена" disclaimer;
- for `reliability: unconfirmed` — an explicit caveat;
- if the question concerns version comparison — use the reports in `diffs/`; do not compare "by eye".

### 15.4. Optimizing the base for lookup

For reference mode to work fast and accurately, the following rules are observed while building the base:

- `INDEX.md` is the entry point: the list of versions, links to slices, a map of sections;
- each version slice has its own `README.md` with the slice's table of contents;
- file names are predictable and descriptive (`ansible-tags.yaml`, `variables/cni.yaml`);
- the metadata (Section 8) is present in every file — it is used for filtering by version and topic.

### 15.5. Usage example

```bash
cd kubespray-encyclopedia
claude
> Что делает запуск cluster.yml с --tags etcd в v2.29.1?
```

Or a one-off question without an interactive session:

```bash
claude -p "Какие переменные CNI изменились между v2.29.1 и v2.30.0?"
```

---

## 16. Nightly Automatic Run (Monitoring)

### 16.1. What it is

Every evening at **18:00** (UTC+3), Claude is launched automatically in headless mode and looks for new information. Claude cannot schedule itself — scheduling is configured with an external scheduler (cron / systemd timer) that invokes Claude Code in headless mode (`claude -p`).

Example cron job:

```cron
0 18 * * * cd /path/to/kubespray-encyclopedia && claude -p "Выполни ежевечерний мониторинг по разделу 16 CLAUDE.md" >> logs/nightly.log 2>&1
```

The exact headless-mode flags and allowed tools (permissions) are agreed upon during rollout based on the current Claude Code documentation: https://docs.claude.com/en/docs/claude-code/overview

### 16.2. What the nightly run does

1. Checks for new **stable** Git tags:
   - `https://github.com/kubernetes-sigs/kubespray/tags`
   - `https://github.com/kubernetes-sigs/kubespray/releases`
2. Checks for new merged PRs and confirmed Issues affecting **already indexed versions** (per the rules of Section 10).
3. Runs the consistency validator `scripts/validate_kb.py` (read-only) and records any index/filesystem divergence in the report — this does not edit the base (Section 16.3); it only surfaces defects of the navigation layer for the user to fix in an interactive session.
4. Produces a report `reports/nightly/<YYYY-MM-DD>.md` (written in Russian) with the following structure:

```markdown
---
project: kubespray
report_type: nightly
retrieved_at: 2026-07-14
---

# Ежевечерний отчёт — 2026-07-14

## Новые стабильные теги
(если найдены — предложение по шаблону раздела 9)

## Новые подтверждённые Issues / merged PR по проиндексированным версиям
(кандидаты в troubleshooting/ с указанием affected_versions)

## Кандидаты в unversioned/
(материалы без подтверждённой версии)

## Консистентность базы (validate_kb.py)
(результат прогона валидатора: PASS или список расхождений индекса с ФС; если есть — это дефекты навигационного слоя, требующие правки в интерактивной сессии)

## Требуется решение пользователя
(список действий, ожидающих одобрения)

## Ничего нового
(если изменений нет — явно зафиксировать это)
```

### 16.3. Hard constraints of the automatic mode

- ✅ Allowed: reading external sources, creating a report in `reports/nightly/`, writing to the log.
- ❌ Forbidden: modifying `versions/`, `diffs/`, `troubleshooting/`, `INDEX.md`, or any materials of the main base.
- ❌ Forbidden: adding new tags — only a proposal in the report (Section 9 applies without exceptions).
- All discovered actions are formatted as **proposals awaiting approval**; the user reviews the report and approves them in an interactive session.
- If the run fails (no network, GitHub unavailable) — the error is recorded in the report; no retries are performed the same night.

---

## 17. Obsidian Compatibility

The user works with the knowledge base not only through Claude but also through **Obsidian**. The `knowledge-base/` directory is an Obsidian vault, therefore:

### 17.1. File format

- The primary format for textual materials is **Markdown (`.md`) with YAML frontmatter**;
- the metadata from Section 8 is placed **in the frontmatter** at the beginning of the file:

```markdown
---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: docs
source_path: docs/operations/upgrades.md
retrieved_at: 2026-07-14
topics:
  - upgrade
reliability: authoritative
---

# Обновление кластера в v2.29.1
...
```

- structured machine-readable references (`ansible-tags.yaml`, `variables/*.yaml`, `components.yaml`) are kept in YAML, but a **paired Markdown note** with a human-readable exposition (in Russian) is created for each — this is what the user sees in Obsidian;
- the `topics` field in the frontmatter is used by Obsidian as tags — values must be short and contain no spaces (`kube-proxy`, `cilium`, `upgrade`).

### 17.2. Links and navigation

- Obsidian **wiki-links** are used between notes: `[[v2.29.1/ansible-tags|Теги запуска v2.29.1]]`;
- `INDEX.md` is formatted as a MOC (Map of Content) — the root note linking to all version slices, comparison reports, and troubleshooting;
- in each version slice, `README.md` serves as the local MOC of the slice;
- comparison reports in `diffs/` link to the slices of both compared versions.

### 17.3. Naming rules

- file and directory names use Latin characters, no spaces (hyphen as the separator), and none of the characters invalid in Obsidian/file systems: `# ^ [ ] | \ / : ?`;
- the version in a file name uses the tag format: `v2.29.1`;
- reports use the `YYYY-MM-DD` date format.

### 17.4. What to avoid

- ❌ HTML markup inside notes — pure Markdown only;
- ❌ duplicating the same information in `.md` and `.yaml` without marking which is the source of truth (the source of truth is the YAML reference; the Markdown note is a presentation);
- ❌ breaking wiki-links when moving files (e.g., when moving from `unversioned/` to `versions/` — update the links);
- ❌ Obsidian's service files (`.obsidian/`) are never indexed or modified by Claude.
