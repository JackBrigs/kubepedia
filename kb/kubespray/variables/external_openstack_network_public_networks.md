---
id: VARIABLE-EXTERNAL_OPENSTACK_NETWORK_PUBLIC_NETWORKS
type: variable
title: external_openstack_network_public_networks
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - external_openstack_network_public_networks
tags:
  - openstack
  - network
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "List of OpenStack public networks for the cloud controller; default empty list"
relations: []
---

# external_openstack_network_public_networks

## Summary
Defines the list of OpenStack public networks the external cloud controller should consider when resolving node external addresses. Default: `[]` (empty list).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
external_openstack_network_public_networks: []
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line numbers 499, 499, 500, 507 respectively).

## Compatibility
Kubespray v2.29.0–v2.31.0. Applies when the external OpenStack cloud provider is used. Related: `external_openstack_network_internal_networks`, `external_openstack_network_ipv6_disabled`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
