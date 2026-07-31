---
id: TROUBLE-KUBE_VIP_0_9_DEFECTS
type: troubleshooting
title: "kube-vip 0.9: defects fixed in the 0.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.9.0 <0.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-vip 0.9 known issues
  - kube-vip 0.9 fixed in
  - is this kube-vip bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-vip
sources:
  - type: docs
    path: kube-vip/kube-vip release notes for the 0.9 line — bug-fix entries
    url: https://github.com/kube-vip/kube-vip/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-vip 0.9: defects fixed in the 0.9 line

## Summary

**8 defects** the project fixed across **3 releases** of the 0.9 line, from 0.9.0 to
0.9.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.9.0

- Fixed service IP address deletion on service modification bug by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1122
- Fix DualStack in BGP mode by @Cellebyte in https://github.com/kube-vip/kube-vip/pull/1123
- fix #1127 as we have a nil deref if router does not support IPv6 by @Cellebyte in https://github.com/kube-vip/kube-vip/pull/1130

### 0.9.1

- fix: s/endoints/endpoints/ in RBAC manifest generation code by @sdwilsh in https://github.com/kube-vip/kube-vip/pull/1141
- Fixed instance finding by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1140

### 0.9.2

- Fix/map concurrency by @Cellebyte in https://github.com/kube-vip/kube-vip/pull/1166
- Fixed service-tests + minor changes by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1174
- Fixed BGP clear deadlock by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1178


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

- Upstream releases of `kube-vip/kube-vip`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kube-vip.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
