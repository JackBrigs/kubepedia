---
id: VARIABLE-OPENSTACK_LBAAS_MONITOR_DELAY
type: variable
title: openstack_lbaas_monitor_delay
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - openstack_lbaas_monitor_delay
tags:
  - openstack
  - loadbalancer
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Delay between OpenStack LBaaS health monitor checks; default '1m'."
relations: []
---

# openstack_lbaas_monitor_delay

## Summary
Sets the delay between successive health checks performed by the OpenStack LBaaS health monitor. The default value is the string `"1m"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
openstack_lbaas_monitor_delay: "1m"
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number drifts from 490 in v2.29.0 to 498 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Effective only when `openstack_lbaas_enabled` and `openstack_lbaas_create_monitor` are true. Related variables: `openstack_lbaas_monitor_timeout`, `openstack_lbaas_monitor_max_retries`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
