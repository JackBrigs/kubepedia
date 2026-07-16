---
id: VARIABLE-KUBELET_MAX_PARALLEL_IMAGE_PULLS
type: variable
title: kubelet_max_parallel_image_pulls
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_max_parallel_image_pulls
tags:
  - kubelet
  - images
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Maximum number of image pulls the kubelet performs in parallel (maxParallelImagePulls); default 1"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_max_parallel_image_pulls

## Summary
Maximum number of image pulls the kubelet performs in parallel (maps to the kubelet `maxParallelImagePulls` setting). Default is `1` (serial pulls).

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_max_parallel_image_pulls: 1
```

Line number: 195 (v2.29.0/v2.29.1), 192 (v2.30.0), 191 (v2.31.0). The value `1` is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Effective only when serialized image pulling is disabled at the kubelet level.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
