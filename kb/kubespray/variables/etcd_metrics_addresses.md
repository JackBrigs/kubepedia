---
id: VARIABLE-ETCD_METRICS_ADDRESSES
type: variable
title: etcd_metrics_addresses
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_metrics_addresses
tags:
  - etcd
  - metrics
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Comma-separated list of etcd metrics endpoints across etcd hosts on port 2381"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_metrics_addresses

## Summary
Comma-separated list of HTTPS etcd metrics endpoints, one per etcd host, on `etcd_metrics_port` (default 2381). Built from `etcd_hosts`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a Jinja block:

```yaml
etcd_metrics_addresses: |-
  {% for item in etcd_hosts -%}
    https://{{ hostvars[item]['main_access_ip'] | ansible.utils.ipwrap }}:{{ etcd_metrics_port | default(2381) }}{% if not loop.last %},{% endif %}
  {%- endfor %}
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0 (present in every tag inspected). Depends on `etcd_hosts` and `etcd_metrics_port`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
