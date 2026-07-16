---
id: VARIABLE-CSI_ATTACHER_IMAGE_REPO
type: variable
title: csi_attacher_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - csi_attacher_image_repo
tags:
  - csi
  - images
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "computed repo path for the CSI external-attacher sidecar image"
relations: []
---

# csi_attacher_image_repo

## Summary

`csi_attacher_image_repo` is the container image repository for the CSI
external-attacher sidecar. It is derived from `kube_image_repo` with the
`/sig-storage/csi-attacher` suffix.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
csi_attacher_image_repo: "{{ kube_image_repo }}/sig-storage/csi-attacher"
```

The expression is unchanged across v2.29.0-v2.31.0. The resulting repository depends
on `kube_image_repo`.

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `kube_image_repo`, `csi_attacher_image_tag`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
