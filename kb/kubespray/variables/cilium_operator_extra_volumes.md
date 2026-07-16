---
id: VARIABLE-CILIUM_OPERATOR_EXTRA_VOLUMES
type: variable
title: cilium_operator_extra_volumes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_operator_extra_volumes
tags:
  - cilium
  - cni
  - operator
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_operator_extra_volumes, default empty list []"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_operator_extra_volumes

## Summary
Extra volumes exposed to the Cilium operator pod. Default is an empty list (`[]`), so no additional volumes are defined.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_operator_extra_volumes: []
```

The default value `[]` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when `kube_network_plugin: cilium`. Usually combined with `cilium_operator_extra_volume_mounts` to mount the volumes into the operator container.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
