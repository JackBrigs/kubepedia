---
id: VARIABLE-ETCD_LOG_LEVEL
type: variable
title: etcd_log_level
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_log_level
tags:
  - etcd
  - logging
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Defines default etcd_log_level: info"
relations: []
---

# etcd_log_level

## Summary
Sets the log verbosity of etcd. Default is `info`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as:

```yaml
etcd_log_level: info
```

Consumed as `ETCD_LOG_LEVEL={{ etcd_log_level }}` in `roles/etcd/templates/etcd.env.j2`, and as the `log-level` extra arg in the kubeadm-config templates under `roles/kubernetes/control-plane/templates/`. The default `info` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. (Note: the unrelated `netchecker_etcd_log_level` in `roles/kubernetes-apps/ansible` is a separate variable.)

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related: `etcd_heartbeat_interval`, `etcd_max_request_bytes`.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/etcd/templates/etcd.env.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
