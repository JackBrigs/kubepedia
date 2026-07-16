---
id: VARIABLE-CILIUM_ENCRYPTION_TYPE
type: variable
title: cilium_encryption_type
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_encryption_type
tags:
  - cilium
  - encryption
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_encryption_type, default \"ipsec\""
relations: []
---

# cilium_encryption_type

## Summary
Selects the transparent encryption backend used by Cilium. Default is `"ipsec"` (the alternative is WireGuard).

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_encryption_type: "ipsec"
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0-v2.31.0 when `kube_network_plugin: cilium` and `cilium_encryption_enabled: true`. Related to `cilium_encryption_node_encryption`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
