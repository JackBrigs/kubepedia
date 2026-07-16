---
id: VARIABLE-KUBE_VIP_IMAGE_TAG
type: variable
title: kube_vip_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_image_tag
tags:
  - kube-vip
  - image
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the kube-vip container image tag"
relations: []
---

# kube_vip_image_tag

## Summary
Container image tag for the kube-vip image. The default changed between releases: a hardcoded tag in v2.29.x, and a value derived from `kube_vip_version` from v2.30.0 onward.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The default differs between tags:

| Tag | Value |
|-----|-------|
| v2.29.0 | `v0.8.9` |
| v2.29.1 | `v0.8.9` |
| v2.30.0 | `"v{{ kube_vip_version }}"` |
| v2.31.0 | `"v{{ kube_vip_version }}"` |

In v2.30.0/v2.31.0 the tag is computed by prefixing `v` to `kube_vip_version` (which is `1.0.3`), yielding `v1.0.3`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_vip_version`, `kube_vip_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
