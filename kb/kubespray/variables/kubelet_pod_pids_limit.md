---
id: VARIABLE-KUBELET_POD_PIDS_LIMIT
type: variable
title: kubelet_pod_pids_limit
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_pod_pids_limit
tags:
  - kubelet
  - limits
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Per-pod PID limit enforced by the kubelet (podPidsLimit); default -1 (unlimited)"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_pod_pids_limit

## Summary
Maximum number of process IDs (PIDs) allowed per pod, enforced by the kubelet (maps to the kubelet `podPidsLimit` setting). Default is `-1`, meaning no limit.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_pod_pids_limit: -1
```

Line number: 119 (v2.29.0/v2.29.1), 116 (v2.30.0), 118 (v2.31.0). The value `-1` is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. A value of `-1` disables the per-pod PID limit; set a positive integer to cap PIDs per pod.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
