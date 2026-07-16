---
id: VARIABLE-APISERVER_EXTRA_VOLUMES
type: variable
title: apiserver_extra_volumes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - apiserver_extra_volumes
tags:
  - control-plane
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines extra host volume mounts for the kube-apiserver; default {} (empty mapping)."
relations: []
---

# apiserver_extra_volumes

## Summary
Defines additional host-path volumes to mount into the kube-apiserver static pod (extra control plane host volume mounts). Each entry provides `name`, `hostPath`, `mountPath`, and optional `readOnly`. Default is an empty mapping `{}`, meaning no extra volumes are added.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `apiserver_extra_volumes: {}`. The commented example in the same file shows the expected list form (`name`, `hostPath`, `mountPath`, `readOnly`). The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Sibling variables in the same file include `controller_manager_extra_volumes` and `scheduler_extra_volumes`. Typically used together with audit-log/audit-policy variables when custom host paths must be exposed to the apiserver.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
