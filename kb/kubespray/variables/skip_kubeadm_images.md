---
id: VARIABLE-SKIP_KUBEADM_IMAGES
type: variable
title: skip_kubeadm_images
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - skip_kubeadm_images
tags:
  - download
  - kubeadm
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Toggle to skip downloading kubeadm-managed images; false by default"
relations: []
---

# skip_kubeadm_images

## Summary
Boolean toggle controlling whether the kubeadm-managed images are skipped during the download phase. Disabled (`false`) by default.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
skip_kubeadm_images: false
```

The default is unchanged across v2.29.0-v2.31.0 (line 23 in v2.29.0, 25 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the download-role image handling.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
