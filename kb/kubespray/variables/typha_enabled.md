---
id: VARIABLE-TYPHA_ENABLED
type: variable
title: typha_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - typha_enabled
tags:
  - calico
  - cni
sources:
  - type: code
    path: roles/network_plugin/calico_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/calico_defaults/defaults/main.yml
    note: "Toggles the Calico Typha component: false"
relations: []
---

# typha_enabled

## Summary
Boolean toggle that enables Typha, the Calico datastore-scaling component that fans out datastore updates to Felix agents. Default is `false` (disabled).

## Implementation
Defined in `roles/network_plugin/calico_defaults/defaults/main.yml` as `typha_enabled: false` (line 131, unchanged across all four tags). The same default is also declared in `roles/kubespray_defaults/defaults/main/main.yml` and (for download/image resolution) `roles/kubespray_defaults/defaults/main/download.yml`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-net-calico.yml` shows a commented `typha_enabled: false`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies to the Calico CNI plugin.

## References
- roles/network_plugin/calico_defaults/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
