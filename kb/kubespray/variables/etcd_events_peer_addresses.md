---
id: VARIABLE-ETCD_EVENTS_PEER_ADDRESSES
type: variable
title: etcd_events_peer_addresses
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_events_peer_addresses
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines etcd_events_peer_addresses, initial-cluster peer list (port 2382)"
relations: []
---

# etcd_events_peer_addresses

## Summary
The etcd-events initial-cluster peer list: `name-events=https://<ip>:2382`
entries for every host in the `etcd` group, comma-separated. Used to form the
`--initial-cluster` value for the events etcd cluster.

## Implementation
Default defined in `roles/kubespray_defaults/defaults/main/main.yml`:
```
etcd_events_peer_addresses: |-
  {% for item in groups['etcd'] -%}
    {{ hostvars[item].etcd_member_name | default("etcd" + loop.index | string) }}-events=https://{{ hostvars[item]['main_access_ip'] | ansible.utils.ipwrap }}:2382{% if not loop.last %},{% endif %}
  {%- endfor %}
```
It is also recomputed at member-join time in
`roles/etcd/tasks/join_etcd-events_member.yml` (a `vars:` override that only
includes already-joined members plus the new one). Both expressions are
unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when
`etcd_events_cluster_enabled` is `true`. Related: `etcd_peer_addresses`,
`etcd_events_peer_url`, `etcd_member_name`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/etcd/tasks/join_etcd-events_member.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
