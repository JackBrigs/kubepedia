---
id: VARIABLE-INGRESS_ALB_ENABLED
type: variable
title: ingress_alb_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ingress_alb_enabled
tags:
  - ingress
  - addons
  - aws
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles deployment of the AWS ALB ingress controller, defaults to false"
relations: []
---

# ingress_alb_enabled

## Summary
Enables or disables deployment of the AWS ALB (Application Load Balancer) ingress controller addon. It defaults to `false` (the addon is not installed).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
ingress_alb_enabled: false
```

Also surfaced in the sample inventory at `inventory/sample/group_vars/k8s_cluster/addons.yml`. The value `false` is unchanged across v2.29.0–v2.31.0 (defaults line 459 in v2.29.0/v2.29.1, 460 in v2.30.0, 467 in v2.31.0; addons.yml line 104 in v2.29.0–v2.30.0, 67 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related to other `alb_ingress_*` addon variables.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/addons.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
