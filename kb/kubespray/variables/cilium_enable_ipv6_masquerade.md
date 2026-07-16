---
id: VARIABLE-CILIUM_ENABLE_IPV6_MASQUERADE
type: variable
title: cilium_enable_ipv6_masquerade
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_enable_ipv6_masquerade
tags:
  - cilium
  - masquerade
  - ipv6
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_enable_ipv6_masquerade: true"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_enable_ipv6_masquerade

## Summary
Controls whether Cilium masquerades IPv6 traffic leaving the cluster to the node's IP. Default: `true`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_enable_ipv6_masquerade: true
```

The value is a literal `true` and is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 286 in v2.29.0/v2.29.1, line 284 in v2.30.0, line 269 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0 (Cilium CNI only). Related: `cilium_enable_ipv4_masquerade`, `cilium_enable_bpf_masquerade`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
