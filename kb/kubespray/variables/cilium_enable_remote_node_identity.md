---
id: VARIABLE-CILIUM_ENABLE_REMOTE_NODE_IDENTITY
type: variable
title: cilium_enable_remote_node_identity
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_enable_remote_node_identity
tags:
  - cilium
  - identity
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_enable_remote_node_identity, default true"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_enable_remote_node_identity

## Summary
Enables the Cilium remote-node identity, which assigns a dedicated security identity to remote cluster nodes. Default is `true`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_enable_remote_node_identity: true
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0-v2.31.0 when `kube_network_plugin: cilium`. Related to Cilium node security identities.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
