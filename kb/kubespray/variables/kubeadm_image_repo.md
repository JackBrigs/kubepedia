---
id: VARIABLE-KUBEADM_IMAGE_REPO
type: variable
title: kubeadm_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_image_repo
tags:
  - kubeadm
  - images
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines kubeadm_image_repo defaulting to kube_image_repo"
relations: []
---

# kubeadm_image_repo

## Summary
Container image registry used for kubeadm-managed control-plane images. Defaults to the value of `kube_image_repo` (which is `registry.k8s.io`).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
kubeadm_image_repo: "{{ kube_image_repo }}"
```

The definition is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 91 in v2.29.0, line 93 in v2.29.1/v2.30.0/v2.31.0). `kube_image_repo` defaults to `registry.k8s.io` in the same file.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related variables: `kube_image_repo`, `kubeadm_images`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
