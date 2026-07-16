---
id: VARIABLE-KUBE_APISERVER_ETCD_COMPACTION_INTERVAL
type: variable
title: kube_apiserver_etcd_compaction_interval
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_etcd_compaction_interval
tags:
  - apiserver
  - etcd
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Default \"5m0s\" — kube-apiserver --etcd-compaction-interval"
relations: []
---

# kube_apiserver_etcd_compaction_interval

## Summary
Sets the interval of compaction requests the kube-apiserver sends to etcd, passed to the `--etcd-compaction-interval` flag. Default is `"5m0s"`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `kube_apiserver_etcd_compaction_interval: "5m0s"`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0–v2.31.0. Applies to the control-plane (kube-apiserver) role.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
