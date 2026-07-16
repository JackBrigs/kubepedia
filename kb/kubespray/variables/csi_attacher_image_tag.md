---
id: VARIABLE-CSI_ATTACHER_IMAGE_TAG
type: variable
title: csi_attacher_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - csi_attacher_image_tag
tags:
  - csi
  - images
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "image tag of the CSI external-attacher sidecar; changed v3.3.0 -> v4.4.2 at v2.30.0"
relations: []
---

# csi_attacher_image_tag

## Summary

`csi_attacher_image_tag` pins the image tag (version) of the CSI external-attacher
sidecar. Its default value changed between the indexed tags: `v3.3.0` up to v2.29.1
and `v4.4.2` from v2.30.0 onward.

## Implementation

Defined as a literal string in `roles/kubespray_defaults/defaults/main/download.yml`.
The value differs between tags:

| Tag      | csi_attacher_image_tag |
|----------|------------------------|
| v2.29.0  | `v3.3.0`               |
| v2.29.1  | `v3.3.0`               |
| v2.30.0  | `v4.4.2`               |
| v2.31.0  | `v4.4.2`               |

## Compatibility

- Kubespray `v2.29.0`-`v2.29.1`: `v3.3.0`.
- Kubespray `v2.30.0`-`v2.31.0`: `v4.4.2`.
- Related: `csi_attacher_image_repo`, `kube_image_repo`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
