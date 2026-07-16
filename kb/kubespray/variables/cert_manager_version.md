---
id: VARIABLE-CERT_MANAGER_VERSION
type: variable
title: cert_manager_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cert_manager_version
tags:
  - cert-manager
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Version of cert-manager deployed; default 1.15.3"
relations: []
---

# cert_manager_version

## Summary
Version of the cert-manager addon deployed by Kubespray. Default value is `1.15.3`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cert_manager_version: "1.15.3"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. It feeds the `v{{ cert_manager_version }}` image tags for the controller, cainjector, and webhook components.

## Compatibility
Available in Kubespray `>=v2.29.0 <=v2.31.0`. Used only when `cert_manager_enabled` is true; drives `cert_manager_controller_image_tag`, `cert_manager_cainjector_image_tag`, and `cert_manager_webhook_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
