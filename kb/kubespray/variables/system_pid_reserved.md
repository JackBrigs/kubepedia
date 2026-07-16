---
id: VARIABLE-SYSTEM_PID_RESERVED
type: variable
title: system_pid_reserved
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - system_pid_reserved
tags:
  - kubelet
  - node
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines the default number of PIDs reserved for the system: 1000"
relations: []
---

# system_pid_reserved

## Summary
Number of process IDs reserved for the operating system and system daemons, applied to the kubelet `--system-reserved` allocatable calculation when `system_reserved` is enabled. Default is `1000`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `system_pid_reserved: 1000`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (all at line 54). The sample inventory `inventory/sample/group_vars/k8s_cluster/kube_control_plane.yml` shows a commented example `system_pid_reserved: "1000"`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Takes effect only when `system_reserved: true`. Related: `system_memory_reserved`, `system_reserved_cgroups`, `system_reserved`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
