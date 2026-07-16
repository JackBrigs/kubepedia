---
id: VARIABLE-CILIUM_CONFIG_EXTRA_VARS
type: variable
title: cilium_config_extra_vars
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_config_extra_vars
tags:
  - cilium
  - cni
  - configmap
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Extra key/value entries merged into the Cilium ConfigMap; default {}"
relations: []
---

# cilium_config_extra_vars

## Summary
A dictionary of arbitrary extra key/value entries merged into the Cilium ConfigMap, allowing users to set Cilium options not otherwise exposed by Kubespray. Default is an empty mapping `{}`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_config_extra_vars: {}`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Applies only when Cilium is the selected CNI.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
