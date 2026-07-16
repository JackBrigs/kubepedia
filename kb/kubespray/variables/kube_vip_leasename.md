---
id: VARIABLE-KUBE_VIP_LEASENAME
type: variable
title: kube_vip_leasename
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_leasename
tags:
  - kube-vip
  - leader-election
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_vip_leasename with default value plndr-cp-lock"
relations: []
---

# kube_vip_leasename

## Summary
Name of the kube-vip control-plane leader-election lease. Default is `plndr-cp-lock`. Rendered into the kube-vip manifest as the `vip_leasename` env var.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_leasename: plndr-cp-lock`. Also documented (commented) in `inventory/sample/group_vars/k8s_cluster/addons.yml`. Consumed by `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2` (`value: {{ kube_vip_leasename | string | to_json }}`). The default `plndr-cp-lock` is unchanged across v2.29.0-v2.31.0 (line moved from 86 to 83).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Effective only when kube-vip leader election is enabled. Related: `kube_vip_svc_leasename`, `kube_vip_leaseduration`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
