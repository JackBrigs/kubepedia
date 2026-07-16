---
id: VARIABLE-CRI_SOCKET
type: variable
title: cri_socket
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cri_socket
tags:
  - cri
  - container-runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "CRI runtime socket path, selected by container_manager"
relations: []
---

# cri_socket

## Summary
The CRI (Container Runtime Interface) socket path used by kubelet / kubeadm. It
is computed from `container_manager`, resolving to the crio, containerd, or
cri-dockerd socket accordingly.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a Jinja
conditional, identical across all four tags:

```yaml
cri_socket: >-
  {%- if container_manager == 'crio' -%}
  unix:///var/run/crio/crio.sock
  {%- elif container_manager == 'containerd' -%}
  unix:///var/run/containerd/containerd.sock
  {%- elif container_manager == 'docker' -%}
  unix:///var/run/cri-dockerd.sock
  {%- endif -%}
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only
the line number shifts between tags).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `container_manager`
(`crio`, `containerd`, or `docker`).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
