---
id: VARIABLE-FORCE_ETCD_CERT_REFRESH
type: variable
title: force_etcd_cert_refresh
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - force_etcd_cert_refresh
tags:
  - etcd
  - certificates
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Controls forced refresh/regeneration of etcd certificates; default true"
relations: []
---

# force_etcd_cert_refresh

## Summary
Controls whether etcd certificates are force-refreshed (regenerated) during a run. Default: `true`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` (line 18) as:

```yaml
force_etcd_cert_refresh: true
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0–v2.31.0. Affects the etcd certificate management workflow.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
