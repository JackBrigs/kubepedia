---
id: VARIABLE-KUBELET_DOWNLOAD_URL
type: variable
title: kubelet_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_download_url
tags:
  - kubelet
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "URL from which the kubelet binary is downloaded; computed from dl_k8s_io_url, kube_version, image_arch"
relations: []
---

# kubelet_download_url

## Summary
URL from which the kubelet binary is downloaded. Computed from the download mirror, the target Kubernetes version, and the node architecture.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as a computed expression:

```yaml
kubelet_download_url: "{{ dl_k8s_io_url }}/release/v{{ kube_version }}/bin/linux/{{ image_arch }}/kubelet"
```

This expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 154 in v2.29.0, line 156 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `dl_k8s_io_url`, `kube_version`, and `image_arch`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
