---
id: VARIABLE-SYSTEM_RESERVED_CGROUPS_FOR_SERVICE_SLICE
type: variable
title: system_reserved_cgroups_for_service_slice
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - system_reserved_cgroups_for_service_slice
tags:
  - kubelet
  - cgroups
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "systemd slice name used to build the system-reserved cgroup path: system.slice"
relations: []
---

# system_reserved_cgroups_for_service_slice

## Summary
Name of the systemd slice used to construct the system-reserved cgroup path (`system_reserved_cgroups`). Default is `system.slice`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `system_reserved_cgroups_for_service_slice: system.slice`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (all at line 49). The sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` shows the same commented value.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `system_reserved_cgroups` to form the `--system-reserved-cgroup` path. Takes effect only when `system_reserved: true`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
