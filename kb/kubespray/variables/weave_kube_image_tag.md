---
id: VARIABLE-WEAVE_KUBE_IMAGE_TAG
type: variable
title: weave_kube_image_tag
status: active
kubespray_version: ">=v2.27.0 <=v2.28.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - weave_kube_image_tag
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/roles/kubespray_defaults/defaults/main/download.yml
    note: "default: {{ weave_version }}"
relations: []
---
<!-- generated: variable-stub -->

# weave_kube_image_tag

## Summary

Kubespray variable `weave_kube_image_tag` — default `{{ weave_version }}`. Defined in `roles/kubespray_defaults/defaults/main/download.yml`. Present in Kubespray
`v2.27.0`–`v2.28.1` of the indexed range. **Removed after `v2.28.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.28.1`):

```yaml
weave_kube_image_tag: {{ weave_version }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.28.1`. **Removed after `v2.28.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.28.1`).
