---
id: VARIABLE-CILIUM_PREALLOCATE_BPF_MAPS
type: variable
title: cilium_preallocate_bpf_maps
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_preallocate_bpf_maps
tags:
  - cilium
  - bpf
  - performance
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_preallocate_bpf_maps, default false"
relations: []
---

# cilium_preallocate_bpf_maps

## Summary
Controls whether Cilium pre-allocates BPF map memory. When `true`, maps are pre-allocated for lower per-packet latency at the cost of higher memory use. Default is `false`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_preallocate_bpf_maps: false
```

The default value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when `kube_network_plugin: cilium`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
