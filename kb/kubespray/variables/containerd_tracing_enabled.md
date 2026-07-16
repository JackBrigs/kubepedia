---
id: VARIABLE-CONTAINERD_TRACING_ENABLED
type: variable
title: containerd_tracing_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_tracing_enabled
tags:
  - containerd
  - tracing
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Toggles the containerd OpenTelemetry tracing config block, defaults to false"
relations: []
---

# containerd_tracing_enabled

## Summary
Master switch for containerd OpenTelemetry tracing configuration. When `false` (default), the tracing config block is omitted from the containerd config. When `true`, the tracing endpoint/protocol/sampling/service_name settings are rendered.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_tracing_enabled: false
```

(line 134 in v2.29.x, line 133 in v2.30.0/v2.31.0). Used as a Jinja guard `{% if containerd_tracing_enabled %}` in `templates/config.toml.j2` and `templates/config-v1.toml.j2` to conditionally emit the tracing block. Value is `false` and unchanged across v2.29.0–v2.31.0.

## Compatibility
Present and identical in v2.29.0–v2.31.0. Related: `containerd_tracing_endpoint`, `containerd_tracing_protocol`, `containerd_tracing_sampling_ratio`, `containerd_tracing_service_name`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
