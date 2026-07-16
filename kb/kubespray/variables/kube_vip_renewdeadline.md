---
id: VARIABLE-KUBE_VIP_RENEWDEADLINE
type: variable
title: kube_vip_renewdeadline
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_renewdeadline
tags:
  - kube-vip
  - leader-election
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_vip_renewdeadline with default value 3"
relations: []
---

# kube_vip_renewdeadline

## Summary
kube-vip leader-election renew deadline (seconds). Default is `3`. Rendered into the kube-vip manifest as the `vip_renewdeadline` env var.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_renewdeadline: 3`. Consumed by `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2` (`value: {{ kube_vip_renewdeadline | string | to_json }}`). The default value `3` is unchanged across v2.29.0-v2.31.0 (line moved from 89 to 86).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Effective only when kube-vip leader election is enabled. Related: `kube_vip_leaseduration`, `kube_vip_retryperiod`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
