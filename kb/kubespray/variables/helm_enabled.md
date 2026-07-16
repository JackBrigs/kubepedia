---
id: VARIABLE-HELM_ENABLED
type: variable
title: helm_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - helm_enabled
tags:
  - helm
  - addons
sources:
  - type: code
    path: roles/kubernetes-apps/helm/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/helm/defaults/main.yml
    note: "Toggle to install the Helm client on control-plane nodes; default false"
relations: []
---

# helm_enabled

## Summary
Boolean toggle that controls whether Kubespray installs the Helm client as an addon. Default is `false`, so Helm is not installed unless the user opts in.

## Implementation
Defined as `helm_enabled: false` in three consistent places:
`roles/kubernetes-apps/helm/defaults/main.yml`, `roles/kubespray_defaults/defaults/main/main.yml`, and the sample inventory `inventory/sample/group_vars/k8s_cluster/addons.yml`.

The default value `false` is unchanged across v2.29.0-v2.31.0 (line numbers shift between tags but the value does not).

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `helm_version`, `helm_download_url`.

## References
- roles/kubernetes-apps/helm/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/addons.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
