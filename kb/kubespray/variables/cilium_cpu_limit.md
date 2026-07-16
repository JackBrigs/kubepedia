---
id: VARIABLE-CILIUM_CPU_LIMIT
type: variable
title: cilium_cpu_limit
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_cpu_limit
tags:
  - cilium
  - cni
  - resources
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "CPU resource limit for the Cilium agent; default 500m"
relations: []
---

# cilium_cpu_limit

## Summary
Sets the CPU resource limit for the Cilium agent DaemonSet pods. Default is `500m`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_cpu_limit: 500m`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Applies only when Cilium is the selected CNI. Related: `cilium_cpu_requests`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
