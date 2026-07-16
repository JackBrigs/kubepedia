---
id: VARIABLE-ETCD_EVENTS_ACCESS_ADDRESSES_LIST
type: variable
title: etcd_events_access_addresses_list
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_events_access_addresses_list
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Jinja list literal of etcd-events client URLs (port 2383) per etcd host"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_events_access_addresses_list

## Summary
A Jinja/YAML-style list literal of client URLs for every etcd-events member,
one `https://<main_access_ip>:2383` entry per host in `etcd_hosts`. Serves as
the base from which the comma- and semicolon-joined address strings are built.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a multi-line
block that renders a bracketed list:
```
etcd_events_access_addresses_list: |-
  [
  {% for item in etcd_hosts -%}
    'https://{{ hostvars[item].main_access_ip | ansible.utils.ipwrap }}:2383'{% if not loop.last %},{% endif %}
  {%- endfor %}
  ]
```
It is consumed by `etcd_events_access_addresses` and
`etcd_events_access_addresses_semicolon`. The expression is unchanged across
v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when
`etcd_events_cluster_enabled` is `true`. Related: `etcd_hosts`,
`etcd_events_access_addresses`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
