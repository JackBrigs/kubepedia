---
id: CONCEPT-ADDON_LVM_LOCALPV
type: concept
title: "OpenEBS lvm-localpv — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.23 <=1.35"
component_version: "1.7.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - lvm-localpv
  - openebs lvm
  - lvm local pv
tags:
  - addons
  - storage
  - openebs
  - local-storage
sources:
  - type: docs
    path: lvm-localpv v1.7.0 README
    url: https://raw.githubusercontent.com/openebs/lvm-localpv/v1.7.0/README.md
    note: "K8s 1.23+; no documented upper bound"
  - type: docs
    path: lvm-localpv v1.7.0 release
    url: https://github.com/openebs/lvm-localpv/releases/tag/v1.7.0
    note: "CSI driver 1.7.0, CSI spec v1.9.0, new mkfs options"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# OpenEBS lvm-localpv — addon

## Summary

OpenEBS **lvm-localpv** provisions node-local PVs backed by LVM logical volumes. Chart/app
**1.7.0** (CSI driver 1.7.0, CSI spec v1.9.0). Volumes are **strictly node-local** — a pod
using one cannot reschedule to another node.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].
- **Chart caveat:** there is no `lvm-localpv-1.7.0` git chart tag; the released chart is
  verified from the OpenEBS Helm tarball (v2, version/appVersion 1.7.0, `crds` dep 1.7.0).

## Implementation

- Chart→app: 1.7.0. Chart `kubeVersion`: **none**. CSI spec bumped to **v1.9.0**.
- 1.7.0 adds `mkfs` format options (new StorageClass params), a Helm label/selector refactor,
  a CRD YAML fix and `parseInt` capacity parsing. No breaking changes declared.

## Configuration

- **Prerequisites per node:** `lvm2` installed and a **pre-created Volume Group** — a missing
  VG leaves provisioning `Pending`. The `dm-snapshot` kernel module must be loaded or
  snapshots fail.
- Because volumes are node-local, use `volumeBindingMode: WaitForFirstConsumer` and pin
  workloads that must stay put.

## Compatibility

- **Kubernetes range:** README states **K8s 1.23+** with no documented upper bound — the
  upper end of 1.29–1.35 is **unverified** but expected to work.
- **CVEs:** none found for `openebs/lvm-localpv` at 1.7.0 (OSV empty).

## References

- lvm-localpv v1.7.0 README + release notes (above); OpenEBS prerequisites.
- Catalog: [[CONCEPT-ADDON_CATALOG]].
