---
id: VARIABLE-CILIUM_ENABLE_HOST_FIREWALL
type: variable
title: cilium_enable_host_firewall
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_enable_host_firewall
tags:
  - cilium
  - firewall
  - network
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_enable_host_firewall: false"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_enable_host_firewall

## Summary
Enables Cilium's Host Firewall feature, which allows applying CiliumClusterwideNetworkPolicy to host-namespace traffic on nodes. Default: `false`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_enable_host_firewall: false
```

The value is a literal `false` and is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 360 in v2.29.0/v2.29.1, line 358 in v2.30.0, line 340 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0 (Cilium CNI only).

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
