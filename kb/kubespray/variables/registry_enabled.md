---
id: VARIABLE-REGISTRY_ENABLED
type: variable
title: registry_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - registry_enabled
tags:
  - registry
  - addons
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggle for deploying the in-cluster container registry addon; default false"
relations: []
---

# registry_enabled

## Summary
Boolean toggle that controls whether Kubespray deploys the in-cluster Docker registry addon. Defaults to `false`.

## Implementation
Defined as a role default in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
registry_enabled: false
```

Also exposed to users in the sample inventory `inventory/sample/group_vars/k8s_cluster/addons.yml` with the same value `false`. Both are unchanged across v2.29.0-v2.31.0 (role default at line 444 in v2.29.0, line 453 in v2.31.0; sample inventory at line 10 in v2.29.0, line 6 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. When enabled, the registry addon uses `registry_image_repo`, `registry_image_tag`, and `registry_version`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/addons.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
