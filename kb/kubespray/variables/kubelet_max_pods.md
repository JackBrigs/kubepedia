---
id: VARIABLE-KUBELET_MAX_PODS
type: variable
title: kubelet_max_pods
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_max_pods
tags:
  - kubelet
  - scheduling
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Maximum number of pods per node the kubelet will run (maxPods); default 110"
relations: []
---

# kubelet_max_pods

## Summary
Maximum number of pods the kubelet will run on a single node (maps to the kubelet `maxPods` setting). Default is `110`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_max_pods: 110
```

Line number: 115 (v2.29.0/v2.29.1), 112 (v2.30.0), 114 (v2.31.0). The value `110` is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Node capacity constraint; must be consistent with the pod CIDR size per node.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
