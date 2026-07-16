---
id: VARIABLE-KUBE_PROXY_FEATURE_GATES
type: variable
title: kube_proxy_feature_gates
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_feature_gates
tags:
  - kube-proxy
  - feature-gates
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines feature gates applied to kube-proxy; default [] (empty list)"
relations: []
---

# kube_proxy_feature_gates

## Summary
List of feature gates applied specifically to kube-proxy. Default is an empty list `[]`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_proxy_feature_gates: []
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The defining line moves within the file across tags (line 605 in v2.29.0/v2.29.1, line 606 in v2.30.0, line 625 in v2.31.0) but the file path and default value are identical.

## Compatibility
Kubespray v2.29.0 through v2.31.0. One of the per-component feature-gate lists alongside `kube_feature_gates`, `kube_apiserver_feature_gates`, `kube_controller_feature_gates`, `kube_scheduler_feature_gates`, `kubelet_feature_gates`, and `kubeadm_feature_gates`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
