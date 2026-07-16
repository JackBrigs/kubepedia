---
id: VARIABLE-ETCD_EXPERIMENTAL_DISTRIBUTED_TRACING_ADDRESS
type: variable
title: etcd_experimental_distributed_tracing_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_experimental_distributed_tracing_address
tags:
  - etcd
  - tracing
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Defines etcd_experimental_distributed_tracing_address, default localhost:4317"
relations: []
---

# etcd_experimental_distributed_tracing_address

## Summary
The OTLP endpoint address to which etcd sends distributed tracing spans when
experimental distributed tracing is enabled. Default is `"localhost:4317"`.

## Implementation
Defined as `etcd_experimental_distributed_tracing_address: "localhost:4317"` in
`roles/etcd_defaults/defaults/main.yml`. It sits alongside the related toggles
`etcd_experimental_enable_distributed_tracing` (default `false`),
`etcd_experimental_distributed_tracing_sample_rate`, and
`etcd_experimental_distributed_tracing_service_name`. The value is unchanged
across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Effective only when
`etcd_experimental_enable_distributed_tracing` is `true`. Related:
`etcd_experimental_distributed_tracing_sample_rate`,
`etcd_experimental_distributed_tracing_service_name`.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
