---
id: VARIABLE-CILIUM_CGROUP_HOST_ROOT
type: variable
title: cilium_cgroup_host_root
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_cgroup_host_root
tags:
  - cilium
  - cni
  - cgroup
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Host path where Cilium mounts the cgroup v2 filesystem; default /run/cilium/cgroupv2"
relations: []
---

# cilium_cgroup_host_root

## Summary
Host path where Cilium mounts the cgroup v2 filesystem. Default is `/run/cilium/cgroupv2`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_cgroup_host_root: "/run/cilium/cgroupv2"`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Applies only when Cilium is the selected CNI. Related: `cilium_cgroup_auto_mount`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
