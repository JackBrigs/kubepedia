---
id: VARIABLE-CONTAINERD_METRICS_GRPC_HISTOGRAM
type: variable
title: containerd_metrics_grpc_histogram
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_metrics_grpc_histogram
tags:
  - containerd
  - metrics
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Enables gRPC metrics histograms in containerd; default false"
relations: []
---

# containerd_metrics_grpc_histogram

## Summary
Toggles whether containerd emits gRPC metrics histograms on its metrics endpoint. Default is `false`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_metrics_grpc_histogram: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Applies only when the container runtime is containerd. Related variable: `containerd_metrics_address`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
