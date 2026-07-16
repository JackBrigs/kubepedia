---
id: VARIABLE-KUBE_NETWORK_NODE_PREFIX_IPV6
type: variable
title: kube_network_node_prefix_ipv6
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_network_node_prefix_ipv6
tags:
  - networking
  - ipv6
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kube_network_node_prefix_ipv6 default 120"
relations: []
---

# kube_network_node_prefix_ipv6

## Summary
Length of the per-node IPv6 subnet prefix carved out of the IPv6 pods subnet (dual-stack / IPv6 clusters). Default is `120`, giving each node a /120 block of pod IPv6 addresses.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_network_node_prefix_ipv6: 120
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. It is also exposed (uncommented, same value) in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only for IPv6/dual-stack clusters. Related variables: `kube_network_node_prefix`, `kube_pods_subnet_ipv6`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
