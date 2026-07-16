---
id: VARIABLE-ENABLE_NODELOCALDNS
type: variable
title: enable_nodelocaldns
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - enable_nodelocaldns
tags:
  - dns
  - nodelocaldns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Enables the NodeLocal DNSCache; default true"
relations: []
---

# enable_nodelocaldns

## Summary
Toggles deployment of NodeLocal DNSCache, a per-node DNS caching agent that reduces latency and load on the cluster CoreDNS. Default is `true`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:
```yaml
enable_nodelocaldns: true
```
Also exposed as `true` in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. The default value `true` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `enable_nodelocaldns_secondary`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
