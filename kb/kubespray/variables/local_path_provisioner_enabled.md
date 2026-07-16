---
id: VARIABLE-LOCAL_PATH_PROVISIONER_ENABLED
type: variable
title: local_path_provisioner_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local_path_provisioner_enabled
tags:
  - storage
  - addons
sources:
  - type: code
    path: roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml
    note: "Defines local_path_provisioner_enabled with default false"
relations: []
---

# local_path_provisioner_enabled

## Summary
Toggles deployment of the Rancher local-path-provisioner addon. Default is `false` (disabled).

## Implementation
Default is `false`, set consistently in several places:

- `roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml`
- `roles/kubespray_defaults/defaults/main/main.yml`
- `inventory/sample/group_vars/k8s_cluster/addons.yml`

```yaml
local_path_provisioner_enabled: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Gates the related `local_path_provisioner_*` variables (image repo, tag, version).

## References
- roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
