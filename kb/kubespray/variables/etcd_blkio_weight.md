---
id: VARIABLE-ETCD_BLKIO_WEIGHT
type: variable
title: etcd_blkio_weight
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_blkio_weight
tags:
  - etcd
  - resources
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Block IO weight for the etcd container/process; default 1000"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_blkio_weight

## Summary
Sets the block IO weight applied to etcd. Default is `1000`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as `etcd_blkio_weight: 1000` (line 69 in v2.29.0/v2.29.1, line 68 in v2.30.0/v2.31.0). The default value `1000` is **unchanged across v2.29.0-v2.31.0**; only the line number shifted.

## Compatibility
Kubespray v2.29.0-v2.31.0. Related etcd resource/tuning variables live in the same `etcd_defaults` defaults file.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
