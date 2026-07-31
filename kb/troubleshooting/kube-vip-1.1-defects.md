---
id: TROUBLE-KUBE_VIP_1_1_DEFECTS
type: troubleshooting
title: "kube-vip 1.1: defects fixed in the 1.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.1.0 <1.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-vip 1.1 known issues
  - kube-vip 1.1 fixed in
  - is this kube-vip bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-vip
sources:
  - type: docs
    path: kube-vip/kube-vip release notes for the 1.1 line — bug-fix entries
    url: https://github.com/kube-vip/kube-vip/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-vip 1.1: defects fixed in the 1.1 line

## Summary

**15 defects** the project fixed across **3 releases** of the 1.1 line, from 1.1.0 to
1.1.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.1.0

- Reverted missing change from #623 by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1416
- Added context inheritance for services by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1432
- Added waitgroups by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1434
- Cleanup of channels by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1444
- fix: don't add VIP to interface in routing table and BGP service modes by @chdxD1 in https://github.com/kube-vip/kube-vip/pull/1442
- fix: align CLI lease flag defaults with Kubernetes client-go defaults (15/10/2) by @k-jun in https://github.com/kube-vip/kube-vip/pull/1429
- fix: skip UPNP refresh logging when no service instances by @ohauer in https://github.com/kube-vip/kube-vip/pull/1446
- Now will ensure egress rules are cleaned for nft-internal by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/1447
- fix(metrics): register correct gauge for BGP session info by @sebastiangaiser in https://github.com/kube-vip/kube-vip/pull/1460
- Fixed E2E ARP tests by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1412
- Fixed actions failure when whoami image cannot be loaded by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1417

### 1.1.1

- Fixed BGP route advertisement in control-plane only mode by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1468
- Fixed leader election restart issue by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1477
- Fixed services error handling by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1478

### 1.1.2

- fix(egress): prevent unnecessary SNAT updates and fix missed updates by @RnkeZ in https://github.com/kube-vip/kube-vip/pull/1433


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.1.2**, the newest release recorded here for this line.

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
