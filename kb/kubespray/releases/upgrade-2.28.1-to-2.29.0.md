---
id: UPGRADE-V2_28_1__V2_29_0
type: upgrade
title: "Upgrade report v2.28.1 → v2.29.0"
status: active
kubespray_version: ">=v2.28.1 <=v2.29.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - v2.28.1 to v2.29.0
  - upgrade 2.28.1 2.29.0
tags:
  - upgrade
  - change-report
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main
    url: https://github.com/kubernetes-sigs/kubespray/compare/v2.28.1...v2.29.0
    note: "version deltas verified from tag code; changes from release notes"
relations:
  - type: see_also
    target: RELEASE-V2_29_0
  - type: see_also
    target: CONCEPT-COMPONENT_VERSION_SELECTION
---

# Upgrade report v2.28.1 → v2.29.0

## Summary

A **minor** upgrade. BREAKING — weave network plugin removed — migrate off `weave` before upgrading.

## Implementation

Version deltas:

| Item | v2.28.1 | v2.29.0 |
|------|-------|------|
| Kubernetes default | 1.32.8 | **1.33.5** |
| etcd | 3.5.22 | 3.5.22 |
| containerd | 2.0.6 | **2.1.4** |
| cilium | 1.17.7 | **1.18.2** |
| cni-plugins | 1.4.1 | **1.8.0** |
| CoreDNS | 1.11.3 | **1.12.0** |
| cri-o | 1.32.0 | 1.33.4 |

## Upgrade Notes

- **BREAKING — weave network plugin removed** — migrate off `weave` before upgrading.
- **BREAKING — tag `master` removed, replaced by `control-plane`** — update any `--tags master` usage.
- **Removed:** `conntrack_modules` (hardcoded now); **cri-o on Ubuntu 20 dropped**.
- `/etc/hosts` is **no longer populated** with all cluster nodes; CoreDNS **node affinity removed** (pods no longer scheduled on control-planes by default) — set `coredns_affinity` if needed.
- Kubernetes 1.32 → 1.33; snapshot etcd first ([[PRACTICE-UPGRADE_PREFLIGHT]]).

## Compatibility

- Kubernetes moves 1.32 → 1.33; weave users must migrate CNI first.
- One Kubespray minor at a time ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]).

## References

- Compare `v2.28.1...v2.29.0`; per-tag components: [[RELEASE-V2_29_0]].
