---
id: VARIABLE-CONTAINERD_STORAGE_DIR
type: variable
title: containerd_storage_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_storage_dir
tags:
  - containerd
  - container-runtime
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Persistent storage/root directory for containerd, default /var/lib/containerd"
relations: []
---

# containerd_storage_dir

## Summary
Persistent storage (root) directory for containerd where images and container data are kept. Default value: `/var/lib/containerd`.

## Implementation
Defined identically in two places (same value):
- `roles/container-engine/containerd/defaults/main.yml`: `containerd_storage_dir: "/var/lib/containerd"`
- `roles/kubespray_defaults/defaults/main/main.yml`: `containerd_storage_dir: "/var/lib/containerd"`

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only line numbers shift between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when containerd is the container runtime. Related: `containerd_state_dir`, `containerd_cfg_dir`, `containerd_systemd_dir`.

## References
- roles/container-engine/containerd/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
