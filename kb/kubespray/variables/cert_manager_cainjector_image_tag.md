---
id: VARIABLE-CERT_MANAGER_CAINJECTOR_IMAGE_TAG
type: variable
title: cert_manager_cainjector_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cert_manager_cainjector_image_tag
tags:
  - cert-manager
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the cert-manager cainjector; derived from cert_manager_version"
relations: []
---

# cert_manager_cainjector_image_tag

## Summary
Container image tag for the cert-manager cainjector component. Default is derived from `cert_manager_version`, resolving to `v1.15.3`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cert_manager_cainjector_image_tag: "v{{ cert_manager_version }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0; since `cert_manager_version` is `1.15.3` in all four tags, it resolves to `v1.15.3`.

## Compatibility
Available in Kubespray `>=v2.29.0 <=v2.31.0`. Depends on `cert_manager_version`; used only when `cert_manager_enabled` is true. Related to `cert_manager_cainjector_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
