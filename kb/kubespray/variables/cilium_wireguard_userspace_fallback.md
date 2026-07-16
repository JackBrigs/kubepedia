---
id: VARIABLE-CILIUM_WIREGUARD_USERSPACE_FALLBACK
type: variable
title: cilium_wireguard_userspace_fallback
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_wireguard_userspace_fallback
tags:
  - cilium
  - wireguard
  - encryption
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_wireguard_userspace_fallback, default false"
relations: []
---

# cilium_wireguard_userspace_fallback

## Summary
Controls whether Cilium falls back to a userspace WireGuard implementation when the kernel module is unavailable. Default is `false`, so only kernel WireGuard is used.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_wireguard_userspace_fallback: false
```

The default value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when `kube_network_plugin: cilium` and WireGuard-based encryption is in use (see `cilium_encryption_type`).

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
