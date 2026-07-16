---
id: VARIABLE-CILIUM_ENABLE_IPV4
type: variable
title: cilium_enable_ipv4
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_enable_ipv4
tags:
  - cilium
  - ipv4
  - network
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_enable_ipv4, defaults to ipv4_stack"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_enable_ipv4

## Summary
Enables the IPv4 address family in Cilium. Default: the value of `ipv4_stack` (which itself defaults to `true`).

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as a computed default:

```yaml
cilium_enable_ipv4: "{{ ipv4_stack }}"
```

`ipv4_stack` is defined in `roles/kubespray_defaults/defaults/main/main.yml` as `true`, so the effective default is `true`. The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 10 in v2.29.0/v2.29.1, line 8 in v2.30.0/v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0 (Cilium CNI only). Related: `cilium_enable_ipv6`, `ipv4_stack`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml (ipv4_stack)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
