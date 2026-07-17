---
id: UPGRADE-V2_28_0__V2_28_1
type: upgrade
title: "Upgrade report v2.28.0 → v2.28.1"
status: active
kubespray_version: ">=v2.28.0 <=v2.28.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - v2.28.0 to v2.28.1
  - upgrade 2.28.0 2.28.1
tags:
  - upgrade
  - change-report
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main
    url: https://github.com/kubernetes-sigs/kubespray/compare/v2.28.0...v2.28.1
    note: "version deltas verified from tag code; changes from release notes"
relations:
  - type: see_also
    target: RELEASE-V2_28_1
  - type: see_also
    target: CONCEPT-COMPONENT_VERSION_SELECTION
---

# Upgrade report v2.28.0 → v2.28.1

## Summary

A **patch** upgrade. Patch upgrade: same Kubernetes 1.32 line; bug fixes only.

## Implementation

Version deltas:

| Item | v2.28.0 | v2.28.1 |
|------|-------|------|
| Kubernetes default | 1.32.5 | 1.32.8 |
| etcd | 3.5.16 | 3.5.22 |
| containerd | 2.0.5 | 2.0.6 |
| cilium | 1.17.3 | **1.17.7** |
| calico | 3.29.3 | 3.29.5 |

## Upgrade Notes

- **Patch** upgrade: same Kubernetes 1.32 line; bug fixes only.
- Fixes: Cilium install/templating & loadBalancer.mode, Cilium BGP control-plane, calico BGP, external etcd member removal.
- Low-risk.

## Compatibility

- Kubernetes stays on 1.32.
- One Kubespray minor at a time ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]).

## References

- Compare `v2.28.0...v2.28.1`; per-tag components: [[RELEASE-V2_28_1]].
