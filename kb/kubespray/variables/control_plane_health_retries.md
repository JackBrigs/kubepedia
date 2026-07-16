---
id: VARIABLE-CONTROL_PLANE_HEALTH_RETRIES
type: variable
title: control_plane_health_retries
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - control_plane_health_retries
tags:
  - control-plane
  - healthcheck
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Number of retries for apiserver/scheduler/controller-manager health checks, defaults to 60"
relations: []
---

# control_plane_health_retries

## Summary
The number of retries used when polling the health of the control-plane components (kube-apiserver, kube-scheduler, kube-controller-manager). Default is `60`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
control_plane_health_retries: 60  # Default retries for apiserver, scheduler, controller-manager health checks
```

(line 35 in v2.29.x, line 38 in v2.30.0/v2.31.0). Consumed in `roles/kubernetes/control-plane/handlers/main.yml` as `retries: "{{ control_plane_health_retries }}"` for the apiserver, scheduler, and controller-manager health-check handlers. Value is `60` and unchanged across v2.29.0–v2.31.0.

## Compatibility
Present and identical in v2.29.0–v2.31.0.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubernetes/control-plane/handlers/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
