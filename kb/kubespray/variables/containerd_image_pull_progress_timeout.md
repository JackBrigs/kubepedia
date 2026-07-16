---
id: VARIABLE-CONTAINERD_IMAGE_PULL_PROGRESS_TIMEOUT
type: variable
title: containerd_image_pull_progress_timeout
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_image_pull_progress_timeout
tags:
  - containerd
  - images
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Timeout for no image pull progress before cancel; default 5m"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_image_pull_progress_timeout

## Summary
Sets the maximum duration containerd waits without image pull progress before cancelling the pull. Default is `5m`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_image_pull_progress_timeout: 5m
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Applies to the containerd CRI image pull configuration.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
