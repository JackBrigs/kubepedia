---
id: TROUBLE-KUBE_VIP_1_0_DEFECTS
type: troubleshooting
title: "kube-vip 1.0: defects fixed in the 1.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.0.0 <1.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-vip 1.0 known issues
  - kube-vip 1.0 fixed in
  - is this kube-vip bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-vip
sources:
  - type: docs
    path: kube-vip/kube-vip release notes for the 1.0 line — bug-fix entries
    url: https://github.com/kube-vip/kube-vip/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-vip 1.0: defects fixed in the 1.0 line

## Summary

**17 defects** the project fixed across **4 releases** of the 1.0 line, from 1.0.1 to
1.0.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.0.1

- Fix deletion of ConfiguredNetworks entry after deleting BGP host by @rmarkdev in https://github.com/kube-vip/kube-vip/pull/1246
- Fixed nil pointer reference when endpoints serving condition is not set by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1260
- fix for layer 3 issues with not added ip by @T-Bonhagen in https://github.com/kube-vip/kube-vip/pull/1252

### 1.0.2

- fix: normalize IPv6 to 32-hex (fixes #1302) by @seungtae62 in https://github.com/kube-vip/kube-vip/pull/1313
- Fixed DDNS nil pointer dereference (1305) by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1310

### 1.0.3

- Avoid access inside WANIPv6FirewallControlClient when it might be nil by @ivucica in https://github.com/kube-vip/kube-vip/pull/1336
- Fixed service DNS resolve by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1356
- Fixed service port security rules for iptables by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1357
- Fixed service deletion when service leader election is enabled by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1360
- Bump to golang to fix stdlib vuln by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/1355

### 1.0.4

- Fixed preserveVipOnLeadershipLoss setting in manifest generation by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1376
- Fixed endpointslices handling in dualstack clusters by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1379
- Fixed an issue with default gateway interface retrieval in multi-path… by @hindungWang in https://github.com/kube-vip/kube-vip/pull/1373
- fix common lease fix from 1.0.1 by @slimm609 in https://github.com/kube-vip/kube-vip/pull/1383
- Fixed leaderelection retry on error by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1386
- Fix context propagation and panic() calls by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1375
- Fix IP refresh when using FQDN for VIP by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1390


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.0.4**, the newest release recorded here for this line.

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
