---
id: VARIABLE-CILIUM_BPF_MAP_DYNAMIC_SIZE_RATIO
type: variable
title: cilium_bpf_map_dynamic_size_ratio
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_bpf_map_dynamic_size_ratio
tags:
  - cilium
  - cni
  - bpf
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Ratio of memory used to auto-size Cilium BPF maps; default \"0.0025\""
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_bpf_map_dynamic_size_ratio

## Summary
Sets the fraction of total system memory Cilium uses to dynamically size its BPF maps (`bpf-map-dynamic-size-ratio`). Defaults to `"0.0025"` (a quoted string).

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_bpf_map_dynamic_size_ratio: "0.0025"
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number shifts: 279 in v2.29.0/v2.29.1, 277 in v2.30.0, 262 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Cilium CNI only.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
