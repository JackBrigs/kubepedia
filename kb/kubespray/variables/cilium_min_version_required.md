---
id: VARIABLE-CILIUM_MIN_VERSION_REQUIRED
type: variable
title: cilium_min_version_required
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_min_version_required
tags:
  - cilium
  - cni
  - version
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Default cilium_min_version_required: \"1.15\""
relations: []
---

# cilium_min_version_required

## Summary
Declares the minimum Cilium version supported by the role. Default `"1.15"`. Used to guard against deploying an unsupported Cilium version.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_min_version_required: "1.15"` (line 2). The default value `"1.15"` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. This variable is not exposed in the sample inventory `k8s-net-cilium.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variable: `cilium_version`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
