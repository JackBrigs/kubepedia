---
id: VARIABLE-OPENSTACK_LBAAS_MONITOR_MAX_RETRIES
type: variable
title: openstack_lbaas_monitor_max_retries
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - openstack_lbaas_monitor_max_retries
tags:
  - openstack
  - loadbalancer
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Number of health monitor retries before marking an OpenStack LBaaS member unhealthy; default '3'."
relations: []
---

# openstack_lbaas_monitor_max_retries

## Summary
Sets the number of failed health checks the OpenStack LBaaS monitor tolerates before marking a member as unhealthy. The default value is the string `"3"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
openstack_lbaas_monitor_max_retries: "3"
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number drifts from 492 in v2.29.0 to 500 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Effective only when `openstack_lbaas_enabled` and `openstack_lbaas_create_monitor` are true. Related variables: `openstack_lbaas_monitor_delay`, `openstack_lbaas_monitor_timeout`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
