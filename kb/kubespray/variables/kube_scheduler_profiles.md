---
id: VARIABLE-KUBE_SCHEDULER_PROFILES
type: variable
title: kube_scheduler_profiles
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_scheduler_profiles
tags:
  - kube-scheduler
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    note: "Defines kube_scheduler_profiles, default []"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_scheduler_profiles

## Summary
List of scheduling profiles (dicts) supported by kube-scheduler. Defaults to an empty list `[]`, meaning no custom scheduling profiles are configured.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml` (line 30):

```yaml
kube_scheduler_profiles: []
```

The default value `[]` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related: `kube_scheduler_extenders`, `kube_scheduler_config_extra_opts`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
