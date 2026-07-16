---
id: VARIABLE-KUBE_FEATURE_GATES
type: variable
title: kube_feature_gates
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_feature_gates
tags:
  - feature-gates
  - control-plane
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Cluster-wide list of Kubernetes feature gates; default empty list"
relations: []
---

# kube_feature_gates

## Summary
Cluster-wide list of Kubernetes feature gates applied across control-plane components. Default: `[]` (empty list — no extra feature gates enabled beyond Kubernetes defaults).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
kube_feature_gates: []
```

The default is unchanged across v2.29.0–v2.31.0 (line ~601 in v2.29.x, ~602 in v2.30.0, ~621 in v2.31.0).

## Compatibility
Kubespray v2.29.0–v2.31.0. Serves as the base list that component-specific feature-gate variables (e.g. `kube_apiserver_feature_gates`) extend.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
