---
id: VARIABLE-ARGOCD_INSTALL_URL
type: variable
title: argocd_install_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - argocd_install_url
tags:
  - argocd
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "URL of the Argo CD install manifest for the selected argocd_version"
relations: []
---

# argocd_install_url

## Summary
URL from which the Argo CD install manifest (`install.yaml`) is downloaded, built from the selected `argocd_version`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:
```yaml
argocd_install_url: "https://raw.githubusercontent.com/argoproj/argo-cd/v{{ argocd_version }}/manifests/install.yaml"
```
This computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `argocd_version`; paired with `argocd_install_checksum`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
