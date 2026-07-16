---
id: VARIABLE-EVENT_TTL_DURATION
type: variable
title: event_ttl_duration
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - event_ttl_duration
tags:
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kube-apiserver event TTL (--event-ttl); default \"1h0m0s\""
relations: []
---

# event_ttl_duration

## Summary
Amount of time to retain Kubernetes events, passed to the kube-apiserver `--event-ttl` flag. Default is `"1h0m0s"`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `event_ttl_duration: "1h0m0s"` (line 232 in v2.29.0/v2.29.1, line 235 in v2.30.0/v2.31.0). The same value also appears in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`, matching the role default. The value `"1h0m0s"` is unchanged across v2.29.0-v2.31.0; only the line numbers shifted.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
