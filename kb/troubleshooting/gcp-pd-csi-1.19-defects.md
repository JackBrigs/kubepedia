---
id: TROUBLE-GCP_PD_CSI_1_19_DEFECTS
type: troubleshooting
title: "gcp-pd-csi 1.19: defects fixed in the 1.19 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.19.0 <1.20.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - gcp-pd-csi 1.19 known issues
  - gcp-pd-csi 1.19 fixed in
  - is this gcp-pd-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - gcp-pd-csi
sources:
  - type: docs
    path: kubernetes-sigs/gcp-compute-persistent-disk-csi-driver release notes for the 1.19 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# gcp-pd-csi 1.19: defects fixed in the 1.19 line

## Summary

**8 defects** the project fixed across **1 releases** of the 1.19 line, from 1.19.0 to
1.19.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.19.0

- Fix logic bug while checking available LSSDs for RAIDing for Data Cache by @hungnguyen243 in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/1993
- update debian image to fix CVE by @Sneha-at in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/1997
- Use strings.Fields for whitespace splitting to fix issues with strings.Split in case of multiple consecutive spaces by @hungnguyen243 in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2006
- Fix units for cache size while calculating chunk size for LVM by @Sneha-at in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2007
- fix outdated metadata error in watcher by @hungnguyen243 in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2028
- Fix hyperdisk attach limits by @jsafrane in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2057
- Fix Hyperdisk Resize That Requires Iops/Throughput Adjustment by @sunnylovestiramisu in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2054
- Fix Gen4 Custom VM Cases by @sunnylovestiramisu in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2096


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.19.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes-sigs/gcp-compute-persistent-disk-csi-driver`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/gcp-pd-csi.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
