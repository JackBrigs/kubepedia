---
id: VARIABLE-ETCD_EVENTS_ACCESS_ADDRESS
type: variable
title: etcd_events_access_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_events_access_address
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines etcd_events_access_address, defaults to the host main_access_ip"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_events_access_address

## Summary
The address on which the local node's etcd-events member is reachable. Defaults
to the host's `main_access_ip`. Used to build the events etcd peer and client
URLs for the current host.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:
`etcd_events_access_address: "{{ hostvars[inventory_hostname]['main_access_ip'] }}"`.
It feeds `etcd_events_peer_url` and `etcd_events_client_url`. The expression is
unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when
`etcd_events_cluster_enabled` is `true`. Related: `etcd_access_address`,
`etcd_events_peer_url`, `etcd_events_client_url`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
