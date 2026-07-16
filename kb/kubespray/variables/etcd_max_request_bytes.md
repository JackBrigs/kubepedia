---
id: VARIABLE-ETCD_MAX_REQUEST_BYTES
type: variable
title: etcd_max_request_bytes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_max_request_bytes
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Defines default etcd_max_request_bytes: \"1572864\""
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_max_request_bytes

## Summary
Sets the maximum client request size etcd will accept, in bytes. Default is `"1572864"` (1.5 MiB).

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as:

```yaml
etcd_max_request_bytes: "1572864"
```

Consumed as `ETCD_MAX_REQUEST_BYTES` in `roles/etcd/templates/etcd.env.j2` and `etcd-events.env.j2`, and as the `max-request-bytes` extra arg in the kubeadm-config templates. In `roles/kubernetes/control-plane/defaults/main/etcd.yml` the same variable appears only as a commented-out example (`# etcd_max_request_bytes: "1572864"`), so the active default comes from `etcd_defaults`. The default `"1572864"` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related: `etcd_heartbeat_interval`, `etcd_log_level`, `etcd_extra_vars`.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/etcd/templates/etcd.env.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
