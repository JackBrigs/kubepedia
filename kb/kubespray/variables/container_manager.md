---
id: VARIABLE-CONTAINER_MANAGER
type: variable
title: container_manager
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - container_manager
tags:
  - container-runtime
  - containerd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "container_manager: containerd (default, unchanged v2.29.0–v2.31.0)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "container_manager == 'containerd'|'crio'|'docker' branches select the runtime role"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# container_manager

## Summary

`container_manager` selects the container runtime Kubespray installs and
configures on cluster nodes. The default is `containerd`, unchanged across
`v2.29.0`–`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` (`containerd`,
unchanged across all three tags). The value drives which container-engine role is
enabled — the same file gates roles on `container_manager == 'containerd'`,
`== 'crio'`, and `== 'docker'`.

Accepted values:

- `containerd` (default) — installs containerd from an archive
  (see [[COMPONENT-CONTAINERD]]).
- `crio` — installs CRI-O.
- `docker` — installs Docker with the cri-dockerd shim.

The value also switches derived helpers, e.g. `image_command_tool`
(`nerdctl` for containerd, `crictl` for crio) and enables container-runtime-
specific features such as NRI (containerd only).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `containerd`; accepted `containerd` |
  `crio` | `docker`.
- gVisor is supported only with `container_manager` `docker` or `containerd`.

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default and per-runtime
  branches (tags v2.29.0 `9991412`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`).
