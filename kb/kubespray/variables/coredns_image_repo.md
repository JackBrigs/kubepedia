---
id: VARIABLE-COREDNS_IMAGE_REPO
type: variable
title: coredns_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - coredns_image_repo
tags:
  - coredns
  - dns
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computes the CoreDNS image repository path"
relations: []
---

# coredns_image_repo

## Summary
The container image repository for CoreDNS. Built from `kube_image_repo`, inserting a `/coredns` segment for CoreDNS versions `>= 1.7.1`, and always ending in `/coredns`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
coredns_image_repo: "{{ kube_image_repo }}{{ '/coredns' if coredns_version is version('1.7.1', '>=') else '' }}/coredns"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only line numbers shift).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related: `kube_image_repo`, `coredns_version`, `coredns_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
