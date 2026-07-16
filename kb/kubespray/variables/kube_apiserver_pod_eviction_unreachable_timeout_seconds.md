---
id: VARIABLE-KUBE_APISERVER_POD_EVICTION_UNREACHABLE_TIMEOUT_SECONDS
type: variable
title: kube_apiserver_pod_eviction_unreachable_timeout_seconds
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_pod_eviction_unreachable_timeout_seconds
tags:
  - apiserver
  - eviction
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Default \"300\" — unreachable toleration seconds"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_pod_eviction_unreachable_timeout_seconds

## Summary
Number of seconds a pod tolerates the `node.kubernetes.io/unreachable` taint before eviction is triggered. Default is `"300"` (5 minutes).

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `kube_apiserver_pod_eviction_unreachable_timeout_seconds: "300"`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0–v2.31.0. Related: `kube_apiserver_pod_eviction_not_ready_timeout_seconds`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
