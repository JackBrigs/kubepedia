---
id: TROUBLE-CERT_MANAGER_0_7_DEFECTS
type: troubleshooting
title: "cert-manager 0.7: defects fixed in the 0.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.7.0 <0.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 0.7 known issues
  - cert-manager 0.7 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 0.7 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 0.7: defects fixed in the 0.7 line

## Summary

**9 defects** the project fixed across **3 releases** of the 0.7 line, from 0.7.0 to
0.7.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.7.0

- Fix potential race when updating secret resource (#1318, @munnerz)
- Fix bug causing certficates to be re-issued endlessly in certain edge cases (#1280, @munnerz)
- Fix bug when specify certificate keyAlgorithm without an explicit keySize (#1309, @munnerz)
- Fix bug where --dns01-recursive-nameservers flag was not respected when looking up the zone to update for a DNS01 challenge (#1266, @munnerz)

### 0.7.1

- Fix issues running the cainjector controller on Kubernetes 1.9 (#1579, @munnerz)
- Fix upgrade bug where lastTransitionTime may be set to nil, rendering cert-manager inoperable without manual intervention (#1576, @munnerz)

### 0.7.2

- Fix update loop in certificates controller and add additional debug logging (#1602, @munnerz)
- Fixes additionalPrinterColumn formatting for Certificate resources (#1616, @munnerz)
- Fix issues running the cainjector controller on Kubernetes 1.9 (#1579, @munnerz)


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

- Upstream releases of `cert-manager/cert-manager`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cert-manager.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
