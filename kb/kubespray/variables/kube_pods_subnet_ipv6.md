---
id: VARIABLE-KUBE_PODS_SUBNET_IPV6
type: variable
title: kube_pods_subnet_ipv6
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_pods_subnet_ipv6
tags:
  - networking
  - ipv6
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "IPv6 pod CIDR; defaults to fd85:ee78:d8a6:8607::1:0000/112."
relations: []
---

# kube_pods_subnet_ipv6

## Summary
The IPv6 subnet (CIDR) from which pod addresses are allocated in dual-stack or IPv6-only clusters. Defaults to `fd85:ee78:d8a6:8607::1:0000/112`. Used together with the IPv4 `kube_pods_subnet` to build `kube_pods_subnets` for the active network stack.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
kube_pods_subnet_ipv6: fd85:ee78:d8a6:8607::1:0000/112
```

The same value is also surfaced in the sample inventory at `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (role-default line 271 in v2.29.x, 272 in v2.30.0, 284 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_pods_subnet`, `kube_pods_subnets`, `ipv6_stack`, `ipv4_stack`, and `kube_network_node_prefix`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
