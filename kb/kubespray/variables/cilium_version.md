---
id: VARIABLE-CILIUM_VERSION
type: variable
title: cilium_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_version
tags:
  - cilium
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "cilium_version: 1.19.3 in v2.31.0 (differs per tag)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_version

## Summary

`cilium_version` pins the Cilium version Kubespray deploys and downloads. Unlike
most Cilium variables, this literal value CHANGES between tags. It drives
`cilium_image_tag` and `cilium_operator_image_tag`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The value
differs per tag:

| Tag | Value |
| --- | --- |
| v2.29.0 | `1.18.2` |
| v2.29.1 | `1.18.4` |
| v2.30.0 | `1.18.6` |
| v2.31.0 | `1.19.3` |

The value is a quoted string literal (e.g. `cilium_version: "1.19.3"`).

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: value increases with each tag.
- Related: `cilium_image_tag`, `cilium_operator_image_tag` (both derive
  `v{{ cilium_version }}`).

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
