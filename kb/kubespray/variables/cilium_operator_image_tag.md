---
id: VARIABLE-CILIUM_OPERATOR_IMAGE_TAG
type: variable
title: cilium_operator_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_operator_image_tag
tags:
  - cilium
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "cilium_operator_image_tag: v{{ cilium_version }} (unchanged expression v2.29.0-v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_operator_image_tag

## Summary

`cilium_operator_image_tag` is the container image tag for the Cilium operator
image. It is a computed expression prefixing `cilium_version` with `v`, unchanged
across `v2.29.0`-`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cilium_operator_image_tag: "v{{ cilium_version }}"
```

The expression is identical across all four tags (line 242 in v2.29.0, 244 in
v2.29.1/v2.30.0, 238 in v2.31.0). The resolved tag tracks `cilium_version`, which
itself differs per tag (1.18.2 / 1.18.4 / 1.18.6 / 1.19.3).

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `cilium_version`, `cilium_operator_image_repo`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
