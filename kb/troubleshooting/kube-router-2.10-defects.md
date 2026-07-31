---
id: TROUBLE-KUBE_ROUTER_2_10_DEFECTS
type: troubleshooting
title: "kube-router 2.10: defects fixed in the 2.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.10.0 <2.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-router 2.10 known issues
  - kube-router 2.10 fixed in
  - is this kube-router bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-router
sources:
  - type: docs
    path: cloudnativelabs/kube-router release notes for the 2.10 line — bug-fix entries
    url: https://github.com/cloudnativelabs/kube-router/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-router 2.10: defects fixed in the 2.10 line

## Summary

**6 defects** the project fixed across **1 releases** of the 2.10 line, from 2.10.0 to
2.10.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.10.0

- - fix(.grype.yaml): don't include upstream CNI plugin in grype results `<Aaron U'Ren>`
- - fix(NRC): correct exact-match policy name in checkPolicies test runner `<Aaron U'Ren>`
- - fix(bgp): also reject defaultRouteSetV6 from peers `<Richard Kojedzinszky>`
- - fix(NPC): return error when deny by default without range `<Aaron U'Ren>`
- - fix(k8s): update k8s library calls for for version 0.36 `<Aaron U'Ren>`
- - fix(NPC,LBC): harden network policy and load balancer controllers `<Aprazors>`


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.10.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cloudnativelabs/kube-router`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kube-router.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
