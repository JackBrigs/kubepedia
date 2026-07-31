---
id: TROUBLE-GCP_PD_CSI_1_21_DEFECTS
type: troubleshooting
title: "gcp-pd-csi 1.21: defects fixed in the 1.21 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.21.0 <1.22.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - gcp-pd-csi 1.21 known issues
  - gcp-pd-csi 1.21 fixed in
  - is this gcp-pd-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - gcp-pd-csi
sources:
  - type: docs
    path: kubernetes-sigs/gcp-compute-persistent-disk-csi-driver release notes for the 1.21 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# gcp-pd-csi 1.21: defects fixed in the 1.21 line

## Summary

**5 defects** the project fixed across **3 releases** of the 1.21 line, from 1.21.0 to
1.21.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.21.0

- fix: update Hyperdisk attach limits to match GCP documentation for Ge… by @arsiesys in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2127
- fix ci by @carlory in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2139

### 1.21.1

- fix: update Hyperdisk attach limits to match GCP documentation for Ge… by @arsiesys in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2127
- fix ci by @carlory in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2139

### 1.21.2

- [release-1.21] Fix partial cache tail latency by correcting the cache chunk size calc by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2177


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.21.2**, the newest release recorded here for this line.

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
