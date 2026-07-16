---
id: VARIABLE-DL_K8S_IO_URL
type: variable
title: dl_k8s_io_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - dl_k8s_io_url
tags:
  - download
  - url
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Base URL for downloading Kubernetes binaries from dl.k8s.io."
relations: []
---

# dl_k8s_io_url

## Summary
Sets the base URL used to download Kubernetes binaries (kubelet, kubeadm, kubectl, etc.). Default is `https://dl.k8s.io`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
dl_k8s_io_url: https://dl.k8s.io
```

The value `https://dl.k8s.io` is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present across Kubespray v2.29.0-v2.31.0. Used as the base for constructing Kubernetes binary download URLs; override for mirrors or offline setups.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
