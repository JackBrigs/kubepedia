---
id: TROUBLE-FLANNEL_0_19_DEFECTS
type: troubleshooting
title: "flannel 0.19: defects fixed in the 0.19 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.19.0 <0.20.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - flannel 0.19 known issues
  - flannel 0.19 fixed in
  - is this flannel bug already fixed
tags:
  - troubleshooting
  - upgrade
  - flannel
sources:
  - type: docs
    path: flannel-io/flannel release notes for the 0.19 line — bug-fix entries
    url: https://github.com/flannel-io/flannel/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# flannel 0.19: defects fixed in the 0.19 line

## Summary

**9 defects** the project fixed across **3 releases** of the 0.19 line, from 0.19.0 to
0.19.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.19.0

- Fixed subnet allocation in case of etcd manager with IPv6 by @rbrtbnfgl in https://github.com/flannel-io/flannel/pull/1582
- Fix the v6 unit test failing by @manuelbuil in https://github.com/flannel-io/flannel/pull/1597
- Fix etcd key removal in CI and add -e flag by @manuelbuil in https://github.com/flannel-io/flannel/pull/1595
- wireguard: fix segmentation fault if only ipv6 is enabled by @andreek in https://github.com/flannel-io/flannel/pull/1601
- Fix waiting for iperf docker is running before launch test by @louiznk in https://github.com/flannel-io/flannel/pull/1599

### 0.19.1

- Fixed wireguard interface MTU with the overhead by @rbrtbnfgl in https://github.com/flannel-io/flannel/pull/1620

### 0.19.2

- Fix CI by @manuelbuil in https://github.com/flannel-io/flannel/pull/1631
- fix some typos by @cuishuang in https://github.com/flannel-io/flannel/pull/1635
- Fixed iptables-restore version check in case of version older than 1.6.2 by @rbrtbnfgl in https://github.com/flannel-io/flannel/pull/1637


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.19.2**, the newest release recorded here for this line.

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
