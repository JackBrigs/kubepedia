---
id: VARIABLE-CILIUM_ENABLE_HUBBLE_UI
type: variable
title: cilium_enable_hubble_ui
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_enable_hubble_ui
tags:
  - cilium
  - hubble
  - observability
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_enable_hubble_ui, defaults to cilium_enable_hubble"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_enable_hubble_ui

## Summary
Controls whether the Cilium Hubble UI (web observability dashboard) is deployed. Default: the value of `cilium_enable_hubble` (itself `false` by default).

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as a computed default:

```yaml
cilium_enable_hubble_ui: "{{ cilium_enable_hubble }}"
```

`cilium_enable_hubble` defaults to `false`, so the effective default is `false`. The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 152 in v2.29.0/v2.29.1, line 150 in v2.30.0, line 135 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0 (Cilium CNI only). Related: `cilium_enable_hubble`, `cilium_enable_hubble_metrics`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
