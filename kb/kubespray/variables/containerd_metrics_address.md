---
id: VARIABLE-CONTAINERD_METRICS_ADDRESS
type: variable
title: containerd_metrics_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_metrics_address
tags:
  - containerd
  - metrics
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Address for the containerd metrics endpoint; default empty string (disabled)"
relations: []
---

# containerd_metrics_address

## Summary
Sets the listen address for the containerd metrics endpoint. Default is an empty string `""`, which leaves metrics exposure unconfigured (disabled).

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_metrics_address: ""
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Applies only when the container runtime is containerd. Related variable: `containerd_metrics_grpc_histogram`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
