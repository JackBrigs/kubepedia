---
id: VARIABLE-OPENSTACK_LBAAS_CREATE_MONITOR
type: variable
title: openstack_lbaas_create_monitor
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - openstack_lbaas_create_monitor
tags:
  - openstack
  - loadbalancer
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Whether the OpenStack LBaaS should create a health monitor; default 'yes'."
relations: []
---

# openstack_lbaas_create_monitor

## Summary
Controls whether the OpenStack LBaaS (Load Balancer as a Service) integration creates a health monitor for load balancers. The default value is the string `"yes"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
openstack_lbaas_create_monitor: "yes"
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number drifts from 489 in v2.29.0 to 497 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Effective only when `openstack_lbaas_enabled` is true. Related variables: `openstack_lbaas_enabled`, `openstack_lbaas_monitor_delay`, `openstack_lbaas_monitor_timeout`, `openstack_lbaas_monitor_max_retries`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
