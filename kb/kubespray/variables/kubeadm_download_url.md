---
id: VARIABLE-KUBEADM_DOWNLOAD_URL
type: variable
title: kubeadm_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_download_url
tags:
  - kubeadm
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed download URL for the kubeadm binary"
relations: []
---

# kubeadm_download_url

## Summary
The download URL for the kubeadm binary. Computed from `dl_k8s_io_url`, the requested `kube_version`, and the target `image_arch`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```
kubeadm_download_url: "{{ dl_k8s_io_url }}/release/v{{ kube_version }}/bin/linux/{{ image_arch }}/kubeadm"
```

The computed expression is unchanged across v2.29.0-v2.31.0; only the line number shifts (156 in v2.29.0, 158 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `dl_k8s_io_url`, `kube_version`, `image_arch`, `kubeadm_binary_checksum`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
