---
id: TROUBLE-KUBE_ROUTER_2_7_DEFECTS
type: troubleshooting
title: "kube-router 2.7: defects fixed in the 2.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.7.0 <2.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-router 2.7 known issues
  - kube-router 2.7 fixed in
  - is this kube-router bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-router
sources:
  - type: docs
    path: cloudnativelabs/kube-router release notes for the 2.7 line — bug-fix entries
    url: https://github.com/cloudnativelabs/kube-router/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-router 2.7: defects fixed in the 2.7 line

## Summary

**11 defects** the project fixed across **2 releases** of the 2.7 line, from 2.7.0 to
2.7.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.7.0

- Retry certain netlink calls which fixes early start race conditions - Some users noticed a race condition on ip link setup when kube-router was starting as the node's OS was also starting. This should fix that edge case
- Go Safecast bug fixes and unit test efficiencies: @ccoVeille
- - test(NSC): fix two DSR service tests to create pods `<Aaron U'Ren>`
- - fix(NSC): cleanup historical bad IPv6 TCPMSS vals `<Aaron U'Ren>`
- - fix: convert ginkgo tests to standard go tests `<Aaron U'Ren>`
- - fix(BGP): always configure AFI SAFI `<Aaron U'Ren>`
- - fix(dsr): set TCPMSS based on address family `<Richard Kojedzinszky>`
- - fix: Replace all netlink functions that throw ErrDumpInterrupted with a retry wrapper `<Cat C>`
- - fix(nrc): Update make test-pretty to test internal subdirectory. Update nlretry and LocalLinkQuerier interface to support passing in contexts `<Cat C>`
- - fix(nrc): Add netlink.Handle wrapper to retry netlink calls that raise ErrDumpInterrupted errors `<Cat C>`

### 2.7.1

- fix(aws.go): load region before attempting to assume a role


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.7.1**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cloudnativelabs/kube-router`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kube-router.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
