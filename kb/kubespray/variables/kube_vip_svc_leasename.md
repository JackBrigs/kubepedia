---
id: VARIABLE-KUBE_VIP_SVC_LEASENAME
type: variable
title: kube_vip_svc_leasename
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_svc_leasename
tags:
  - kube-vip
  - leader-election
  - loadbalancer
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Lease name for kube-vip service leader election, default plndr-svcs-lock"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_svc_leasename

## Summary
The Kubernetes Lease name used by kube-vip for leader election in service (LoadBalancer) mode. Default is `plndr-svcs-lock`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_svc_leasename: plndr-svcs-lock`. The value is unchanged across v2.29.0-v2.31.0; only the line number shifts (line 87 in v2.29.0/v2.29.1, line 84 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant in kube-vip service mode. Related variables: `kube_vip_leasename` (control-plane lock), `kube_vip_services_enabled`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
