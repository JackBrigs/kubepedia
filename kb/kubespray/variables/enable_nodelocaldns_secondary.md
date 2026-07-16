---
id: VARIABLE-ENABLE_NODELOCALDNS_SECONDARY
type: variable
title: enable_nodelocaldns_secondary
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - enable_nodelocaldns_secondary
tags:
  - dns
  - nodelocaldns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Enables a secondary NodeLocal DNSCache instance; default false"
relations: []
---

# enable_nodelocaldns_secondary

## Summary
Toggles deployment of a second NodeLocal DNSCache instance for high availability of the node-local DNS cache. Default is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:
```yaml
enable_nodelocaldns_secondary: false
```
Also exposed as `false` in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. The default value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Only meaningful when `enable_nodelocaldns` is `true`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
