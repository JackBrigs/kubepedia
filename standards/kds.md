# Knowledge Document Specification (KDS)

Version: 1.2

Changelog:

- 1.2 — Added the `ansible_tag` document type (Kubespray run-tags), with ID prefix
  `TAG`, section profile (Context, Implementation, Compatibility), and Kubespray
  version scope. See `standards/decisions.md` D-012.
- 1.1 — Section profiles per document type replace the fixed ten-section layout;
  formal ID grammar and repository layout; typed `relations` replace the flat
  `related` list; version-field nullability rules; confidence ordering and
  semantics; generated machine-readable index; document-size rule fixed
  (removed the 100-line minimum). See `standards/decisions.md` for rationale.
- 1.0 — Initial specification.

---

# Purpose

KDS defines the canonical format for every knowledge document stored in Kubepedia.

Every document must follow this specification.

KDS is the **single source of truth** for the document schema. Other standards
(`validation.md` above all) reference KDS instead of restating it, so the schema
never drifts across files.

---

# Design Goals

KDS is designed to be:

- AI-first
- Human-readable
- Machine-readable
- Version-aware
- Source-driven
- Graph-oriented
- Stable over time

The specification should evolve rarely.

Knowledge should evolve continuously.

---

# Core Principles

Every document must satisfy the following principles:

- one document
- one subject
- one responsibility
- one stable identifier

Documents should be easy to update independently.

---

# Atomic Knowledge

One document represents one engineering entity.

Examples:

- one Kubernetes component
- one Kubespray variable
- one Role
- one Playbook
- one Feature Gate
- one API
- one Issue
- one Pull Request
- one Release
- one Upgrade Action
- one Troubleshooting Scenario

Never combine unrelated entities.

---

# Required Metadata

Every document begins with YAML Front Matter.

Required fields:

```yaml
id:                 # permanent unique identifier, see "Stable Identifier"
type:               # one document type, see "Document Types"
title:              # short human-readable name
status:             # active | deprecated | superseded

kubespray_version:  # value or null, see "Version Fields"
kubernetes_version: # value or null, see "Version Fields"
component_version:  # value or null, see "Version Fields"

verified_at:        # ISO 8601 date (YYYY-MM-DD) the facts were checked against sources
confidence:         # confirmed | verified | probable | hypothesis, see "Confidence Levels"

aliases:            # list; improves search; never replaces the ID
tags:               # list; technology / subsystem / feature / category

sources:            # list of inspected sources, see "Source Rules"
relations:          # list of typed edges, see "Relations"
```

No required key may be removed. A key that does not apply to a given document
carries an explicit `null` value where the type permits it (see "Version
Fields"); it is never silently dropped.

---

# Stable Identifier

Each document must have a permanent ID. The ID never changes.

Changing the filename, title, directory, or aliases must not change the ID.
Changing the ID creates a new entity.

## ID Grammar

```
ID    = TYPE "-" SLUG
TYPE  = one token from the ID-type table below (uppercase)
SLUG  = SEGMENT ( "_" SEGMENT )*  ( "__" SEGMENT ( "_" SEGMENT )* )?
SEGMENT = [A-Z0-9]+
```

- The SLUG is derived from the entity's canonical name, uppercased
  (`kube_proxy_remove` → `KUBE_PROXY_REMOVE`).
- When the same name exists in more than one scope (e.g. a variable defined in
  two roles), disambiguate by prefixing the owning scope and a double
  underscore: `VARIABLE-ETCD__ETCD_VERSION`.
- Issues and Pull Requests use the upstream number: `ISSUE-12345`, `PR-7821`.
- IDs are **globally unique**. One entity has exactly one ID **across all
  versions**; version differences live inside the document as version-ranged
  facts (see "Version Fields" and "Version Rules"), never as duplicate IDs.

## ID-type table

| type          | ID prefix   |
|---------------|-------------|
| component     | COMPONENT   |
| variable      | VARIABLE    |
| role          | ROLE        |
| playbook      | PLAYBOOK    |
| task          | TASK        |
| api           | API         |
| feature_gate  | FEATUREGATE |
| configuration | CONFIG      |
| release       | RELEASE     |
| issue         | ISSUE       |
| pull_request  | PR          |
| troubleshooting | TROUBLE   |
| best_practice | PRACTICE    |
| migration     | MIGRATION   |
| upgrade       | UPGRADE     |
| command       | COMMAND     |
| concept       | CONCEPT     |
| ansible_tag   | TAG         |

---

# Document Types

Supported types:

- component
- variable
- role
- playbook
- task
- api
- feature_gate
- configuration
- release
- issue
- pull_request
- troubleshooting
- best_practice
- migration
- upgrade
- command
- concept
- ansible_tag

New document types require a KDS update.

---

# Section Profiles

Kubepedia stores atomic facts, not uniform long-form articles. A fixed heavy
layout forced empty sections onto small documents; instead, **each type declares
the sections it requires**. A required section must be present and carry real
content. A non-required section is included only when it has real content, and is
otherwise omitted — never left as an empty stub.

All types require `Summary` and `References`. Additional required sections per
type:

| type            | additional required sections |
|-----------------|------------------------------|
| component       | Context, Implementation, Configuration, Compatibility |
| variable        | Implementation, Compatibility |
| role            | Implementation, Configuration, Compatibility |
| playbook        | Implementation, Compatibility |
| task            | Implementation |
| api             | Implementation, Compatibility, Upgrade Notes |
| feature_gate    | Implementation, Compatibility |
| configuration   | Configuration, Compatibility |
| release         | Implementation, Upgrade Notes, Compatibility |
| issue           | Problem, Context, Known Issues |
| pull_request    | Implementation |
| troubleshooting | Problem, Context, Diagnostics, Known Issues |
| best_practice   | Context, Implementation |
| migration       | Problem, Implementation, Upgrade Notes, Compatibility |
| upgrade         | Implementation, Upgrade Notes, Compatibility |
| command         | Diagnostics |
| concept         | Context |
| ansible_tag     | Context, Implementation, Compatibility |

The full section vocabulary (order is fixed when sections are present):

```
Summary
Problem
Context
Implementation
Configuration
Diagnostics
Known Issues
Upgrade Notes
Compatibility
References
```

Additional non-standard sections are allowed after `Compatibility` and before
`References` when they carry real engineering content.

## Section meaning

- **Summary** — engineering purpose. Maximum 10 lines.
- **Problem** — what the entity solves and why it exists.
- **Context** — affected versions, dependencies, prerequisites, assumptions.
- **Implementation** — actual implementation only; never hypothetical behavior.
- **Configuration** — configuration files, variables, defaults, generated artifacts.
- **Diagnostics** — safe commands, verification steps, expected output; never assume production access.
- **Known Issues** — affected versions, symptoms, workarounds, fixes; each references its sources.
- **Upgrade Notes** — migration requirements, incompatible behavior, breaking changes, rollback limitations.
- **Compatibility** — Kubernetes, Kubespray, OS, container runtime, CNI, kernel; never omit version ranges.
- **References** — only inspected sources; every important statement is traceable.

---

# Version Fields

Every technical statement is bound to the versions for which it is valid. The
three version keys are always present; each holds a value or an explicit `null`.
A document must set a non-null value for the version dimension that scopes its
type:

| type family | non-null version dimension required |
|-------------|-------------------------------------|
| Kubespray-scoped: variable, role, playbook, task, release, migration, upgrade, ansible_tag | `kubespray_version` |
| Kubernetes-scoped: api, feature_gate, and Kubernetes concepts | `kubernetes_version` |
| component | `component_version` **and** `kubespray_version` (as shipped by that Kubespray release); `kubernetes_version` records the compatibility range |
| troubleshooting, issue, pull_request | at least one of `kubespray_version` / `kubernetes_version` / `component_version` non-null, matching the affected subsystem |

A version field that does not apply is `null`. Validation accepts `null` only for
the dimensions a type does not require (see `validation.md`).

Version values may be a single version or an explicit range
(`">=1.31.0 <1.34.0"`). Historical behavior is never overwritten; future behavior
never overwrites historical behavior — both are represented as ranges within the
one document for the entity.

---

# Confidence Levels

Allowed values, from strongest to weakest:

1. `confirmed` — derived from tagged source code (the authoritative
   implementation), preferably with a second independent confirmation.
2. `verified` — from an authoritative non-code source at the correct tag
   (release notes, migration guide, official documentation), internally
   consistent, but not cross-checked against source code.
3. `probable` — a single secondary source or a reasoned inference from related
   facts.
4. `hypothesis` — not yet verified. A `hypothesis` must never back an operational
   recommendation; resolve it first.

Use the lowest confidence that accurately reflects the available evidence. Never
assign a higher confidence than the sources support.

---

# Relations

Relationships are first-class knowledge and are **typed**. `relations` is a list
of edges; each edge names its type and a target ID:

```yaml
relations:
  - type: depends_on
    target: COMPONENT-ETCD
  - type: affected_by
    target: ISSUE-12345
  - type: fixed_by
    target: PR-8421
```

Relation vocabulary (reverse pairs noted):

| type         | reverse      | meaning |
|--------------|--------------|---------|
| depends_on   | (—)          | A requires B to function |
| part_of      | (—)          | A is a component of B |
| replaces     | replaced_by  | A supersedes B in a later version |
| affects      | affected_by  | A (issue/change) impacts B |
| fixes        | fixed_by     | A (PR/release) resolves B (issue/known problem) |
| supersedes   | (—)          | A makes B historical without a direct replacement |
| see_also     | see_also     | untyped related knowledge |

Every target must be an existing ID (checked by validation). The knowledge graph
is built from these edges, not from folders. Tags never replace relations.

---

# Repository Layout

KDS documents live under `kb/`, sharded by domain and entity so that no directory
holds an unmanageable number of files at scale:

```
kb/
  kubernetes/          # Kubernetes-scoped docs: versions, feature gates, APIs, KEPs
  kubespray/
    variables/         # sharded further by owning role/group when large
    roles/
    playbooks/
    releases/
  components/<name>/    # one directory per managed component, e.g. components/etcd/
  troubleshooting/
  migrations/
index/                 # generated, never hand-edited (see "Index")
  documents.jsonl
  relations.jsonl
  ids.txt
schema/
  kds.schema.json      # machine-readable KDS schema (produced in an implementation stage)
```

- Filenames are the lowercased slug with a `.md` extension; the frontmatter `id`
  is authoritative, so renaming a file never breaks a link.
- The legacy `knowledge-base/` tree (Kubepedia 0.1.0) is **not** part of `kb/`.
  It is preserved as a raw, pre-analyzed **source cache**: useful as extracted
  material, but every fact must be re-verified against the tag before it becomes
  a KDS document. See `CLAUDE.md` → "Baseline".

---

# Index

`index/` holds machine-readable indexes generated from document frontmatter. They
let simple clients answer basic questions from metadata alone, without an LLM.

- `documents.jsonl` — one JSON object per document: `id, type, title, status,
  versions, tags, path`.
- `relations.jsonl` — one JSON object per edge: `source, type, target`.
- `ids.txt` — every ID, for uniqueness checks.

Indexes are **derived**: never edited by hand, always regenerated from the
documents, and checked by validation against a fresh recompute. The documents are
the source of truth; the index is a convenience view (the same filesystem-wins
invariant Kubepedia already applies to navigation).

---

# Source Rules

Every document must reference at least one primary source in `References`, and
record it in the `sources` metadata. Whenever possible, confirm knowledge using
multiple independent sources. Source selection and priority are governed by
`standards/sources.md` (the single normative priority list).

---

# Document Size

- Prefer the smallest document that fully and correctly captures one entity.
  There is **no minimum size**; a correct atomic fact may be a dozen lines.
- Soft cap: about 400 lines.
- Hard maximum: 500 lines. Beyond it, split **by concern** — never by version.

---

# One Fact Rule

Do not duplicate facts.

One engineering fact has exactly one canonical document. Other documents link to
it through `relations` instead of copying it.

---

# Deprecation

Deprecated knowledge is never deleted. It is marked `status: deprecated` (or
`status: superseded` with a `replaced_by` relation). Historical knowledge remains
searchable.

---

# Machine Readability

A parser must be able to extract metadata, versions, relations, and sources
without understanding natural language. Frontmatter must be valid YAML; relation
targets must be valid IDs; version fields must parse as a version or a range.

---

# AI Compatibility

Documents must work equally well across the AI-first clients listed in
`standards/project.md`. The format must never depend on a specific model, tool,
or database.

---

# Final Rule

If a human can read the document but software cannot reliably parse it, the
document is invalid.

If software can parse the document but engineers cannot understand it, the
document is also invalid.

KDS exists to satisfy both requirements simultaneously.
