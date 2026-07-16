---
id: VARIABLE-ETCD_EVENTS_ACCESS_ADDRESSES
type: variable
title: etcd_events_access_addresses
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_events_access_addresses
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Comma-joined list of etcd-events client URLs from etcd_events_access_addresses_list"
relations: []
---

# etcd_events_access_addresses

## Summary
Comma-separated list of client URLs for all etcd-events members. Derived by
joining `etcd_events_access_addresses_list` with `,`. Used as the endpoints
list when talking to the events etcd cluster.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:
`etcd_events_access_addresses: "{{ etcd_events_access_addresses_list | join(',') }}"`.
`etcd_events_access_addresses_list` is a Jinja loop over `etcd_hosts` producing
`https://<main_access_ip>:2383` entries. The expression is unchanged across
v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when
`etcd_events_cluster_enabled` is `true`. Related:
`etcd_events_access_addresses_list`, `etcd_events_access_addresses_semicolon`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
