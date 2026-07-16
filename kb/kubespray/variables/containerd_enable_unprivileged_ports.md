---
id: VARIABLE-CONTAINERD_ENABLE_UNPRIVILEGED_PORTS
type: variable
title: containerd_enable_unprivileged_ports
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_enable_unprivileged_ports
tags:
  - containerd
  - network
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Allows non-root users to bind ports <1024; default false"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_enable_unprivileged_ports

## Summary
Controls whether non-root users are allowed to use port numbers below 1024. Default is `false`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`, with an inline comment "If enabled it will allow non root users to use port numbers <1024":

```yaml
containerd_enable_unprivileged_ports: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related: `containerd_enable_unprivileged_icmp`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
