---
id: VARIABLE-ETCD_MEMBER_NAME
type: variable
title: etcd_member_name
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_member_name
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "The etcd member name for the current host; defaults to etcd<index> if not set in inventory"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_member_name

## Summary
The etcd member name for the current host. Users may set it per host in inventory; otherwise it defaults to `etcd<loop.index>` derived from the host's position in the `etcd` group.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a Jinja block:

```yaml
etcd_member_name: |-
  {% for host in groups['etcd'] %}
  {% if inventory_hostname == host %}{{ hostvars[host].etcd_member_name | default("etcd" + loop.index | string) }}{% endif %}
  {% endfor %}
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0 (present in every tag inspected). Depends on the `etcd` inventory group; used by `etcd_peer_addresses`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
