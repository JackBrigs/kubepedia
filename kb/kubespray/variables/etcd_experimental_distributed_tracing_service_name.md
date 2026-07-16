---
id: VARIABLE-ETCD_EXPERIMENTAL_DISTRIBUTED_TRACING_SERVICE_NAME
type: variable
title: etcd_experimental_distributed_tracing_service_name
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_experimental_distributed_tracing_service_name
tags:
  - etcd
  - tracing
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Defines default etcd_experimental_distributed_tracing_service_name: etcd"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_experimental_distributed_tracing_service_name

## Summary
Sets the service name reported by etcd's experimental distributed tracing. Default is `etcd`. Only rendered into the etcd environment when `etcd_experimental_enable_distributed_tracing` is `true`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as:

```yaml
etcd_experimental_distributed_tracing_service_name: etcd
```

Consumed in `roles/etcd/templates/etcd.env.j2`, where it is written as `ETCD_EXPERIMENTAL_DISTRIBUTED_TRACING_SERVICE_NAME` inside the `{% if etcd_experimental_enable_distributed_tracing %}` block. The default value `etcd` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Effective only when `etcd_experimental_enable_distributed_tracing: true`. Related: `etcd_experimental_enable_distributed_tracing`, `etcd_experimental_distributed_tracing_sample_rate`.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/etcd/templates/etcd.env.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
