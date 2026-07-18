---
id: VARIABLE-RBD_PROVISIONER_IMAGE_TAG
type: variable
title: rbd_provisioner_image_tag
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - rbd_provisioner_image_tag
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray-defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.27.1/roles/kubespray-defaults/defaults/main/download.yml
    note: "default: {{ rbd_provisioner_version }}"
relations: []
---
<!-- generated: variable-stub -->

# rbd_provisioner_image_tag

## Summary

Kubespray variable `rbd_provisioner_image_tag` — default `{{ rbd_provisioner_version }}`. Defined in `roles/kubespray-defaults/defaults/main/download.yml`. Present in Kubespray
`v2.27.0`–`v2.27.1` of the indexed range. **Removed after `v2.27.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray-defaults/defaults/main/download.yml` (Kubespray `v2.27.1`):

```yaml
rbd_provisioner_image_tag: {{ rbd_provisioner_version }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.27.1`. **Removed after `v2.27.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray-defaults/defaults/main/download.yml` (Kubespray `v2.27.1`).
