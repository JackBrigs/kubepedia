---
id: CONCEPT-ADDON_ROOK_CEPH
type: concept
title: "Rook-Ceph (operator + cluster) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.34"
component_version: "1.18.9"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - rook-ceph
  - rook-operator
  - rook-ceph-cluster
  - ceph storage
tags:
  - addons
  - storage
  - ceph
  - rook
sources:
  - type: docs
    path: Rook v1.18 prerequisites
    url: https://rook.io/docs/rook/v1.18/Getting-Started/Prerequisites/prerequisites/
    note: "K8s v1.29–v1.34 (min raised to 1.29)"
  - type: docs
    path: Rook v1.18 upgrade guide
    url: https://rook.io/docs/rook/v1.18/Upgrade/rook-upgrade/
    note: "CSI operator required; StorageClass immutability; operator-before-cluster"
  - type: docs
    path: Ceph upgrade doc
    url: https://raw.githubusercontent.com/rook/rook/v1.18.9/Documentation/Upgrade/ceph-upgrade.md
    note: "supported Ceph Reef/Squid/Tentacle; Tentacle read-affinity corruption bug"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-ADDON_CEPH_CSI_CEPHFS
---

# Rook-Ceph (operator + cluster) — addon

## Summary

Rook deploys and manages Ceph storage in-cluster. Two charts are paired: **rook-ceph**
(operator) **1.18.9** and **rook-ceph-cluster** **1.18.9** (the `CephCluster` + pools/SCs).
Supported Kubernetes **1.29–1.34** (v1.18 raised the minimum to 1.29). Two upgrade traps:
the **CSI-operator migration** and **StorageClass immutability**.

## Context

- Class: upstream addon; `rook-operator` + `rook-ceph-cluster` rows in
  [[CONCEPT-ADDON_CATALOG]]. Supported Ceph: **Reef v18.2.0+, Squid v19.2.0+, Tentacle
  v20.2.0+** (Quincy dropped).

## Implementation

- App/appVersion **v1.18.9** for both charts. Chart `kubeVersion`: **none** (the tag
  Chart.yaml is a build placeholder; released charts confirmed via Artifact Hub).
- **Upgrade the operator chart before the cluster chart.**

## Configuration

- **CSI operator now required** for RBD/CephFS/NFS: Rook auto-converts legacy CSI settings to
  CSI-operator CRs (revert with `ROOK_USE_CSI_OPERATOR: false`); the operator chart adds
  `ceph-csi-operator` v0.4.1 as a conditional dependency.
- **StorageClasses are immutable** — the cluster chart adds new SC params
  (`controller-publish-secret-name`/`-namespace`), so `helm upgrade` fails unless existing
  SCs are deleted or the new params removed first.
- Node topology is validated at `CephCluster` creation (new clusters rejected on a bad CRUSH
  hierarchy).

## Compatibility

- **Kubernetes range:** **1.29–1.34**.
- **Known issues:** StorageClass-immutability upgrade failure; CSI-operator conversion
  failures (use the revert flag); **Ceph v20.2.0 (Tentacle) data-corruption bug when "read
  affinity" is enabled — wait for v20.2.1**.
- **CVEs:** none against `rook/rook`. The cluster is exposed to **Ceph-level CVE-2025-52555**
  (ceph-fuse/CephFS privilege bypass; affects Ceph 18.2.1–18.2.4, 19.0.0–19.2.2; fixed
  18.2.5 / 19.2.3) if running an affected Ceph patch level.

## References

- Rook v1.18 prerequisites, upgrade guide, ceph-upgrade doc (above); Ceph CVE-2025-52555.
- Catalog: [[CONCEPT-ADDON_CATALOG]]; CephFS CSI: [[CONCEPT-ADDON_CEPH_CSI_CEPHFS]].
