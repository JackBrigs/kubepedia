---
id: TROUBLE-CNI_PLUGINS_1_0_DEFECTS
type: troubleshooting
title: "cni-plugins 1.0: defects fixed in the 1.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.0.0 <1.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cni-plugins 1.0 known issues
  - cni-plugins 1.0 fixed in
  - is this cni-plugins bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cni-plugins
sources:
  - type: docs
    path: containernetworking/plugins release notes for the 1.0 line — bug-fix entries
    url: https://github.com/containernetworking/plugins/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cni-plugins 1.0: defects fixed in the 1.0 line

## Summary

**11 defects** the project fixed across **2 releases** of the 1.0 line, from 1.0.0 to
1.0.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.0.0

- host-local: remove redundant startRange in RangeIterator to avoid mismatching with startIP ([#583](https://github.com/containernetworking/plugins/pull/583)). Fixes possible infinite loop
- portmap: use slashes in sysctl template to support interface names which separated by dots ([#589](https://github.com/containernetworking/plugins/pull/589))
- pkg/ipam: convert dots to slashes in interface names for sysctl ([#585](https://github.com/containernetworking/plugins/pull/585))
- win-bridge: fix panic while calling HNS api ([#590](https://github.com/containernetworking/plugins/pull/590)). fix a nil pointer panic while calling HNS API (V1) on win-bridge
- [macvlan] Stop setting proxy-arp on macvlan interface ([#586](https://github.com/containernetworking/plugins/pull/586))

### 1.0.1

- plugins: fix bug where support for CNI version 0.4.0 or 1.0.0 was dropped
- host-local: remove redundant startRange in RangeIterator to avoid mismatching with startIP ([#583](https://github.com/containernetworking/plugins/pull/583)). Fixes possible infinite loop
- portmap: use slashes in sysctl template to support interface names which separated by dots ([#589](https://github.com/containernetworking/plugins/pull/589))
- pkg/ipam: convert dots to slashes in interface names for sysctl ([#585](https://github.com/containernetworking/plugins/pull/585))
- win-bridge: fix panic while calling HNS api ([#590](https://github.com/containernetworking/plugins/pull/590)). fix a nil pointer panic while calling HNS API (V1) on win-bridge
- [macvlan] Stop setting proxy-arp on macvlan interface ([#586](https://github.com/containernetworking/plugins/pull/586))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.0.1**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `containernetworking/plugins`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cni-plugins.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
