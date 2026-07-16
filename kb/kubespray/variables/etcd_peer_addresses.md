---
id: VARIABLE-ETCD_PEER_ADDRESSES
type: variable
title: etcd_peer_addresses
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_peer_addresses
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Comma-separated name=peer-URL list of all etcd members on port 2380"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_peer_addresses

## Summary
Comma-separated list of `<member_name>=https://<host>:2380` entries for every member of the `etcd` group, used as the etcd initial-cluster peer list.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a Jinja block:

```yaml
etcd_peer_addresses: |-
  {% for item in groups['etcd'] -%}
    {{ hostvars[item].etcd_member_name | default("etcd" + loop.index | string) }}=https://{{ hostvars[item]['main_access_ip'] | ansible.utils.ipwrap }}:2380{% if not loop.last %},{% endif %}
  {%- endfor %}
```

The default expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. It is also redefined locally as a task-level `vars` value in `roles/etcd/tasks/join_etcd_member.yml` (member-join flow), likewise unchanged across the four tags.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0 (present in every tag inspected). Depends on the `etcd` group, `etcd_member_name`, and `etcd_peer_url`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/etcd/tasks/join_etcd_member.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
