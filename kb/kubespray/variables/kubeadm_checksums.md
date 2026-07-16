---
id: VARIABLE-KUBEADM_CHECKSUMS
type: variable
title: kubeadm_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_checksums
tags:
  - download
  - checksum
  - kubeadm
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Map of per-arch, per-Kubernetes-version sha256 checksums for the kubeadm binary"
relations: []
---

# kubeadm_checksums

## Summary
A nested map holding the sha256 checksums of the `kubeadm` binary, keyed first by CPU architecture (`arm64`, `amd64`, etc.) and then by Kubernetes version. It is the lookup table backing `kubeadm_binary_checksum`.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml`, e.g. in v2.31.0:

```yaml
kubeadm_checksums:
  arm64:
    1.35.4: sha256:e8f6b5bee3e2c8b5965f4ae65c2ae04e3f9f426d2458a1e2f159e824d419d92c
    ...
```

The variable name and structure are unchanged, but its contents (the set of supported Kubernetes versions and their checksums) differ per tag as new Kubernetes releases are added. Its declaration line moves per tag: line 331 (v2.29.0), 371 (v2.29.1), 277 (v2.30.0), 254 (v2.31.0).

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Consumed by `kubeadm_binary_checksum` via `kubeadm_checksums[image_arch][kube_version]`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
