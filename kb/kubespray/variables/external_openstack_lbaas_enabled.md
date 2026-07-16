---
id: VARIABLE-EXTERNAL_OPENSTACK_LBAAS_ENABLED
type: variable
title: external_openstack_lbaas_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - external_openstack_lbaas_enabled
tags:
  - openstack
  - loadbalancer
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Enables OpenStack LBaaS (Octavia/Neutron LBaaS) integration for the external cloud controller; default true"
relations: []
---

# external_openstack_lbaas_enabled

## Summary
Toggles OpenStack Load Balancer as a Service (LBaaS) integration for the external OpenStack cloud controller. Default: `true`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
external_openstack_lbaas_enabled: true
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line numbers 496, 496, 497, 504 respectively).

## Compatibility
Kubespray v2.29.0–v2.31.0. Applies when the external OpenStack cloud provider is used. Related: `external_openstack_network_internal_networks`, `external_openstack_network_public_networks`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
