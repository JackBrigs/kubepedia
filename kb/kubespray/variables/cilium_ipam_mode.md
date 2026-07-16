---
id: VARIABLE-CILIUM_IPAM_MODE
type: variable
title: cilium_ipam_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_ipam_mode
tags:
  - cilium
  - ipam
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Cilium IPAM mode; default cluster-pool"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_ipam_mode

## Summary
Selects Cilium's IP Address Management mode (`ipam.mode`). Default: `cluster-pool`. The sample inventory shows a commented alternative `kubernetes`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_ipam_mode: cluster-pool
```

Consumed in `roles/network_plugin/cilium/templates/values.yaml.j2` (`ipam.mode: {{ cilium_ipam_mode }}`). Exposed (commented) in `inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml` as `# cilium_ipam_mode: kubernetes`, and documented in `docs/CNI/cilium.md`. The role default `cluster-pool` is unchanged across v2.29.0-v2.31.0 (only line numbers shift between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_pool_cidr`, `cilium_pool_mask_size`, `kube_network_plugin`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- roles/network_plugin/cilium/templates/values.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
