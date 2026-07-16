---
id: VARIABLE-SYSTEM_MEMORY_RESERVED
type: variable
title: system_memory_reserved
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - system_memory_reserved
tags:
  - kubelet
  - node
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines the default memory reserved for the system: \"512Mi\""
relations: []
---

# system_memory_reserved

## Summary
Amount of memory reserved for the operating system and system daemons on Kubernetes nodes, applied to the kubelet `--system-reserved` allocatable calculation when `system_reserved` is enabled. Default is `"512Mi"`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `system_memory_reserved: "512Mi"`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (all at line 51). The sample inventory `inventory/sample/group_vars/k8s_cluster/kube_control_plane.yml` overrides it with a commented `256Mi` for control plane nodes and `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` shows a commented `512Mi`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Takes effect only when `system_reserved: true`. Related: `system_pid_reserved`, `system_reserved_cgroups`, `system_reserved`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
