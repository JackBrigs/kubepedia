---
id: TROUBLE-FLANNEL_0_21_DEFECTS
type: troubleshooting
title: "flannel 0.21: defects fixed in the 0.21 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.21.0 <0.22.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - flannel 0.21 known issues
  - flannel 0.21 fixed in
  - is this flannel bug already fixed
tags:
  - troubleshooting
  - upgrade
  - flannel
sources:
  - type: docs
    path: flannel-io/flannel release notes for the 0.21 line — bug-fix entries
    url: https://github.com/flannel-io/flannel/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# flannel 0.21: defects fixed in the 0.21 line

## Summary

**6 defects** the project fixed across **3 releases** of the 0.21 line, from 0.21.0 to
0.21.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.21.0

- Upgrade base images to fix CVE by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/1708
- fix: old document with wrong path :tea: by @mrnonz in https://github.com/flannel-io/flannel/pull/1710

### 0.21.3

- fix randomness in k3s end to end tests by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/1729
- Fix etcd index outofrange by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/1726

### 0.21.4

- Fixed iptables rules in case random-fully is not supported by @rbrtbnfgl in https://github.com/flannel-io/flannel/pull/1743
- Fix existing ns issue by @lexfrei in https://github.com/flannel-io/flannel/pull/1741


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.21.4**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `flannel-io/flannel`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/flannel.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
