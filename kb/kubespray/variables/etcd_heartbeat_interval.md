---
id: VARIABLE-ETCD_HEARTBEAT_INTERVAL
type: variable
title: etcd_heartbeat_interval
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_heartbeat_interval
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Defines default etcd_heartbeat_interval: \"250\" (milliseconds)"
relations: []
---

# etcd_heartbeat_interval

## Summary
Sets the etcd leader heartbeat interval in milliseconds. Default is `"250"`. Applied both to standalone etcd and to the kubeadm-managed etcd.

## Implementation
Defined as `etcd_heartbeat_interval: "250"` in `roles/etcd_defaults/defaults/main.yml` (and repeated with the same `"250"` value in `roles/kubernetes/control-plane/defaults/main/etcd.yml` and `roles/kubespray_defaults/defaults/main/main.yml`). Consumed as `ETCD_HEARTBEAT_INTERVAL` in `roles/etcd/templates/etcd.env.j2` and `etcd-events.env.j2`, and as the `heartbeat-interval` extra arg in the kubeadm-config templates. The default `"250"` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related: `etcd_max_request_bytes`, `etcd_log_level`, `etcd_extra_vars`.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/etcd/templates/etcd.env.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
