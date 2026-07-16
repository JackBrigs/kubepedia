---
id: VARIABLE-CONTROLLER_MANAGER_EXTRA_VOLUMES
type: variable
title: controller_manager_extra_volumes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - controller_manager_extra_volumes
tags:
  - control-plane
  - kubeadm
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines controller_manager_extra_volumes with default {} (empty dict)"
relations: []
---

# controller_manager_extra_volumes

## Summary
Extra host-path volumes to mount into the kube-controller-manager static pod, passed through to the kubeadm control-plane configuration. Default is an empty dict `{}`, i.e. no additional volumes.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
controller_manager_extra_volumes: {}
```

The default value `{}` is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0. Only the line number shifts (191 in v2.29.0/v2.29.1, 194 in v2.30.0/v2.31.0) due to surrounding edits.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Companion variable to `apiserver_extra_volumes`; consumed when rendering the kubeadm control-plane manifests.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
