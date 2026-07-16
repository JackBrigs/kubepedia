---
id: VARIABLE-CILIUM_IMAGE_REPO
type: variable
title: cilium_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_image_repo
tags:
  - cilium
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "cilium_image_repo derived from quay_image_repo/cilium/cilium (unchanged v2.29.0-v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_image_repo

## Summary

`cilium_image_repo` is the container image repository for the Cilium agent image.
It is a computed expression based on `quay_image_repo`, unchanged across
`v2.29.0`-`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cilium_image_repo: "{{ quay_image_repo }}/cilium/cilium"
```

The expression is identical across all four tags; only the line number shifts
(239 in v2.29.0, 241 in v2.29.1/v2.30.0, 235 in v2.31.0).

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `quay_image_repo`, `cilium_image_tag`, `cilium_version`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
