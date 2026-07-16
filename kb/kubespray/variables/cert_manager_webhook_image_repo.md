---
id: VARIABLE-CERT_MANAGER_WEBHOOK_IMAGE_REPO
type: variable
title: cert_manager_webhook_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cert_manager_webhook_image_repo
tags:
  - cert-manager
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image repository for the cert-manager webhook component"
relations: []
---

# cert_manager_webhook_image_repo

## Summary
Container image repository for the cert-manager webhook component. Default resolves to the `jetstack/cert-manager-webhook` image under the configured quay registry.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cert_manager_webhook_image_repo: "{{ quay_image_repo }}/jetstack/cert-manager-webhook"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray `>=v2.29.0 <=v2.31.0`. Depends on `quay_image_repo`; used only when `cert_manager_enabled` is true. Related to `cert_manager_webhook_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
