---
id: VARIABLE-ETCD_PEER_CLIENT_AUTH
type: variable
title: etcd_peer_client_auth
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_peer_client_auth
tags:
  - etcd
  - tls
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Enables client cert authentication on the etcd peer interface; default true"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_peer_client_auth

## Summary
Controls etcd's `--peer-client-cert-auth`, i.e. whether client certificate authentication is enforced on the etcd peer interface. Default is `true`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as:

```yaml
etcd_peer_client_auth: true
```

The value `true` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0 (present in every tag inspected).

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
