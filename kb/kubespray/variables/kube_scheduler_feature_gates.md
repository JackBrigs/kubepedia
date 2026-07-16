---
id: VARIABLE-KUBE_SCHEDULER_FEATURE_GATES
type: variable
title: kube_scheduler_feature_gates
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_scheduler_feature_gates
tags:
  - kube-scheduler
  - feature-gates
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kube_scheduler_feature_gates, default []"
relations: []
---

# kube_scheduler_feature_gates

## Summary
List of feature gates to enable or disable for the kube-scheduler component. Defaults to an empty list `[]`, meaning no scheduler-specific feature gates are set beyond upstream/global defaults.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_scheduler_feature_gates: []
```

The default value `[]` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The line number shifts between tags (604 in v2.29.0/v2.29.1, 605 in v2.30.0, 624 in v2.31.0) but the definition and default are identical.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related: `kube_feature_gates`, `kube_apiserver_feature_gates`, `kube_controller_feature_gates`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
