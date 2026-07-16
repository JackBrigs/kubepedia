---
id: VARIABLE-DNSAUTOSCALER_IMAGE_TAG
type: variable
title: dnsautoscaler_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - dnsautoscaler_image_tag
tags:
  - dns
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Container image tag for the DNS cluster-proportional-autoscaler"
relations: []
---

# dnsautoscaler_image_tag

## Summary
Container image tag for the DNS cluster-proportional-autoscaler. Defaults to `v{{ dnsautoscaler_version }}`, i.e. the `dnsautoscaler_version` value prefixed with `v` (currently `v1.8.8`).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
dnsautoscaler_image_tag: "v{{ dnsautoscaler_version }}"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `dnsautoscaler_version`; paired with `dnsautoscaler_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
