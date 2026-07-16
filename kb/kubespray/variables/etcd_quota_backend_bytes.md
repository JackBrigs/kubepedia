---
id: VARIABLE-ETCD_QUOTA_BACKEND_BYTES
type: variable
title: etcd_quota_backend_bytes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_quota_backend_bytes
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "etcd backend storage quota in bytes; default \"2147483648\" (2 GiB)"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_quota_backend_bytes

## Summary
Sets etcd's `--quota-backend-bytes`, the maximum size of the etcd backend database. Default is `"2147483648"` (2 GiB).

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as:

```yaml
etcd_quota_backend_bytes: "2147483648"
```

The same default is present, commented out, in `roles/kubernetes/control-plane/defaults/main/etcd.yml` (`# etcd_quota_backend_bytes: "2147483648"`). The active value `"2147483648"` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0 (present in every tag inspected).

## References
- roles/etcd_defaults/defaults/main.yml
- roles/kubernetes/control-plane/defaults/main/etcd.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
