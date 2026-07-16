---
id: VARIABLE-CONTAINERD_ENABLE_UNPRIVILEGED_ICMP
type: variable
title: containerd_enable_unprivileged_icmp
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_enable_unprivileged_icmp
tags:
  - containerd
  - network
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Allows non-root users to use ICMP sockets; default false"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_enable_unprivileged_icmp

## Summary
Controls whether non-root users are allowed to use ICMP sockets. Default is `false`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`, with an inline comment "If enabled it will allow non root users to use icmp sockets":

```yaml
containerd_enable_unprivileged_icmp: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related: `containerd_enable_unprivileged_ports`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
