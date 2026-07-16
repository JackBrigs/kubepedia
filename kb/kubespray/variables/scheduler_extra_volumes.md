---
id: VARIABLE-SCHEDULER_EXTRA_VOLUMES
type: variable
title: scheduler_extra_volumes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - scheduler_extra_volumes
tags:
  - kube-scheduler
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    note: "Extra host volumes for kube-scheduler, default empty map"
relations: []
---

# scheduler_extra_volumes

## Summary
Additional host-path volumes to mount into the kube-scheduler static pod. Default is an empty map `{}`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml` as `scheduler_extra_volumes: {}`. The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. Applies to the kube-scheduler control-plane component; user supplies a map of extra volumes when needed.

## References
- roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
