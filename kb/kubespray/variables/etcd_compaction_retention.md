---
id: VARIABLE-ETCD_COMPACTION_RETENTION
type: variable
title: etcd_compaction_retention
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_compaction_retention
tags:
  - etcd
  - tuning
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "etcd history compaction retention; default '8'"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_compaction_retention

## Summary
Controls etcd's history compaction retention setting. Default is the string `"8"`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as `etcd_compaction_retention: "8"` (line 74 in v2.29.0/v2.29.1, line 73 in v2.30.0/v2.31.0). Also mirrored in `roles/kubernetes/control-plane/defaults/main/etcd.yml:29` as `etcd_compaction_retention: "8"`. The default `"8"` is **unchanged across v2.29.0-v2.31.0**.

## Compatibility
Kubespray v2.29.0-v2.31.0. Related etcd tuning variables in the same defaults files.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/kubernetes/control-plane/defaults/main/etcd.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
