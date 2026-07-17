---
id: UPGRADE-V2_27_0__V2_27_1
type: upgrade
title: "Upgrade report v2.27.0 → v2.27.1"
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - v2.27.0 to v2.27.1
  - upgrade 2.27.0 2.27.1
tags:
  - upgrade
  - change-report
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main
    url: https://github.com/kubernetes-sigs/kubespray/compare/v2.27.0...v2.27.1
    note: "version deltas verified from tag code; changes from release notes"
relations:
  - type: see_also
    target: RELEASE-V2_27_1
  - type: see_also
    target: CONCEPT-COMPONENT_VERSION_SELECTION
---

# Upgrade report v2.27.0 → v2.27.1

## Summary

A **patch** upgrade. Patch upgrade: same Kubernetes 1.31 line; bug fixes only.

## Implementation

Version deltas:

| Item | v2.27.0 | v2.27.1 |
|------|-------|------|
| Kubernetes default | 1.31.4 | 1.31.9 |
| containerd | 1.7.24 | 1.7.27 |
| calico | 3.29.1 | 3.29.4 |
| runc | 1.2.3 | **1.2.6** |
| cni-plugins | 1.4.0 | 1.4.1 |
| cri-dockerd | 0.3.11 | 0.3.16 |

## Upgrade Notes

- **Patch** upgrade: same Kubernetes 1.31 line; bug fixes only.
- Fixes: control-plane reconfiguration on upgrades, kubeadm v1beta4 UpgradeConfiguration, calico RBAC.
- Low-risk; snapshot etcd first ([[PRACTICE-UPGRADE_PREFLIGHT]]).

## Compatibility

- Kubernetes stays on 1.31.
- One Kubespray minor at a time ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]).

## References

- Compare `v2.27.0...v2.27.1`; per-tag components: [[RELEASE-V2_27_1]].
