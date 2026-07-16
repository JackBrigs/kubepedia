---
id: VARIABLE-ETCD_EVENTS_DATA_DIR
type: variable
title: etcd_events_data_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_events_data_dir
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines etcd_events_data_dir, default /var/lib/etcd-events"
relations: []
---

# etcd_events_data_dir

## Summary
Filesystem directory where the etcd-events cluster stores its data. Default is
`/var/lib/etcd-events`.

## Implementation
Defined as `etcd_events_data_dir: "/var/lib/etcd-events"` in
`roles/kubespray_defaults/defaults/main/main.yml`. This is the events-cluster
counterpart of the main etcd data directory. The value is unchanged across
v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when
`etcd_events_cluster_enabled` is `true`. Related: `etcd_events_cluster_enabled`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
