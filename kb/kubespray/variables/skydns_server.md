---
id: VARIABLE-SKYDNS_SERVER
type: variable
title: skydns_server
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - skydns_server
tags:
  - dns
  - network
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computes the cluster DNS service IP (3rd address of the first service subnet)"
relations: []
---

# skydns_server

## Summary
The cluster DNS service IP address, computed as the 3rd usable address of the first Kubernetes service subnet. Default `"{{ kube_service_subnets.split(',') | first | ansible.utils.ipaddr('net') | ansible.utils.ipaddr(3) | ansible.utils.ipaddr('address') }}"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
skydns_server: "{{ kube_service_subnets.split(',') | first | ansible.utils.ipaddr('net') | ansible.utils.ipaddr(3) | ansible.utils.ipaddr('address') }}"
```

The expression is unchanged across v2.29.0-v2.31.0 (line 154 in v2.29.0/v2.29.1, 155 in v2.30.0, 152 in v2.31.0). The same value also appears in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` (line 213 in v2.29.0/v2.29.1, 214 in v2.30.0, 229 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Derived from `kube_service_subnets` using the `ansible.utils.ipaddr` filters.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
