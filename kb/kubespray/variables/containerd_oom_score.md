---
id: VARIABLE-CONTAINERD_OOM_SCORE
type: variable
title: containerd_oom_score
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_oom_score
tags:
  - containerd
  - oom
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "oom_score value written to the containerd config; default 0"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_oom_score

## Summary
Sets the `oom_score` for the containerd daemon in its configuration, influencing the OOM killer's ranking of the containerd process. Default is `0`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_oom_score: 0
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Applies only when the container runtime is containerd; rendered into the containerd configuration.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
