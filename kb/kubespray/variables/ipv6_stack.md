---
id: VARIABLE-IPV6_STACK
type: variable
title: ipv6_stack
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ipv6_stack
tags:
  - networking
  - ipv6
  - dual-stack
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Enables IPv6 stack networking, defaults to enable_dual_stack_networks or false"
relations: []
---

# ipv6_stack

## Summary
Enables IPv6 networking for the cluster. It defaults to the value of the deprecated `enable_dual_stack_networks`, falling back to `false`, so IPv6 is off by default.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
ipv6_stack: "{{ enable_dual_stack_networks | default(false) }}"
```

The expression is unchanged across v2.29.0–v2.31.0 (line 260 in v2.29.0/v2.29.1, 261 in v2.30.0, 273 in v2.31.0). The referenced `enable_dual_stack_networks` is marked deprecated in the same file.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Paired with `ipv4_stack`; setting both `true` yields a dual-stack cluster.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
