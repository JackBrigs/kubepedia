---
id: VARIABLE-CILIUM_EXTRA_VALUES
type: variable
title: cilium_extra_values
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_extra_values
tags:
  - cilium
  - helm
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_extra_values, default {}"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_extra_values

## Summary
A user-supplied mapping of additional values merged into the Cilium configuration, allowing overrides not exposed by dedicated variables. Default is an empty dict `{}`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_extra_values: {}
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0-v2.31.0 when `kube_network_plugin: cilium`. Used to inject extra Cilium settings beyond the built-in variables.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
