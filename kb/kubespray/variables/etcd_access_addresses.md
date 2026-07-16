---
id: VARIABLE-ETCD_ACCESS_ADDRESSES
type: variable
title: etcd_access_addresses
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_access_addresses
tags:
  - etcd
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Comma-separated list of client URLs for all etcd hosts; computed from etcd_hosts"
relations: []
---

# etcd_access_addresses

## Summary
A comma-separated list of client endpoint URLs (`https://<ip>:2379`) for every etcd host, used by clients to reach the etcd cluster. It is a computed default built by iterating over `etcd_hosts`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a Jinja block:
```yaml
etcd_access_addresses: |-
  {% for item in etcd_hosts -%}
    https://{{ hostvars[item]['main_access_ip'] | ansible.utils.ipwrap }}:2379{% if not loop.last %},{% endif %}
  {%- endfor %}
```
The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `etcd_access_address` and `etcd_address`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
