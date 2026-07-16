---
id: VARIABLE-ETCD_CLUSTER_SETUP
type: variable
title: etcd_cluster_setup
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_cluster_setup
tags:
  - etcd
  - cluster
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Whether to set up the etcd cluster; default true"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_cluster_setup

## Summary
Boolean controlling whether Kubespray sets up the etcd cluster. Default is `true`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml:6` as `etcd_cluster_setup: true`. The default `true` and the line number are **unchanged across v2.29.0-v2.31.0**.

## Compatibility
Kubespray v2.29.0-v2.31.0. Related etcd lifecycle variables reside in the same `etcd_defaults` defaults file.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
