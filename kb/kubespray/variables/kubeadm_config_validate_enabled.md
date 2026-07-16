---
id: VARIABLE-KUBEADM_CONFIG_VALIDATE_ENABLED
type: variable
title: kubeadm_config_validate_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_config_validate_enabled
tags:
  - kubeadm
  - validation
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Enables validation of generated kubeadm config, default true"
relations: []
---

# kubeadm_config_validate_enabled

## Summary
Controls whether Kubespray validates the generated kubeadm configuration. Default is `true`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `kubeadm_config_validate_enabled: true`. The value is unchanged across v2.29.0-v2.31.0; only the line number shifts (line 39 in v2.29.0/v2.29.1/v2.30.0, line 38 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
