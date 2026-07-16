---
id: VARIABLE-ETCD_PEER_URL
type: variable
title: etcd_peer_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_peer_url
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "This host's etcd peer URL; computed from etcd_access_address on port 2380"
relations: []
---

# etcd_peer_url

## Summary
The etcd peer URL advertised by the current host, over HTTPS on port 2380. Computed from `etcd_access_address`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
etcd_peer_url: "https://{{ etcd_access_address | ansible.utils.ipwrap }}:2380"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0 (present in every tag inspected). Depends on `etcd_access_address`; related to `etcd_peer_addresses`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
