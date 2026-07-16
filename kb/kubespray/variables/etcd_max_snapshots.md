---
id: VARIABLE-ETCD_MAX_SNAPSHOTS
type: variable
title: etcd_max_snapshots
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_max_snapshots
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Maximum number of etcd snapshot files to retain; default 5"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_max_snapshots

## Summary
Sets etcd's `--max-snapshots` flag, i.e. the maximum number of snapshot files to retain. Default is `5`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as:

```yaml
etcd_max_snapshots: 5
```

The value `5` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0 (present in every tag inspected). Related etcd retention variable: `etcd_max_wals`.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
