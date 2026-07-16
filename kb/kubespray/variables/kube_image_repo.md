---
id: VARIABLE-KUBE_IMAGE_REPO
type: variable
title: kube_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_image_repo
tags:
  - images
  - registry
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Registry for core Kubernetes images; default registry.k8s.io"
relations: []
---

# kube_image_repo

## Summary
Container registry from which core Kubernetes images (kube-apiserver, kube-controller-manager, kube-scheduler, kube-proxy, etc.) are pulled. Default: `registry.k8s.io`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
kube_image_repo: "registry.k8s.io"
```

The default is unchanged across v2.29.0–v2.31.0 (line 90 in v2.29.0, line 92 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0–v2.31.0. Used as the base for constructing image references of the core Kubernetes components; override for mirrors or offline/air-gapped registries.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
