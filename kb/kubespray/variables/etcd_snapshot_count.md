---
id: VARIABLE-ETCD_SNAPSHOT_COUNT
type: variable
title: etcd_snapshot_count
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_snapshot_count
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Number of committed transactions between etcd snapshots; default \"100000\""
relations: []
---

# etcd_snapshot_count

## Summary
Number of committed transactions to trigger an etcd snapshot to disk. Default is the string `"100000"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `etcd_snapshot_count: "100000"` (line 711 in v2.29.0/v2.29.1, line 714 in v2.30.0, line 733 in v2.31.0). The value `"100000"` is unchanged across v2.29.0-v2.31.0; only the line number shifted.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
