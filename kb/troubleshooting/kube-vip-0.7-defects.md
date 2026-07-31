---
id: TROUBLE-KUBE_VIP_0_7_DEFECTS
type: troubleshooting
title: "kube-vip 0.7: defects fixed in the 0.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.7.0 <0.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-vip 0.7 known issues
  - kube-vip 0.7 fixed in
  - is this kube-vip bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-vip
sources:
  - type: docs
    path: kube-vip/kube-vip release notes for the 0.7 line — bug-fix entries
    url: https://github.com/kube-vip/kube-vip/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-vip 0.7: defects fixed in the 0.7 line

## Summary

**12 defects** the project fixed across **3 releases** of the 0.7 line, from 0.7.0 to
0.7.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.7.0

- fixes go modules by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/707
- More fixes by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/709
- fixes to the new ipvs import by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/710
- fix #723 and allow short hostnames as well by @Cellebyte in https://github.com/kube-vip/kube-vip/pull/724
- No-leader-election mode for BGP and fixes for routing table mode by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/740
- fix: Using log instead of fmt.print by @ii2day in https://github.com/kube-vip/kube-vip/pull/746
- fix: print manifests to stdout by @Wielewout in https://github.com/kube-vip/kube-vip/pull/750

### 0.7.1

- Added common endpoint provider interface and fixed route deletion iss… by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/761
- Fix IPVS service error: netlink receive invalid argument by @lou-lan in https://github.com/kube-vip/kube-vip/pull/765
- fixes a bug that wouldn't return CIDRs for egress by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/768

### 0.7.2

- Fix flaky e2e test by @lubronzhan in https://github.com/kube-vip/kube-vip/pull/776
- Fixes conntrack deleting wrong connections and cleaning old SNAT rules by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/777


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.7.2**, the newest release recorded here for this line.

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
