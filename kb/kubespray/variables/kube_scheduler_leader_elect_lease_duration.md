---
id: VARIABLE-KUBE_SCHEDULER_LEADER_ELECT_LEASE_DURATION
type: variable
title: kube_scheduler_leader_elect_lease_duration
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_scheduler_leader_elect_lease_duration
tags:
  - kube-scheduler
  - leader-election
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    note: "Defines kube_scheduler_leader_elect_lease_duration, default 15s"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_scheduler_leader_elect_lease_duration

## Summary
Leader election lease duration for the kube-scheduler. Defaults to `15s`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml` (line 24):

```yaml
kube_scheduler_leader_elect_lease_duration: 15s
```

The default value `15s` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related: `kube_scheduler_leader_elect_renew_deadline`, `kube_scheduler_leader_elect_extra_opts`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
