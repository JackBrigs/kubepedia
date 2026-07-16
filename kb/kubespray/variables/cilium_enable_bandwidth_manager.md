---
id: VARIABLE-CILIUM_ENABLE_BANDWIDTH_MANAGER
type: variable
title: cilium_enable_bandwidth_manager
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_enable_bandwidth_manager
tags:
  - cilium
  - network
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_enable_bandwidth_manager: false"
relations: []
---

# cilium_enable_bandwidth_manager

## Summary
Enables Cilium's Bandwidth Manager, which provides pod egress rate limiting via the `kubernetes.io/egress-bandwidth` annotation. Default: `false`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_enable_bandwidth_manager: false
```

The value is a literal `false` and is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 120 in v2.29.0/v2.29.1, line 118 in v2.30.0, line 103 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0 (Cilium CNI only). Related: `cilium_enable_bandwidth_manager_bbr`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
