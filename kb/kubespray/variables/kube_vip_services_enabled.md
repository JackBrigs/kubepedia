---
id: VARIABLE-KUBE_VIP_SERVICES_ENABLED
type: variable
title: kube_vip_services_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_services_enabled
tags:
  - kube-vip
  - loadbalancer
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Enables kube-vip service (LoadBalancer) mode, default false"
relations: []
---

# kube_vip_services_enabled

## Summary
Enables kube-vip's Kubernetes Service (LoadBalancer) mode, allowing kube-vip to provide load-balancer IPs for Services. Default is `false`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_services_enabled: false`. The value is unchanged across v2.29.0-v2.31.0; only the line number shifts (line 74 in v2.29.0/v2.29.1, line 72 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_vip_services_interface`, `kube_vip_svc_leasename`, `kube_vip_controlplane_enabled`, `kube_vip_lb_enable`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
