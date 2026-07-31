---
id: TROUBLE-KUBE_VIP_1_2_DEFECTS
type: troubleshooting
title: "kube-vip 1.2: defects fixed in the 1.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <1.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-vip 1.2 known issues
  - kube-vip 1.2 fixed in
  - is this kube-vip bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-vip
sources:
  - type: docs
    path: kube-vip/kube-vip release notes for the 1.2 line — bug-fix entries
    url: https://github.com/kube-vip/kube-vip/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-vip 1.2: defects fixed in the 1.2 line

## Summary

**22 defects** the project fixed across **3 releases** of the 1.2 line, from 1.2.0 to
1.2.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.2.0

- Fixed restart on node watcher error by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1511
- This fixes the rules for egress allowed-networks by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/1528
- Configuration of the deprecated endpoints in the tests fixed by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1542
- fix(config): update comments for env vars by @lbohdanl in https://github.com/kube-vip/kube-vip/pull/1560
- Fixed services test logs by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1552
- Fixed ARP mode with cluster policy in 1.2.0-rc.0 by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1553
- fix(bgp): improve IPv6 peer parsing robustness by @MaxRink in https://github.com/kube-vip/kube-vip/pull/1551
- Fixed ARP and RT modes with global leader election for services in 1.2.0-rc.0 by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1561
- fix: refactor labeler interface, enable labeling with cp_enabled=true by @lbohdanl in https://github.com/kube-vip/kube-vip/pull/1566
- Fix and E2E tests for endpoints deletion - ARP and RT by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1572
- Fix - Backend Watch Ticker by @mattcarp12 in https://github.com/kube-vip/kube-vip/pull/1565

### 1.2.1

- Fix ListAdvertisedRoutes by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1593
- Fix control-plane leaderelection restart in etcd mode by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1603
- Fix minor error handling issue in pkg/bgp/peer.go by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1601
- Fixed deadlock on AddIP() call in StartVipService by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1594

### 1.2.2

- Fixed BGP metrics by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1616
- Added support in ipoib interfaces in ARP mode. Fixes #694 by @ichaytay in https://github.com/kube-vip/kube-vip/pull/1596
- fix(egress): isolate nftables tables by instance by @GabboPenna in https://github.com/kube-vip/kube-vip/pull/1635
- Fixed tables creation when nftables is used, IP deletion on leadership loss and race condition in backend by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1626
- fix(cmd): throw an error when no valid mode detected by @thebhdn in https://github.com/kube-vip/kube-vip/pull/1641
- fix: optionally attach BGP service VIPs to interface by @MarijnRitzen in https://github.com/kube-vip/kube-vip/pull/1644
- Fixes issues with seperate etcd prs by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/1653


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.2.2**, the newest release recorded here for this line.

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
