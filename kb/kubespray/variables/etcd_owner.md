---
id: VARIABLE-ETCD_OWNER
type: variable
title: etcd_owner
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_owner
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "OS user owning etcd files/certificates; default \"etcd\""
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_owner

## Summary
OS user that owns etcd certificates and related files. Default is `etcd`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml`:

```yaml
etcd_owner: etcd
```

The same default also appears in `roles/kubernetes/control-plane/defaults/main/etcd.yml`. The value `etcd` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0 (present in every tag inspected).

## References
- roles/etcd_defaults/defaults/main.yml
- roles/kubernetes/control-plane/defaults/main/etcd.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
