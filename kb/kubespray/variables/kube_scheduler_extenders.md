---
id: VARIABLE-KUBE_SCHEDULER_EXTENDERS
type: variable
title: kube_scheduler_extenders
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_scheduler_extenders
tags:
  - kube-scheduler
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    note: "Defines kube_scheduler_extenders, default []"
relations: []
---

# kube_scheduler_extenders

## Summary
List of kube-scheduler extenders (dicts), each holding the values of how to communicate with the extender. Defaults to an empty list `[]`, meaning no scheduler extenders are configured.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml` (line 17):

```yaml
kube_scheduler_extenders: []
```

The default value `[]` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related kube-scheduler configuration variables in the same file: `kube_scheduler_config_extra_opts`, `kube_scheduler_profiles`, `kube_scheduler_leader_elect_extra_opts`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
