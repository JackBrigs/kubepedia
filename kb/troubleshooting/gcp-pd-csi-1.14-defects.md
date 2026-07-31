---
id: TROUBLE-GCP_PD_CSI_1_14_DEFECTS
type: troubleshooting
title: "gcp-pd-csi 1.14: defects fixed in the 1.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.14.0 <1.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - gcp-pd-csi 1.14 known issues
  - gcp-pd-csi 1.14 fixed in
  - is this gcp-pd-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - gcp-pd-csi
sources:
  - type: docs
    path: kubernetes-sigs/gcp-compute-persistent-disk-csi-driver release notes for the 1.14 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# gcp-pd-csi 1.14: defects fixed in the 1.14 line

## Summary

**6 defects** the project fixed across **2 releases** of the 1.14 line, from 1.14.0 to
1.14.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.14.0

- fix pointer issue for GCE staging support by @Sneha-at in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/1609
- Fix error when no compute endpoint is passed by @Sneha-at in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/1620
- Fix nvme path filtering logic for udevadm trigger by @pwschuurman in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/1633
- Fix e2e tests to run on cloudtop by @mattcary in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/1692
- Update debian image from bullseye to bookworm to fix CVEs by @Sneha-at in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/1694

### 1.14.5

- [release-1.14] Fix Gen4 Custom VM Cases by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/2100


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.14.5**, the newest release recorded here for this line.

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
