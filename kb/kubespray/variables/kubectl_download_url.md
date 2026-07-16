---
id: VARIABLE-KUBECTL_DOWNLOAD_URL
type: variable
title: kubectl_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubectl_download_url
tags:
  - kubectl
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "URL used to download the kubectl binary"
relations: []
---

# kubectl_download_url

## Summary
The download URL for the `kubectl` binary, built from the Kubernetes release
mirror, the target Kubernetes version, and the target architecture. Default:
`{{ dl_k8s_io_url }}/release/v{{ kube_version }}/bin/linux/{{ image_arch }}/kubectl`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:
`kubectl_download_url: "{{ dl_k8s_io_url }}/release/v{{ kube_version }}/bin/linux/{{ image_arch }}/kubectl"`.
The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 155
in v2.29.0, 157 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `dl_k8s_io_url`, `kube_version`, and
`image_arch`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
