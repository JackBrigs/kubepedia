---
id: VARIABLE-KUBELET_SHUTDOWN_GRACE_PERIOD_CRITICAL_PODS
type: variable
title: kubelet_shutdown_grace_period_critical_pods
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_shutdown_grace_period_critical_pods
tags:
  - kubelet
  - shutdown
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Portion of the shutdown grace period reserved for critical pods; default 20s"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_shutdown_grace_period_critical_pods

## Summary
Portion of the node shutdown grace period reserved for critical pods (kubelet `shutdownGracePeriodCriticalPods`). Default is `20s`. Per the inline comment, it should be less than `kubelet_shutdown_grace_period` (default 60s).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kubelet_shutdown_grace_period_critical_pods: 20s
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Line moves across tags (309 in v2.29.0/v2.29.1, 310 in v2.30.0, 322 in v2.31.0) but the value is constant.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Must be smaller than `kubelet_shutdown_grace_period`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
