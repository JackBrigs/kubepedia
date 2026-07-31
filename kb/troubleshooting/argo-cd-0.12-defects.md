---
id: TROUBLE-ARGO_CD_0_12_DEFECTS
type: troubleshooting
title: "argo-cd 0.12: defects fixed in the 0.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.12.0 <0.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 0.12 known issues
  - argo-cd 0.12 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 0.12 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 0.12: defects fixed in the 0.12 line

## Summary

**9 defects** the project fixed across **3 releases** of the 0.12 line, from 0.12.0 to
0.12.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.12.0

- Documentation fixes and improvements (@twz123, @yann-soubeyrand, @OmerKahani, @dulltz)
- Fixed multiple goroutine leaks in controller and api-server
- Fix issue where `argocd app set -p` required repo privileges. (#1280)
- Fix local diff of non-namespaced resources. Also handle duplicates in local diff (#1289)
- Fix issue where CLI would panic after timeout when cli did not have get permissions (#1209)

### 0.12.1

- Fix invalid group filtering in 'patch-resource' command (#1319)
- Fix null pointer dereference error in 'argocd app wait' (#1366)

### 0.12.2

- Fix racing condition in controller cache (#1498)
- Fix null pointer exception in secret normalization function (#1389)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.12.2**, the newest release recorded here for this line.

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
