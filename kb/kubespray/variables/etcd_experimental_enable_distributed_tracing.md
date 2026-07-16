---
id: VARIABLE-ETCD_EXPERIMENTAL_ENABLE_DISTRIBUTED_TRACING
type: variable
title: etcd_experimental_enable_distributed_tracing
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_experimental_enable_distributed_tracing
tags:
  - etcd
  - tracing
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Defines default etcd_experimental_enable_distributed_tracing: false"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_experimental_enable_distributed_tracing

## Summary
Toggles etcd's experimental OpenTelemetry distributed tracing. Default is `false`. When `true`, the etcd environment gains the tracing sampling-rate and service-name settings.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as:

```yaml
etcd_experimental_enable_distributed_tracing: false
```

Used as the gate `{% if etcd_experimental_enable_distributed_tracing %}` in `roles/etcd/templates/etcd.env.j2`, which conditionally renders `ETCD_EXPERIMENTAL_DISTRIBUTED_TRACING_SAMPLING_RATE` and `ETCD_EXPERIMENTAL_DISTRIBUTED_TRACING_SERVICE_NAME`. The default value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related: `etcd_experimental_distributed_tracing_sample_rate`, `etcd_experimental_distributed_tracing_service_name`.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/etcd/templates/etcd.env.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
