---
id: VARIABLE-KUBELET_FAIL_CGROUP_V1
type: variable
title: kubelet_fail_cgroup_v1
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_fail_cgroup_v1
tags:
  - kubelet
  - cgroups
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Kubernetes 1.35+: fail on cgroup v1 by default; default true"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_fail_cgroup_v1

## Summary
Controls whether the kubelet fails to start on cgroup v1 hosts. Introduced in v2.31.0 with the comment "Kubernetes 1.35+: fail on cgroup v1 by default". Default is `true`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` (line 21 in v2.31.0):

```yaml
# Kubernetes 1.35+: fail on cgroup v1 by default
kubelet_fail_cgroup_v1: true
```

This variable does NOT exist in v2.29.0, v2.29.1, or v2.30.0 — grep returns no match in those tags. It was introduced in v2.31.0.

## Compatibility
Kubespray v2.31.0 only (not present in earlier indexed tags). Related to the cgroup v1/v2 host configuration.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
