---
id: VARIABLE-CILIUM_DEBUG
type: variable
title: cilium_debug
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_debug
tags:
  - cilium
  - cni
  - debug
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Enables Cilium debug logging; default false"
relations: []
---

# cilium_debug

## Summary
Toggles Cilium's debug logging (the `debug` option in the Cilium ConfigMap). When set to `true`, the Cilium agent emits verbose debug-level logs. Default is `false`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_debug: false`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Applies only when Cilium is the selected CNI (`kube_network_plugin: cilium`).

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
