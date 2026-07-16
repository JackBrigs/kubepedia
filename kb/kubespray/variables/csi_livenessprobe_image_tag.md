---
id: VARIABLE-CSI_LIVENESSPROBE_IMAGE_TAG
type: variable
title: csi_livenessprobe_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - csi_livenessprobe_image_tag
tags:
  - csi
  - download
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the sig-storage csi-livenessprobe sidecar image."
relations: []
---

# csi_livenessprobe_image_tag

## Summary
Sets the container image tag for the CSI livenessprobe sidecar used by CSI drivers. Default changes between versions: `v2.5.0` in v2.29.0/v2.29.1 and `v2.11.0` in v2.30.0/v2.31.0.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The value differs between tags:

| Tag | Value |
|-----|-------|
| v2.29.0 | `v2.5.0` |
| v2.29.1 | `v2.5.0` |
| v2.30.0 | `v2.11.0` |
| v2.31.0 | `v2.11.0` |

## Compatibility
Present across Kubespray v2.29.0-v2.31.0. Paired with the repo variable `csi_livenessprobe_image_repo`. Consumed as part of the CSI sidecar image set.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
