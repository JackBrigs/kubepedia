---
id: VARIABLE-KUBE_VIP_ENABLED
type: variable
title: kube_vip_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_enabled
tags:
  - kube-vip
  - loadbalancer
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Master switch for kube-vip; default false"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_enabled

## Summary
Master switch that enables deployment of kube-vip as the API server load balancer / VIP provider. Default is `false`. Also gates whether the kube-vip container image is included in the downloads (`kube_vip_enabled` controls the `enabled` field of the kube-vip download entry).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `kube_vip_enabled: false`. The value is unchanged across v2.29.0-v2.31.0. Referenced in `roles/kubespray_defaults/defaults/main/download.yml` as `enabled: "{{ kube_vip_enabled }}"` for the kube-vip download.

## Compatibility
Kubespray v2.29.0 through v2.31.0. When `true`, additional kube-vip variables (`kube_vip_controlplane_enabled`, `kube_vip_interface`, `kube_vip_lb_enable`, BGP options) take effect.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
