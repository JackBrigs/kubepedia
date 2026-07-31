---
id: TROUBLE-KUBE_VIP_0_5_DEFECTS
type: troubleshooting
title: "kube-vip 0.5: defects fixed in the 0.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.5.0 <0.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-vip 0.5 known issues
  - kube-vip 0.5 fixed in
  - is this kube-vip bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-vip
sources:
  - type: docs
    path: kube-vip/kube-vip release notes for the 0.5 line — bug-fix entries
    url: https://github.com/kube-vip/kube-vip/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-vip 0.5: defects fixed in the 0.5 line

## Summary

**21 defects** the project fixed across **7 releases** of the 0.5 line, from 0.5.5 to
0.5.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.5.5

- Allow fixed virtual MAC for DHCP VIPs by @valtzu in https://github.com/kube-vip/kube-vip/pull/434
- fix: --table flag should add vip_routingtable env var not vip_wireguard by @alexandrevilain in https://github.com/kube-vip/kube-vip/pull/446
- Build-fixes by @cprivitere in https://github.com/kube-vip/kube-vip/pull/440

### 0.5.6

- Fix typo in EnableControlPlane config option by @abhay-krishna in https://github.com/kube-vip/kube-vip/pull/467
- Fixes to logging by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/470
- Fixes all leaderElection code to use config by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/472
- This fixes an issue with the cache being wiped by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/474
- Fixes to where iptables are gc by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/478
- logging and fixed an issue with multiple elections by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/480
- Fix to egress rules by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/482

### 0.5.7

- Fix CVE by @lubronzhan in https://github.com/kube-vip/kube-vip/pull/489

### 0.5.8

- Fix watching for endpoints RBAC rule by @kriansa in https://github.com/kube-vip/kube-vip/pull/498

### 0.5.9

- Fixes to negative waitgroup by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/509
- Adds services testing and fixes missing context by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/511

### 0.5.10

- Fix service deletion not registering by @spideyfusion in https://github.com/kube-vip/kube-vip/pull/510
- Fixes and testing for endpoints by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/513
- Fix broken link in docs by @fimmicon in https://github.com/kube-vip/kube-vip/pull/494
- lint fixes by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/517
- Actions fixes by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/518

### 0.5.12

- Fix the doc link by @lubronzhan in https://github.com/kube-vip/kube-vip/pull/531
- Adds nftables as an option, and fixes a panic by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/540


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.5.12**, the newest release recorded here for this line.

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
