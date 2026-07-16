# Knowledge Document Specification (KDS)

Version: 1.0

---

# Purpose

KDS defines the canonical format for every knowledge document stored in Kubepedia.

Every document must follow this specification.

No exceptions.

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
id:
type:
title:

status:

kubespray_version:
kubernetes_version:
component_version:

verified_at:
confidence:

aliases:
tags:

sources:
related:
```

No required field may be removed.

---

# Stable Identifier

Each document must have a permanent ID.

The ID never changes.

Changing:

- filename
- title
- directory
- aliases

must not change the ID.

Examples:

```
COMPONENT-CONTAINERD

VARIABLE-KUBE_PROXY_REMOVE

ROLE-DOWNLOAD

ISSUE-12345

PR-7821
```

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

New document types require a KDS update.

---

# Required Sections

Each document follows the same layout.

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

Additional sections are allowed.

Required sections must never disappear.

---

# Summary

Explain the engineering purpose.

Maximum length:

10 lines.

---

# Problem

Describe:

- what the entity solves
- why it exists

---

# Context

Describe:

- affected versions
- dependencies
- prerequisites
- assumptions

---

# Implementation

Describe actual implementation.

Never describe hypothetical behavior.

---

# Configuration

Describe:

- configuration files
- variables
- defaults
- generated artifacts

---

# Diagnostics

Provide:

- safe commands
- verification steps
- expected output

Diagnostics must never assume production access.

---

# Known Issues

Describe:

- affected versions
- symptoms
- workarounds
- fixes

Every issue should reference its sources.

---

# Upgrade Notes

Describe:

- migration requirements
- incompatible behavior
- breaking changes
- rollback limitations

---

# Compatibility

Describe compatibility with:

- Kubernetes
- Kubespray
- Operating Systems
- Container Runtime
- CNI
- Kernel

Never omit version ranges.

---

# References

List only inspected sources.

Every important engineering statement should be traceable.

---

# Version Rules

Every statement must explicitly define:

- Kubespray version
- Kubernetes version
- Component version

Historical behavior must remain available.

Future behavior must never overwrite historical behavior.

---

# Source Rules

Every document must reference at least one primary source.

Whenever possible, confirm knowledge using multiple independent sources.

---

# Confidence Levels

Allowed values:

- confirmed
- verified
- probable
- hypothesis

Use the lowest confidence that accurately reflects available evidence.

---

# Related Knowledge

Every document should define relationships.

Examples:

```
related:

- COMPONENT-ETCD
- VARIABLE-ETCD_VERSION
- ISSUE-5932
- PR-8421
```

The knowledge graph is built from these relations.

---

# Tags

Tags should describe:

- technology
- subsystem
- feature
- category

Do not use tags as replacements for relationships.

---

# Aliases

Aliases improve search.

Aliases never replace IDs.

---

# Document Size

Target size:

100–300 lines.

Maximum:

500 lines.

If the document grows beyond the limit:

split it.

---

# One Fact Rule

Do not duplicate facts.

One engineering fact should have exactly one canonical location.

Other documents reference it.

---

# Deprecation

Deprecated knowledge is never deleted.

It is marked:

```
status: deprecated
```

Historical knowledge remains searchable.

---

# File Naming

File names should be descriptive.

IDs remain the primary identifier.

Changing filenames must never affect links.

---

# Machine Readability

A parser should be able to extract:

- metadata
- versions
- relations
- sources

without understanding natural language.

---

# AI Compatibility

Documents must work equally well with:

- Claude
- ChatGPT
- Gemini
- NotebookLM
- Telegram Bot
- CLI
- Web UI
- RAG
- Graph Database

The format must never depend on a specific model.

---

# Final Rule

If a human can read the document but software cannot reliably parse it,

the document is invalid.

If software can parse the document but engineers cannot understand it,

the document is also invalid.

KDS exists to satisfy both requirements simultaneously.
