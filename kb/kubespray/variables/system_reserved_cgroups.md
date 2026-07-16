---
id: VARIABLE-SYSTEM_RESERVED_CGROUPS
type: variable
title: system_reserved_cgroups
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - system_reserved_cgroups
tags:
  - kubelet
  - cgroups
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Cgroup path for system-reserved resources, computed from system_reserved_cgroups_for_service_slice"
relations: []
---

# system_reserved_cgroups

## Summary
Cgroup path passed to the kubelet `--system-reserved-cgroup` flag identifying where system-reserved resources are enforced. Default is computed as `"/{{ system_reserved_cgroups_for_service_slice }}"` (i.e. `/system.slice`).

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `system_reserved_cgroups: "/{{ system_reserved_cgroups_for_service_slice }}"`. The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (all at line 50). The sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` shows the same commented expression.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Takes effect only when `system_reserved: true`. Derived from `system_reserved_cgroups_for_service_slice` (default `system.slice`).

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
