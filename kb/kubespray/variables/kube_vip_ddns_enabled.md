---
id: VARIABLE-KUBE_VIP_DDNS_ENABLED
type: variable
title: kube_vip_ddns_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_ddns_enabled
tags:
  - kube-vip
  - dns
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_vip_ddns_enabled with default false"
relations: []
---

# kube_vip_ddns_enabled

## Summary
Enables dynamic DNS (DDNS) mode for the kube-vip virtual IP. Default is `false`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as:

```yaml
kube_vip_ddns_enabled: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Part of the kube-vip configuration block; relevant only when `kube_vip_enabled: true`. Related to `kube_vip_dns_mode`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
