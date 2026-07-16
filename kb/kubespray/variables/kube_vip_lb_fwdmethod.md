---
id: VARIABLE-KUBE_VIP_LB_FWDMETHOD
type: variable
title: kube_vip_lb_fwdmethod
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_lb_fwdmethod
tags:
  - kube-vip
  - loadbalancer
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kube_vip_lb_fwdmethod with default value 'local'"
relations: []
---

# kube_vip_lb_fwdmethod

## Summary
Selects the kube-vip service load-balancer forwarding method. Default is `local`. When set to `masquerade`, the kube-vip image repo switches to the `-iptables` variant and an extra `vip_iptables` env var is emitted in the manifest.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `kube_vip_lb_fwdmethod: local`. Consumed by `roles/kubespray_defaults/defaults/main/download.yml` (`kube_vip_image_repo` appends `-iptables` when the value is `masquerade`) and by `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2`. The default value `local` is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when kube-vip is used as the control-plane / service load balancer. Related: `kube_vip_image_repo`, `kube_vip_services_enabled`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
