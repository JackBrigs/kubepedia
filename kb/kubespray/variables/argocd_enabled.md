---
id: VARIABLE-ARGOCD_ENABLED
type: variable
title: argocd_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - argocd_enabled
tags:
  - argocd
  - addon
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles deployment of the Argo CD addon; default false"
relations: []
---

# argocd_enabled

## Summary
Toggles installation of the Argo CD addon. Default is `false` (Argo CD is not deployed).

## Implementation
Defined as `argocd_enabled: false` in both `roles/kubespray_defaults/defaults/main/main.yml` and the addon role `roles/kubernetes-apps/argocd/defaults/main.yml`. It is also exposed (commented/false) in `inventory/sample/group_vars/k8s_cluster/addons.yml`. The default value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `argocd_version`, `argocd_install_url`, `argocd_install_checksum`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/kubernetes-apps/argocd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
