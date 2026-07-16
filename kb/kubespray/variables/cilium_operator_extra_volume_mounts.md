---
id: VARIABLE-CILIUM_OPERATOR_EXTRA_VOLUME_MOUNTS
type: variable
title: cilium_operator_extra_volume_mounts
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_operator_extra_volume_mounts
tags:
  - cilium
  - cni
  - operator
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_operator_extra_volume_mounts, default empty list []"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_operator_extra_volume_mounts

## Summary
Extra volume mounts added to the Cilium operator container. Default is an empty list (`[]`), so no additional volume mounts are configured.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_operator_extra_volume_mounts: []
```

The default value `[]` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when `kube_network_plugin: cilium`. Typically paired with `cilium_operator_extra_volumes` to mount volumes declared there.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
