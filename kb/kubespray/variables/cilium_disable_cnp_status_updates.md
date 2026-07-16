---
id: VARIABLE-CILIUM_DISABLE_CNP_STATUS_UPDATES
type: variable
title: cilium_disable_cnp_status_updates
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_disable_cnp_status_updates
tags:
  - cilium
  - cni
  - policy
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Disables CiliumNetworkPolicy status updates; default true"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_disable_cnp_status_updates

## Summary
Controls whether Cilium disables status updates on CiliumNetworkPolicy (CNP) objects. Disabling these updates reduces load on the Kubernetes API server. Default is `true`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_disable_cnp_status_updates: true`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Applies only when Cilium is the selected CNI.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
