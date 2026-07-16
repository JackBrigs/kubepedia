---
id: CONCEPT-KUBERNETES_VERSION_SUPPORT
type: concept
title: Kubernetes version support in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31.0 <=1.35.4"
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
    note: "v2.29.0 kubelet_checksums['amd64'] — installable versions"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    lines: "112"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "v2.30.0 kubelet_checksums['amd64'] — installable versions"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    lines: "112"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "v2.31.0 kubelet_checksums['amd64'] — installable versions"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "25,28"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "default = first key; min = last key"
  - type: code
    path: roles/validate_inventory/tasks/main.yml
    lines: "39-43"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/validate_inventory/tasks/main.yml
    note: "assert kube_version >= kube_version_min_required"
relations:
  - type: depends_on
    target: VARIABLE-KUBE_VERSION
  - type: see_also
    target: COMPONENT-ETCD
---

# Kubernetes version support in Kubespray

## Summary

Each Kubespray release supports a moving window of three consecutive Kubernetes
minor lines, defined by the versions for which it ships kubelet/kubeadm/kubectl
checksums. The default is the newest patch of the newest minor; the minimum is the
oldest shipped version. This document tracks the window per indexed tag.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0` (baseline forward).
- The installed version is [[VARIABLE-KUBE_VERSION]].
- The etcd version tracks the Kubernetes minor line (see [[COMPONENT-ETCD]]).

## Implementation

The authoritative source is `kubelet_checksums['amd64']` in
`roles/kubespray_defaults/vars/main/checksums.yml`; its keys are the installable
versions. Default and minimum are the first and last keys
(`roles/kubespray_defaults/defaults/main/main.yml:25,28`), enforced by the assert
in `roles/validate_inventory/tasks/main.yml`.

Support window per tag:

| Kubespray | Minor lines | Patch ranges | Count | Default | Minimum |
|-----------|-------------|--------------|-------|---------|---------|
| v2.29.0   | 1.31, 1.32, 1.33 | 1.31.0–1.31.13, 1.32.0–1.32.9, 1.33.0–1.33.5 | 30 | 1.33.5 | 1.31.0 |
| v2.30.0   | 1.32, 1.33, 1.34 | 1.32.0–1.32.11, 1.33.0–1.33.7, 1.34.0–1.34.3 | 24 | 1.34.3 | 1.32.0 |
| v2.31.0   | 1.33, 1.34, 1.35 | 1.33.0–1.33.11, 1.34.0–1.34.7, 1.35.0–1.35.4 | 25 | 1.35.4 | 1.33.0 |

Notes:

- The window advances by one minor per Kubespray minor release; the oldest minor
  is dropped and a new one added (1.31 present in v2.29.0, dropped in v2.30.0).
- No explicit upper bound is asserted; a version without a checksum fails during
  download.
- CI: the inventories under `tests/files/` do not pin `kube_version`, so CI
  exercises the per-tag default.

## Compatibility

- Kubespray `v2.29.0`: `>=1.31.0 <=1.33.5`, default `1.33.5`.
- Kubespray `v2.30.0`: `>=1.32.0 <=1.34.3`, default `1.34.3`.
- Kubespray `v2.31.0`: `>=1.33.0 <=1.35.4`, default `1.35.4`.
- Below the per-tag minimum: rejected by inventory validation.

## References

- `roles/kubespray_defaults/vars/main/checksums.yml` (`kubelet_checksums`) —
  v2.29.0 `9991412`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`
- `roles/kubespray_defaults/defaults/main/main.yml:25,28`
- `roles/validate_inventory/tasks/main.yml` (version assert)
- `tests/files/` (no `kube_version` override → default is tested)
