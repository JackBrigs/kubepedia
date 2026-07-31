---
id: TROUBLE-ARGO_CD_1_0_DEFECTS
type: troubleshooting
title: "argo-cd 1.0: defects fixed in the 1.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.0.0 <1.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 1.0 known issues
  - argo-cd 1.0 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 1.0 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 1.0: defects fixed in the 1.0 line

## Summary

**18 defects** the project fixed across **1 releases** of the 1.0 line, from 1.0.0 to
1.0.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.0.0

- Don't compare secrets in the CLI, since argo-cd doesn't have access to their data (#1459)
- Dropdown menu should not have sync item for unmanaged resources #1357
- Issue #908 - Surface Service/Ingress external IPs, hostname to application (#1347)
- Resource node details is crashing if live resource is missing $1505
- Rollback UI is not showing correct ksonnet parameters in preview #1326
- See details of applications fails with "r.nodes is undefined" #1371
- UI fails to load custom actions is resource is not deployed #1502
- Unable to create app from private repo: x509: certificate signed by unknown authority (#1171)
- Fix hardcoded 'git' user in `util/git.NewClient` (#1555)
- Application controller becomes unresponsive (#1476)
- Load target resource using K8S if conversion fails (#1414)
- Can't ignore a non-existent pointer anymore (#1586)
- Impossible to sync to HEAD from UI if auto-sync is enabled (#1579)
- Application controller is unable to delete self-referenced app (#1570)
- Prevent reconciliation loop for self-managed apps (#1533)
- Controller incorrectly report health state of self managed application (#1557)
- Fix kustomize manifest generation crash is manifest has image without version (#1540)
- Supply resourceVersion to watch request to prevent reading of stale cache (#1605)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.0.0**, the newest release recorded here for this line.

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
