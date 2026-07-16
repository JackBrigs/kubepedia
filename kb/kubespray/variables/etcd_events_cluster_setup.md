---
id: VARIABLE-ETCD_EVENTS_CLUSTER_SETUP
type: variable
title: etcd_events_cluster_setup
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_events_cluster_setup
tags:
  - etcd
  - playbook
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Defines etcd_events_cluster_setup, role default false (overridden by playbooks)"
relations: []
---

# etcd_events_cluster_setup

## Summary
Controls whether the etcd-events cluster is actually set up (as opposed to only
certificate management). Role default is `false`; the playbooks override it per
run.

## Implementation
Default `etcd_events_cluster_setup: false` in
`roles/etcd_defaults/defaults/main.yml`. Playbooks set it as a play var:
`playbooks/cluster.yml` and `playbooks/upgrade_cluster.yml` set
`etcd_events_cluster_setup: "{{ etcd_events_cluster_enabled }}"`, while
`playbooks/scale.yml` sets `etcd_events_cluster_setup: false`. All of these are
unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Tied to `etcd_events_cluster_enabled`.
Mirrors `etcd_cluster_setup` for the main etcd cluster.

## References
- roles/etcd_defaults/defaults/main.yml
- playbooks/cluster.yml
- playbooks/upgrade_cluster.yml
- playbooks/scale.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
