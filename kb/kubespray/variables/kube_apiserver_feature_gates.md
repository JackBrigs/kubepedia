---
id: VARIABLE-KUBE_APISERVER_FEATURE_GATES
type: variable
title: kube_apiserver_feature_gates
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_feature_gates
tags:
  - apiserver
  - feature-gates
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Default [] — extra feature gates for kube-apiserver"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_feature_gates

## Summary
List of additional feature gates enabled specifically for the kube-apiserver, appended to the cluster-wide `kube_feature_gates`. Default is an empty list `[]`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `kube_apiserver_feature_gates: []`. The default value `[]` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. In v2.29.0–v2.30.0 a commented-out usage example accompanied the definition; that comment was removed in v2.31.0, but the effective default remains `[]`.

## Compatibility
Available in Kubespray v2.29.0–v2.31.0. Related: `kube_feature_gates` (cluster-wide feature gates).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
