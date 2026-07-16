---
id: VARIABLE-KUBE_NODE_ADDRESSES
type: variable
title: kube_node_addresses
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_node_addresses
tags:
  - kubelet
  - networking
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Computes the space-separated list of node IPs for kubelet secure addresses"
relations: []
---

# kube_node_addresses

## Summary
Computed space-separated list of the primary IP addresses of all cluster nodes (the union of the `k8s_cluster` and `etcd` host groups). It is used to build `kubelet_secure_addresses`, the list of IPs kubelet treats as secure. Includes IPv6 addresses for dual-stack because `main_ips` is collected per host.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kube_node_addresses: >-
  {%- for host in (groups['k8s_cluster'] | union(groups['etcd'])) -%}
    {{ hostvars[host]['main_ips'] | join(' ') }}{{ ' ' if not loop.last else '' }}
  {%- endfor -%}
```

It iterates over the union of `groups['k8s_cluster']` and `groups['etcd']` and joins each host's `main_ips`. The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `kubelet_secure_addresses`. Depends on the per-host fact `main_ips` and the `k8s_cluster` / `etcd` inventory groups.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
