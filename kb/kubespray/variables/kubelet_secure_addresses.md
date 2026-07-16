---
id: VARIABLE-KUBELET_SECURE_ADDRESSES
type: variable
title: kubelet_secure_addresses
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_secure_addresses
tags:
  - kubelet
  - network
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "List of secure IPs for kubelet; default localhost link-local + pod subnets + node addresses"
relations: []
---

# kubelet_secure_addresses

## Summary
Defines the list of IP addresses considered secure for kubelet. Default:
`"localhost link-local {{ kube_pods_subnets | regex_replace(',', ' ') }} {{ kube_node_addresses }}"`, combining localhost, link-local, the pod subnets, and the computed `kube_node_addresses` of all cluster and etcd hosts.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_secure_addresses: "localhost link-local {{ kube_pods_subnets | regex_replace(',', ' ') }} {{ kube_node_addresses }}"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 36 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kube_pods_subnets` and the computed `kube_node_addresses` (which iterates over `k8s_cluster` and `etcd` host groups).

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
