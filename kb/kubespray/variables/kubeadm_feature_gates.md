---
id: VARIABLE-KUBEADM_FEATURE_GATES
type: variable
title: kubeadm_feature_gates
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_feature_gates
tags:
  - kubeadm
  - feature-gates
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "List of kubeadm feature gates, empty list by default"
relations:
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
---

# kubeadm_feature_gates

## Summary
A list of feature gates passed to kubeadm. Empty (`[]`) by default, so no additional kubeadm feature gates are enabled.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `kubeadm_feature_gates: []`. The value is unchanged across v2.29.0-v2.31.0; only the line number shifts (607 in v2.29.0/v2.29.1, 608 in v2.30.0, 627 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_feature_gates`, `kube_apiserver_feature_gates`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
