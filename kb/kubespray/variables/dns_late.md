---
id: VARIABLE-DNS_LATE
type: variable
title: dns_late
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - dns_late
tags:
  - preinstall
  - dns
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Defines dns_late with default false"
relations: []
---

# dns_late

## Summary
Internal flag marking the "late" DNS configuration pass in the preinstall role (DNS handling deferred to run after other setup). Default is `false`.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 10 in all four tags):

```yaml
dns_late: false
```

The default value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Part of the DNS/resolv.conf handling in the `kubernetes/preinstall` role, alongside `disable_host_nameservers` and `disable_ipv6_dns`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
