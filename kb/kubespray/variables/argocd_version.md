---
id: VARIABLE-ARGOCD_VERSION
type: variable
title: argocd_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - argocd_version
tags:
  - argocd
  - version
sources:
  - type: code
    path: roles/kubernetes-apps/argocd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/argocd/defaults/main.yml
    note: "Argo CD version deployed by the addon; default 2.14.5"
relations: []
---

# argocd_version

## Summary
Version of Argo CD deployed by the addon. Default is `2.14.5`.

## Implementation
Defined as `argocd_version: 2.14.5` in `roles/kubernetes-apps/argocd/defaults/main.yml`. In `roles/kubespray_defaults/defaults/main/download.yml` it is also derived from the checksum table as `argocd_version: "{{ (argocd_install_checksums.no_arch | dict2items)[0].key }}"` (first key of `argocd_install_checksums.no_arch`). The default `2.14.5` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `argocd_install_url` and `argocd_install_checksum`; gated by `argocd_enabled`.

## References
- roles/kubernetes-apps/argocd/defaults/main.yml
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
