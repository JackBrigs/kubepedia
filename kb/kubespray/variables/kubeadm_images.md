---
id: VARIABLE-KUBEADM_IMAGES
type: variable
title: kubeadm_images
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_images
tags:
  - kubeadm
  - images
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines kubeadm_images: {} (empty mapping default)"
relations: []
---

# kubeadm_images

## Summary
Mapping of kubeadm-managed images to their download definitions. Default is an empty mapping (`{}`); it is populated dynamically during the download role's evaluation of kubeadm images.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
kubeadm_images: {}
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 24 in v2.29.0, line 26 in v2.29.1/v2.30.0/v2.31.0). Nearby, `skip_kubeadm_images: false` guards whether kubeadm images are downloaded.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related variables: `skip_kubeadm_images`, `kubeadm_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
