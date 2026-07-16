---
id: VARIABLE-KUBE_VIP_CP_DETECT
type: variable
title: kube_vip_cp_detect
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_cp_detect
tags:
  - kube-vip
  - networking
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_vip_cp_detect with default false"
relations: []
---

# kube_vip_cp_detect

## Summary
Controls whether kube-vip performs control-plane detection for the virtual IP. Default is `false`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as:

```yaml
kube_vip_cp_detect: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Part of the kube-vip configuration block; relevant only when `kube_vip_enabled: true`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
