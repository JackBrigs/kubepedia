---
id: VARIABLE-ETCD_EVENTS_ACCESS_ADDRESSES_SEMICOLON
type: variable
title: etcd_events_access_addresses_semicolon
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_events_access_addresses_semicolon
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Semicolon-joined list of etcd-events client URLs from etcd_events_access_addresses_list"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_events_access_addresses_semicolon

## Summary
Semicolon-separated list of client URLs for all etcd-events members. Derived by
joining `etcd_events_access_addresses_list` with `;`. Used where a semicolon
delimiter is required instead of a comma.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:
`etcd_events_access_addresses_semicolon: "{{ etcd_events_access_addresses_list | join(';') }}"`.
It differs from `etcd_events_access_addresses` only in the join separator. The
expression is unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when
`etcd_events_cluster_enabled` is `true`. Related:
`etcd_events_access_addresses_list`, `etcd_events_access_addresses`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
