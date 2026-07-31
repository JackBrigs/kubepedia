---
id: TROUBLE-ARGO_CD_0_9_DEFECTS
type: troubleshooting
title: "argo-cd 0.9: defects fixed in the 0.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.9.0 <0.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 0.9 known issues
  - argo-cd 0.9 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 0.9 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 0.9: defects fixed in the 0.9 line

## Summary

**8 defects** the project fixed across **2 releases** of the 0.9 line, from 0.9.0 to
0.9.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.9.0

- Fix issue where changes were not pulled when tracking a branch (issue #567)
- Fix controller hot loop when app source contains bad manifests (issue #568)
- Fix issue where Argo CD fails to deploy when resources are in a K8s list format (issue #584)
- Fix comparison failure when app contains unregistered custom resource (issue #583)
- Fix issue where helm hooks were being deployed as part of sync (issue #605)
- Fix race conditions in kube.GetResourcesWithLabel and DeleteResourceWithLabel (issue #587)
- [UI] Fix issue where projects filter does not work when application got changed

### 0.9.2

- Fix issue where argocd-server logged credentials in plain text during repo add (issue #653)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.9.2**, the newest release recorded here for this line.

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
