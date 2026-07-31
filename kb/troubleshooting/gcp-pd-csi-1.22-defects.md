---
id: TROUBLE-GCP_PD_CSI_1_22_DEFECTS
type: troubleshooting
title: "gcp-pd-csi 1.22: defects fixed in the 1.22 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.22.0 <1.23.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - gcp-pd-csi 1.22 known issues
  - gcp-pd-csi 1.22 fixed in
  - is this gcp-pd-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - gcp-pd-csi
sources:
  - type: docs
    path: kubernetes-sigs/gcp-compute-persistent-disk-csi-driver release notes for the 1.22 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# gcp-pd-csi 1.22: defects fixed in the 1.22 line

## Summary

**6 defects** the project fixed across **4 releases** of the 1.22 line, from 1.22.0 to
1.22.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.22.0

- Fix partial cache tail latency by correcting the cache chunk size calc by @cemakd in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2176
- Fix invalid maintenance exclusion command by @tonyzhc in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2204

### 1.22.1

- Fix partial cache tail latency by correcting the cache chunk size calc by @cemakd in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2176
- Fix invalid maintenance exclusion command by @tonyzhc in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2204

### 1.22.2

- [release-1.22] Fix disk size validation branch by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2233

### 1.22.5

- [btrfs csi driver] fix blkid argument by @motiejus in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2252


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.22.5**, the newest release recorded here for this line.

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
