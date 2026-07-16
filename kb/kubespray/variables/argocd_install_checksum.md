---
id: VARIABLE-ARGOCD_INSTALL_CHECKSUM
type: variable
title: argocd_install_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - argocd_install_checksum
tags:
  - argocd
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Checksum of the Argo CD install manifest, looked up by argocd_version"
relations: []
---

# argocd_install_checksum

## Summary
Checksum of the Argo CD install manifest, used to verify the downloaded `install.yaml`. Computed by looking up the current `argocd_version` in the `argocd_install_checksums.no_arch` map.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:
```yaml
argocd_install_checksum: "{{ argocd_install_checksums.no_arch[argocd_version] }}"
```
The `argocd_install_checksums` map lives in `roles/kubespray_defaults/vars/main/checksums.yml`. This computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `argocd_version` and `argocd_install_checksums`; paired with `argocd_install_url`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
