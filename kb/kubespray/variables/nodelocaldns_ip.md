---
id: VARIABLE-NODELOCALDNS_IP
type: variable
title: nodelocaldns_ip
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nodelocaldns_ip
tags:
  - dns
  - nodelocaldns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines the link-local IP the nodelocaldns cache listens on; default 169.254.25.10"
relations: []
---

# nodelocaldns_ip

## Summary
Link-local IP address on which the nodelocaldns DNS cache listens on each node. Default is `169.254.25.10`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `nodelocaldns_ip: 169.254.25.10`. The value is unchanged across v2.29.0-v2.31.0 (only the line number shifts). The sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` carries the same default.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when `enable_nodelocaldns: true`. Related: `enable_nodelocaldns`, `nodelocaldns_second_health_port`, `nodelocaldns_version`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
