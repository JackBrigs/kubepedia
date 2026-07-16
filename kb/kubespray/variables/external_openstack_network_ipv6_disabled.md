---
id: VARIABLE-EXTERNAL_OPENSTACK_NETWORK_IPV6_DISABLED
type: variable
title: external_openstack_network_ipv6_disabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - external_openstack_network_ipv6_disabled
tags:
  - openstack
  - network
  - ipv6
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Controls whether IPv6 is disabled for the OpenStack cloud controller networking; default false"
relations: []
---

# external_openstack_network_ipv6_disabled

## Summary
Controls whether IPv6 address handling is disabled for the external OpenStack cloud controller networking configuration. Default: `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
external_openstack_network_ipv6_disabled: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line numbers 497, 497, 498, 505 respectively).

## Compatibility
Kubespray v2.29.0–v2.31.0. Applies when the external OpenStack cloud provider is used. Related: `external_openstack_network_internal_networks`, `external_openstack_network_public_networks`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
