---
id: CONCEPT-KUBERNETES_VERSION_SUPPORT
type: concept
title: Kubernetes version support in Kubespray v2.29.0
status: active
kubespray_version: v2.29.0
kubernetes_version: ">=1.31.0 <=1.33.5"
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kubernetes version support
  - supported kubernetes versions
tags:
  - kubernetes
  - version
  - support-matrix
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    lines: "112"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "kubelet_checksums['amd64'] enumerates every installable version"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "25,28"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "default = first key (1.33.5); min = last key (1.31.0)"
  - type: code
    path: roles/validate_inventory/tasks/main.yml
    lines: "40-42"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/validate_inventory/tasks/main.yml
    note: "assert kube_version >= kube_version_min_required"
relations:
  - type: depends_on
    target: VARIABLE-KUBE_VERSION
  - type: see_also
    target: COMPONENT-ETCD
---

# Kubernetes version support in Kubespray v2.29.0

## Summary

Kubespray `v2.29.0` supports three Kubernetes minor lines — `1.31`, `1.32`, and
`1.33` — for a total of 30 installable patch versions. The default is `1.33.5`,
the minimum is `1.31.0`. The supported set is defined by the versions for which
the release ships kubelet/kubeadm/kubectl checksums.

## Context

- Applies to Kubespray `v2.29.0` (commit `9991412`).
- The version actually installed is [[VARIABLE-KUBE_VERSION]].
- The etcd version tracks the Kubernetes minor line
  (see [[COMPONENT-ETCD]]): all three supported minors map to etcd `3.5.23`.

## Implementation

The single source that enumerates supported versions is
`kubelet_checksums['amd64']` in
`roles/kubespray_defaults/vars/main/checksums.yml`. Its keys in `v2.29.0`:

| Minor | Supported patch versions |
|-------|--------------------------|
| 1.33  | 1.33.0 – 1.33.5 |
| 1.32  | 1.32.0 – 1.32.9 |
| 1.31  | 1.31.0 – 1.31.13 |

- **Default** — the first key, `1.33.5` (`main.yml:25`).
- **Minimum required** — the last key, `1.31.0` (`main.yml:28`).
- **Enforcement** — `roles/validate_inventory/tasks/main.yml:40-42` asserts
  `kube_version >= kube_version_min_required`. No explicit upper bound exists; a
  version without a checksum entry fails during download instead.
- **CI** — the test inventories under `tests/files/` do not pin `kube_version`,
  so continuous integration exercises the default (`1.33.5`).

Version-conditional behavior keyed to these bounds includes the kubeadm config
API version (`v1beta4` for `>=1.31`, i.e. always in this release;
`main.yml:35`).

## Compatibility

- Kubespray: `v2.29.0`.
- Kubernetes: `>=1.31.0 <=1.33.5` installable; `1.33.5` default.
- Below `1.31.0`: rejected by inventory validation.
- Above `1.33.5`: no checksum, not installable without adding one.

## References

- `roles/kubespray_defaults/vars/main/checksums.yml` (`kubelet_checksums`)
- `roles/kubespray_defaults/defaults/main/main.yml:25,28,35`
- `roles/validate_inventory/tasks/main.yml:40-42`
- `tests/files/` (no `kube_version` override → default is tested)
- Tag `v2.29.0`, commit `9991412b4597d6eaf37f86e5f20f9f903a731c08`.
