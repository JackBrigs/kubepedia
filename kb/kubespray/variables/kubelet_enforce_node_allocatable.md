---
id: VARIABLE-KUBELET_ENFORCE_NODE_ALLOCATABLE
type: variable
title: kubelet_enforce_node_allocatable
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_enforce_node_allocatable
tags:
  - kubelet
  - allocatable
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "kubelet enforceNodeAllocatable value; default empty string to avoid cgroup creation"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_enforce_node_allocatable

## Summary
Controls the kubelet `enforceNodeAllocatable` setting. The default is an empty string, chosen to avoid cgroup creation for node-allocatable enforcement.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` (line 13) with the comment `# Set to empty to avoid cgroup creation`:

```yaml
kubelet_enforce_node_allocatable: "\"\""
```

The value is a quoted empty string (`""`). This default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 13 in all four tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `kube_reserved`, `system_reserved`, and the kubelet cgroup enforcement settings.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
