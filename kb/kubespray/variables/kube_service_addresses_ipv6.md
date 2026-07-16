---
id: VARIABLE-KUBE_SERVICE_ADDRESSES_IPV6
type: variable
title: kube_service_addresses_ipv6
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_service_addresses_ipv6
tags:
  - networking
  - ipv6
  - services
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kube_service_addresses_ipv6, default fd85:ee78:d8a6:8607::1000/116"
relations:
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# kube_service_addresses_ipv6

## Summary
IPv6 CIDR from which Kubernetes assigns Service ClusterIP addresses in dual-stack or IPv6-only clusters. Defaults to `fd85:ee78:d8a6:8607::1000/116`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` and mirrored in the sample inventory (`inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`):

```yaml
kube_service_addresses_ipv6: fd85:ee78:d8a6:8607::1000/116
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Line numbers shift between tags (role defaults: 265 in v2.29.0/v2.29.1, 266 in v2.30.0, 278 in v2.31.0) but the value is identical.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related: `kube_service_addresses`, `kube_service_subnets`, `ipv6_stack`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
