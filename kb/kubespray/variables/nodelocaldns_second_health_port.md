---
id: VARIABLE-NODELOCALDNS_SECOND_HEALTH_PORT
type: variable
title: nodelocaldns_second_health_port
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nodelocaldns_second_health_port
tags:
  - dns
  - nodelocaldns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Health-check port for the secondary nodelocaldns instance; default 9256"
relations: []
---

# nodelocaldns_second_health_port

## Summary
Health-check port used by the secondary nodelocaldns instance (deployed when `enable_nodelocaldns_secondary` is true). Default is `9256`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `nodelocaldns_second_health_port: 9256`. Value is unchanged across v2.29.0-v2.31.0 (line number only shifts). The sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` carries the same default.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant when `enable_nodelocaldns_secondary: true`. Related: `enable_nodelocaldns_secondary`, `nodelocaldns_ip`, `nodelocaldns_secondary_skew_seconds`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
