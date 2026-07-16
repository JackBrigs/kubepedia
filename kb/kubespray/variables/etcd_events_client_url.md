---
id: VARIABLE-ETCD_EVENTS_CLIENT_URL
type: variable
title: etcd_events_client_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_events_client_url
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines etcd_events_client_url, https://<etcd_events_access_address>:2383"
relations: []
---

# etcd_events_client_url

## Summary
The client-facing URL of the local node's etcd-events member, on port 2383.
Built from `etcd_events_access_address`. Used by clients connecting to the
separate events etcd cluster.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:
`etcd_events_client_url: "https://{{ etcd_events_access_address | ansible.utils.ipwrap }}:2383"`.
Port 2383 is the events client port (vs. 2379 for the main etcd client). The
expression is unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when
`etcd_events_cluster_enabled` is `true`. Related: `etcd_events_access_address`,
`etcd_events_peer_url`, `etcd_client_url`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
