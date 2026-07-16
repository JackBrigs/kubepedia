---
id: VARIABLE-KUBE_VIP_DNS_MODE
type: variable
title: kube_vip_dns_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_dns_mode
tags:
  - kube-vip
  - dns
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_vip_dns_mode with default first"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_dns_mode

## Summary
Sets the DNS resolution mode used by kube-vip when DDNS is active. Default is `first`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as:

```yaml
kube_vip_dns_mode: first
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Part of the kube-vip configuration block; related to `kube_vip_ddns_enabled`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
