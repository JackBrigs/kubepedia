---
id: VARIABLE-CONTAINERD_TOLERATE_MISSING_HUGETLB_CONTROLLER
type: variable
title: containerd_tolerate_missing_hugetlb_controller
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_tolerate_missing_hugetlb_controller
tags:
  - containerd
  - cgroups
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Whether containerd tolerates a missing hugetlb cgroup controller, defaults to true"
relations: []
---

# containerd_tolerate_missing_hugetlb_controller

## Summary
Controls the containerd CRI `tolerate_missing_hugetlb_controller` setting. When `true` (default), containerd does not fail if the hugetlb cgroup controller is absent. Rendered as a lowercased boolean into the containerd config.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_tolerate_missing_hugetlb_controller: true
```

(line 78 in v2.29.x, line 77 in v2.30.0/v2.31.0). Rendered in `templates/config.toml.j2` and `templates/config-v1.toml.j2` as `tolerate_missing_hugetlb_controller = {{ containerd_tolerate_missing_hugetlb_controller | lower }}`. Value is `true` and unchanged across v2.29.0–v2.31.0.

## Compatibility
Present and identical in v2.29.0–v2.31.0.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
