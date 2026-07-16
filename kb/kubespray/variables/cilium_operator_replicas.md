---
id: VARIABLE-CILIUM_OPERATOR_REPLICAS
type: variable
title: cilium_operator_replicas
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_operator_replicas
tags:
  - cilium
  - cni
  - operator
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_operator_replicas, default 2"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_operator_replicas

## Summary
Number of Cilium operator replicas to run. Default is `2`, providing a highly available operator deployment.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_operator_replicas: 2
```

The default value `2` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when `kube_network_plugin: cilium`. Related operator variables: `cilium_operator_tolerations`, `cilium_operator_extra_args`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
