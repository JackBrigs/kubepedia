---
id: VARIABLE-KUBELET_CHECKSUMS
type: variable
title: kubelet_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_checksums
tags:
  - kubelet
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Map of kubelet binary sha256 checksums keyed by architecture and Kubernetes version"
relations: []
---

# kubelet_checksums

## Summary
A nested mapping of kubelet binary checksums, keyed first by CPU architecture (for example `arm64`, `amd64`) and then by Kubernetes version, with each entry a `sha256:` digest. It is the source map consumed by `kubelet_binary_checksum`.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` as a dictionary:

```yaml
kubelet_checksums:
  arm64:
    1.35.4: sha256:d710eef03bb4ad164bb77af9be5b11b44f874e2fc08153c7d383420d685f73e8
    ...
```

The variable exists in all four tags (line 112 in v2.29.0, line 70 in v2.31.0). Its structure is unchanged; the enumerated architectures and per-version digests differ between tags as the supported Kubernetes versions and their released binaries change.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `kubelet_binary_checksum` via `kubelet_checksums[image_arch][kube_version]`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
