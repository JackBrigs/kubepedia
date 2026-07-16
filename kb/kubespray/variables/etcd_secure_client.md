---
id: VARIABLE-ETCD_SECURE_CLIENT
type: variable
title: etcd_secure_client
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_secure_client
tags:
  - etcd
  - tls
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Whether etcd client access uses TLS; default true"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_secure_client

## Summary
Controls whether etcd client access is secured with TLS. Default is `true`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as `etcd_secure_client: true` (line 77 in v2.29.0/v2.29.1, line 76 in v2.30.0/v2.31.0). The value `true` is unchanged across v2.29.0-v2.31.0; only the line number shifted.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
