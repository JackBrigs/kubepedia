---
id: VARIABLE-ETCD_NODE_CERT_HOSTS
type: variable
title: etcd_node_cert_hosts
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_node_cert_hosts
tags:
  - etcd
  - certificates
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Hosts that receive etcd node client certificates; default all k8s_cluster members"
relations: []
---

# etcd_node_cert_hosts

## Summary
List of hosts that receive etcd node (client) certificates. Defaults to all members of the `k8s_cluster` group.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as:

```yaml
etcd_node_cert_hosts: "{{ groups['k8s_cluster'] }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0 (present in every tag inspected). Depends on the inventory group `k8s_cluster`.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
