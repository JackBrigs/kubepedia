---
id: TROUBLE-FLANNEL_0_18_DEFECTS
type: troubleshooting
title: "flannel 0.18: defects fixed in the 0.18 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.18.0 <0.19.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - flannel 0.18 known issues
  - flannel 0.18 fixed in
  - is this flannel bug already fixed
tags:
  - troubleshooting
  - upgrade
  - flannel
sources:
  - type: docs
    path: flannel-io/flannel release notes for the 0.18 line — bug-fix entries
    url: https://github.com/flannel-io/flannel/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# flannel 0.18: defects fixed in the 0.18 line

## Summary

**7 defects** the project fixed across **2 releases** of the 0.18 line, from 0.18.0 to
0.18.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.18.0

- Fix overwriting etcd data when local subnet file exists by @zhangzhangzf in https://github.com/flannel-io/flannel/pull/1505
- ARM64 build fix by @AleksandrNull in https://github.com/flannel-io/flannel/pull/1553
- fix document and comment of configuration by @ari1021 in https://github.com/flannel-io/flannel/pull/1555
- Fixed a route conflict bug. by @zhangzhangzf in https://github.com/flannel-io/flannel/pull/1546
- Upgrade netlink to fix ipsec issue by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/1565
- Fixed wireguard MTU and added windows iface func by @rbrtbnfgl in https://github.com/flannel-io/flannel/pull/1567

### 0.18.1

- fix: assign IPv6 `podCIDR` from kubelet spec. by @sergelogvinov in https://github.com/flannel-io/flannel/pull/1572


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.18.1**, the newest release recorded here for this line.

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
