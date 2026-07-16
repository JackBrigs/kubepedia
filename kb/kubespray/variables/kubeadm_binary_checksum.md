---
id: VARIABLE-KUBEADM_BINARY_CHECKSUM
type: variable
title: kubeadm_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_binary_checksum
tags:
  - download
  - checksum
  - kubeadm
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed checksum for the kubeadm binary of the selected kube_version/arch"
relations:
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
---

# kubeadm_binary_checksum

## Summary
The expected checksum of the downloaded `kubeadm` binary, used to verify the download. It is not a literal value but a lookup into the `kubeadm_checksums` map, keyed by CPU architecture and Kubernetes version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
kubeadm_binary_checksum: "{{ kubeadm_checksums[image_arch][kube_version] }}"
```

The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 185 in v2.29.0, line 187 in v2.29.1/v2.30.0/v2.31.0). The resolved value depends on `image_arch` and `kube_version` via the `kubeadm_checksums` map.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Depends on `kubeadm_checksums`, `image_arch`, and `kube_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
