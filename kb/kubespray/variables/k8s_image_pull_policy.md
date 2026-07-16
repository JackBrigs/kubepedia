---
id: VARIABLE-K8S_IMAGE_PULL_POLICY
type: variable
title: k8s_image_pull_policy
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - k8s_image_pull_policy
tags:
  - images
  - kubernetes
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Default imagePullPolicy applied to Kubernetes components, defaults to IfNotPresent"
relations: []
---

# k8s_image_pull_policy

## Summary
Sets the `imagePullPolicy` applied to Kubernetes component images. It defaults to `IfNotPresent`, so images already present on a node are not re-pulled.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
k8s_image_pull_policy: IfNotPresent
```

Also surfaced in the sample inventory at `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. The value `IfNotPresent` is unchanged across v2.29.0–v2.31.0 (defaults line 436 in v2.29.0/v2.29.1, 437 in v2.30.0, 449 in v2.31.0; inventory line 228 in v2.29.0/v2.29.1, 229 in v2.30.0, 244 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Accepts standard Kubernetes pull-policy values (`Always`, `IfNotPresent`, `Never`).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
