---
id: UPGRADE-V2_27_1__V2_28_0
type: upgrade
title: "Upgrade report v2.27.1 → v2.28.0"
status: active
kubespray_version: ">=v2.27.1 <=v2.28.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - v2.27.1 to v2.28.0
  - upgrade 2.27.1 2.28.0
tags:
  - upgrade
  - change-report
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main
    url: https://github.com/kubernetes-sigs/kubespray/compare/v2.27.1...v2.28.0
    note: "version deltas verified from tag code; changes from release notes"
relations:
  - type: see_also
    target: RELEASE-V2_28_0
  - type: see_also
    target: CONCEPT-COMPONENT_VERSION_SELECTION
---

# Upgrade report v2.27.1 → v2.28.0

## Summary

A **minor** upgrade. BREAKING — remove the leading `v` from all explicit component versions (notably `kube_version`).

## Implementation

Version deltas:

| Item | v2.27.1 | v2.28.0 |
|------|-------|------|
| Kubernetes default | 1.31.9 | **1.32.5** |
| etcd | 3.5.21 | 3.5.16 |
| containerd | 1.7.27 | **2.0.5** (major) |
| cilium | 1.15.9 | **1.17.3** |
| cri-o | 1.31.6 | 1.32.0 |
| kube-vip | 0.8.0 | 0.8.9 |

## Upgrade Notes

- **BREAKING — remove the leading `v`** from all explicit component versions (notably `kube_version`).
- **Removed:** Krew install support; `etcd_kubeadm_enabled` — drop them from inventory.
- **Renames:** role `kubespray-defaults` → `kubespray_defaults`, `bootstrap-os` → `bootstrap_os` — update any references.
- **containerd 1.7 → 2.0 (major).** Review containerd config; Cilium now installs via the **Cilium CLI** (not template), `cilium_identity_allocation_mode` default → `crd`.
- Control-plane memory requirement raised to **2GB**. **Last RHEL 8 release.** One minor at a time.

## Compatibility

- Kubernetes moves 1.31 → 1.32; do not skip minors.
- One Kubespray minor at a time ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]).

## References

- Compare `v2.27.1...v2.28.0`; per-tag components: [[RELEASE-V2_28_0]].
