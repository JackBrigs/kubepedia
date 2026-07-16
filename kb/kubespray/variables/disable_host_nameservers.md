---
id: VARIABLE-DISABLE_HOST_NAMESERVERS
type: variable
title: disable_host_nameservers
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - disable_host_nameservers
tags:
  - preinstall
  - dns
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Defines disable_host_nameservers with default false"
relations: []
---

# disable_host_nameservers

## Summary
Controls whether the host's upstream nameservers are removed from the generated resolv.conf during DNS configuration. Default is `false`, so host nameservers are retained.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 8 in all four tags):

```yaml
disable_host_nameservers: false
```

The default value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Part of the DNS/resolv.conf handling in the `kubernetes/preinstall` role, alongside `disable_ipv6_dns` and `dns_late`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
