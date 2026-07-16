---
id: VARIABLE-CONTAINERD_TRACING_SAMPLING_RATIO
type: variable
title: containerd_tracing_sampling_ratio
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_tracing_sampling_ratio
tags:
  - containerd
  - tracing
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Trace sampling ratio for containerd tracing, defaults to 1.0"
relations: []
---

# containerd_tracing_sampling_ratio

## Summary
The sampling ratio for containerd's tracing processor. Default is `1.0` (sample all traces). Only rendered when `containerd_tracing_enabled` is true.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_tracing_sampling_ratio: 1.0
```

(line 137 in v2.29.x, line 136 in v2.30.0/v2.31.0). Rendered inside the tracing block of `templates/config.toml.j2` and `templates/config-v1.toml.j2` as `sampling_ratio = {{ containerd_tracing_sampling_ratio }}`. Value is unchanged across v2.29.0–v2.31.0.

## Compatibility
Present and identical in v2.29.0–v2.31.0. Active only with `containerd_tracing_enabled: true`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
