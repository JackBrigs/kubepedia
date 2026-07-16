---
id: VARIABLE-KUBELET_TRACING_ENDPOINT
type: variable
title: kubelet_tracing_endpoint
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_tracing_endpoint
tags:
  - kubelet
  - tracing
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "OTLP collector endpoint for kubelet tracing; default [::]:4317"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_tracing_endpoint

## Summary
Sets the OpenTelemetry (OTLP) collector endpoint for kubelet distributed tracing. Default is `"[::]:4317"`. Only relevant when `kubelet_tracing` is enabled.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_tracing_endpoint: "[::]:4317"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Line moves across tags (191 in v2.29.0/v2.29.1, 188 in v2.30.0, 187 in v2.31.0) but the value is constant.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies when `kubelet_tracing: true`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
