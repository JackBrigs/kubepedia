---
id: VARIABLE-KUBELET_SHUTDOWN_GRACE_PERIOD
type: variable
title: kubelet_shutdown_grace_period
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_shutdown_grace_period
tags:
  - kubelet
  - shutdown
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Total graceful node shutdown period for kubelet; default 60s"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_shutdown_grace_period

## Summary
Total duration kubelet grants for graceful node shutdown (the kubelet `shutdownGracePeriod`). Default is `60s`. The critical-pods portion (`kubelet_shutdown_grace_period_critical_pods`) must be less than this value.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kubelet_shutdown_grace_period: 60s
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Line moves across tags (306 in v2.29.0/v2.29.1, 307 in v2.30.0, 319 in v2.31.0) but the value is constant.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Pairs with `kubelet_shutdown_grace_period_critical_pods`, which should be smaller.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
