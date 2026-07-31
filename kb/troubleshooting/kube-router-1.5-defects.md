---
id: TROUBLE-KUBE_ROUTER_1_5_DEFECTS
type: troubleshooting
title: "kube-router 1.5: defects fixed in the 1.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.5.0 <1.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-router 1.5 known issues
  - kube-router 1.5 fixed in
  - is this kube-router bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-router
sources:
  - type: docs
    path: cloudnativelabs/kube-router release notes for the 1.5 line — bug-fix entries
    url: https://github.com/cloudnativelabs/kube-router/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-router 1.5: defects fixed in the 1.5 line

## Summary

**9 defects** the project fixed across **4 releases** of the 1.5 line, from 1.5.0 to
1.5.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.5.0

- fix(NPC): make code more understandable by @lx1036 in https://github.com/cloudnativelabs/kube-router/pull/1261
- fix(NPC): add missing quotes by @aauren in https://github.com/cloudnativelabs/kube-router/pull/1278
- fix(constant): use constant from resourcelock package by @lx1036 in https://github.com/cloudnativelabs/kube-router/pull/1298

### 1.5.1

- - fix(NSC): don't check protocol on DSR svcs (21 minutes ago) <Aaron U'Ren>
- - fix(ipset): remove initval during ipset parse (21 minutes ago) <Aaron U'Ren>
- - fix(bgp): set graceful restart on enabled family (21 minutes ago) <Aaron U'Ren>
- - fix: remove multiple MTU reductions (22 minutes ago) <Aaron U'Ren>

### 1.5.2

- - iptables mode selection fixed. iptables-wrapper script updated to the latest upstream version <@makhov>

### 1.5.4

- - fix(dsr): CRI runtime/v1alpha2 -> runtime/v1 `<Aaron U'Ren>`


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.5.4**, the newest release recorded here for this line.

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
