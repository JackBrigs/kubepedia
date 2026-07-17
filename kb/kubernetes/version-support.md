---
id: CONCEPT-KUBERNETES_VERSION_SUPPORT
type: concept
title: Kubernetes version support in Kubespray
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29.0 <=1.35.4"
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

- Covers Kubespray `v2.27.0`–`v2.31.0` (v2.29.0 is the research baseline; v2.27.0–v2.28.1 added for range extension).
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
| v2.27.0   | 1.29, 1.30, 1.31 | (per tag checksums) | — | 1.31.4 | 1.29.0 |
| v2.27.1   | 1.29, 1.30, 1.31 | (per tag checksums) | — | 1.31.9 | 1.29.0 |
| v2.28.0   | 1.30, 1.31, 1.32 | (per tag checksums) | — | 1.32.5 | 1.30.x |
| v2.28.1   | 1.30, 1.31, 1.32 | (per tag checksums) | — | 1.32.8 | 1.30.x |
| v2.29.0   | 1.31, 1.32, 1.33 | 1.31.0–1.31.13, 1.32.0–1.32.9, 1.33.0–1.33.5 | 30 | 1.33.5 | 1.31.0 |
| v2.29.1   | 1.31, 1.32, 1.33 | 1.31.0–1.31.14, 1.32.0–1.32.10, 1.33.0–1.33.7 | 34 | 1.33.7 | 1.31.0 |
| v2.30.0   | 1.32, 1.33, 1.34 | 1.32.0–1.32.11, 1.33.0–1.33.7, 1.34.0–1.34.3 | 24 | 1.34.3 | 1.32.0 |
| v2.31.0   | 1.33, 1.34, 1.35 | 1.33.0–1.33.11, 1.34.0–1.34.7, 1.35.0–1.35.4 | 25 | 1.35.4 | 1.33.0 |

Notes:

- The window advances by one minor per Kubespray minor release; the oldest minor
  is dropped and a new one added (1.31 present in v2.29.0, dropped in v2.30.0).
- A patch release keeps the same minor window as its parent but refreshes patch
  versions and the default (v2.29.1 stays on 1.31–1.33 but adds newer patches and
  bumps the default to 1.33.7).
- No explicit upper bound is asserted; a version without a checksum fails during
  download.
- CI: the inventories under `tests/files/` do not pin `kube_version`, so CI
  exercises the per-tag default.

## Compatibility

- Kubespray `v2.27.0`: default `1.31.4`, minimum `1.29.0` (minor lines 1.29–1.31).
- Kubespray `v2.27.1`: default `1.31.9`, minimum `1.29.0`.
- Kubespray `v2.28.0`: default `1.32.5` (minor lines 1.30–1.32); **remove the leading `v`
  from `kube_version`** from this release on.
- Kubespray `v2.28.1`: default `1.32.8`.
- Kubespray `v2.29.0`: `>=1.31.0 <=1.33.5`, default `1.33.5`.
- Kubespray `v2.29.1`: `>=1.31.0 <=1.33.7`, default `1.33.7`.
- Kubespray `v2.30.0`: `>=1.32.0 <=1.34.3`, default `1.34.3`.
- Kubespray `v2.31.0`: `>=1.33.0 <=1.35.4`, default `1.35.4`.
- Below the per-tag minimum: rejected by inventory validation.

## References

- `roles/kubespray_defaults/vars/main/checksums.yml` (`kubelet_checksums`) —
  v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`
- `roles/kubespray_defaults/defaults/main/main.yml:25,28`
- `roles/validate_inventory/tasks/main.yml` (version assert)
- `tests/files/` (no `kube_version` override → default is tested)
