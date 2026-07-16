---
id: CONCEPT-COMPONENT_VERSION_SELECTION
type: concept
title: "Component version-selection matrix (how each version is chosen)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - component matrix
  - component versions
  - how component versions are chosen
  - version selection mechanism
  - which components move with kube_version
tags:
  - components
  - versions
  - upgrade
  - stage-3
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "*_version expressions for all managed components (tag v2.31.0)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "etcd/coredns supported_versions maps, pinned add-on versions (tag v2.31.0)"
relations:
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: CONCEPT-K8S_CONTROL_PLANE_VERSIONS
  - type: see_also
    target: COMPONENT-ETCD
---

# Component version-selection matrix (how each version is chosen)

## Summary

Every Kubespray-managed component gets its version from **one of four mechanisms**.
Knowing which mechanism applies tells you whether a component moves when you change
`kube_version`, when you bump Kubespray, or only when you override it explicitly — the
foundation for any upgrade/change report. Values below are for tag **`v2.31.0`**; the
*mechanism* is stable across `v2.29.0`–`v2.31.0`, the *pinned values* differ per tag
(see the `RELEASE-*` docs).

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Definitions live in
  `roles/kubespray_defaults/defaults/main/{download,main}.yml`.
- Control-plane components (apiserver/controller-manager/scheduler/kube-proxy) are **not**
  here — they all equal `kube_version` via kubeadm ([[CONCEPT-K8S_CONTROL_PLANE_VERSIONS]]).

## Implementation

### 1. Derived from the target Kubernetes minor (`*_supported_versions[kube_major_version]`)

Moves **with `kube_version`** — different K8s minors get different component versions.

| Component | v2.31.0 mapping |
|-----------|-----------------|
| **etcd** | 1.33/1.34 → `3.5.29`; 1.35 → `3.6.10` |
| **CoreDNS** | 1.33 → `1.12.0`; 1.34 → `1.12.1`; 1.35 → `1.12.4` |

### 2. Filtered by the Kubernetes version (`select('version', kube_major_next_version, '<')`)

Picks the newest bundled version **compatible with** the target K8s minor — also
effectively K8s-coupled.

| Component | note |
|-----------|------|
| **crictl** | newest checksum `< next K8s minor` |
| **cri-o** | newest checksum `< next K8s minor` (CRI-O tracks K8s minors) |

### 3. Newest entry in the bundled checksums map (`(X_checksums['amd64'] | dict2items)[0].key`)

Version = whatever Kubespray **bundled** for this tag; changing it requires the target to
exist in the checksums dict. Moves **only when you bump Kubespray** (or override + add a
checksum).

| Component | v2.31.0 |
|-----------|---------|
| **containerd** | `2.2.3` |
| **runc** | `1.4.2` |
| **cni-plugins** | `1.9.1` |
| **calico** | (newest in `calicoctl_binary_checksums`) |
| **helm** | (newest in `helm_archive_checksums`) |
| **nerdctl** | `2.2.2` |
| **kata-containers** | (newest in checksums) |

### 4. Fixed literal pin (only changes on a Kubespray bump)

Hard-coded; independent of `kube_version`.

| Component | v2.31.0 |
|-----------|---------|
| **Cilium** | `1.19.3` |
| **kube-vip** | `1.0.3` |
| **NodeLocal DNS** (k8s-dns-node-cache) | `1.25.0` |
| **dns-autoscaler** | `1.8.8` |
| **metrics-server** | `0.8.1` |
| **cert-manager** | `1.15.3` |
| **MetalLB** | `0.13.9` |

### Implications for the upgrade report

- **Cross a K8s minor** → categories **1 & 2** change automatically (etcd, CoreDNS,
  crictl, CRI-O). etcd 3.6 first appears with K8s `1.35`.
- **Bump Kubespray only (same K8s)** → categories **3 & 4** change (runtime, CNI,
  add-ons) via the new tag's bundled/pinned versions.
- **Override a component** → only categories 3 (needs a checksum entry) and 4 are meant to
  be user-pinned; overriding categories 1/2 fights the K8s-compat logic.

## References

- `download.yml` / `main.yml` `*_version` expressions at tag `v2.31.0`.
- Per-tag concrete versions: `RELEASE-V2_29_0`…`RELEASE-V2_31_0` and the `UPGRADE-*`
  reports; K8s coupling: [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
