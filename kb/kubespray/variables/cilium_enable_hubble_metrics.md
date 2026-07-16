---
id: VARIABLE-CILIUM_ENABLE_HUBBLE_METRICS
type: variable
title: cilium_enable_hubble_metrics
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_enable_hubble_metrics
tags:
  - cilium
  - hubble
  - observability
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_enable_hubble_metrics: false"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_enable_hubble_metrics

## Summary
Controls whether Cilium Hubble exports Prometheus metrics. Default: `false`. When `true`, the specific metric sets are listed via the accompanying `cilium_hubble_metrics` variable.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_enable_hubble_metrics: false
```

The value is a literal `false` and is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 154 in v2.29.0/v2.29.1, line 152 in v2.30.0, line 137 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0 (Cilium CNI only). Related: `cilium_enable_hubble`, `cilium_enable_hubble_ui`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
