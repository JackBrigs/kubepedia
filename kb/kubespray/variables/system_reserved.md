---
id: VARIABLE-SYSTEM_RESERVED
type: variable
title: system_reserved
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - system_reserved
tags:
  - kubelet
  - node
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Toggles reserving resources for the system: false"
relations: []
---

# system_reserved

## Summary
Boolean toggle that enables reserving compute resources (memory, PIDs) for the operating system and system daemons via the kubelet `--system-reserved` flag and `--system-reserved-cgroup`. Default is `false` (disabled).

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `system_reserved: false`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (all at line 48). The sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` shows a commented example `system_reserved: true`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. When enabled, the associated `system_memory_reserved`, `system_pid_reserved`, `system_reserved_cgroups`, and `system_reserved_cgroups_for_service_slice` values take effect.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
