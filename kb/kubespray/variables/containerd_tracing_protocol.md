---
id: VARIABLE-CONTAINERD_TRACING_PROTOCOL
type: variable
title: containerd_tracing_protocol
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_tracing_protocol
tags:
  - containerd
  - tracing
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "OTLP exporter protocol for containerd tracing, defaults to grpc"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_tracing_protocol

## Summary
The OpenTelemetry (OTLP) exporter protocol used when containerd tracing is enabled. Default is `grpc`. The template also branches on this value (`== "grpc"`) when rendering the tracing block.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_tracing_protocol: "grpc"
```

(line 136 in v2.29.x, line 135 in v2.30.0/v2.31.0). Rendered in `templates/config.toml.j2` and `templates/config-v1.toml.j2` as `protocol = "{{ containerd_tracing_protocol }}"`, with an additional `{% if containerd_tracing_protocol == "grpc" %}` conditional. Value is unchanged across v2.29.0–v2.31.0.

## Compatibility
Present and identical in v2.29.0–v2.31.0. Active only with `containerd_tracing_enabled: true`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
