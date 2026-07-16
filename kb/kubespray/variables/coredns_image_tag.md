---
id: VARIABLE-COREDNS_IMAGE_TAG
type: variable
title: coredns_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - coredns_image_tag
tags:
  - coredns
  - dns
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computes the CoreDNS image tag"
relations: []
---

# coredns_image_tag

## Summary
The image tag for the CoreDNS container image. Equals the CoreDNS version, prefixed with `v` for versions `>= 1.7.1`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
coredns_image_tag: "{{ 'v' if coredns_version is version('1.7.1', '>=') else '' }}{{ coredns_version }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only line numbers shift). The concrete value depends on `coredns_version` in each tag.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related: `coredns_version`, `coredns_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
