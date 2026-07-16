---
id: VARIABLE-ETCD_EVENTS_CLUSTER_ENABLED
type: variable
title: etcd_events_cluster_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_events_cluster_enabled
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Defines etcd_events_cluster_enabled, default false (separate etcd for k8s events)"
relations: []
---

# etcd_events_cluster_enabled

## Summary
When set to `true`, Kubernetes events are stored in a separate etcd cluster
(etcd-events) instead of the main etcd cluster. Default is `false`.

## Implementation
Defined as `etcd_events_cluster_enabled: false` in
`roles/etcd_defaults/defaults/main.yml` (commented "Set to true to separate k8s
events to a different etcd cluster") and also in
`roles/kubespray_defaults/defaults/main/main.yml`, both with value `false`. The
default is unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Drives `etcd_events_cluster_setup` in the
`cluster.yml` and `upgrade_cluster.yml` playbooks. Related:
`etcd_events_cluster_setup`, `etcd_events_data_dir`.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
