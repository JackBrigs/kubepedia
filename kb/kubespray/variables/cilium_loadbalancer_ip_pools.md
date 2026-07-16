---
id: VARIABLE-CILIUM_LOADBALANCER_IP_POOLS
type: variable
title: cilium_loadbalancer_ip_pools
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_loadbalancer_ip_pools
tags:
  - cilium
  - loadbalancer
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "List of CiliumLoadBalancerIPPool definitions; default empty list"
relations: []
---

# cilium_loadbalancer_ip_pools

## Summary
A list of `CiliumLoadBalancerIPPool` definitions to be applied to the cluster. Default: `[]` (empty). When non-empty, Kubespray renders and applies the pool manifests.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_loadbalancer_ip_pools: []
```

Consumed in `roles/network_plugin/cilium/tasks/apply.yml` (guarded by `cilium_loadbalancer_ip_pools is defined and (cilium_loadbalancer_ip_pools|length>0)`) which renders `roles/network_plugin/cilium/templates/cilium/cilium-loadbalancer-ip-pool.yml.j2` (iterating over the list). Exposed (commented) in `inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml` and documented in `docs/CNI/cilium.md`. The default `[]` is unchanged across v2.29.0-v2.31.0 (only line numbers shift between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_loadbalancer_mode`, `cilium_l2announcements`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- roles/network_plugin/cilium/tasks/apply.yml
- roles/network_plugin/cilium/templates/cilium/cilium-loadbalancer-ip-pool.yml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
