---
id: VARIABLE-KUBELET_TRACING
type: variable
title: kubelet_tracing
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_tracing
tags:
  - kubelet
  - tracing
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Enables distributed tracing for kubelet; default false"
relations: []
---

# kubelet_tracing

## Summary
Boolean toggle that enables distributed (OpenTelemetry) tracing for kubelet. Default is `false`. When enabled, `kubelet_tracing_endpoint` and `kubelet_tracing_sampling_rate_per_million` configure the exporter.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_tracing: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Line moves across tags (190 in v2.29.0/v2.29.1, 187 in v2.30.0, 186 in v2.31.0) but the value is constant.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Pairs with `kubelet_tracing_endpoint` and `kubelet_tracing_sampling_rate_per_million`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
