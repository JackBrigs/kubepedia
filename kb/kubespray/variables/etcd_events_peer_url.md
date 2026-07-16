---
id: VARIABLE-ETCD_EVENTS_PEER_URL
type: variable
title: etcd_events_peer_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_events_peer_url
tags:
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines etcd_events_peer_url, https://<etcd_events_access_address>:2382"
relations: []
---

# etcd_events_peer_url

## Summary
The peer (member-to-member) URL of the local node's etcd-events member, on port
2382. Built from `etcd_events_access_address`. Used for peer communication in
the separate events etcd cluster.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:
`etcd_events_peer_url: "https://{{ etcd_events_access_address | ansible.utils.ipwrap }}:2382"`.
Port 2382 is the events peer port (vs. 2380 for the main etcd peer). The
expression is unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when
`etcd_events_cluster_enabled` is `true`. Related: `etcd_events_access_address`,
`etcd_events_client_url`, `etcd_peer_url`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
