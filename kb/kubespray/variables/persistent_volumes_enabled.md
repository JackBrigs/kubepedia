---
id: VARIABLE-PERSISTENT_VOLUMES_ENABLED
type: variable
title: persistent_volumes_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - persistent_volumes_enabled
tags:
  - storage
  - persistentvolume
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggle for enabling PersistentVolume support; default false."
relations: []
---

# persistent_volumes_enabled

## Summary
Toggle that enables PersistentVolume support in the cluster. The default is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
persistent_volumes_enabled: false
```

The same default is also exposed to users in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. Both role defaults and the sample inventory agree, and the value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (role-defaults line drifts from 457 in v2.29.0 to 466 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `expand_persistent_volumes`, cloud-provider CSI toggles.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
