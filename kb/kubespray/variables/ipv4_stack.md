---
id: VARIABLE-IPV4_STACK
type: variable
title: ipv4_stack
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ipv4_stack
tags:
  - networking
  - ipv4
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Enables IPv4 stack networking, defaults to true"
relations: []
---

# ipv4_stack

## Summary
Enables IPv4 networking for the cluster. It defaults to `true`, so IPv4 is on by default.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
ipv4_stack: true
```

The value `true` is unchanged across v2.29.0–v2.31.0 (line 258 in v2.29.0/v2.29.1, 259 in v2.30.0, 271 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Paired with `ipv6_stack` to form single- or dual-stack configurations.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
