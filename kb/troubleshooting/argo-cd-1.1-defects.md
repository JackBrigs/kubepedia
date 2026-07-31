---
id: TROUBLE-ARGO_CD_1_1_DEFECTS
type: troubleshooting
title: "argo-cd 1.1: defects fixed in the 1.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.1.0 <1.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 1.1 known issues
  - argo-cd 1.1 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 1.1 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 1.1: defects fixed in the 1.1 line

## Summary

**18 defects** the project fixed across **1 releases** of the 1.1 line, from 1.1.0 to
1.1.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.1.0

- Project Editor: Whitelisted Cluster Resources doesn't strip whitespace [#1693](https://github.com/argoproj/argo-cd/issues/1693)
- \[ui small bug\] menu position outside block [#1711](https://github.com/argoproj/argo-cd/issues/1711)
- UI will crash when create application without destination namespace [#1701](https://github.com/argoproj/argo-cd/issues/1701)
- ArgoCD synchronization failed due to internal error [#1697](https://github.com/argoproj/argo-cd/issues/1697)
- Replicasets ordering is not stable on app tree view [#1668](https://github.com/argoproj/argo-cd/issues/1668)
- Stuck processor on App Controller after deleting application with incomplete operation [#1665](https://github.com/argoproj/argo-cd/issues/1665)
- Role edit page fails with JS error [#1662](https://github.com/argoproj/argo-cd/issues/1662)
- failed parsing on parameters with comma [#1660](https://github.com/argoproj/argo-cd/issues/1660)
- Handle nil obj when processing custom actions [#1700](https://github.com/argoproj/argo-cd/pull/1700)
- Account for missing fields in Rollout HealthStatus [#1699](https://github.com/argoproj/argo-cd/pull/1699)
- Sync operation unnecessary waits for a healthy state of all resources [#1715](https://github.com/argoproj/argo-cd/issues/1715)
- argocd app sync hangs when cluster is not configured (#1935)
- Do not allow app-of-app child app's Missing status to affect parent (#1954)
- Argo CD don't handle well k8s objects which size exceeds 1mb (#1685)
- Secret data not redacted in last-applied-configuration (#897)
- Running app actions requires only read privileges (#1827)
- Make status fields as optional fields (#1779)
- Use correct healthcheck for Rollout with empty steps list (#1776)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.1.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `argoproj/argo-cd`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/argo-cd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
