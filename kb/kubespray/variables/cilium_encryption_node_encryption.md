---
id: VARIABLE-CILIUM_ENCRYPTION_NODE_ENCRYPTION
type: variable
title: cilium_encryption_node_encryption
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_encryption_node_encryption
tags:
  - cilium
  - encryption
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_encryption_node_encryption, default false"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_encryption_node_encryption

## Summary
Controls whether Cilium also encrypts node-to-node (host-level) traffic in addition to pod traffic. Default is `false`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_encryption_node_encryption: false
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0-v2.31.0 when `kube_network_plugin: cilium` and `cilium_encryption_enabled: true`. Related to `cilium_encryption_type`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
