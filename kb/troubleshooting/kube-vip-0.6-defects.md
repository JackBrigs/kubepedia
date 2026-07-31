---
id: TROUBLE-KUBE_VIP_0_6_DEFECTS
type: troubleshooting
title: "kube-vip 0.6: defects fixed in the 0.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.6.0 <0.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-vip 0.6 known issues
  - kube-vip 0.6 fixed in
  - is this kube-vip bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-vip
sources:
  - type: docs
    path: kube-vip/kube-vip release notes for the 0.6 line — bug-fix entries
    url: https://github.com/kube-vip/kube-vip/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-vip 0.6: defects fixed in the 0.6 line

## Summary

**12 defects** the project fixed across **5 releases** of the 0.6 line, from 0.6.0 to
0.6.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.6.0

- fix LB annotations by @tuxtof in https://github.com/kube-vip/kube-vip/pull/553

### 0.6.1

- Fix makefile default target by @runsisi in https://github.com/kube-vip/kube-vip/pull/579
- Fixes to e2e tests and re-enabling by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/592

### 0.6.2

- Fixes to ginko by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/593
- Fix to main by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/598
- action fix by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/599
- Fix dos through checking for remaining services before releasing ip. … by @usiegl00 in https://github.com/kube-vip/kube-vip/pull/601

### 0.6.3

- chore: Spelling fixes by @mjtrangoni in https://github.com/kube-vip/kube-vip/pull/612

### 0.6.4

- Use a separate etcd cluster for the HA control plane / leaderElection
- Fixes to routing/table mode for VIP lifecycle
- Fix etcd e2e tests in GitHub actions by @g-gaston in https://github.com/kube-vip/kube-vip/pull/629
- Fixes to linting for routing table by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/670


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.6.4**, the newest release recorded here for this line.

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
