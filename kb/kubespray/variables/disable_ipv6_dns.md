---
id: VARIABLE-DISABLE_IPV6_DNS
type: variable
title: disable_ipv6_dns
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - disable_ipv6_dns
tags:
  - preinstall
  - dns
  - ipv6
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Defines disable_ipv6_dns with default false"
relations: []
---

# disable_ipv6_dns

## Summary
Controls whether IPv6 DNS resolution is disabled during host DNS configuration. Default is `false`, so IPv6 DNS is left enabled.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 15 in all four tags):

```yaml
disable_ipv6_dns: false
```

The default value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Part of the DNS/resolv.conf handling in the `kubernetes/preinstall` role, alongside `disable_host_nameservers` and `dns_late`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
