---
id: VARIABLE-KUBE_VIP_VERSION
type: variable
title: kube_vip_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_version
tags:
  - kube-vip
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the kube-vip component version"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_version

## Summary
The kube-vip component version deployed by Kubespray. Both the default value and its defining file changed between releases: `0.8.0` in v2.29.x (in the node role defaults) and `1.0.3` from v2.30.0 (moved into kubespray_defaults download.yml).

## Implementation
The default and its location differ between tags:

| Tag | Value | Defining file |
|-----|-------|---------------|
| v2.29.0 | `0.8.0` | roles/kubernetes/node/defaults/main.yml (line 64) |
| v2.29.1 | `0.8.0` | roles/kubernetes/node/defaults/main.yml (line 64) |
| v2.30.0 | `1.0.3` | roles/kubespray_defaults/defaults/main/download.yml (line 268) |
| v2.31.0 | `1.0.3` | roles/kubespray_defaults/defaults/main/download.yml (line 262) |

From v2.30.0 the value drives `kube_vip_image_tag` via `"v{{ kube_vip_version }}"`. The kube-vip manifest template in v2.31.0 also branches on this version (`kube_vip_version is version('0.9.0', '>=')`).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_vip_image_tag`, `kube_vip_image_repo`.

## References
- roles/kubernetes/node/defaults/main.yml (v2.29.0, v2.29.1)
- roles/kubespray_defaults/defaults/main/download.yml (v2.30.0, v2.31.0)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
