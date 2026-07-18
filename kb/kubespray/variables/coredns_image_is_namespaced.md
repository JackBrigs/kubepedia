---
id: VARIABLE-COREDNS_IMAGE_IS_NAMESPACED
type: variable
title: coredns_image_is_namespaced
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - coredns_image_is_namespaced
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray-defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.27.1/roles/kubespray-defaults/defaults/main/download.yml
    note: "default: {{ (coredns_version is version('v1.7.1', '>=')) }}"
relations: []
---
<!-- generated: variable-stub -->

# coredns_image_is_namespaced

## Summary

Kubespray variable `coredns_image_is_namespaced` — default `{{ (coredns_version is version('v1.7.1', '>=')) }}`. Defined in `roles/kubespray-defaults/defaults/main/download.yml`. Present in Kubespray
`v2.27.0`–`v2.27.1` of the indexed range. **Removed after `v2.27.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray-defaults/defaults/main/download.yml` (Kubespray `v2.27.1`):

```yaml
coredns_image_is_namespaced: {{ (coredns_version is version('v1.7.1', '>=')) }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.27.1`. **Removed after `v2.27.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray-defaults/defaults/main/download.yml` (Kubespray `v2.27.1`).
