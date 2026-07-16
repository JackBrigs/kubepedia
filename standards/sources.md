# Sources Standard

Version: 1.1

Changelog:

- 1.1 — "Source Priority" is declared the single normative priority list;
  `workflow.md` now references it instead of keeping a second, conflicting list.
- 1.0 — Initial standard.

---

# Purpose

This document defines where Kubepedia is allowed to obtain engineering knowledge.

Every fact stored in Kubepedia must be traceable to one or more verified sources.

Knowledge without verifiable sources is not considered trusted knowledge.

The purpose of source analysis is not to collect documents, but to extract reusable engineering knowledge.

---

# Source Philosophy

Kubepedia follows these principles:

- Prefer implementation over documentation.
- Prefer official sources over community content.
- Prefer tagged releases over moving branches.
- Prefer multiple independent confirmations over a single reference.
- Prefer reproducible facts over opinions.
- Preserve historical information.
- Never mix information from different versions without explicitly documenting version boundaries.

Every engineering statement should be reproducible from its sources.

---

# Source Categories

Kubepedia currently recognizes six source categories:

1. Kubespray
2. Kubernetes
3. Kubernetes Components
4. Security
5. Engineering Experience
6. Community Knowledge

Each category has its own trust level and purpose.

---

# Kubespray Sources

Kubespray is the primary implementation source.

Every supported Kubespray release must be analyzed independently.

Mandatory sources include:

- Git tags
- GitHub Releases
- Release Notes
- CHANGELOG
- Migration Guides
- Official documentation
- Repository README
- Component README files
- Roles
- Defaults
- Vars
- Tasks
- Templates
- Handlers
- Inventory samples
- Group variables
- Playbooks
- Modules
- Plugins
- Library
- GitHub Actions
- CI configuration
- Molecule tests
- Integration tests
- Unit tests
- Pull Requests
- Issues
- Discussions

The tagged source code is the authoritative implementation.

---

# Kubernetes Sources

For every supported Kubernetes version collect information from:

- kubernetes/kubernetes
- kubernetes/enhancements
- kubernetes.io
- Kubernetes Release Notes
- Kubernetes API Reference
- Kubernetes Enhancement Proposals (KEP)
- Feature Gates documentation
- API Deprecation Guide
- Upgrade documentation
- kubeadm documentation
- kubelet documentation
- kubectl documentation
- SIG Release
- SIG Node
- SIG Network
- SIG Cluster Lifecycle
- SIG Scheduling
- SIG Storage
- Kubernetes Blog (secondary source only)

Do not rely on blog articles as primary implementation evidence.

---

# Kubernetes Component Sources

Every managed component must be researched independently.

Required sources include:

- Official repository
- Official documentation
- Release Notes
- CHANGELOG
- Migration Guide
- Compatibility Matrix
- Roadmap
- Security Advisories
- GitHub Releases
- Pull Requests
- Issues
- Discussions
- Example configurations

Only analyze component versions supported by the active Kubespray release.

---

# Security Sources

Security information should be collected from:

- Kubernetes Security Advisories
- GitHub Security Advisories
- CVE
- CVSS
- Vendor Security Advisories
- Component Security Releases

For every security issue identify:

- affected versions
- fixed versions
- severity
- mitigation
- workaround
- upgrade recommendation

---

# Engineering Experience

Engineering knowledge explains how systems behave in production.

Useful sources include:

- CNCF
- Linux Foundation
- KubeCon presentations
- Official conference talks
- Engineering blogs
- Vendor engineering blogs
- Production postmortems
- Incident reports
- Performance benchmarks
- Architecture discussions

Engineering experience explains implementation.

It never replaces implementation.

---

# Community Sources

Community knowledge is useful for discovering operational problems.

Allowed sources include:

- Reddit
- Stack Overflow
- Server Fault
- GitHub Discussions
- Slack archives
- Discord archives

Community information is never authoritative.

Every important engineering statement must be verified using higher-priority sources.

---

# Source Priority

This is the **single normative source-priority list** for the whole project.
Every conflict-resolution rule in other standards (notably `workflow.md`)
references this list; no other file defines its own ordering.

When sources disagree, use the following priority:

1. Tagged source code
2. Tagged implementation (release artifacts, generated config at the tag)
3. Official documentation
4. Migration Guides
5. Release Notes
6. API Reference
7. KEP
8. Security Advisories
9. Merged Pull Requests
10. GitHub Issues
11. Discussions
12. CNCF
13. Linux Foundation
14. Conference material
15. Engineering blogs
16. Community discussions

Never reverse this priority.

Migration Guides rank above Release Notes: a migration guide is the authoritative,
actionable account of required upgrade actions, whereas release notes summarize
and may be incomplete. Documentation (3) explains; source code (1) defines. When
code contradicts any lower source, code wins and the conflict is recorded.

---

# Pull Request Analysis

Every merged Pull Request should be analyzed.

Extract:

- engineering objective
- implementation details
- affected files
- affected components
- breaking changes
- migration notes
- related issues

Unmerged Pull Requests must never be treated as implementation.

---

# Issue Analysis

GitHub Issues describe real production problems.

Collect:

- symptoms
- affected versions
- root cause
- workaround
- fix status
- related Pull Requests

A closed issue does not automatically mean the problem is fixed.

Always identify the merged implementation.

---

# Discussion Analysis

Discussions explain engineering decisions.

Extract:

- design rationale
- rejected approaches
- future plans
- trade-offs

Do not treat discussions as implementation evidence.

---

# Release Note Analysis

For every release extract:

- breaking changes
- new functionality
- deprecated functionality
- removed functionality
- upgrade notes
- compatibility changes

Release Notes summarize implementation.

They do not replace source code analysis.

---

# Migration Guide Analysis

Migration Guides are mandatory.

Collect:

- required actions
- incompatible behavior
- migration sequence
- rollback limitations
- operational risks

Migration Guides take precedence over community recommendations.

---

# Version Matching

Every source must belong to the documented version.

Never mix:

- master
- main
- latest documentation

with historical tagged releases.

Version drift is one of the most common causes of incorrect knowledge.

---

# Multi-Source Verification

Important engineering knowledge should be confirmed by multiple independent sources.

Examples:

Source Code
+
Release Notes
+
Migration Guide

or

Issue
+
Merged Pull Request
+
Tagged Implementation

Confidence increases with independent confirmation.

---

# Source Metadata

Every knowledge document must record:

- source type
- source location
- version
- verification date
- confidence

Every engineering statement must be traceable.

---

# Knowledge Extraction

Do not copy documentation.

Instead:

- extract engineering knowledge
- normalize terminology
- remove duplication
- preserve version context
- identify relationships
- convert implementation into reusable knowledge

Kubepedia stores knowledge, not documentation.

---

# Continuous Research

Every new Kubespray release should automatically trigger:

- source collection
- source comparison
- change detection
- knowledge update
- validation
- Pull Request generation

Knowledge acquisition is continuous.

Architecture changes are exceptional.

---

# Future Sources

Future Kubepedia versions may integrate additional verified sources.

Examples include:

- Kubernetes Enhancement tracking
- Kubernetes Testgrid
- SIG meeting notes
- Kubernetes design proposals
- Component maintainers' documentation
- Benchmark reports
- Automated compatibility testing

These sources should be added only after defining validation rules.

---

# Final Rule

The objective of source analysis is not to collect links.

The objective is to build a trusted engineering knowledge base where every fact can be traced back to verified implementation and authoritative documentation.
