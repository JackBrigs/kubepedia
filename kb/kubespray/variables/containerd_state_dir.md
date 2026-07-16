---
id: VARIABLE-CONTAINERD_STATE_DIR
type: variable
title: containerd_state_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_state_dir
tags:
  - containerd
  - container-runtime
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Runtime state directory for containerd, default /run/containerd"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_state_dir

## Summary
Runtime (ephemeral) state directory for containerd. Default value: `/run/containerd`.

## Implementation
Defined identically in two places (same value):
- `roles/container-engine/containerd/defaults/main.yml`: `containerd_state_dir: "/run/containerd"`
- `roles/kubespray_defaults/defaults/main/main.yml`: `containerd_state_dir: "/run/containerd"`

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only line numbers shift between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when containerd is the container runtime. Related: `containerd_storage_dir`, `containerd_cfg_dir`, `containerd_systemd_dir`.

## References
- roles/container-engine/containerd/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
